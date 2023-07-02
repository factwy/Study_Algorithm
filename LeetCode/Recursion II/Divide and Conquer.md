# Divide and Conquer

**Benefits**
- know some classical examples of divide-and-conquer algorithms
- know how to apply a pseudocode template to implement the divide-and-conquer algorithms
- know a theoretical tool called master theorem to calculate the time complexity for certain types of divide-and-conquer algorithms

## A D&C Introduction
- Divide and conquer(D&C) algorithm works by **recursively** breaking the problem down into **two** or more subproblems of the same or related type, until these subproblems become simple enough to be solved directly.
- Then one combines the results of subproblems to form the final solution.

> 1. **Divide** : Divide the problem S into a set of subproblems {S1, S2, ... , Sn} where n >= 2
> 2. **Conquer** : Solve each subproblem recursively.
> 3. **Combine** : Combine the results of each subproblem.

 ![image](https://github.com/factwy/Study_Algorithm/assets/52695468/d08c6663-f8bf-49c3-ab21-3c44884fd3fe)
 [**Fig** - General Steps involved in Divide-and-Conquer Algorithms](https://leetcode.com/explore/learn/card/recursion-ii/470/divide-and-conquer/2897/)

## A Merge Sort
### Intuition
- approaches to implement the merge sort algorithm : **top down** and **bottom up**
> 1. **Divide** : Divide the given unsorted list into several sublists.
> 2. **Conquer** : Sort each of the sublists recursively.
> 3. **Combine** : Merge the sorted sublists to produce new sorted list.

### Top-down Approach
> 1. Divide the list into two sublists.
> 2. Recursively sort the sublists in the previous step.
> 3. Merge the sorted sublists in the above step repeatedly to obtain the final list of sorted elements.

- **time complexity** : O(NlogN)
- **space complexity** : O(N)

## P Sort_an_Array.py
```python
# 912. Sort an Array
# difficulty : medium
# algorithm : recursion, merge sort
# Runtime : 1966 ms (68.5%), Memory : 25.1 MB (44.39%)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # top-down approach
        
        def divide(self, arr):
            if len(arr) <= 1:
                return arr
            
            divide_size = len(arr) // 2
            left_arr = divide(self, arr[:divide_size])
            right_arr = divide(self, arr[divide_size:])
            
            return conquer(self, left_arr, right_arr)
            
            
        def conquer(self, left, right):
            left_index = right_index = 0
            sorted_arr = []
            
            while left_index < len(left) and right_index < len(right):
                if left[left_index] < right[right_index]:
                    sorted_arr.append(left[left_index])
                    left_index += 1
                else:
                    sorted_arr.append(right[right_index])
                    right_index += 1
                    
            sorted_arr.extend(left[left_index:])
            sorted_arr.extend(right[right_index:])
            
            return sorted_arr
        
        return divide(self, nums)
```

## A D&C Template
- Template
> 1. **Divide.** Divide the problem S into a set of subproblems: {S1, S2, ..., Sn} where n >= 2
> 2. **Conquer.** Solve each subproblems recursively
> 3. **Combine.** Combine the results of each subproblem
