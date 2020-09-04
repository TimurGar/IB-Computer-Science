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



deaposoneOfAllItems = list()
Items = list(["1. RAM","2. CPU","3. Motherboard","4. GPU","5. test"])
CostOfItems =list(["1btc","5tc","10btc","2btc","test"])
NumberOfItems = len(Items)

for i in range(1,NumberOfItems +1 ,1):
  deaposoneOfAllItems.append(i)
  i += i

for i in range(NumberOfItems):
  print("{} {}".format(Items[i],CostOfItems[i]))

print("")

while(1):
  SelectingItems = int(input("Select Item 1-4:  "))

  for n in range(NumberOfItems):
    if SelectingItems == deaposoneOfAllItems[n]:
      print(Items[n])
      

  if SelectingItems > NumberOfItems :
    print("The item with this number doesn't exsist")
  if SelectingItems <= NumberOfItems :
    print("The item with this number doesn't exsist")

```
