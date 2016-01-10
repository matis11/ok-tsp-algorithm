#!/usr/bin/env python
# coding=utf-8
import argparse

from random import randint

argparser = argparse.ArgumentParser()
argparser.add_argument("-d", "--distances", action="store", type=int, nargs='+',
                       help="Distances between nodes")
argparser.add_argument("-n", "--nodes", action="store", type=int,
                       help="Number of nodes", default=5)

args = argparser.parse_args()

distances = args.distances
graph_size = args.nodes
graph = []


def parse_distances():
    global graph
    graph = [[0 for x in range(graph_size)] for x in range(graph_size)]
    for i in range(graph_size):
        for j in range(i + 1, graph_size):
            value = distances.pop(0)
            graph[i][j] = value
            graph[j][i] = value
            print(i, j, graph[i][j])
            print("-")
    print("__________")
    print(graph)


def generate_random_graph():
    edges = (graph_size * (graph_size - 1)) / 2
    edges = int(round(edges))
    global distances
    distances = [randint(1, 20) for x in range(edges)]
    parse_distances()


def main():
    if args.distances is None:
        generate_random_graph()
    else:
        parse_distances()


if __name__ == "__main__":
    main()
