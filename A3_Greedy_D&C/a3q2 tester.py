
import random
# change this to whatever your file is called
import a3q2 as solution


def bruteForce(A, low, high):
     
    for b in A:
        count =0
        for c in A:
            if b == c:
                count += 1
                if count == len(A)//2  + 1:
                    return b
    return None

even = False
countT = 1
countF = 1


n = 3
low = 1
high = 4

while (True):      

    if ((countF % 100) == 0) or ((countT % 100) == 0):
        n += 1
        
        if high > 2 and ((countF % 2000) == 0):
            high -= 1
        elif high == 2:
            high += 1
        countF += 1
        countT += 1
    
    A = []
    for i in range(0, n):
        A.append(random.randint(low,high))

    # change this to whatever your function is called
    result = solution.majority(A, 0, len(A) -1)

    brute = bruteForce(A, 0, len(A) -1)
    #print(A)
    if result != brute:
        print(A)
        print ( "Solution:", result, "\nBruteForce:", brute)
        break
        
    if result != None:
        countT += 1
    else:
        countF += 1

    print("Found: ", countT, "No majority:", countF, " n:", n ,"  high:", high)

