'''Given an array, reduce the array to a single element with minimum cost. For reducing, remove two elements from the array, 
add those two numbers and keep the sum back in the array. 
The cost of each operation is the sum of the elements removed in that step.'''


from heapq import heapify, heappush, heappop

arr = [5,5,5,5]

heapify(arr)

cost = 0

while len(arr)>1:
    elem1 = heappop(arr)
    elem2 = heappop(arr)
    val = elem1 + elem2
    cost += val
    heappush(arr, val)
print(cost)