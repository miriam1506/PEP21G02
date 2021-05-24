class Car:
    color = 'green'
    number_of_doors = 5
    speed = 0
    def change_color(self, new_color):
        self.color = self.color.replace('green', new_color)
    def accelerate(self, val_acc, time):
        self.speed += val_acc * time
        if self.speed > 30000000:
            raise ValueError('Fast & Furious')
    def decelerate(self, val_acc, time):
        self.speed -= val_acc * time
        if self.speed < 0 :
            raise ValueError('Speed is negative')
    def read_speed(self):
        km_per_h = (3600/1000) * self.speed
        return km_per_h
bmw = Car()
bmw.change_color('red')
print('The new BMW color is:', bmw.color)
bmw.accelerate(3, 200)
print(bmw.speed)

bmw.decelerate(400,200)

print(bmw.read_speed())
