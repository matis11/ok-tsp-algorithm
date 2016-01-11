import datetime

import sys

import itertools

graph = []


def load_graph(_graph):
    global graph
    graph = _graph


def brute_force():
    start_time = datetime.datetime.now()

    min_length = sys.maxsize

    paths = list(itertools.product(*graph))
    print(paths)

    # Evaluate all possible paths.
    # for path in paths:
    #     path_cost = Evaluate(path, cost_table)
    #     if min_length > path_cost:
    #         best_path = path
    #         min_length = path_cost
    # print("Minimum Path Cost: " + str(min_length))

    end_time = datetime.datetime.now()
    time = end_time - start_time
    print("BruteForce finished in: " + str(time.total_seconds()) + " sec.")
