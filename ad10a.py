with open ('input10.txt') as fin:
    input = fin.read().split('\n')

X = [1]

for line in input:
    line = line.split(' ')
    
    if len(line) == 2:
        X.append(X[len(X)-1])
        X.append(X[len(X)-1]+int(line[1]))
    else:
        X.append( X[len(X)-1] )
    
    
strength = 0
for i in range (20,221,40):
    strength += i * X[i]

print('str = ', strength)

