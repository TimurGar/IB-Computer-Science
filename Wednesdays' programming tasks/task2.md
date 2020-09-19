# Wednesday taks no.2
### My answers to questions:
https://docs.google.com/document/d/1Bf2aEPQtkkUBMLzZrbdUHItwD2amJHihQUefAelCn2w/edit?usp=sharing

## Task 1

```.py
number_of_lockers = 2400
color_of_each_locker = []

for i in range(number_of_lockers):
    color_of_each_locker.append(int(i % 4))
    if color_of_each_locker[i] == 0:
        color_of_each_locker[i] = "red"
    if color_of_each_locker[i] == 1:
        color_of_each_locker[i] = "white"
    if color_of_each_locker[i] == 2:
        color_of_each_locker[i] = "yellow"
    if color_of_each_locker[i] == 3:
        color_of_each_locker[i] = "blue"

    print("{} = {}".format(i+1,color_of_each_locker[i], sep="\n"))
```

## Task 2

```.py
number_of_lockers = 2400
color_of_each_locker = []

range_of_lockers =[]
for i in range(1, number_of_lockers + 1, 1):
    range_of_lockers.append(i)
    i += i

for i in range(number_of_lockers):
    color_of_each_locker.append(int(i % 4))
    if color_of_each_locker[i] == 0:
        color_of_each_locker[i] = "red"
    if color_of_each_locker[i] == 1:
        color_of_each_locker[i] = "white"
    if color_of_each_locker[i] == 2:
        color_of_each_locker[i] = "yellow"
    if color_of_each_locker[i] == 3:
        color_of_each_locker[i] = "blue"

while 1:
    x = 1
    while x == 1:
        input_number = input("Enter the number of locker ")
        for i in range(len(color_of_each_locker)):

            if input_number == str(range_of_lockers[i]):
                print(color_of_each_locker[i])
                x += 1
        if x == 1:
            print("invalid input")
```

## Task 3
```.py
number_of_lockers = 2400
color_of_each_locker = []

red =[]
white = []
yellow = []
blue = []

range_of_lockers =[]
for i in range(1, number_of_lockers + 1):
    range_of_lockers.append(i)

for i in range(number_of_lockers):
    color_of_each_locker.append(int(i % 4))
    if color_of_each_locker[i] == 0:
        color_of_each_locker[i] = "red"
        red.append(range_of_lockers[i])

    if color_of_each_locker[i] == 1:
        color_of_each_locker[i] = "white"
        white.append(range_of_lockers[i])

    if color_of_each_locker[i] == 2:
        color_of_each_locker[i] = "yellow"
        yellow.append(range_of_lockers[i])

    if color_of_each_locker[i] == 3:
        color_of_each_locker[i] = "blue"
        blue.append(range_of_lockers[i])

while 1:
    x = 1
    while x == 1:
        input_number = input("Enter the color of locker ")
        for i in range(int(number_of_lockers/4)):

            if input_number == "red":
                print("{}".format(red[i]))
                x += 1
            if input_number == "white":
                print("{}".format(white[i]))
                x += 1
            if input_number == "yellow":
                print("{}".format(yellow[i]))
                x += 1
            if input_number == "blue":
                print("{}".format(blue[i]))
                x += 1

        if x == 1:
            print("invalid input")
```
