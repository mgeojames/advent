with open("input8.txt") as fin:
    input = fin.read().split() 


int_list = []

for line in input:
    int_list.append(list(map(int, list(line))))

rows = len(int_list)
cols = len(int_list[0])
print('\nrows: ', rows, '\ncols: ', cols)

def check_right(i,j):
    # print('in check right:', i,j)
    element = int_list[i][j]
    rcount = 0
    for j in range(j+1, cols):
        if (int_list[i][j] >= element):
            rcount+=1
            return rcount
        else:
            rcount += 1
    return rcount  

def check_left(i,j):
    # print('in check left:', i,j)
    element = int_list[i][j]
    count = 0
    for j in range(j-1, -1, -1):
        if (int_list[i][j] >= element):
            count+=1
            return count
        else:
            count += 1
    return count  

def check_top(i,j):
    # print('in check top:', i,j)
    element = int_list[i][j]
    count = 0
    for i in range(i-1, -1, -1):
        if (int_list[i][j] >= element):
            count+=1
            return count
        else:
            count += 1
    return count 

def check_bottom(i,j):
    # print('in check bottom:', i,j)
    element = int_list[i][j]
    count = 0
    for i in range(i+1, rows):
        if (int_list[i][j] >= element):
            count+=1
            return count
        else:
            count += 1
    return count 


score = []

for i in range (1,rows-1):
    for j in range (1,cols-1):
        r_val = check_right(i,j)
        # print (r_val)
        l_val = check_left(i,j)
        # print(l_val) 
        t_val = check_top(i,j)
        # print(t_val)
        b_val = check_bottom(i,j)
        # print(b_val)

        score.append(l_val*r_val*t_val*b_val)

print(max(score))
        
