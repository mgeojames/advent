X = [l.strip() for l in open('input02.txt', 'r')]
score = 0
for x in X:
    #print('starting score', score)
    op, me = x.split()
    print(op, me)
    score += {'X': 0, 'Y': 3, 'Z': 6}[me]
    #print('my score', score)

    score += {('A', 'X'): 3, ('A', 'Y'): 1, ('A', 'Z'): 2,
            ('B', 'X'): 1, ('B', 'Y'): 2, ('B', 'Z'): 3,
            ('C', 'X'): 2, ('C', 'Y'): 3, ('C', 'Z'): 1}[(op, me)]  
    #count+=1
    #print('level ', count, ' score ', score)
    

      
print(score)
