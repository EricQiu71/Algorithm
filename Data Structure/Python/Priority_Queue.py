import heapq

def priority_queue(iterable):
    pq = []
    for value in iterable:
        heapq.heappush(pq, value)
    # heapq.heapify(pq)
    print('initiate:',pq)
    heapq.heappush(pq,10)
    print('push 10:', pq)

    print(f'pop: {heapq.heappop(pq)}', pq)

    print(f'pushpop: {heapq.heappushpop(pq, 15)}', pq)

    print(f'replace: {heapq.heapreplace(pq, 13)}', pq)

    print('nlargest: ',heapq.nlargest(5,pq))
    print('nsmallest: ', heapq.nsmallest(5, pq))

    pq2= heapq.merge([1,3],[2,4])
    for i in pq2:
        print(i)

# def heapsort(iterable):
#     h = []
#     for value in iterable:
#         heapq.heappush(h, value)
#     return [heapq.heappop(h) for i in range(len(h))]
#
# heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
priority_queue([1,4,3,2,8,5,7,6])