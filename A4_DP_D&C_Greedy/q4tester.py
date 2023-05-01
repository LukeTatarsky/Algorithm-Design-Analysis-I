import q4_nosubmit as q4
import random, string, time

def randomword(length):
   letters = string.ascii_uppercase
   letters += string.digits
   return ''.join(random.choice(letters) for i in range(length))

#  geeks for geeks code ( known working)
def lps(str):
    n = len(str)
    L = [[0 for i in range(n)]for j in range(n)]  
    for i in range(n):
        L[i][i] = 1  # Create a table to store results of subproblems
 
    for cl in range(2, n+1):
        for i in range(n-cl+1):
            j = i+cl-1
            if str[i] == str[j] and cl == 2:
                L[i][j] = 2
            elif str[i] == str[j]:
                L[i][j] = L[i+1][j-1]+2
            else:
                L[i][j] = max(L[i][j-1], L[i+1][j])
 
    return L[0][n-1]
 

# Driver Code
# tests to see if the longest subsequence length is the same as known working solution
if __name__ == '__main__':
    count = 0

    while (True):
        n = 10
        seq = randomword(n)
        print (seq)
        
        geeksSol = lps(seq)

        myTable= q4.LPS(seq)
        myAns = myTable[-1][-1]

        if myAns >= len(seq)//3 :
            print (seq) 
        
        if geeksSol != myAns:
            print(seq, geeksSol, myAns)
            break
        else:
            count += 1
        print (" count: ", count, "longest: ",myAns)
        
        
        