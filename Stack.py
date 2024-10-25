
In Python, a stack can be implemented using a few different approaches, depending on the requirements. A stack is a data structure that follows the LIFO (Last In, First Out) principle, where the last element added is the first one to be removed.



Python doesn't have a built-in stack data structure, but you can implement one easily using lists or the collections.deque module.


Method 1: Using a List

In Python, you can use a list to implement a stack because it supports appending and removing elements efficiently at the end.


stack = []

stack.append('A')  # Stack: ['A']
stack.append('B')  # Stack: ['A', 'B']
print("Stack after pushing:", stack)

top_element = stack.pop()  # Removes 'B'

print("Stack after popping:", stack)   # Stack: ['A']



Pros of using a List:

Simple to use and understand.
Built-in append() and pop() make it easy to implement stack operations.
Cons:

Removing from the beginning of the list (pop(0)) can be slow (O(n)) because elements need to be shifted.


###############################   Method 2: Using collections.deque  ###############################




from collections import deque

# Creating a stack using deque
stack = deque()

stack.append('A')  # Stack: deque(['A'])
stack.append('B')  # Stack: deque(['A', 'B'])

top_element = stack.pop()  # Removes 'B'

print("Stack after popping:", stack)   # Stack: deque(['A'])










































