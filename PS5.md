### Problem 1
#### 1.1
Let *k.v* store the size (number of node) of subtree rooted at *k*.

```python
def Rank(k):
	return Smaller(root, k)
	
def Smaller(n, k):
	// given subtree n, and target k
	// return how many nodes in n are smaller than k
	// in other words, Rank of k in the subtree n
	if not n:
		return 0
	if k < n.value:
		return Smaller(n.left, k)
	elif k > n.value:
		return n.left.v + 1 + Smaller(n.right, k)
	else:
		return n.left.v
```
Where default value of *node.v* is 0 when *node* is null.

#### 1.2

INSERT should increase every node's *v* value by 1 along the search path.

When creating new node, set *v* to 1.

#### 1.3

Left Rotate:

*k* becomes child of its original right child, hence *k.v* losing the size of the right most subtree.

```
newLeftRotate(k):
	k.rightchild.v = k.v
	k.v -= k.rightchild.rightchild.v
	normalLeftRotate(k)
```

Right Rotate:

*k* becomes child of its original left child, hence *k.v* losing the size of the left most subtree.

```python
newRightRotate(k):
	k.leftchild.v = k.v
	k.v -= k.leftchild.leftchild.v
	normalRightRotate(k)
```
### Problem 2
Problem formalized to:
##### Given: 
- *k* is an n-dimensional binary vector.
- *a* is an n-dimensional random binary vector.
- *h(a,k) = a·k modulo 2*

##### Prove that
- *Pr(h(a,k)=h(a,k')) = 1/2*
- where for a fixed pair of unequal *k* and *k'*, a random *a* is assigned, the probability property holds for all such fixed pairs.

#### Proof

Observation1: Ɐ<sub>i∈[1,|a|]</sub> Pr(a<sub>i</sub>=1) = 1/2 (Pr of any given digit of *a* being 1 is 1/2)

Corollary1: *Pr ( Ɐm ∈ [1, |a|]: ∑<sub>i∈[1,|a|]</sub> a<sub>i</sub> = m ) = C(|a|,m)(1/2)<sup>|a|</sup>*

Corollary2: *Pr ( Ɐm ∈ [1, |x|]: ∑<sub>i∈[1,|x|]</sub> x<sub>i</sub> = m ) = C(|x|,m)(1/2)<sup>|x|</sup>*
where x is non-empty subset of *a*

Let Z(x) denote number of '1's in vector *v* (which is the dot product of v and all-one-vector).

Corollary2 can then be rewritten as *Pr ( Ɐm ∈ [1, |a|]: Z(x) = m ) = C(|x|,m)(1/2)<sup>|x|</sup>*

Corollary3: *Pr ( Z(x) mod 2 = 1 ) <=> ∑<sub>m ∈ [1, |x|] | m mod 2 = 1</sub> Pr ( Ɐ: Z(x) = m ) <=> ∑<sub>m ∈ [1, |x|] | m mod 2 = 1</sub> C(|x|,m)(1/2)<sup>|x|</sup> <=> (1/2)∑<sub>m ∈ [1, |x|]</sub> C(|x|,m)(1/2)<sup>|x|</sup> <=> (1/2)·1 <=> 1/2*.

Now, to prove *Pr(h(a,k)=h(a,k')) = 1/2*, that is to prove:

*Pr(ak - ak' mod 2 = 1) = 1/2*

<=> *Pr(a(k - k') mod 2 = 1) = 1/2*

<=> *Pr(av mod 2 = 1) = 1/2* (let *v = k - k'*, because *k≠k'*, we have *v≠0⃗*.)

Note that *av* is actually Z(some non-empty subset of *a*) which is Z(x), so we apply Corollary3 to prove the above equation.

End of Proof.


### Problem 3

Using hash function h<sub>a</sub>(k) = ∑<sub>i∈[1,|a|]</sub> a<sub>i</sub>k<sub>i</sub> mod 2.

Set t to a prime larger than 1000n<sup>2</sup>

We then have Pr ( ∃ x ≠ y: h<sub>a</sub>(x) = h<sub>a</sub>(y) ) < 1/1000 (n-hash claim)

Procedure:

```python
def check(A):
	// given initialzed all-zero array B 
	for i in A:
		if B[h(i)]:
			return False
		else:
			B[h(i)] = 1
	return True
```





