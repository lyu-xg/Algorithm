## Problem 1

Subproblem: `planWork(t,m,s)` returns maxium sum of wage at given year t, job m and at most job-switch-time s. Therefore, the original problem is `planWork(T,m,S)`.

Subproblem dependency:

- planWork(t,m,s) = MAX<sub>for s in S[:s],  for j in m</sub>(planWord(t-1, j, (j==m ? s : s+1)) + W(t,j)) 

Recurrence: 

```java
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
        	for s in S[:s] for j in m)
		wageMax = MAX(relatedSubproblems)
        maxWageJob = ARGMAX(relatedSubproblems)
        maxWages[(t,m,s)] = maxWages
        maxWageJob[(t,m,s)] = maxWageJob
        return result
```

Using Two-Table-Paradigm:

​	We two tables (wageMax and maxWageJob) to store max value and argmax value. 

​	Although our recurrence only depends on max value, we need argmax values to reconstruct 

​	the original path. 

Time complexity: 

​	Number of subproblem: TmS

​	Time Complexity for each subproblem: O(mS)

​	Overall: O(Tm^2S^2)

## Problem 2

