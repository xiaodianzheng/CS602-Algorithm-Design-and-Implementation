import sys
import heapq


def construct_graph(n, roadmap, qrtn, spaceship):
    graph = {}
    for city_id in range(1, n + 1):
        graph[(city_id, 'g')] = {}
        graph[(city_id, 'o')] = {}
        graph[(city_id, 'r')] = {}
        graph[city_id, 'o'][city_id, 'r'] = qrtn[city_id][0]
        graph[city_id, 'g'][city_id, 'o'] = qrtn[city_id][1]
    for key, cost in roadmap.items():
        start = key[0]
        end = key[1]
        if cost > 0:
            if start not in spaceship:
                graph[end, 'g'][start, 'g'] = cost
                graph[end, 'o'][start, 'o'] = cost
            if end not in spaceship:
                graph[start, 'g'][end, 'g'] = cost
                graph[start, 'o'][end, 'o'] = cost
        else:
            if start not in spaceship:
                graph[end, 'o'][start, 'g'] = -cost
                graph[end, 'r'][start, 'o'] = -cost
            if end not in spaceship:
                graph[start, 'o'][end, 'g'] = -cost
                graph[start, 'r'][end, 'o'] = -cost
    return graph


def dijkstra(graph, spaceship):
    visited = {}
    waited = []
    for city_id in spaceship:
        visited[city_id, 'g'] = 0
        heapq.heappush(waited, (0, (city_id, 'g')))
    nodes = set(graph.keys())
    while nodes and waited:
        current_cost, current_city = heapq.heappop(waited)
        try:
            while current_city not in nodes:
                current_cost, current_city = heapq.heappop(waited)
        except IndexError:
            break
        nodes.remove(current_city)
        for next_city, next_cost in graph[current_city].items():
            cost = current_cost + next_cost
            if next_city not in visited or cost < visited[next_city]:
                visited[next_city] = cost
                heapq.heappush(waited, (cost, next_city))
    res = [visited[i, 'g'] for i in range(1, n+1)]
    return res


def escape(n, roadmap, qrtn, spaceship):
    graph = construct_graph(n, roadmap, qrtn, spaceship)
    res = dijkstra(graph, spaceship)
    return res


n = int(sys.stdin.readline())
roadmap = {}
s = sys.stdin.readline().split()
for t in s:
    u = t.split(':')
    roadmap[int(u[0]), int(u[1])] = int(u[2])
qrtn = [0] * (n + 1)
s = sys.stdin.readline().split()
i = 1
for t in s:
    u = t.split(':')
    qrtn[i] = int(u[0]), int(u[1])
    i += 1
spaceship = [int(t) for t in sys.stdin.readline().split()]
print(' '.join([str(i) for i in escape(n, roadmap, qrtn, spaceship)]))