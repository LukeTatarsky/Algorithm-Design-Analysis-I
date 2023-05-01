"""
In the 2-Way-2- Sum decision problem, we are given arrays A and B of length
n containing (not necessarily distinct) integers, and we must determine whether there are
two pairs of indices i1; j1; i2; j2 (not necessary distinct) for which A[i1] + A[i2] = B[j1] + B[j2]
brute force is n^4, a slightly better approach is n^3.
produce a solution that runs in O(n^2logn)
this solution is n^2logn^2 -> n^2logn
"""
A = [-4, -48, -2, -3,  17, 18]
B = [15, 19, 23, 26, 28, 30]   # A  4 4 34    B  0 1 34



def binSearch(arr, x, low, high):

    if high >= low: 	
        mid = (low + high) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            return binSearch(arr, x, mid+1, high)
        else:
            return binSearch(arr, x, low, mid-1)
    else:
        return False

def aSum_calc(A):
    aSums = []
    for i in range(len(A)):
        for j in range(i,len(A)):
            #Asums.append([i,j,A[i]+A[j]])  if we wanted indices then it would be something like this
            aSums.append(A[i]+A[j])
    return aSums

def bSum_calc(B):
    bSums = []
    for i in range(len(B)):
        for j in range(i,len(B)):
            bSums.append(B[i]+B[j])
    return bSums

def twoWayTwoSum(A,B):
    # create array of all possible sums. new array is n(n+1)/2 -> n^2
    aSums = aSum_calc(A)
    bSums = bSum_calc(B)

    # merge sort run time is n^2logn^2  -> n^2logn
    bSums = sorted(bSums)

    # now do linear checking of one array and binary search of the other
    for i in range(len(aSums)):
        #found = binSearch(bSums, aSums[i], 0, len(bSums)-1)
        if (binSearch(bSums, aSums[i], 0, len(bSums)-1)):
            return True
    
    return False


print(twoWayTwoSum(A,B))   