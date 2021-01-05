import sys
import heapq

def select(cr, c, k):
    #create a copy of the list of corresponding cost and revenue for each project
    costheap = cr[:]
    #heapify costheap so that the project with the least cost is at the root     
    heapq.heapify(costheap)
    profitheap = []
    #using the created heap costheap, retrieve a pool of selectable projects where the project cost does not exceed existing capital  
    #by repeatedly comparing the capital against the cost at the root node, which would contain the remaining project with lowest cost
    for i in range(k):
        while len(costheap) > 0 and c >= costheap[0][0]:
            cost, rev = heapq.heappop(costheap)
            #create another heap profitheap to store the corresponding profits from the pool of selectable projects where cost does not exceed capital,
            #and the most ideal selectable project with max profit would at the root of profitheap
            heapq.heappush(profitheap, -(rev-cost))
        if len(profitheap) > 0:
            #from the pool of selectable projects, retrieve the root of profitheap which would have max profit
            c += -heapq.heappop(profitheap)
        else: 
            #if run out of selectable projects, end iteration and return impossible
            return "impossible"
    return c

a = [int(s) for s in sys.stdin.readline().split()]
cr = [[int(t) for t in s.split(':')] for s in sys.stdin.readline().split()]
for _ in range(a[1]):
    b = [int(s) for s in sys.stdin.readline().split()]
    c, k = b[0], b[1]
    print(select(cr, c, k))  