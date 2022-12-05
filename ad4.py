F = (l.strip() for l in open('input4.txt', 'r'))

part1_count = 0
part2_count = 0

def retrunInt (x):
    x1, x2 = x.split('-')
    return (int(x1), int(x2))


for pair in F:
    a, b = pair.split(',')
    #print('\na:', a, 'b:', b)

    a1, a2 = retrunInt(a)
    b1, b2 = retrunInt(b)
    
    if ( (a1 in range(b1, b2+1, 1) and a2 in range(b1, b2+1, 1)) or (b1 in range(a1,a2+1,1) and b2 in range(a1,a2+1,1)) ):
        part1_count += 1
    
 
    if ( (a1 in range(b1, b2+1, 1) or a2 in range(b1, b2+1, 1)) or (b1 in range(a1,a2+1,1) or b2 in range(a1,a2+1,1)) ):
        part2_count += 1
    
print('\npart 1 count: ', part1_count, '\npart 2 count: ', part2_count)


    
