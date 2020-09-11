# Unit 1: A electronic hardware store

## Criteria A: Planing

### Context of the problem
There is a hardware store in Karuizawa. This store is quite old, Like 1000 years old. The owner, Mr. Sakamoto, wants to upgrade his accounting system. On the moment is kept on paper. He would like to have a software 
### Justification of the solution
**Here we will write the design statement: what we will do, how, by when**

## Criteria B: Design

### System diagram
![Photo](Images/Hardware%20Store%20Design.png)



## Criteria C: Development

### This is my code to for the Hardware store

```.py
from datetime import datetime

date = datetime.today()
print("Welcome to Mr. Sakomoto's store {}".format(date))
print("")
print("Items")
print("=" * 21)

deaposoneOfAllItems = []
Items = ["1. RAM", "2. CPU", "3. Motherboard", "4. GPU", "5. test"]
CostOfItems = ["1", "5", "10", "2", "5"]
NumberOfItems = len(Items)


for i in range(1, NumberOfItems + 1, 1):
    deaposoneOfAllItems.append(i)
    i += i

for i in range(NumberOfItems):
    print('{} {} '.format(Items[i],CostOfItems[i].rjust(20 - len(Items[i]))))



while 1:
    x = 1
    while x == 1:
        SelectingItems = input("Select Item 1-4:  ")
        for i in range(NumberOfItems):
            if SelectingItems == str(deaposoneOfAllItems[i]):
                print("")
                print("{}  {} {}".format(Items[i], CostOfItems[i], "btc"))
                x += 1

                print("=" * 20)
                y = 1
                while y == 1:
                    AmountOfItem = input("How many do you want:  ")
                    for n in range(100000):
                        if AmountOfItem == str(n):
                            print("")
                            print("Your total cost will be: ", int(CostOfItems[i]) * int(AmountOfItem), "btc")
                            print("")
                            y += 1
                            break
                    input("To exit, enter your credit card number: ")

                    if y == 1:
                        print("Invalid input")
                break
        if x == 1:
            print("This item",SelectingItems,"does not exist")
```
