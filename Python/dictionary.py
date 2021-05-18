# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import*;
Number_items= int(input("How many items you want to add" ))
L= OrderedDict();
for i in range(Number_items):
    item = input("Add item with price").split()
    item_price = int(item[-1])
    item_name = "".join(item[:-1])
    if (L.get(item_name)):
        L[item_name] += item_price
    else:
        L[item_name] = item_price
for i in L.keys():
    print(i, L[i])


