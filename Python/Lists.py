# Consider a list (list = []). You can perform the following commands:
# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.

if __name__ == '__main__':
    arr = []
    for i in range(int(input())):
        aline = input().split()
        for al in range(1, len(aline)):
            aline[al] = int(aline[al])
        if aline[0] == "insert":
            arr.insert(int(aline[2]), int(aline[1]))
        elif aline[0] == "print":
            print(arr)
        elif aline[0] == 'remove':
            arr.remove(int(aline[1]))
        elif aline[0] == 'append':
            arr.append(int(aline[1]))
        elif aline[0] == 'sort':
            arr.sort()
        elif aline[0] == 'pop':
            arr.pop()
        elif aline[0] == 'reverse':
            arr.reverse()


N = int(input('Number of commands You want to Enter :'))
l=[]
for i in range(N):
    x=input().split(" ")
    command=x[0]
    if command=='insert':
        l.insert(int(x[1]),int(x[2]))
    if command=='remove':
        l.remove(int(x[1]))
    if command=='append':
        l.append(int(x[1]))
    if command=='sort':
        l.sort()
    if command=='reverse':
        l.reverse()
    if command=='pop':
        if (len(l)!=0):
            l.pop()
    if command=='print':
            print(l)