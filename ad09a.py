with open('input09.txt') as f:
    X = f.read().split('\n')

hx, hy = [0, 0]
tx, ty = [0, 0]
contact = False
tailvisit = []
tailvisit.append([tx, ty])

for line in X:
    dir, steps = line.split(' ')
    if dir == 'R':
        for _ in range(int(steps)):
            # move  head in right direction
            hy += 1
            # check if tail inin contact with head
            if (abs(hx - tx) <= 1 and abs(hy-ty) <= 1):
                contact = True  # No tail movement
            else:  # tail movement(row,column or diagonal)
                if (hx == tx):
                    changeX = 0
                    changeY = 1
                else:
                    changeX = (hx-tx)/abs(hx-tx)
                    changeY = (hy-ty)/abs(hy-ty)
                tx += changeX
                ty += changeY
                tailvisit.append([tx, ty])
    if dir == 'L':
        for _ in range(int(steps)):
            hy += -1  # move  head in left direction
            if (abs(hx - tx) <= 1 and abs(hy-ty) <= 1):  # check if tail inin contact with head
                contact = True  # No tail movement
            else:  # tail movement(row,column or diagonal)
                if (hx == tx):
                    changeX = 0
                    changeY = -1
                else:
                    changeX = (hx-tx)/abs(hx-tx)
                    changeY = (hy-ty)/abs(hy-ty)
                tx += changeX
                ty += changeY
                tailvisit.append([tx, ty])
    if dir == 'U':
        for _ in range(int(steps)):
            hx += -1  # move  head in upper direction
            if (abs(hx - tx) <= 1 and abs(hy-ty) <= 1):  # check if tail inin contact with head
                contact = True  # No tail movement
            else:  # tail movement(row,column or diagonal)
                if (hy == ty):
                    changeX = -1
                    changeY = 0
                else:
                    changeX = (hx-tx)/abs(hx-tx)
                    changeY = (hy-ty)/abs(hy-ty)
                tx += changeX
                ty += changeY
                tailvisit.append([tx, ty])
    if dir == 'D':
        for _ in range(int(steps)):
            hx += 1  # move  head in down direction
            if (abs(hx - tx) <= 1 and abs(hy-ty) <= 1):  # check if tail inin contact with head
                contact = True  # No tail movement
            else:  # tail movement(row,column or diagonal)
                if (hy == ty):
                    changeX = 1
                    changeY = 0
                else:
                    changeX = (hx-tx)/abs(hx-tx)
                    changeY = (hy-ty)/abs(hy-ty)
                tx += changeX
                ty += changeY
                tailvisit.append([tx, ty])

my_set = set(tuple(x) for x in tailvisit)
print("No.of sites tail visited atleast once : ", len(my_set))
