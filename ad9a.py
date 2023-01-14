with open ('sample.txt') as fin:
    input = fin.read().split('\n')

hx, hy = [1, 1]
tx, ty = [2, 0]
contact = False
tailVisited = []
tailVisited.append([tx, ty])

def printall():
    print('hx:', hx, 'hy:', hy, '\ntx:', tx, 'ty:', ty)

for line in input:
    print('on start')
    printall()

    direction, steps = line.split(' ')
    print('dir:', direction, ' steps:', steps)

    if direction == 'R':
        for _ in range(int(steps)):
            # move head in right direction
            hy += 1
            print('new head pos after R')
            printall()
        
            # check if tail is in contact with head after head move
            if (abs(hx-tx) <= 1 and abs(hy-ty)<=1):
                contact = True # => no movement of tail
                print('in contact')
            else: # => tail movement, row wise, col wise, diagonally
                print('no contact, tail movement')
                if (hx == tx):            
                    changeX = 0
                    changeY = 1
                else:
                    changeX = int((hx-tx)/abs(hx-tx))
                    changeY = int((hy-ty)/abs(hy-ty))
                    print(changeX, changeY)
                
                tx += changeX
                ty += changeY
                tailVisited.append([tx, ty])
    
            print('updated values')
            printall()

print('tails visited: ', len(tailVisited))

