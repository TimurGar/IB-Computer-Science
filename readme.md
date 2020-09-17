# Unit 1: A electronic hardware store

## Criteria A: Planing

### Context of the problem
There is a hardware store in Karuizawa. This store is quite old, Like 1000 years old. The owner, Mr. Sakamoto, wants to upgrade his accounting system. On the moment is kept on paper. He would like to have a software 
### Justification of the solution
**Here we will write the design statement: what we will do, how, by when**
We want to ctreate a text based application that runs on a computer,which provides the functionality for the hardware store. The app should provide actiona such as record of purchases, categorization of items, record of inventory, calculation of totals, biling. We will develop this application using Python. We will use Python because it is the software we are using in class at the moment. In comparison to C++ or C, Pytho has a lean and simple programming syntax. In addition, Python become the most popular programming language over the last years[1]. Similarly Python has a large repository of libraries and documendation.

T.E.L.O.S study:
* T - Technical
* E - Economic
* L - Legal
* O - Operational
* S - Scheduling 

[1] Goal, Aman. “Best Programming Language to Learn in 2020 (for Job &amp; Future).” Hackr.io, hackr.io/blog/best-programming-languages-to-learn-2020-jobs-future. 

## Criteria for Success
1. Provides clear feedback to the user(Usability)
1. **There are no bugs in the application
1. The application should allow to calculate the total and billing
1. Secure application: It allows user login/autenthication


## Criteria B: Design

### System diagram
![Photo](Images/Hardware%20Store%20Design.png)

<img src="Images/Hardware%20store%20flowchart.png" alt = "FlowChart" width="600">



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
### System diagram of the computer:
<img src="Images/Fig1%20Computer%20components.jpg" alt = "System Diagram">

In the image above you can see a general architecture of the computer which includes:
1. Dual core CPU
1. Video card RTX 3080(connected to PCI express port)
1. RAM (4 DDR4 DIMMS slots, 16Gb each) 
1. Chipset
1. BIOS
1. CMOS with a backup battery(next to BIOS)
1. connectors for peripherals

which are located on the motherboard or directly connected to it(without wires, placed directly to a sertain slot on the motherboard)

And 
1. SSD 128GB(connected to SATA port)
1. HDD 1Tb(connected to SATA port)
1. Power supply 1000w(it's also connected to external power socket). 
1. Cooling fans(located on computer case)

Which are connected to a motherboards via wires.
We also have keyboard and mouse as an input and monitor as an output.


