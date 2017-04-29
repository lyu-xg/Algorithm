import sys
from random import shuffle

def isInter(x,y):
    (a,b), (c,d) = x, y
    if (a>c and b<d) or (a<c and b>d):
        #print x,y
        return True
    else:
        return False

class Solution(object):
    def __init__(self,lines):
        self.L2R = {}
        self.R2L = {}
        for a,b in lines:
            self.L2R[a] = b
            self.R2L[b] = a
        self.N = max(max(self.L2R.keys()),max(self.R2L.keys()))
        self.history = [0]*(self.N+1)
        self.count = 0

    def intersections(self):
        for i in xrange(self.N):
            self.history[i]=self.history[i-1] if i else 0
            L = (i,self.L2R[i]) if i in self.L2R and self.L2R[i]<i else None
            R = (self.R2L[i],i) if i in self.R2L and self.R2L[i]<i else None
            Same = (i,i) if i in self.R2L and self.R2L==i else None
            if L:
                self.count+=self.history[L[0]]-self.history[L[1]+1]
                self.history[i]+=1
            if R:
                self.count+=self.history[R[1]]-self.history[R[0]+1]
                self.history[i]+=1
            if Same:
                self.history[i]+=1
            print self.count
        print self.history
        return self.count
        


def readInput():
    lines = []
    m = int(sys.stdin.readline().strip('\n'))
    for i in range(m):
        l,r = sys.stdin.readline().strip('\n').split(' ')
        lines.append((int(l),int(r)))
    assert(len(lines)==m)
    return lines


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
    #length = 100
    #print all( testing(length) for i in range(3))
    lines = [(0,1),(17,3),(6,15),(8,9),(9,17),(12,14),(15,13)]
    S = Solution(lines)
    result = S.intersections()
    print 'Final Result:' , result
    print bruteFindAll(lines)
