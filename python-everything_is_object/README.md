# 0. Who am I?

Write the name of the function used to print the type of an object.

# 1. Where are you?

How do you get the variable identifier (which is the memory address in the CPython implementat

### 18. List assignation

**Question:** What does this script print?

```python
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)

### 19. Copy a list object

**Question:** Write a function `def copy_list(a_list):` that returns a copy of a list.  

- The input list can contain any type of objects.  
- Your file should be **maximum 3 lines long**.  
- **No documentation or imports needed.**

**Example usage:**

```python
my_list = [1, 2, 3]
new_list = copy_list(my_list)

print(new_list == my_list)  # True
print(new_list is my_list)  # False
