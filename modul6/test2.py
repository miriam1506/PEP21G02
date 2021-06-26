"""
A factory needs an iterable object to keep track of employee working schedule for each day.
Each employee has a string name and an object of type datetime that indicate when employee started work
Iterating the object will return tuple with name and time that employee entered the factory
1) 40p: Definition
    a) 10p: Class with constructor that receives the date in the format you desire (representing the day)
    b) 10p: Create method to add worker information when he/she enters the factory
         - if worker is already in the factory a custom exception inheriting ValueError (exception: WorkStartError)
         will be raised with message indicating employee name and current time
    c) 10p: Create method to remove worker information when he/she leaves the factory
         - if worker is not in the factory a custom exception inheriting ValueError (exception: WorkEndError)
         will be raised with message indicating employee name and current time
    c) 10p: Iterating the object will return tuple with name and time employee entered the factory
2) 40p: Execution:
    a) 10p: Create instance of class with date format you selected.
    b) 10p: Add the following employees with time of arrival:
        - Joe: 09:01:20
        - Ana: 09:03:15
        - Tim: 09:04:25
        - Tim: 09:04:30 - treat this exception
    c) 10p: Remove the following employees:
        - Joe
        - Ana
        - Tim
        - Tim - treat this exception
    d) 10p: Iterate the created object and save each value on a new line in a file
3) 20p: Documenting:
   a) 5p: type hints for all arguments (optional for returned values)
   a) 5p: module documentation
   b) 5p: class documentation for all classes
   c) 5p: method documentation for all methods
"""

from datetime import datetime


class WorkStartError(ValueError):
    pass


class WorkEndError(ValueError):
    pass
class TimeIter:
    """Iterator for working hours by name"""

    def __init__(self, working_time: list):
        self.working_time = working_time

    def __iter__(self):
        return self

    def __next__(self):
        if not self.working_time:
            raise StopIteration
        else:
            return self.working_time.pop(0)

class TimeKeeper:
    """Keeps track of entering hours for employees"""
    ledger = {}

    def __init__(self, date: tuple):
        self.date = date

    def __iter__(self):
        remove_from_factory = []
        for name, start, remove_from_factory in self.ledger.items():
            remove_from_factory.append((name, start))
            return TimeIter(remove_from_factory)

    def start_work(self, name: str, start: tuple):
        """add start work time"""
        if self.ledger.get(name, None):
            raise WorkStartError(f'{name} already started work')
        self.ledger[name] = [datetime(*self.date, *start)]

    def remove_from_factory(self, name: str):
        """remove from factory and raise error"""
        if self.ledger.get(name) is None:
            raise WorkEndError(f'{name} is not in the factory{datetime.now()}')
        self.ledger.pop(name)


time = TimeKeeper((2021, 5, 6))

time.start_work('Joe', (9, 1, 20))
time.start_work('Ana', (9, 3, 15))
time.start_work('Tim', (9, 4, 25))
try:
    time.start_work('Tim', (9, 4, 30))
except WorkStartError as e:
    print(e,'got passed WorkStartError')

time.remove_from_factory('Joe')
time.remove_from_factory('Ana')
time.remove_from_factory('Tim')
try:
    time.remove_from_factory('Tim')
except WorkEndError as e:
    print(e,'got passed WorkEndError')

with open('timer.log', 'w') as file:
    for date in time :
        file.write(f'{date[0]}: {date[1]}\n')
