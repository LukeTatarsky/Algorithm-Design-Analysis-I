'''
Here is a special "matching" problem: given a set A of n numbers and a set B of n numbers,
form pairs (a1; b1), ..., (an; bn), so that the following cost function is minimized
 - SUM  from i=1 to n    (ai-bi)^2
'''

def minSquare(A, B, n):

    # we want to always either select the largest element in the set or the smallest
    A.sort()
    B.sort()
 
    sum = 0
    s = ""
     
    for i in range(n):
        s += "abs(" + str(A[i]) + "-" + str(B[i]) + ")^2 +"
        sum += (A[i] - B[i])**2
    #print (s)
    return sum
 

a = [1,-5,7,3]  
b = [1,4,6,9]

n = len(a) 
print(minSquare(a, b, n))
