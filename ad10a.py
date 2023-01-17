with open ('day10a.txt') as fin:
    input = fin.read().split('\n')

def updatePos ():
    global pos, strength 
    pos += 1
    if pos in (range(20,221,40)):
        strength += pos * X

X = 1
pos = 0
strength = 0

for line in input:
    line = line.split(' ')
    
    if len(line) == 2:
        updatePos()
        updatePos()
        X += int(line[1])
    else:
        updatePos()

print('str = ', strength)

