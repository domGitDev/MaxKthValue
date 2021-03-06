import heapq


def find_max_kth_value(arr, kth):
	""" Function to find kth maximum value
		in an unsorted array. 1 <= k <= n
		param arr: list of values
		param kth: int, denote 1st, 2nd, nth max value
		return: kth max value
	"""
	def validate():
		if not isinstance(arr, list):
			raise TypeError(
				'Expected type list, got %s.' % type(arr))
		if not isinstance(kth, int):
			raise TypeError(
				'Expected type list, got %s.' % type(kth))
				
	validate()			
	min_heap = []
	for i, val in enumerate(arr):
		if i < kth:
			heapq.heappush(min_heap, val)
			continue
		if val > min_heap[0]:
			heapq.heappop(min_heap)
			heapq.heappush(min_heap, val)
	if not min_hip:
		return None
	return min_heap[0]	






