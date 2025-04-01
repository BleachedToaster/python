cars = ["bavlna","tresne","brambory","mrkve","trava","plantaz"]

print(len(cars))
for i in cars:
    print(i)

cars.append("cernoch")
print(cars)
cars.pop(1)
print(cars)
cars.sort()
print(cars)
cars.reverse()
print(cars)