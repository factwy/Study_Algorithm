# Memoization

## A Duplicate Calculation in Recursion
- To eliminate the duplicate calculation, one of the ideas would be to **store** the intermediate results in the cache so that we could reuse them later without re-calculation
- [Memoization](https://en.wikipedia.org/wiki/Memoization) is an optimication technique used primarily to **speed up** computer programs by **storing** the results of expensive function calls and returning the cached result when the same inputs occur again.

## P Fibonacci_Number.py
```python
class Solution:
    def fib(self, n: int) -> int:
        fibos = [-1] * (n+1)
        
        def recursion(self, x):
            if fibos[x] != -1:
                return fibos[x]
            if x == 0 or x == 1:
                fibos[x] = x
                return fibos[x]
            
            fibos[x] = recursion(self, x-1) + recursion(self, x-2)
            return fibos[x]
            
        return recursion(self, n)
```

## P Climbing_Stairs.py
```python

```
