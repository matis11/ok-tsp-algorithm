import datetime
import random

visited = []
graph = []
path = []
size = 0
s1 = []
s1_index = 0
summary = 0
heuristic_mode = 0


def hm_load_graph(_graph):
    global visited, graph, path, size, s1, s1_index, summary, heuristic_mode
    visited = []
    graph = []
    path = []
    size = 0
    s1 = []
    s1_index = 0
    summary = 0
    heuristic_mode = 0
    graph = _graph
    size = len(graph)
    for i in range(0, size):
        visited.append(False)
        s1.append(0)
        path.append(size * [""])


def hamilton_cycle(node):
    global visited, summary, s1, s1_index
    s1[s1_index] = node
    s1_index += 1
    visited[node] = True
    node_tuples = []

    for u in range(0, size):
        if not visited[u]:
            node_tuples.append((u, graph[node][u]))
    candidates = sorted(node_tuples, key=lambda my_node: my_node[1])
    if not candidates:
        summary += graph[node][0]
        return None
    else:
        if heuristic_mode == 7:
            # random
            random_index = random.randint(0, len(candidates) - 1)
            summary += graph[node][candidates[random_index][0]]
            hamilton_cycle(candidates[random_index][0])
        else:
            summary += graph[node][candidates[heuristic_mode][0]]
            hamilton_cycle(candidates[heuristic_mode][0])


def heuristic(mode):
    global heuristic_mode
    if mode == "MAX":
        heuristic_mode = -1
    elif mode == "MIN":
        heuristic_mode = 0
    elif mode == "RANDOM":
        heuristic_mode = 7

    start_time = datetime.datetime.now()

    hamilton_cycle(0)

    end_time = datetime.datetime.now()
    time = end_time - start_time
    print("Heuristic finished in: " + str(time.total_seconds()) + " sec.")

    if s1_index != 0:
        s1.append(0)
        for i in range(0, s1_index):
            path[s1[i]][s1[i + 1]] = "path"
            path[s1[i + 1]][s1[i]] = "rev-path"
    return [create_paths(), summary, time]


def create_paths():
    edges = ""
    edge_color = "#F22613"
    for i in range(0, size):
        for j in range(i + 1, size):
            if path[i][j] == "path" or path[j][i] == "rev-path":
                edges += "{from: " + str(i) + ", to: " + str(j) + ", label: '" + str(
                        graph[i][j]) + " km', arrows:'to', color: '" + edge_color + "', font:{size:20}},"
            elif path[i][j] == "rev-path" or path[j][i] == "path":
                edges += "{from: " + str(j) + ", to: " + str(i) + ", label: '" + str(
                        graph[j][i]) + " km', arrows:'to', color: '" + edge_color + "', font:{size:20}},"
            elif graph[i][j] != 0:
                edges += "{from: " + str(i) + ", to: " + str(j) + ", label: '" + str(
                        graph[i][j]) + " km', color: '#2B7CE9'},"
    return edges
