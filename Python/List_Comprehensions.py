x = int(input('Which is x'))
y = int(input('Which is y'))
z = int(input('Which is z'))
n = int(input('Which is n'))

list=[]
for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
            if not i+j+k == n:
                list.append((i, j, k))


# List_Compreensions
x = int(input('Which is x'))
y = int(input('Which is y'))
z = int(input('Which is z'))
n = int(input('Which is n'))


list= [[i, j, k] for i in range(0, x+1) for j in range(0, y+1) for k in range(0, z+1) if not i + j + k == n]