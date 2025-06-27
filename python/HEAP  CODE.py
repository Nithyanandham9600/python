import heapq

import heapq
heap = []
heapq.heappush (heap, 20)
heapq.heappush(heap, 10)
heapq.heappush (heap, 30)
heapq.heappush (heap, 15)


print("Heap after insertion:", heap)

smallest = heapq.heappop(heap)

print("Removed element:", smallest)
print("Heap after deletion:", heap)

sorted_list = []
while heap:
	sorted_list.append(heapq.heappop(heap))

print("Sorted numbers:", sorted_list)

nums = [5, 10, 15, 20]
nums[0], nums[-1] = nums[-1], nums[0]
print("Swapped nums:", nums)