# Lat in First Out (Lifo)

stack = []

stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)

stack.pop()  # remove o último elemento (50)

print(stack)  # imprime a pilha restante

# print(stack[-1])

# Stack (LIFO)
#-----------------
# 30  <-- Top
# 20
# 10
# ---------------


# First In First Out = Queues
# Queue (FIFO)
# ----------------------
# front --> [A, B, C, D] --> rear

from collections import deque

queue = deque()
queue.append('A')
queue.append('B')
queue.append('C')
queue.append('D')
print(queue.popleft())