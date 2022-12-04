X = [l.strip()for l in open('input3.txt')]

#part a
common = [] #stores the list of common elements
score = 0 #total score

for x in X:
    firstHalf = x[:len(x)//2]
    secondHalf = x[len(x)//2:]

    for item in firstHalf:
        if item in secondHalf:
            common.append(item)
            if ('a' <= item <= 'z'):
                score += ord(item)-96 #ord('a')=97, so -96 will give score as 1 for 'a'
            else:
                score += ord(item)-38 #this will give score as 27 for 'A'
            break

print('part 1 score: ', score)

##############################################
#part b - method 1

Y = [l.strip() for l in open('input3.txt')]
group = []
common = []
score = 0

for i in range(0, len(Y), 3):
    group.append(Y[i])
    group.append(Y[i+1])
    group.append(Y[i+2])

    for item in group[0]:
        if item in group[1] and item in group[2]:
            common.append(item)
            if ('a' <= item <= 'z'):
                score += ord(item)-96
            else:
                score += ord(item)-38
            break
    
    group = []

print('part 2 score: ', score)