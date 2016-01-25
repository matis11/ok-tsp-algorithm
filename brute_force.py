import datetime
import sys

visited = []
graph = []
path = []
size = 0
s1 = []
s2 = []
s1_index = 0
s2_index = 0
summary = 0
v0 = 0
max_length = sys.maxsize


def bf_load_graph(_graph):
    global graph, size
    graph = _graph
    size = len(graph)
    for i in range(0, size):
        visited.append(False)
        s2.append(0)
        s1.append(0)
        path.append(size * [""])


def hamilton_cycle(node, node_size):
    global s2, s2_index, visited, summary, v0, max_length, s1, s1_index
    s2[s2_index] = node
    s2_index += 1

    if s2_index < node_size:
        visited[node] = True
        for u in range(0, size):
            if graph[node][u] != 0 and not visited[u]:
                summary += graph[node][u]
                hamilton_cycle(u, size)
                summary -= graph[node][u]
        visited[node] = False
    else:
        if graph[v0][node] != 0:
            summary += graph[node][v0]
            if summary < max_length:
                max_length = summary
                for u in range(0, s2_index):
                    s1[u] = s2[u]
                s1_index = s2_index
            summary -= graph[node][v0]
    s2_index -= 1


def brute_force():
    edges = ""
    start_time = datetime.datetime.now()

    hamilton_cycle(v0, size)

    end_time = datetime.datetime.now()
    time = end_time - start_time
    print("BruteForce finished in: " + str(time.total_seconds()) + " sec.")

    if s1_index != 0:
        s1.append(v0)
        for i in range(0, s1_index):
            print(str(s1[i]) + " TO " + str(s1[i + 1]))
            path[s1[i]][s1[i + 1]] = "path"
            path[s1[i + 1]][s1[i]] = "rev-path"
        print("suma = " + str(max_length))
    print("time = " + str(time))
    return [create_paths(), max_length, time]


def create_paths():
    edges = ""
    for i in range(0, size):
        for j in range(i + 1, size):
            if path[i][j] == "path" or path[j][i] == "rev-path":
                edges += "{from: " + str(i) + ", to: " + str(j) + ", label: '" + str(
                    graph[i][j]) + " km', arrows:'to', color: '#F22613', font:{size:20}},"
            elif path[i][j] == "rev-path" or path[j][i] == "path":
                edges += "{from: " + str(j) + ", to: " + str(i) + ", label: '" + str(
                    graph[j][i]) + " km', arrows:'to', color: '#F22613', font:{size:20}},"
            elif graph[i][j] != 0:
                edges += "{from: " + str(i) + ", to: " + str(j) + ", label: '" + str(
                    graph[i][j]) + " km', color: '#2B7CE9'},"
    return edges
