stack = []
stack.append(10)
stack.append(20)
stack.append(38)

print("Stack now:", stack)
stack.pop()
print("After pop:", stack)

queue = [10]
queue.append(10)
queue.append(20)
queue.append(30)
print("Queue after insertion:", queue)
removed = queue.pop(0)
print("Removed element:", removed)
print("Queue after deletion:", queue)
queue.sort()
print("Sorted queue:", queue)
queue[0], queue [1] = queue [1], queue [0]
print("Queue after swapping:", queue)

