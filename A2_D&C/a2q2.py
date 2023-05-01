
def binary_search_p(arr, low, high):
    #print("p")
    if high >= low: # can add a (and high >= 3)
	
        mid = (high + low) // 2
		
        if arr[mid - 1] < arr[mid] and arr[mid] == arr[mid + 1]:
            return mid
			
        elif arr[mid - 1] == arr[mid]  or arr[mid - 1] > arr[mid]:
            return binary_search_p(arr, low, mid)  # recurse left
			
        else:
            return binary_search_p(arr, mid + 1, high)  # recurse right
    else:
        return -1

def binary_search_q(arr, low, high):
    #print("q")
    if high >= low: 
	
        mid = (high + low) // 2
		
        if arr[mid] > arr[mid + 1] and arr[mid - 1] == arr[mid]:
            return mid
			
        elif arr[mid] == arr[mid + 1] or arr[mid] < arr[mid + 1]:
            return binary_search_q(arr, mid + 1, high)  # recurse right
			
        else:
            return binary_search_q(arr, low, mid - 1)  # recurse left
    else:
        return -1


# safe to assume array is in this format

#arr = [-1,0,1,2,3,4,5,5,5,5,5,5,5,4,3,2,1,0,-1]  # p = 6    q = 12
#arr = [1,2,3,5,5,1]                           # p = 3    q = 4
#arr = [1,5,5,4,3,2,1]                         # p = 1    q = 2
#arr = [1,2,2,1]   # I think the min length for this needs to be 4 
#arr = [2,3,4,5,6,6,4,2,1]

#p = 0   # index where  arr[p-1] < arr[p] == arr[p+1]
#q = 0   # index where  arr[q-1] == arr[q] > arr[q+1]


#p = binary_search_p(arr, 0, len(arr) - 1)
#q = binary_search_q(arr, 0, len(arr) - 1)

#print("len: ", len(arr), "   p: ", p, "   q: ", q)
#print(math.log(len(arr),2))
