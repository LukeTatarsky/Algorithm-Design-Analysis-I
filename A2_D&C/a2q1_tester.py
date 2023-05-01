
import a2q1
import random


def bruteforce(A,B): 
    c = 0
    for i1 in range(len(A)):
        for j1 in range(len(A)):
            for i2 in range(len(B)):      
                for j2 in range(len(B)):                    
                    if A[i1] + A[j1] == B[i2] + B[j2]:
                        #print("\n A ", i1,j1, A[i1] + A[j1] ,"   B ", i2,j2, B[i2] + B[j2])
                        return True    
    #print("\n A ", i1,j1, A[i1] + A[j1] ,"   B ", i2,j2, B[i2] + B[j2])
    return False


countT = 0
countF = 0
while (True):    
    
    n = 10
    
    # Equal found and not found with n = 10.   ( almost always found with n=100)
    random.seed()
    A =random.sample(range(-1000,500),n)   
    random.seed()
    B =random.sample(range(-500,1000),n) 
    
    '''
    # never found (worst case). for bruteforce,  noprob if n=10   trouble at n=100    forget n=1000
    random.seed()
    A =random.sample(range(-2000,0),n)   
    random.seed()
    B =random.sample(range(1,2000),n)
    '''
    solution = a2q1.twoWayTwoSum(A, B)

    brute = bruteforce(A,B)
    
    
    if solution != brute:
        print(A)
        print(B)
        print ( solution, brute)
        break
        
    if solution == True:
        countT += 1
    else:
        countF += 1

    print("countT: ", countT, "countF:", countF)

