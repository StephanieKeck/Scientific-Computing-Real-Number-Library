Real Number Library – Python
===

Table of Contents
---

- [Synopsis](#synopsis)
- [Prerequisites](#prerequisites)
- [Theory](#theory)
- [Usage](#usage)
- [Example Input and Output](#example-input-and-output)

Synopsis
---

Class project for CS 4328 Scientific Computing at Texas Tech University during the spring semester of 2017. Command-line program written in Python 3 that attempts a faithful implementation of certain real number functions despite computer memory limitations.

Prerequisites 
---

1. Python 3 shell environment

Theory
---

Many real numbers cannot be represented accurately on a computer. For example, the square root of two is irrational and thus has infinitely many nonrepeating digits. Therefore it cannot be represented in the finite space of computer memory. To get around this limitation, we devised the following alternate definitions:

1.  A natural number is a number that can be the cardinal of a finite set.
2.  An integer is the set of natural numbers extended by the set of negative whole numbers.
3.  A fraction is a pair (*i*,*j*) of integers where *j* != 0. We write *i*/*j* for the pair (*i*,*j*). If *i*/*j* and *k*/*l* are fractions, then *i*/*j* = *k*/*l* iff *i***l* = *j***k*.
4.  A rational number is an integer or a fraction. If *r* is a fraction *a*/*b* and *s* is an integer, then *a*/*b* = *s* iff *a* = *b* * *s*.
5.  A real number is a convergent sequence of rational numbers. If *x* is a real number and the limit of *x*(*n*) as *n* approaches infinity is *L*, then *x* represents the number *L*.

In our library, we represented fractions using the `Fraction` class. Real numbers were implemented by defining functions which were to return a function with the signature `int x(int)`. `x(n)` would return the `n`th number in the sequence `x`. For example, a real number representing the integer 2 would be implemented as follows:

```
two = lambda n: Fraction(2,1)
```

Since the limit of any number *c* as *n* approaches infinity is *c*, we know that `two()` represents 2.

The implementation of addition, subtraction, multiplication, and division were informed by [proofs of limit laws](). Central to these proofs was the following definition:

> If *x* is a real number that converges to *L*, then for every *e* > 0, there is a natural number *K* such that for every *n* > *K*, |*x*(*n*)-*L*| < *e*.

For example, the following proof is relevant to addition:

Theorem: If *x* converges to *L*, and *y* converges to *M*, then (*x*(*n*)+*y*(*n*)) converges to (*L*+*M*).
Proof (by deduction rule, 1 |- 3):
1. Suppose i.) *x* converges to *L* and ii.) *y* converges to *M*.  
2. For every *e* > 0, there is a *K* such that for all *n* > *K*, |(*x*(*n*)+*y*(*n*)) - (*L*+*M*)| < *e* (by universal introduction, i |- v).
    1. Suppose *e* > 0.
    2. Choose *K*1 such that for all *n* > *K*1, |*x*(*n*) - *L*| < *e*/2 (by 1i, existential elimination, and the definition of convergence).
    3. Choose *K*2 such that for all *n* > *K*2, |*y*(*n*) - *M*| < *e*/2 (by 1ii, existential elimination and the definition of convergence).
    4. For all *n* > max(*K*1,*K*2), |(*x*(*n*)+*y*(*n*)) - (*L*+*M*)| < *e* (by 2ii, 2iii).
    5. There is a *K* such that for all *n* > *K*, |(*x*(*n*)+*y*(*n*)) - (*L*+*M*)| < *e* (by existential introduction, 2iv).
3. (*x*(*n*)+*y*(*n*)) converges to (*L*+*M*) (by 2).

Therefore we derive the function:

```
def add(x,y): return (lambda n: x(n) + y(n))
```

The implementation of sine is more complicated. We considered the following formulation of Taylor's Theorem:

> Suppose *f*'s *n*th derivative is continuous over the interval [*a*,*b*], that *f*^(*n*+1) exists on [*a*,*b*], and that *x*0 is in the interval [*a*,*b*]. For every *x* in [*a*,*b*] there exists a number *z*(*x*) between *x*0 and *x* such that
>
> *f*(*x*) = *Pn*(*x*) + *Rn*(*x*)
>
> where *Pn*(*x*) = sum from *k*=0 to *n* of (\[*k*th derivative of *f*\](*x*0)/(*k*!))*(*x*-*x*0)^*k* and *Rn*(*x*) = (\[(*n*+1)th derivative of *f*\](*z*(*x*))/(*n*+1)!)*(*x*-*x*0)^(*n*+1).

Here, *Pn*(*x*) is the *n*th Taylor polynomial and *Rn*(*x*) is the remainder or error term. For sine, we determined that

> |*Rn*(*x*)| = |(\[(*n*+1)th derivative of sin\](*z*)/(*n*+1)!)*(*x*-*x*0)^(n+1)| < (1/(*n*+1)!)(*x*-*x*0).

Therefore, to find the sine of a number to a certain number of digits, we merely need to find a number `n` such that the error term *Rn*(*x*) is less than our desired error `eps`. We devised a function `sineQ(x, eps)` which returns the *n*th Taylor polynomial of the sine of *x* where *Rn*(*x*) < `eps`. We proved that if *x* converges to *L*, then sineQ(*x*(*n*), 1/*n*) converges to sin(*L*). Therefore, the `sine` function returns `lambda n: sineQ(x(n), 1/n)`.

Usage
---

Run project1_002.py in your Python 3 shell environment. The functions `add(x, y)`, `mult(x, y)`, `sub(x, y)`, `div(x, y)`, and `sine(x)` are available. Inputs must be functions which have the signature `Fraction x(int)`. Return values will be functions which have the signature `Fraction x(int)`. The utility function `fr(x,y)` can be used in place of `Fraction(x,y)`.

Example Input and Output
---

```
>>> two = lambda n: fr(2,1)
>>> two(5)
Fraction(2, 1)
>>> three = lambda n: fr(3,1)
>>> five = add(two,three)
>>> five(5)
Fraction(5, 1)
>>> six = mult(two,three)
>>> six(1)
Fraction(6, 1)
>>> twoThirds = div(two,three)
>>> twoThirds(1)
Fraction(2, 3)
>>> sineTwo = sine(two)
>>> sineTwo(1)
Fraction(2, 3)
>>> sineTwo(5)
Fraction(14, 15)
>>> sineTwo(50)
Fraction(286, 315)
```
