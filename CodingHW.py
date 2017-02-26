# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from collections import defaultdict

def isInter(x,y):
    a,b = x
    c,d = y
    if (a>c and b<d) or (a<c and b>d):
        #print x,y
        return True
    else:
        return False

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
    return result\

class Solution(object):
    def __init__(self, lines):
        self.lines = lines
        self.lines.sort(key=lambda x:x[0])
        self.crossings = defaultdict(set)
        for line in self.lines:
            i,j = getRange(line)
            for n in range(i,j+1):
                self.crossings[n].add(line)
        self.visited = set()

    def recursiveFindAll(self):
        def isInter(x,y):
            a,b = x
            c,d = y
            if x in self.visited or y in self.visited:
                return False
            else:
                return (a>c and b<d) or (a<c and b>d)

        def findLineSet(start,end,lineSet):
            result = 0
            for l in lineSet:
                for i in range(start,end):
                    if self.lines[i] in lineSet:
                        continue
                    if isInter(self.lines[i],l):
                        result += 1
            self.visited.union(lineSet)
            return result + bruteFindAll(lineSet)

        def find(i,j):
            mid = (i+j)/2
            midLines = self.crossings[self.lines[mid][0]]
            midLines = set(i for i in midLines if i not in self.visited)
            self.visited = self.visited.union(midLines)
            print midLines
            if not midLines:
                return 0
            midInters = findLineSet(i,j,midLines)
            print i,j,mid
            return midInters+find(i,mid)+find(mid,j)

        return find(0,len(self.lines)-1)

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
    print lines
    bfa = bruteFindAll(lines)
    S = Solution(lines)
    nfa = S.recursiveFindAll()
    print bfa,nfa
    return bfa==nfa

if __name__=="__main__":
    from random import shuffle
    length = 10
    print all( testing(length) for i in range(100))
