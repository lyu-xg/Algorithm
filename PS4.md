## Problem 1

####Subproblem:
 `planWork(t,m,s)` returns maxium sum of wage at given year t, job m and at most job-switch-time s. Therefore, the original problem is `planWork(T,m,S)`.

####Subproblem dependency:

`planWork(t,m,s)` = MAX<sub> j∈[0,m)</sub>(`planWord(t-1, j, (j==m ? s : s-1)) + W(t,j)`) 

####Base case: 

1. if s > S: return 0 
2. elseif t = 1 and m = 0: return W(1,0) 
3. elseif t = 1 and m!= 0: return 0

####Using Two-Table-Paradigm:

​We use two tables (`wageMax` and `maxWageJob`) to store max value and argmax value. 

Although our recurrence only depends on max value, we need argmax values to reconstruct the original path using `m` value in `maxWageJob` trivially. 

####Time complexity: 

​Number of subproblems: O(T m S)

Time Complexity for each subproblem: O(m)

Overall time complexity: O(T m<sup>2</sup> S)

## Problem 2

####Subproblem:

`cut(start,end,breakpoints)` returns minimal time to cut a list of breakpoints `breakpoints` on a rod from `start` to `end` (its length being `end-start`). The original problem can be reframed as `cut(0,n,L)`.

#### Subproblem Recurrence:

`cut(start,end,breakpoints)` = MIN<sub>b ∈ breakpoints</sub> (
`cut(start,b,smallers)+cut(b,end,largers)`)+`(end-start)`

Where `smallers` denote list of elements in `breakpoints` that are smaller than `b`, and `largers` denote list of elements in `breakpoints` that are larger than `b`. 

Explanation: we try to cut all the breakpoints, and find the MIN of what's left of the problem, we then add the cost of cutting the rod which is the length `end-start`.

####Base Case:
`cut(i,j,0) = 0` for all `i` and `j`.

####Using Two-Table-Paradigm:

​We use two tables (`resultTable` and `argminTable`) to store min value and argmin value. 

Although our recurrence only depends on min value, we need argmin values to reconstruct the original path using stored `b` value in `argminTable` trivially. 

####Time Complexity

Number of subproblems: m! = O(m<sup>2</sup>) (combination of start and end, each ∈ [0,m).)

Time complexity for each subproblem: O(m)

Overall time complexity: O(m<sup>3</sup>)

##Problem 3
####Subproblem:
`count(i)` returns number of sequences of length `i` from alphabet {A, B, C} such that no two adjacent symbols are equal.
####Recurrence:
`count(i)` = `count(i-1) * 2` 

- explanation: for each sequence of length n-1, we can add two other character

####Base case:
`count(1)` = 3 (length of alphabet)
####solving the recurrence: 
`count(i) = 3 * pow(2, i-1)`
####Time Complexity:
Number of subproblems: n

Time complexity for each subproblem: O(1)

Overall: O(n)
##Problem4
####Given:

- Let `K` denote given range {1, ..., k}.
- Let `X` denote subset of `K`.
- Let `S` denote all given subsets {S<sub>1</sub>, ..., S<sub>n</sub>}.
- Let `C(X)` denote `SUM(c(i) for i in X)` (total cost of X).

####Subproblem:

`MC(X)` is the Minimun-Cost collection of subsets that covers `X` (subset of [1,k]).

####Recurrence:

- Let `M(X)` = ARGMIN<sub>`x ∈ X`</sub> ( `C(MC(X-{x}) ∪ MC({x})) - C(MC(X-{x}) ∩ MC({x}))` )
- `MC(X)` = `MC(X - {M(X)}) ∪ MC({M(X)})`

####Base case:
when length of `X` is 1:

- `MC(X)` = { ARGMIN<sub>`s∈S`</sub>( `X⊂s ? c(s) : +infinity` ) }


####Time Complexity:
Number of subproblems: O(2<sup>k</sup>)

Time complexity for each subproblem: O(kn)

Overall Time Complexity: O(2<sup>k</sup>kn)








