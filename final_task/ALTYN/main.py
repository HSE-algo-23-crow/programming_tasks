import heapq


def dijkstra(graph, start):
    n = len(graph)
    distances = {node: float('inf') for node in range(n)}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, u = heapq.heappop(priority_queue)

        if current_distance > distances[u]:
            continue

        for neighbor, weight in graph[u]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return [distances[node] for node in range(n)]


def main():
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: [(4, 3)],
        4: []
    }

    start_vertex = 0
    print(dijkstra(graph, start_vertex))


if __name__ == '__main__':
    main()