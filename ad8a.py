with open("input8.txt") as fin:
    input = fin.read().split()  

int_list = []

for line in input:
    int_list.append(list(map(int, list(line))))

rows = len(int_list)
cols = len(int_list[0])
print('\nrows: ', rows, '\ncols: ', cols)

def check_left(i, j):
    element = int_list[i][j]
    left_list = int_list[i][:j]
    # print('left_list of [', i, '][', j, ']', element, left_list)
    if (element > max(left_list)):
        return True
    return False

def check_right(i, j):
    element = int_list[i][j]
    right_list = int_list[i][j+1:]
    if (element > max(right_list)):
        return True
    return False

def check_top(i, j):
    element = int_list[i][j]
    top_list = []
    for index in range (i):
        top_list.append(int_list[index][j])
    if (element > max(top_list)):
        return True
    return False

def check_bottom(i, j):
    element = int_list[i][j]
    bottom_list = []
    for index in range (i+1, cols):
        bottom_list.append(int_list[index][j])
    if (element > max(bottom_list)):
        return True
    return False

count = 0
score = 0
for i in range (rows):
    for j in range (cols):

        if (i == 0  or i==rows-1 or j==0 or j==cols-1):
            print(i,j, 'boundary value')
            count += 1
            print('count:', count)             
        
        elif(check_left(i,j)):
            print(i,j, 'visible from left, number is:', int_list[i][j])
            count += 1
            print('count:', count) 
            
        elif(check_right(i,j)):
            print(i,j, 'visible from right, number is:', int_list[i][j])
            count += 1
            print('count:', count)             

        elif(check_top(i,j)):
            print(i,j, 'visible from top, number is:', int_list[i][j])
            count += 1
            print('count:', count)             

        elif(check_bottom(i,j)):
            print(i,j, 'visible from bottom, number is:', int_list[i][j])
            count += 1
            print('count:', count)             
        
        else:
            print(i,j, 'not visible, number is:', int_list[i][j])
            print('count:', count) 

            
print('total count:', count)