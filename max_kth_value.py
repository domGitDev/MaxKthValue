import heapq


def max_kth_value(arr, kth):
	
	min_heap = []
	for i, val in enumerate(arr):
		if i < kth:
			heapq.heappush(min_heap, val)
			continue
		if val > min_heap[0]:
			heapq.heappop(min_heap)
			heapq.heappush(min_heap, val)
	return min_heap[0]


data = [2, 1, 3, 1, 2]
print max_kth_value(data, 1)

