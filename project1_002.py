from fractions import *

def fr(m,n): return Fraction(m,n)

def add(x,y): return (lambda n: x(n) + y(n))

def mult(x,y): return (lambda n: x(n)*y(n))

def sub(x,y): return (lambda n: x(n) - y(n))

def div(x,y): return (lambda n: 0 if y(n) == 0 else fr(x(n), y(n)))

def sine(x):
    def sineQ(x, eps):
        def fact(n):
            if n == 0: return 1
            i = n - 1
            while i > 0:
                n = n * i
                i = i - 1

            return n
        
        def errRange(n, x):
            return abs(fr(x ** (n+1), fact(n+1)))

        def nthDerivativeOfSineZero(n):
            values = [0, 1, 0, -1]
            return values[n % 4]

        def findnSmallerThan(x, eps):
            n = 1
            while errRange(n, x) > eps:
                n = n + 1

            return n

        n = findnSmallerThan(x, eps)
        sum = 0
        i = 0

        while i <= n:
            sum = sum + fr(nthDerivativeOfSineZero(i) * x ** i, fact(i))
            i = i + 1

        return sum

    return lambda n: sineQ(x(n), 1/n)
