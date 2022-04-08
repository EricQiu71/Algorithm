# Python stack can be implemented using the deque class from the collections module. Deque is preferred over the list
# in the cases where we need quicker append and pop operations from both the ends of the container, as deque provides
# an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity. The
# same methods on deque as seen in the list are used, append() and pop().
# Python program to
# demonstrate stack implementation
# using collections.deque

from collections import deque

stack = deque()

# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')
stack.appendleft('z')

print('Initial stack:')
print(stack)

# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.popleft())

print('\nStack after elements are popped:')
print(stack)

# uncommenting print(stack.pop())
# will cause an IndexError
# as the stack is now empty