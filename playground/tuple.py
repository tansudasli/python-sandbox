# tuples are immutable. 

daysOfWeek = ('Monday','Tuesday', 'Wednesday', 'Thursday', 
              'Friday', 'Saturday', 'Sunday')
mon = daysOfWeek[0]
weekendDays = daysOfWeek[5:]

print(weekendDays)

for day in daysOfWeek:
    print(day)

# list to tuple, and vice versa
daysOfWeekList = list(daysOfWeek)

print(type(daysOfWeek))
print(type(daysOfWeekList))

animalList = ['pig', 'bear', 'pig']
animalTuple = tuple(animalList)

print(type(animalList))
print(type(animalTuple))
