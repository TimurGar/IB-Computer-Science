Numbers = []
for y in range(1, 11):
    Numbers.append(int(input("{} {} {}".format("Enter", y , "number = "))))

NumbersSortStatus = 0
while (NumbersSortStatus == 0):
    NumbersSortStatus = 1
    for i in range(len(Numbers) - 1):
        if Numbers[i] > Numbers[i + 1]:
            Numbers[i], Numbers[i + 1] = Numbers[i + 1], Numbers[i]
            NumbersSortStatus = 0
print("")
for i in range(len(Numbers)):
    print(Numbers[i])

















