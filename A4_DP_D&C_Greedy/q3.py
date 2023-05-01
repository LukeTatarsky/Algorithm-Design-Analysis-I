'''
Consider a sorted in non-descending
order array of n integers in which all elements appear twice (one after one) 
and one element appears only once. Find that element. 
For example, if the given array is [1, 1, 3, 3, 4, 5, 5, 7, 7, 8, 8], the output is 4,
 if the input array is [1, 1, 3, 3, 4, 4, 5, 5, 7, 7, 8],the output is 8.
 Assumes that array is in this format
'''

def loneElement(A, low, high):
    m = (low + high )//2 
    
    #print ("low: {}  high: {}  m: {}  value: {}".format(low,high, m, A[m]))

    
        #print (A[m-1],A[m],A[m+1])   
    if (low == high):
        return A[m]  
     
    elif (A[m-1] != A[m] and A[m+1] != A[m]):
        return A[m]
    
    elif (m % 2 != 0):  # odd middle
        if (A[m+1] == A[m]):
            return loneElement(A, low, m)  # go left
        else:
            return loneElement(A, m+1, high)  # go right

    else:  # even  middle
        if (A[m+1] == A[m]):
            return loneElement(A, m+1, high)  # go right
        else:
            return loneElement(A, low, m)  # go left
    




A = [1, 1, 3, 3,   4,   5, 5, 7, 7, 8, 8]
#A = [1, 1, 3, 3, 4, 4, 5, 5, 7, 7, 8]
A = [10,10,2,2,4,4,7,6,6,7,7,9,9,1,1,23,23]
print("len: ",len(A))
print (loneElement(A,0,len(A)-1))   # change to 1, len