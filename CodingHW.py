# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from collections import defaultdict
from random import shuffle

def isInter(x,y):
    (a,b), (c,d) = x, y
    if (a>c and b<d) or (a<c and b>d):
        #print x,y
        return True
    else:
        return False

def isDown(isleft,x):
    if isleft:
        return x[0]>x[1]
    else:
        return x[1]>x[0]

def getRange(x):
    a,b = x
    if a<b:
        return a,b
    else:
        return b,a

def readInput():
    lines = []
    m = int(sys.stdin.readline().strip('\n'))
    for i in range(m):
        l,r = sys.stdin.readline().strip('\n').split(' ')
        lines.append((int(l),int(r)))
    assert(len(lines)==m)
    return lines

class Solution(object):
    def __init__(self,lines):
        
        self.L2R = defaultdict()
        self.R2L = defaultdict()
        for a,b in lines:
            self.L2R[a] = b
            self.R2L[b] = a
        self.N = max(max(self.L2R.keys()),max(self.R2L.keys()))
        '''
        self.Ldown = [0]*self.N
        self.Rdown = [0]*self.N
        for n in xrange(1,self.N):
            self.Ldown[n] = self.Ldown[n-1] + (1 if n in self.L2R and self.GoesDownL(n) else 0)
            self.Rdown[n] = self.Rdown[n-1] + (1 if n in self.R2L and self.GoesDownR(n) else 0)
        print self.L2R
        print self.R2L
        print self.Ldown
        print self.Rdown
        '''
    def intersections(self):
        res = 0
        for i in xrange(self.N+1):
            #print '\n\nentering iteration {}, res is {}'.format(i,res)
            L = (i,self.L2R[i]) if i in self.L2R else None
            R = (self.R2L[i],i) if i in self.R2L else None
            #print 'Found {} and {}'.format(L,R)
            if L and self.GoesDownL(i):
                #print 'Finding leftRange {} to {}'.format(L[1]+1,i-1)
                rightRange = self.getLefts(L[1]+1,i-1)
                #print 'Got leftRange:', rightRange
                res += rightRange
            if R and self.GoesDownR(i):
                #print 'Finding rightRange {} to {}'.format(R[0]+1,i-1)
                leftRange = self.getRights(R[0]+1,i-1)
                #print 'Got rightRange', leftRange
                res += leftRange
            if L and R and self.GoesDownR(i) and self.GoesDownL(i):
                res += 1 if isInter(L,R) else 0
            
        return res

    def GoesDownL(self,l):
        return l > self.L2R[l]
    def GoesDownR(self,r):
        return self.R2L[r] < r


    # get corresponding range that !goes-down
    def getRights(self,i,j):
        # using left i,j to get set of rights
        count = 0
        for l in xrange(i,j+1):
            if l not in self.L2R: continue
            r = self.L2R[l]
            if r<=j:
                count+=1
        return count
    def getLefts(self,i,j):
        count = 0
        for r in xrange(i,j+1):
            if r not in self.R2L: continue
            l = self.R2L[r]
            if l<=j: 
                count+=1
        return count

    def status(self):
        print 'got {} lines'.format(len(self.L2R))
        print 'max element is {}'.format(self.N)

def iterativeFindAll(lines):
    lines.sort(key=lambda x:x[0])
    crossings = defaultdict(set)
    for line in lines:
        i,j = getRange(line)
        for n in range(i,j+1):
            crossings[n].add(line)

    result = 0
    visited = set()
    for line in lines:
        i,j = getRange(line)
        outNodes = reduce(set.union, (crossings[n] for n in range(i,j+1)))
        outNodes = set(i for i in outNodes if i not in visited)
        visited.add(line)
        result+=sum(isInter(line,node) for node in outNodes)
    return result


def bruteFindAll(lines):
    result = 0
    lines = list(lines)
    for i in range(len(lines)):
        for j in range(i+1,len(lines)):
            if isInter(lines[i],lines[j]):
                result+=1
    return result

def testing(n):
    left = list(range(length))
    right = list(range(length))
    shuffle(left)
    shuffle(right)
    lines = [(left[i],right[i]) for i in range(length)]
    lines = lines[length/2:]
    #print lines
    bfa = bruteFindAll(lines)
    print bfa
    S = Solution(lines)
    nfa = S.intersections()#iterativeFindAll(lines)# S.recursiveFindAll()
    print nfa
    return bfa==nfa

if __name__=="__main__":
    length = 10000
    print all( testing(length) for i in range(3))
    #lines = [(1, 4), (0, 9), (3, 2), (7, 3), (8, 0)]
    #S = Solution(lines)
    #result = S.intersections()
    #print 'Final Result:' , result
    #print bruteFindAll(lines)
