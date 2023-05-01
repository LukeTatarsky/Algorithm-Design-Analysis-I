import random
from a3q3 import minSquare


def greedy_algo(Ao, Bo, n):
    A= []
    B = []
    for i in range(n):
        A.append(Ao[i])
        B.append(Bo[i])
    smallest = []
    while len(A) > 0:
        diffs = []

        for i in range(len(A)):

            for j in range(len(B)):
                diffs.append([i,j, abs(A[i]-B[j])])
        
        min = diffs[0]
        
        for i in range(len(diffs)):
            if diffs[i][2] <= min[2]:
                min = diffs[i]
        smallest.append([A[min[0]],B[min[1]],min[2]])
        #print (min)
        A.pop(min[0])
        B.pop(min[1])
        #print (diffs)
    #print(smallest)
    sum = 0
    for i in range(len(smallest)):
        sum += smallest[i][2]**2
    return sum
 



count = 0

while (True):
    n = 5
    random.seed()
    a =random.sample(range(-1000,1000),n)   
    random.seed()
    b =random.sample(range(-1000,5000),n) 



    #print (a)
    #print (b)
    #print("greedy1:", greedy_algo(a, b, n))
    #print("greedy2:", minSquare(a, b, n))

    greedy1 =greedy_algo(a, b, n)

    greedy2 =minSquare(a, b, n)

    
    if (greedy1< greedy2):
        print (a)
        print (b)
        print (greedy1, greedy2)
        break
    
    count += 1
    print (count)
