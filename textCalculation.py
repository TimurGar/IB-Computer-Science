# This program
taxList =[0]
while 1:
    total = int(input("please enter the total amount (BTC): "))
    if total < 0:
        print("The total cannot be negative. Try again")
    else:
        break
for n in range(5):
    if 250*n < total <= 250*n + 250:
        taxList = 0.25 - 0.05 * n
    if total > 1000:
        taxList = 0.05

taxList = str(taxList)

print("{}".format("-"* 50))
print("{}{}".format("|","|".rjust(49)))
print("{}{}{}{}".format("|","total tax = ".rjust(25), taxList, "|".rjust(24 - len(taxList))))
print("{}{}".format("|","|".rjust(49)))
print("{}".format("-"* 50))



