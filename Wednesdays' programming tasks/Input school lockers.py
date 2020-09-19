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