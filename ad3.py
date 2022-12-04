X = [l.strip()for l in open('input3.txt')]

common = []
score = 0
for x in X:
    firstHalf = x[:len(x)//2]
    secondHalf = x[len(x)//2:]

    for item in firstHalf:
        if item in secondHalf:
            common.append(item)
            if ('a' <= item <= 'z'):
                score += ord(item)-96
            else:
                score += ord(item)-38
            break

print('score: ', score)