from collections import deque
queue = deque(["Eric", "John", "Michael"])
print(queue)
queue.append("Terry")
queue.append("graham")
print(queue.popleft())

print(queue.popleft())

print(queue)