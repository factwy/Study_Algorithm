# Solve Problems Recursively

### A Solve Problems Recursively
a tree can be defined recursively as a node that includes a value and a list of references to children nodes

#### "Top-down" Solution
top-down solution can be considered as a kind of pre-order traversal

```
# top_down(root, params)
1. return sepcific value for null node
2. update the answer if needed
3. left_ans = top_down(root.left, left_params)
4. right_ans = top_down(root.right, right_params)
5. return the answer if needed
```

```python
def maximum_depth(root, depth):
    if root == null:
        return
    if root.left == null and root.right == null:
        answer = max(answer, depth 
    maximum_depth(root.left, depth+1)
    maximum_depth(root.right, depth+1)
```

#### "Bottom-up" Solution
bottom-up solution can be regarded as a kind of post-order traversal

```
# bottom_up(root)
1. return sepcific value for null node
2. left_ans = bottom_up(root.left)
3. right_ans = bottom_up(root.right)
4. return answer
```

```python
def maximum_depth(root):
    if root == null:
        return 0
    left_depth = maximum_depth(root.left)
    right_depth = maximum_depth(root.right)
    return max(left_depth, right_depth) + 1
```

#### Conclusion

1. when we recommended to use "top-down"
>  - can determine some parameters to help the node know its answer
>  - can use these parameters and the value of the node itself to determine what should be the parameters passed to its children

2. when we recommended to use "bottom-up"
>  - can calculate the answer of that node when we know the answer of its children
