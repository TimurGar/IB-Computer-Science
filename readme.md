# Unit 1: A electronic hardware store

## Criteria A: Planing

### Context of the problem
There is a hardware store in Karuizawa. This store is quite old, Like 1000 years old. The owner, Mr. Sakamoto, wants to upgrade his accounting system. On the moment is kept on paper. He would like to have a software 
### Justification of the solution
**Here we will write the design statement: what we will do, how, by when**

```.py
from datetime import datetime

date = datetime.today()
print("Welcome to Mr. Sakomoto's store {}".format(date))

print("Items")
print("=" * 20)

print("1. RAM")
print("2. CPU")
print("3. Motherboard")
print("4. GPU")
print("")

SelectingItems = int(input("Select Item 1-4:  "))



if SelectingItems == 1 :
  print("1. RAM")
if SelectingItems == 2 :
  print("2. CPU") 
if SelectingItems == 3 :
  print("3. Motherboard")
if SelectingItems == 4 :
  print("4. GPU")

if SelectingItems > 4 :
  print("The item with this number doesn't exsist")
if SelectingItems <= 0 :
  print("The item with this number doesn't exsist")
```
