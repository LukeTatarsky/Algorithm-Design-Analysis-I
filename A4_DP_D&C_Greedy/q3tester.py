import q3
import random


n = 100
low = 0
high = 1000

count = 0
while (True):
    A = []
    for i in range(n):
        a = random.randint(low,high)
        if a not in A:
            A.append(a)
            A.append(a)
        
    A.sort()
    
    b = random.randint(0,n)
    if (b %2 != 0):
        b += 1
    ans = -random.randint(low,high)
    A.insert(b, ans)
    A = A[::-1]
    #print (A)
    solution = q3.loneElement(A,0,len(A)-1)

    if solution != ans:
        print (A)
        print (ans, solution)
        print ("FAIL")
        break
    else:
        count += 1
        #print (A)
        #print (ans, solution)
        print (count)
        
