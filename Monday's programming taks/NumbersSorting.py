Numbers = [int(input("1val = ")), int(input("2val = ")), int(input("3val = ")), int(input("4val = ")),
           int(input("5val = ")), int(input("6val = ")), int(input("7val = ")), int(input("8val = ")),
           int(input("9val = ")), int(input("10val = "))]
NumbersSortStatus = 0

while (NumbersSortStatus == 0):
    NumbersSortStatus = 1
    for i in range(len(Numbers) - 1):
        if Numbers[i] > Numbers[i + 1]:
            Numbers[i], Numbers[i + 1] = Numbers[i + 1], Numbers[i]
            NumbersSortStatus = 0
for i in range(len(Numbers)):
    print("")
    print(Numbers[i])
















