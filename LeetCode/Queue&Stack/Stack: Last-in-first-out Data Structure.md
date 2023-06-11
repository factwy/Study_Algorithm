# Stack: Last-in-first-out Data Structure

## A Last-in-first-out Data Structure
- the newest element added to the queue will be processed first
- the insert operation is called **push** : a new element is always added at the end of the stack
- the delete operation is called **pop** : remove the last element

## P Min_Stack.py
```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []
        
    def push(self, val: int):
        self.stack.append(val)
        if not self.minimum:
            self.minimum.append(val)
        else:
            if val <= self.minimum[-1]:
                self.minimum.append(val)
        return None

    def pop(self):
        if self.stack.pop() == self.minimum[-1]:
            self.minimum.pop()
        return None

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minimum[-1]
```

## P Valid_Parentheses.py
```python
class Solution:
    def isValid(self, s: str):
        arr = []
        
        check = ['(', '{', '[', ')', '}', ']']
        
        for character in s:
            character_index = check.index(character)
            
            if character_index < 3:
                arr.append(character_index)
            else:
                if not arr:
                    return False
                
                character_index -= 3
                if arr.pop() != character_index:
                    return False
                
        if arr:
            return False
        return True
```
## P Daily_Temperatures.py
```python

```

## P Evaluate_Reverse_Polish_Notation.py
```python
class Solution:
    def evalRPN(self, tokens: List[str]):
        stack = []
        oper = set(["+", "-", "*", "/"])
        
        for t in tokens:
            if t in oper:
                num1, num2 = stack.pop(), stack.pop()
                number = 0
                
                if t == "+":
                    number = num1 + num2
                elif t == "-":
                    number = num2 - num1
                elif t == "*":
                    number = num1 * num2
                else:
                    number = int(num2 / num1)
                    
                stack.append(number)
                
            else:
                stack.append(int(t))
                
        return stack[-1]
```
