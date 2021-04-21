"""

Get from input 23:30:31
Get from input 23:31:31

find difference between the 2 inputs in second
"""

x=input("Get time1:")
hours=int(x[0:2])
minutes=int(x[3:5])
seconds=int(x[6:8])

print(type(hours))
print(hours)
print(type(minutes))
print(minutes)
print(type(seconds))
print(seconds)

y=input("Get time2:")
hours=int(y[0:2])
minutes=int(y[3:5])
seconds=int(y[6:8])

print(type(hours))
print(hours)
print(type(minutes))
print(minutes)
print(type(seconds))
print(seconds)


t1=3600*hours+60*minutes+seconds
