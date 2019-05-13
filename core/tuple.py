# tuples are immutable. 

daysOfWeek = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

mon = daysOfWeek[0]
weekendDays = daysOfWeek[5:]

print(weekendDays)
print(mon)

print(30 * "-")
for day in daysOfWeek:
    print(day)

print((30 * "-") + "# list 2 tuple")

daysOfWeekList = list(daysOfWeek)

print(type(daysOfWeek))
print(type(daysOfWeekList))

print((30 * "-") + "# tuple 2 list")

animalList = ['pig', 'bear', 'pig']
animalTuple = tuple(animalList)

print(type(animalList))
print(type(animalTuple))

print(30 * "-")

#%%
# another way to create a tupple ! instead of ()
isItTuple = "ali", "veli", 31
isItTuple

#%%
student_tuple = ("ali", "veli", [10, 20, 30])
student_tuple[2][1]