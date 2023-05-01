
'''
Suppose you have an unsorted array A[1::n] of elements. 
You can only do equality tests on the elements (e.g. they are large GIFs). 
In particular this means that you cannot sort the array. 
You want to find (if it exists) a majority element, i.e., an element that
appears more than half the time.
Using observation of part (a) give a divide-and-conquer algorithm to find a majority
element, that runs in time O(n log n).
This runs in O(n log n) time.
'''
A = ["a","a","a","a", "a","a","g","f", "a","b","b","b"]
#A = ["a","a","b","b","c","c","c","b"]
#A = ['a','b','c']
#A = [1,1,1,1,2,2,1,1,1,1,2,2,2,2,1,1,1,1,2,2,1,1,1,1,2,2,2,2]
A = [1,1,1,1,2,2,1,1,1,1,2,2,2,2,1,1,1,2,2,1,1,1,11,1,1,2,2,2,2,2,2,1,1,2,2,1,1,1,1,2,2,2,2,2,1,12,1,2,1,2,1,2,1,2,1,2,1,2,1]
#A = [3, 3, 5, 7]
#A = [5, 2, 6, 6, 6, 6, 6, 5, 2]
#A = [1,2,1,2,1,2]
#A = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
A = [4, 1, 1, 3, 4]
A = [1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2]   # worst case, i think
def majority(A, low, high):

    mid = (low + high - 1)//2

    if (low == high):  # base case single element
        return A[low]
    
    left = majority(A, low, mid)
    right = majority(A, mid +1 , high)

    if (left == None and right == None):  # no major
        return None
    
    elif (left != right):  # major found, must check
        cl = 0
        cr = 0
        n = high - low + 1
        for i in range(low, high + 1):
            if left == A[i]:
                cl += 1
                if cl == n//2 + 1:
                    return left
            elif right == A[i]:
                cr += 1
                if cr == n//2 + 1:
                    return right
        return None
    
    else:         # majors found and they match
        return left

print ()
print ("len:",len(A),"    Majority:",majority(A,0,len(A)-1))


def bruteForce(A, low, high):
     
    for b in A:
        count =0
        for c in A:
            if b == c:
                count += 1
                if count == len(A)//2  + 1:
                    return b
    return None


print ("BruteForce Majority:", bruteForce(A,0,len(A)-1))
print ("Finished")
