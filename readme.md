# Unit 1: A electronic hardware store

## Criteria A: Planing

### Context of the problem
There is a hardware store in Karuizawa. This store is quite old, Like 1000 years old. The owner, Mr. Sakamoto, wants to upgrade his accounting system. On the moment is kept on paper. He would like to have a software application to replace his accounting book. Mr Sakamoto just got a new macbook.
### Justification of the solution
**Here we will write the design statement: what we will do, how, by when**
We want to create a text based application that runs on a computer,which provides the functionality for the hardware store. The app should provide actions such as record of purchases, categorization of items, record of inventory, calculation of totals, biling. We will develop this application using Python. We will use Python because it is the software we are using in class at the moment. In comparison to C++ or C, Python has a lean and simple programming syntax. In addition, Python become the most popular programming language over the last years[1]. Similarly Python has a large repository of libraries and documendation.

T.E.L.O.S study:
* T - Technical
* E - Economic
* L - Legal
* O - Operational
* S - Scheduling 

[1] Goal, Aman. “Best Programming Language to Learn in 2020 (for Job &amp; Future).” Hackr.io, hackr.io/blog/best-programming-languages-to-learn-2020-jobs-future. 

## Criteria for Success
1. Provides clear feedback to the user(Usability)
1. There are no bugs in the application
1. The application should allow to calculate the total and billing
1. Secure application: It allows user login/autenthication


## Criteria B: Design

### My criteria for success is tp optimize the hardware program so that it is going to provide clear feedback to the user(Usability).
To test my program you need to follow these steps:
| Steps No. | Steps to follow                                                                               | What you should get                                                                                                      | What does it mean?                                                                                                                   |
|-----------|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| 1         | Press "Run" button  to start the program.                                                     | The welcome letter and the list  of all the available items  and their cost.                                             | The program is started. It is able to read  the Items and CostOfItems lists and then  print all the items and their cost correctly.  |
| 2         | In the "Select Item"  field print a letter  or a number out of  the items list range,  Ex:10. | An error: "Item {what you printed}  does not exist. Enter a number  within the given range".                             | The program is protected from entering the  wrong input.                                                                             |
| 3         | Type a number of items  that you want to choose.                                              | The name and the cost of an item  that you chose.                                                                        | The program is able to read what you typed, compare it with an existing items,  and print the right cost for the item.               |
| 4         | Type how many items  do you want.                                                             | The name of the selected item,  its cost multiplied by the amount  of the item selected and  the total cost in bitcoins. | The program is able to calculate the  total cost of your purchase.                                                                   |



### System diagram
![Photo](Images/Hardware%20Store%20Design.png)

<img src="Images/Hardware%20store%20flowchart2.png" alt = "FlowChart" width="600">

### Database encryption system
My program reads data from a separate file(Database.txt) and encrypts all the data using Caesar cipher.
Because of that we can prevent styling information if someone would be able to get access to a database as the data will be encrypted.
The flow diagram below describes the algorithm of the encryption system.
You can find code for this algorithm in the Criteria C section.


<img src="Images/Database%20encryptor.png" alt = "Database encryption system" width="400">


### Record of tasks
| Task No | Action | Planned Outcome | Time Estimated | Target Completion date | Criterion |
|-|-|-|-|-|-|
| 1 | Planning: Discuss the context of the situation(1st interview with the client) | Write the context of the problem | 15 min | Sep 11th | A |
| 2 | Developing: Coded the text-based menu system parts in the hardware store | A working program that show menu | 80 min | Sep 18th | C |
| 3 | Design: Created the system diagram and the flow chart of the program | A completed diagram and the flow-chart explaining the process of how the program works | 60 min | Sep 15th | B |

## Criteria C: Development

### This is my code to for the Hardware store

```.py
# This is my version of the electronic hardware story for Mr. Sakomoto

# Inputs:
# The number of the item from the list
# The amount of an item a user wants to purchase

# Outputs:
# Calculated total cost of items

# Real time library import
from datetime import datetime

#  Printing the header of the code
date = datetime.today()
print("")
print("Welcome to Mr. Sakomoto's store {}".format(date))
print("")
print("Items")
print("=" * 21)

# Creating lists with items, their cost
# Creating other useful varibales(NumberOfItems = number of items, RangeOfAllItems = range of items)
RangeOfAllItems = []
Items = ["1. RAM", "2. CPU", "3. Motherboard", "4. GPU", "5. test"]
CostOfItems = ["1", "5", "10", "2", "5"]
NumberOfItems = len(Items)
# If you decide to add a new item, simply type the name and the cost of
# the item into the Items and CostOfItems lists
# Program will do everything else for you!

# Calculating the range of items
for i in range(1, NumberOfItems + 1, 1):
    RangeOfAllItems.append(i)
    i += i

# Printing the names and the costs of all the items
for i in range(NumberOfItems):
    print('{} {} '.format(Items[i],CostOfItems[i].rjust(20 - len(Items[i]))))



# I created the varible FoolProofCheck to make sure that if
# the user will type a wrong number or a letter instead of correct value,
# the program not going to give an error.
FoolProofCheck = 1
while FoolProofCheck == 1:

    # Asking to enter an item from the available ones that user wants to purchase
    SelectingItems = input("Select Item 1 - {}: ".format(NumberOfItems))
    for i in range(NumberOfItems):
        if SelectingItems == str(RangeOfAllItems[i]):

            # Printing selected item and its cost
            print("")
            print("{} cost = {} bitcoins".format(Items[i], CostOfItems[i]))
            FoolProofCheck += 1

            print("=" * 20)
            FoolProofCheck2 = 1
            while FoolProofCheck2 == 1:

                # Asking to enter the amount of selected item the user wants to purchase
                AmountOfItem = input("How many do you want:  ")
                for n in range(100000):
                    if AmountOfItem == str(n):
                        print("")
                        print("You selected item: {}. Your total cost will be {} * {} = {} bitcoins".format(Items[i],int(CostOfItems[i]), int(AmountOfItem), int(CostOfItems[i]) * int(AmountOfItem)))
                        FoolProofCheck2 += 1
                        break

            # This is the message the user is going to get if he/she types a letter
            # instead of the number items.
            if FoolProofCheck2 == 1:
                print("Invalid input")
            break
    # This is the message the user is going to get if he/she types a letter
    # or a number of item that it not included in the list.
    if FoolProofCheck == 1:
        print("")
        print("Item", SelectingItems,"does not exist")
        print("Enter a number within the given range")
        print("")   
```
### Code for the database encryption program
```.py
all_lines_of_database = open("Database.txt","r").readlines()

encrypt_line = ""
shift = int(input("Provide shift "))
for line in all_lines_of_database:
    len_line = len(line)
    for L in range(len_line):
        print("line {} out of {}".format(L, len_line,),"." * 20, "completion {:.2f} %".format( ((L + 1)/len_line) * 100))
        new_L = chr(ord(line[L]) + shift)
        encrypt_line += new_L
print(encrypt_line)
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

## Criteria D: Functionality

## Criteria E: Evaluation
