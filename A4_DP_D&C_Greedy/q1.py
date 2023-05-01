'''
In the Deadline problem, an instance is a
set of n tasks such that each takes 1 (one) unit of time to complete and a set of deadlines
d1, d2, ..., dn. When a task is not completed by its deadline, a fixed penalty of 100$
is applied. A valid solution to the Deadline problem is an ordering of the tasks that
minimizes the total penalty incurred when the tasks are completed one after another in
the order provided starting at time 0.
'''
# To sort by deadline
def funcKey(job):
    return job[1]      


deadlines = [4,5,3,6,1,1,4]  # penalty :100

#deadlines = [2,4,5,3]  # penalty : 0

#deadlines = [2,1,4,2] # penalty : 100

#deadlines = [2,4,2,3,1]   # penalty:  100

deadlines = [5,6,2,3,1,3,4,5,2]   # penalty:  300




n = len(deadlines)

jobs = [0]*n
order = [0]*n
skipped = [0]*n
penalty = 0


for i in range(n):
            # [job #, deadline]
    jobs[i] = [i+1,deadlines[i]]

# sort jobs by deadline
jobs.sort(key=funcKey)


t = 1
for i in range(n):
    #print(t, jobs[i])
    if t <= jobs[i][1]:
        order[t-1] = jobs[i]
        t += 1
    else:        
        skipped[i] = 1
    

for i in range(n):
    if skipped[i] == 1:
        order[t-1] = jobs[i]
        t+=1
        penalty += 100

print (order)
print("penalty: ", penalty)


  