## Problem 1

####Subproblem:
 `planWork(t,m,s)` returns maxium sum of wage at given year t, job m and at most job-switch-time s. Therefore, the original problem is `planWork(T,m,S)`.

####Subproblem dependency:

`planWork(t,m,s)` = MAX<sub>s ∈ S[:s], j ∈ [0,m)</sub>(`planWord(t-1, j, (j==m ? s : s+1)) + W(t,j)`) 

####Recurrence: 

```python
def planWork(t,m,s):
	if (t,m,s) in maxWages:
		return maxWages[(t,m,s)]
	if s > S:
		return 0
	else if t == 1:
		if m == 0: 
			return W(1,0)
		else:
			return 0
	else:
		relatedSubproblems = 
        	(planWord(t-1, j, (j==m ? s : s+1)) + W(t,j)
        	for s in S[:s] for j in range(m))
		wageMax = MAX(relatedSubproblems)
        maxWageJob = ARGMAX(relatedSubproblems)
        maxWages[(t,m,s)] = maxWages
        maxWageJob[(t,m,s)] = maxWageJob
        return result
```

####Using Two-Table-Paradigm:

​We two tables (`wageMax` and `maxWageJob`) to store max value and argmax value. 

Although our recurrence only depends on max value, we need argmax values to reconstruct the original path using `m` entry in `maxWageJob` trivially. 

####Time complexity: 

​Number of subproblem: T \* m \* S

Time Complexity for each subproblem: O(m * S)

Overall: O(T m<sup>2</sup> S<sup>2</sup>)

## Problem 2

####Subproblem:

`cut(start,end,breakpoints)` returns minimal time to cut a list of breakpoints `breakpoints` on a rod from `start` to `end` (its length being `end-start`). The original problem can be reframed as `cut(0,n,L)`.

#### Subproblem dependency

`cut(start,end,breakpoints)` = MIN<sub>b ∈ breakpoints</sub> (
`cut(start,b,smallers)+cut(b,end,largers)`)+`(end-start)`

Where `smallers` denote list of elements in `breakpoints` that are smaller than `b`, and `largers` denote list of elements in `breakpoints` that are larger than `b`. 

Explanation: we try to cut all the breakpoints, and find the MIN of what's left of the problem, we then add the cost of cutting the rod which is the length `end-start`.

####Recurrence
```java
def cut(start,end,breakpoints):
	if len(breakpoints) is 0:
		return 0
	if (start,end,breakpoints) not in resultTable:
		possibleCosts = (
			(cut(start,b,[x for x in breakpoints if x<b])+
			 cut(b,end,[x for x in breakspoints if x>b])+
			 end-start)
			for b in breakpoints)
		resultTable[(start,end,breakpoints)] = min(possibleCosts)
		argminTable[(start,end,breakpoints)] = argmin(possibleCosts)
	return resultTable[(start,end,breakpoints)] 
```
####Using Two-Table-Paradigm:

​We two tables (`resultTable` and `argminTable`) to store min value and argmin value. 

Although our recurrence only depends on min value, we need argmin values to reconstruct the original path using stored `b` entry in `argminTable` trivially. 














