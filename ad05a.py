S1 = ['B','L','D','T','W','C','F','M']
S2 = ['N','B','L']
S3 = ['J','C','H','T','L','V']
S4 = ['S','P','J','W']
S5 = ['Z','S','C','F','T','L','R']
S6 = ['W','D','G','B','H','N','Z']
S7 = ['F','M','S','P','V','G','C','N']
S8 = ['W','Q','R','J','F','V','C','Z']
S9 = ['R','P','M','L','H']
stack = [[],S1, S2, S3, S4, S5, S6, S7, S8, S9]
 

with open ('input05.txt') as fin:
    input_op = fin.readlines()[10:]

print('len(input): ', len(input_op))

    
for line in input_op:
    split = line.split(' ')
    count, start, stop = map(int, [split[1], split[3], split[5]])
    # print(count, start, stop)

    for i in range(count):
        stack[stop].append(stack[start].pop())        
    
message = []
stack.pop(0)
for element in stack:
    message.append(element[-1])
    # print(element)

print('message:', ''.join(message))
    
