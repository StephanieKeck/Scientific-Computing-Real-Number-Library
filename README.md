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
3.  A fraction is a pair (_i_,_j_) of integers where _j_ != 0. We write _i_/_j_ for the pair (_i_,_j_). If _i_/_j_ and _k_/_l_ are fractions, then _i_/_j_ = _k_/_l_ iff _i_*_l_ = _j_*_k_.
4.  A rational number is an integer or a fraction. If _r_ is a fraction _a_/_b_ and _s_ is an integer, then _a_/_b_ = _s_ iff _a_ = _b_ * _s_.
5.  A real number is a convergent sequence of rational numbers. If _x_ is a real number and the limit of _x_(_n_) as _n_ approaches infinity is _L_, then _x_ represents the number _L_.

In our library, we represented fractions using the `Fraction` class. Real numbers were implemented by defining functions which were to return a function with the signature `int x(int)`. `x(n)` would return the `n`th number in the sequence `x`. For example, a real number representing the integer 2 would be implemented as follows:

```
two = lambda n: Fraction(2,1)
```

Since the limit of any number _c_ as _n_ approaches infinity is _c_, we know that `two()` represents 2.

The implementation of addition, subtraction, multiplication, and division were informed by [proofs of limit laws](). Central to these proofs was the following definition:

> If _x_ is a real number that converges to _L_, then for every _e_ > 0, there is a natural number _K_ such that for every _n_ > _K_, |_x_(_n_)-_L_| < _e_.

For example, the following proof is relevant to addition:

Theorem: If _x_ converges to _L_, and _y_ converges to _M_, then (_x_(_n_)+_y_(_n_)) converges to (_L_+_M_).
Proof (by deduction rule, 1 |- 3):
1.  Suppose a.) _x_ converges to _L_ and b.) _y_ converges to _M_.
2.  For every _e_ > 0, there is a _K_ such that for all _n_ > _K_, |(_x_(_n_)+_y_(_n_)) - (_L_+_M_)| < _e_ (by universal introduction, a |- e).
  a.  Suppose _e_ > 0.
  b.  Choose *K*1 such that for all _n_ > *K*1, |_x_(_n_) - _L_| < _e_/2 (by 1a, existential elimination, and the definition of convergence).
  c.  Choose *K*2 such that for all _n_ > *K*2, |_y_(_n_) - _M_| < _e_/2 (by 1b, existential elimination and the definition of convergence).
  d.  For all _n_ > max(*K*1,*K*2), |(_x_(_n_)+_y_(_n_)) - (_L_+_M_)| < _e_ (by 2b, 2c).
  e.  There is a _K_ such that for all _n_ > _K_, |(_x_(_n_)+_y_(_n_)) - (_L_+_M_)| < _e_ (by existential introduction, 2d).
3.  (_x_(_n_)+_y_(_n_)) converges to (_L_+_M_) (by 2).

Therefore we derive the function:

```
def add(x,y): return (lambda n: x(n) + y(n))
```

The implementation of sine is more complicated. We considered the following formulation of Taylor's Theorem:

> Suppose _f_'s *n*th derivative is continuous over the interval [_a_,_b_], that _f_^(_n_+1) exists on [_a_,_b_], and that *x*0 is in the interval [_a_,_b_]. For every _x_ in [_a_,_b_] there exists a number _z_(_x_) between *x*0 and *x* such that 
> *f*(*x*) = *Pn*(*x*) + *Rn*(*x*)
> where *Pn*(*x*) = sum from *k*=0 to *n* of ((_k_th derivative of _f_)(_x_0)/(_k_!))*(_x_-_x_0)^_k_ and _Rn_(_x_) = (((_n_+1)th derivative of _f_)(_z_(_x_))/(_n_+1)!)*(_x_-_x_0)^(_n_+1).

Here, _Pn_(_x_) is the _n_th Taylor polynomial and _Rn_(_x_) is the remainder or error term. For sine, we determined that

> |_Rn_(_x_)| = |(((_n_+1)th derivative of sin)(_z_)/(_n_+1)!)*(_x_-_x_0)^(n+1)| < (1/(_n_+1)!)(_x_-_x_0)$.

Therefore, to find the sine of a number to a certain number of digits, we merely need to find a number `n` such that the error term _Rn_(_x_)$ is less than our desired error `eps`. We devised a function `sineQ(x, eps)` which returns the _n_th Taylor polynomial of the sine of _x_ where _Rn_(_x_) < `eps`. We proved that if _x_ converges to _L_, then sineQ(_x_(_n_), 1/_n_) converges to sin(_L_). Therefore, the `sine` function returns `lambda n: sineQ(x(n), 1/n)`.

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
