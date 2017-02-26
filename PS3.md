## Problem1

~~~~python
sequence = [(0,1),(2,3),(0,2),(1,3),(1,2)]
~~~~

This sequence is essentially an oblivious merge sort.

Firstly, (0,1) and (2,3) makes the first half and second half sorted. When merging, we compare and swap (0,2) & (1,3) which is the base case for odd merge and even merge respectively. 

Finally, we swap (1,2) to ensure there is no off-by-one error.

## Problem 2

Suppose we define `flip` in such a way:

~~~~python
def flip(fruits,index1,index2):
	while index1<index2:
		fruits[index1],fruits[index2] = fruits[index2],fruits[index1]
		index1+=1
		index2-=1
	return fruits

assert(flip([1,2,6,5,4,3,7,8,9],2,5) == [1,2,3,4,5,6,7,8,9])
~~~~

My arrange function should appear as follows:

~~~~python
def arrange(fruits):
	if len(fruits)<=2:
        # base case
		return flip(fruits,0,1) if fruits==list('WP') else fruits
	else:
		left = arrange(fruits[:len(fruits)/2])  # T(N/2)
		right = arrange(fruits[len(fruits)/2:]) # T(N/2)
		# invariant: left and right are sorted,
        #            therefore left+right looks like this: P*W*P*W*
		#            so we just need to locate and flip the W*P* part in the middle
		if 'W' not in left:
			return left+right
		leftFilpPoint = left.index('W')
		rightFlipPint = len(left) + ( right.index('W')-1 if 'W' in right else 0 )
		return flip(left+right,leftFilpPoint,rightFlipPint) # O(N)

assert(arrange(list('PWPPWWPPWP'))==list('PPPPPPWWWW'))
~~~~

Time Complexity: T(N) = 2T(N/2) + O(N) = O( N log(N) )

It is a standard divide and conquer algorithm, each level being O(n) and has log(n) levels.

## Problem 3

Proof:

On top of the randomized quick sort, the algorithm described only adds complexity when comparison of A[1] with A[i] happens. Therefore we now look at possible comparisons for A[1] only.

Here is an observatin for any A[i]: A[1] is selected as pivot at depth *d*, thus been compared to *d-1* number of perivous pivots and will be compared to *n/(d^2)* elements as a pivot. The chance for A being selected as pivot at given level *d* is *1/d^2.*  To formalize this observation, we have:

​	*# cost when A[1] selected as pivot at level d = O(n) * d^2*

​	*P ( A[1] selected as pivot | at level d ) =  1 / d^2*.  

​	*#cost c when A[1] not selected as pivot at level d = O(n)*

​	*P (A[1] not selected as pivot | at level d) = (d^2-1) / d^2*

For example: when *d* being 1, which means A[1] is selected as first pivot (it involves A[1] compared to 0 pervious pivots and will be compared to N elements as a pivot), has 1/N chance.

We calculate the expected cost for comparing A[1] at level d:

​	*E ( cost for A[1] | at level d )*

​	*= #cost when A[1] selected as pivot at level d * P ( A[1] selected as pivot | at level *d* ) +

​		*# cost when A[1] not selected as pivot at level d * P (A[1] not selected as pivot | at level d)*

​	= *O(n) * d^2 * 1/d^2 + O(n) * (d^2-1) / d^2*

​	*= O(n) + O(n)*

​	*= O(n)*

We then calculate the expected cost for comparing A[1] at all levels:

​	Since expected level for randomized quick sort is *E( max(d) ) = O( log(n) )*:

​	We sum over d from 1 to *O( log(n) )*, we get:

​		*E ( cost for A[1] )  = E ( cost for A[1] | at level d ) * E ( max(d) )*

​					      *= O(n) * O( log(n) ) = O( n * log(n) )*

Finally, we conclude:

​	*Total complexity < expected complexity for normal quick sort + E( cost for A[1] )*

​				    *= O(n log(n)) + O(n log(n))*

​			            *= O(n log(n))*

End Proof.

## Problem 4



```python
class Floor(object):
	def __init__(self, k):
		self.floor = []
		for _ in range(2**k):
			self.floor.append([0]*(2**k))
		self.count = 1

	def fillAll(self):
		self.fill((0,0),len(self.floor),(1,1))

	def fill(self,topLeft, side, occupied):
		# invariant: "occupied" has to be inside the square
        #	         which is specified by "topLeft" & "side"
		# invariant: "side" has to be 2^k, where k is PosInt
		x,y = topLeft
		ox,oy = occupied
		if side == 2:
			# base case: 2x2 square with 1x1 occupied, trivially fill
			for i in range(x,x+side):
				for j in range(y,y+side):
					if (i,j) != occupied:
						self.floor[i][j] = self.count
			self.count += 1
		else:
			# equally divide square into four subproblems
			# and place one brick to meet rest three subproblem's invariant
			mx,my = x+side/2, y+side/2
			fillPoints = {(mx,my):(mx,my),(mx,my-1):(mx,y),
                          (mx-1,my):(x,my),(mx-1,my-1):(x,y)}
			# "fillPoints" is mapping from division corner
            # to subproblems' topLeft corner
			if ox < mx and oy < my:
				ignore = (mx-1,my-1)
			elif ox < mx and oy >= my:
				ignore = (mx-1,my)
			elif ox >= mx and oy < my:
				ignore = (mx,my-1)
			else:
				ignore = (mx,my)
			for i,j in fillPoints:
				if (i,j) != ignore:
					self.floor[i][j] = self.count
			self.count += 1
			subproblemSide = side/2
			for i,j in fillPoints:
				self.fill(fillPoints[(i,j)],subproblemSide,
                          occupied if (i,j)==ignore else (i,j))
# tests
from collections import Counter
from random import choice
def test(k):
	f = Floor(k,(choice(range(k)),choice(range(k))))
	f.fillAll()
	bricks = Counter([i for row in f.floor for i in row])
	for i in range((4**k-1)/3):
		assert(bricks[i] == 1 if i==0 else 3)
for i in range(1,10):
	for _ in range(10):
		test(i)
```

Recurrence of running time: (assume input has length N instead of NxN)

​	*T(N) = 4T(N/4) + O(N)*

We Observe that the recurrence has *log(N) base 4* levels and each level sums to O(N), since *log(N) base 4* can be written as *O(log(N) base 2)*, the total time complexity is *O(N) * O(log(N)) = O(Nlog(N))*.
