file1 = open("input01.txt", "r")
lines = file1.readlines()
mylist=[]
for line in lines:
    if(line != '\n'):
        mylist.append(int(line.strip()))
    else:
        mylist.append(' ')
innerlist = []
outerlist = []
for item in mylist:
    if (item != ' '):
        innerlist.append(item)
    else:
        outerlist.append(sum(innerlist))
        innerlist = []

# print('outerlist: ', outerlist)
sumof3 = []
count =0
while count < 3:  
    maxVal = max(outerlist)
    sumof3.append(maxVal)
    index = outerlist.index(maxVal)
    outerlist[index]=0
    count += 1

print('sumof3:', sum(sumof3))