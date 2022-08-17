import heapq

# Construct a Heap
minHeap = []
maxHeap = [-1,-2,-3]
heapq.heapify(minHeap) # 0(n)
heapq.heapify(maxHeap)

# Insert 
heapq.heappush(5, minHeap) # O(log n)

# Get top element
minHeap[0]
-1 * maxHeap[0]

# Delete
heapq.heappop(minHeap)  # O(log n)

# Length
len(minHeap)



