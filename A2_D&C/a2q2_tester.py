import a2q2
import math
import time

n = 1
LIMIT = 100000000
input("WARNING! this will use up to 8.5GB of memory. Press enter to continue.")
while(n < LIMIT):
    n = n*10
    print("\n creating array. this is slow....")
    t5 = time.time()
    arr = []
    x = 0
    b = 0
    for i in range(n):
        arr.append(i)

        b = i

    for i in range(n):
        arr.append(b)

    for i in range(b,-1,-1):
        arr.append(i)
    t6 = time.time()
    
    print("\nlen: ", len(arr))
    print("array creation time: ", round(t6-t5,2))

    #input("array created. press enter to continue")
    t1= time.time()
    # linear search
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            x = 1
    t2 = time.time()

    #print("# binary searching...")
    p = a2q2.binary_search_p(arr, 0, len(arr) - 1)
    q = a2q2.binary_search_q(arr, 0, len(arr) - 1)
    t3 = time.time()
    print("p: ", p)
    print("q: ", q)
    #print("log(n) = ", math.log(len(arr),2))

    print()


    print("linear time:",(t2-t1),"s")
    print("binary time:",(t3-t2),"s")
    #input("done.  press enter to exit")

'''
print("# heavy middle")
arr = []
b = 0
for i in range(5):
    arr.append(i)

    b = i

for i in range(n):
    arr.append(b)

for i in range(b,0,-1):
    arr.append(i)

print("len: ", len(arr))
print("p: ", a2q2.binary_search_p(arr, 0, len(arr) - 1))
print("q: ", a2q2.binary_search_q(arr, 0, len(arr) - 1))
print("log(n) = ", math.log(len(arr),2))
print()

print("# equal")
arr = []
b = 0
for i in range(n):
    arr.append(i)

    b = i

for i in range(n):
    arr.append(b)

for i in range(b,0,-1):
    arr.append(i)

print("len: ", len(arr))
print("p: ", a2q2.binary_search_p(arr, 0, len(arr) - 1))
print("q: ", a2q2.binary_search_q(arr, 0, len(arr) - 1))
print("log(n) = ", math.log(len(arr),2))
'''