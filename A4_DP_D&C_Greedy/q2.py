'''
Dynamic programming
In the MinWeightChange problem, 
for a given list of positive integers 1 = d1 < d2 < d3 < ... < dn 
that represent the denominations of the n types of coins, 
a list of positive integers w1, w2, w3, ..., wn,  
where wi is the weight of the coin of denomination di, 
and a target value V, we must find the weight of a minimum-weight set of coins 
(allowing multiple coins of a given denomination, as usual) whose denominations sum up to V.
'''
import math
def minWeightChange(n:int, D:list, W:list, V:int):
    '''
    Returns the weight of a minimum-weight set of coins 
    whose denominations sum up to V. \n   
    n - number of denominations (int) \n
    D - list of denominations (int) \n
    W - list of denomination weights (int) \n
    V - Target value (int)
    '''
    weight = [math.inf] * (V+1)
    weight[0] = 0


    for i in range(1, V+1):
        
        #print()
        for j in range(0,n):
            
            if (i - D[j] >= 0):

                #print (i2, j, W[j] + colmin[i2-D[j]])
                calc = W[j] + weight[i-D[j]]
                if ( calc < weight[i]):
                    weight[i] = calc
    indList = []
    for i in range(V+1):
        indList.append(i)
    # print(indList) 
    # print(weight)

    return weight[V]






# result is 4
D = [1,2,5]
W = [4,1,4]
V = 5

# result is 8
D = [1,2,5]
W = [1,5,4]
V = 10

# result is  30789  (not checked)
D = [1,2,5,10,15,25,50,100,200]
W = [1,5,4, 5, 7, 5, 3,  5,  7]
V = 879465

# result is 12
D = [1,5,10,25]
W = [2,8,2,10]
V = 26

# result is 9
D = [1,5,10,25]
W = [1,4,2,10]
V = 26

n = len(D)
print (minWeightChange(n,D,W,V))
