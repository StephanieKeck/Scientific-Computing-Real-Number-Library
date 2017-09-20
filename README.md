Real Number Library – Python
===

Synopsis
---

Class project for CS 4328 Scientific Computing at Texas Tech University during the spring semester of 2017. Command-line program written in Python 3 that XXX. 

Prerequisites 
---

1. Python 3 shell environment

Detailed Explanation
---

Many real numbers cannot be represented accurately on a computer. For example, $\sqrt{2}$ is irrational and thus has infinitely many nonrepeating digits. Therefore it cannot be represented in the finite space of computer memory. To get around this limitation, we devised the following alternate definitions:

1.  A natural number is a number that can be the cardinal of a finite set.
2.  An integer is the set of natural numbers extended by the set of negative whole numbers.
3.  A fraction is a pair $(i,j)$ of integers where $j\neq 0$. We write $\fraq{i}{j}$ for the pair $(i,j)$. If $\frac{i}{j}$ and $\frac{k}{l}$ are fractions, then $\frac{i}{j} =_{\textrm{frac}} \frac{k}{l}$ iff $i\cdot l = j\cdot k$.
4.  A rational number is an integer or a fraction. If $r$ is a fraction $\frac{a}{b}$ and $s$ is an integer, then $\frac{a}{b} = s$ iff $a = b\cdot s$.
5.  A real number is a convergent sequence of rational numbers. If $x$ is a real number and $\lim_{n\rightarrow \inf}x(n) = L$, then x represents $L \in R$.

In our library, we represented fractions using the `Fraction` class. Real numbers were implemented by defining functions which were to return a function with the signature `int x(int)`. `x(n)` would return the `n`th number in the sequence `x`. For example, a real number representing the integer 2 would be implemented as follows:

```
def two(): return (lambda n: Fraction(2,1))
```

Since $\lim_{n\rightarrow \inf}c = c$, we know that `two()` represents 2.

The implementation of addition, subtraction, multiplication, and division were informed by [proofs of limit laws](). Central to these proofs was the following definition:

> If $x$ is a real number that converges to $L$, then for every $e\gt 0$, there is a natural number $K$ such that for every $n\gt K$, $\abs{x_n - L} \lt e$.

For example, the following proof is relevant to addition:

Theorem: If $x$ converges to $L$, and $y$ converges to $M$, then $(\lambda n\ldot x_n + y_n)$ converges to $(L+M)$.
Proof (by deduction rule, 1 |- 3):
1.  Suppose a.) $x$ converges to $L$ and b.) $y$ converges to $M$.
2.  For every $e\gt 0$, there is a $K$ such that for all $n\gt K$, $\abs{(\lambda n\ldot x_n + y_n) - (L+M)}\lt e$ (by universal introduction, a |- e).
  a.  Suppose $e>0$.
  b.  Choose $K_1$ such that for all $n\gt K_1$, $\abs{\lambda n\ldot x_n - L} \lt \frac{e}{2}$ (by 1a, existential elimination, and the definition of convergence).
  c.  Choose $K_2$ such that for all $n\gt K_2$, $\abs{\lambda n\ldot y_n - M} \lt \frac{e}{2}$ (by 1b, existential elimination and the definition of convergence).
  d.  For all $n\gt \textrm{max}(K_1,K_2)$, $\abs{(\lambda n\ldot x_n + y_n) - (L+M)}\lt e$ (by 2b, 2c).
  e.  There is a $K$ such that for all $n\gt K$, $\abs{(\lambda n\ldot x_n + y_n) - (L+M)}\lt e$ (by existential introduction, 2d).
3.  $(\lambda n\ldot x_n + y_n)$ converges to $(L+M)$ (by 2).

Therefore we derive the function:

```
def add(x,y): return (lambda n: x(n) + y(n))
```

Sine is implemented with guarantees on accuracy. If `x` is a real number, `sine(x)(n)` will return the sine of `x` accurate to `n` digits. The implementation of `sine(x)` is based on the following formulation of Taylor's Theorem:

> Suppose $f$'s $n$th derivative is continuous over the interval $[a,b]$, that $f^{(n+1)}$ exists on $[a,b]$, and that $x_0 \in [a,b]$. For every $x\in [a,b]$ there exists a number $z(x)$ between $x_0$ and $x$ such that 
> $f(x) = P_n(x) + R_n(x)$
> where $P_n(x) = \sum_{k=0}^n \frac{f^{(k)}(x_0)}{k!}(x-x_0)^k$ and $R_n(x) = \frac{f^{(n+1)}(z(x))}{(n+1)!}(x-x_0)^{(n+1)}$.

Here, $P_n(x)$ is the $n$th Taylor polynomial and $R_n(x)$ is the remainder or error term. For sine, we determined that

> $\abs{R_n(x)} = \abs{\frac{\textrm{sin}^{(n+1)}(z)}{(n+1)!}(x-x_0)^{(n+1)} \le \frac{1}{(n+1)!}(x-x_0)$.

Therefore, to find the sine of a number to a certain number of digits, we merely needed to find a number `n` such that the error term $R_n(x)$ was less than our desired error `eps`. The function 
