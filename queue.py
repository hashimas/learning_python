from collections import deque
queue = deque(['Hashim','Ashir','Yusuf'])
queue.append('Aliyu')
queue.append('Ibrahim')
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)