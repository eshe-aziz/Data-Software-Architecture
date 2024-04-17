from collections import deque

queue = deque()
queue.appendleft("First")
queue.appendleft("Second")
queue.appendleft("Third")
queue.appendleft("Fourth")
print(queue.popleft())