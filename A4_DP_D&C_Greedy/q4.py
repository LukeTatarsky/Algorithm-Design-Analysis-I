'''
191755360
03/21/2023
Given a string (sequence of characters)
we would like to find its longest subsequence which is palindrome. For example, the
string "strabetubsa" has the longest palindromic subsequence "abeba" (note that there
are multiple palindromic subsequences of length 5 in this case, such as "abtba" or "stats").
this -> t
simplest -> sis
dsatatad -> datatad
'''
import time
def LPS(text) -> list:
    '''
    Returns a DP table of the longest pallindrom subsequence.
    '''
    n = len(text) + 1
    # reverse text 

    # init table
    table = []
    for i in range(n):
        table.append([0] * n)

    # build the table
    for r in range(1,n):
        for c in range(1,n):
            #    match then 1 + min(above cell, above and left cell)
            if (text[n-r-1] == text[c-1]):
                table[r][c] = 1 + table[r-1][c-1]

            # no match then  max(above cell, left cell)
            else:
                table[r][c] =  max(table[r-1][c],table[r][c-1])
    
    return table

def retrieval(table,text) -> str:
    '''
    Retrieves the palindrome from the DP table.
    Favours left most characters.
    '''
    result = ''
    n = len(table[0])-1
    r = n
    c = n

    if table[r][c] == 1:
        return text[0]
    
    while ( r > 0 and c > 0):
        
        if (table[r][c]-1 == table[r-1][c] 
            and table[r][c]-1 == table[r][c-1]):
            result += text[c-1]
            c -= 1
            r -= 1
        elif (table[r][c-1] > table[r-1][c]):
            c -= 1
        elif (table[r][c-1] < table[r-1][c]):
            r -= 1
        else:
            # c for left bias,  r for right bias
            c-=1

    return result

'''
MAIN
'''
text = input()
result = ''
while (text != ''):
    # make it so that you can paste multiple lines
    table = LPS(text)
    result += retrieval(table,text) + '\n'
    text = input()
print (result)