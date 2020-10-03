import sys
import heapq


def project_selection(c, k):
    max_heap = []
    min_heap = []
    for ci in cr:
        if ci[0] <= c:
            heapq.heappush(max_heap, ci[0] - ci[1])
        else:
            heapq.heappush(min_heap, (ci[0], ci[1]))
    for i in range(k):
        if len(max_heap) == 0:
            return "impossible"
        new_project_profit = heapq.heappop(max_heap)
        c -= new_project_profit
        while len(min_heap) != 0 and c > min_heap[0][0]:
            cur = heapq.heappop(min_heap)
            max_heap.append(cur[0] - cur[1])
            heapq.heapify(max_heap)
    return c


a = [int(s) for s in sys.stdin.readline().split()]
cr = [[int(t) for t in s.split(':')] for s in sys.stdin.readline().split()]
for _ in range(a[1]):
    b = [int(s) for s in sys.stdin.readline().split()]
    c, k = b[0], b[1]
    print(project_selection(c, k))
