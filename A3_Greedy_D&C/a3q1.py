
'''
C=[17, 17, 12, 10, 7, 4, 2, 2, 1, 1, 1]

H-index is 5(4 in real code) (as there are 5 papers cited at least 5 times each).
'''
C = [6,6,6,6,6,4,1]
#C = [6,6,6,6,4,1]
#C=[17, 17, 12, 10, 7, 4, 2, 2, 1, 1, 1]
#C=[17, 17, 12, 10, 7, 6, 2, 2, 1, 1, 1]
C=[9, 9, 8, 7]
#C=[1, 0, 0, 0]
#C=[0, 0, 0, 0]
C = []

def binSearch(C, low, high):
    m = (low + high) // 2
    print(m, C[low:high], low, high)

    
    if low < high:    

        if high - low == 1:
            if C[0] == 0:
                return 0
            
            return m

        elif C[m] >= m:
            return binSearch(C, m, high)

        else:
            return binSearch(C, low, m)

    else:
        return 0


print (binSearch(C, 0, len(C)))