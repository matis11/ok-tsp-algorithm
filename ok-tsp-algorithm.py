#!/usr/bin/env python
# coding=utf-8
import argparse

from random import randint

argparser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter)
argparser.description = " _____                   _ _ _\n" \
                        "|_   _|                 | | (_)            \n" \
                        "  | |_ __ __ ___   _____| | |_ _ __   __ _ \n" \
                        "  | | '__/ _` \ \ / / _ \ | | | '_ \ / _` |\n" \
                        "  | | | | (_| |\ V /  __/ | | | | | | (_| |\n" \
                        "  \_/_|  \__,_| \_/ \___|_|_|_|_| |_|\__, |\n" \
                        " _____       _                        __/ |\n" \
                        "/  ___|     | |                      |___/     \n" \
                        "\ `--.  __ _| | ___  ___ _ __ ___   __ _ _ __  \n" \
                        " `--. \/ _` | |/ _ \/ __| '_ ` _ \ / _` | '_ \ \n" \
                        "/\__/ / (_| | |  __/\__ \ | | | | | (_| | | | |\n" \
                        "\____/ \__,_|_|\___||___/_| |_| |_|\__,_|_| |_|\n" \
                        "______          _     _                \n" \
                        "| ___ \        | |   | |               \n" \
                        "| |_/ / __ ___ | |__ | | ___ _ __ ___  \n" \
                        "|  __/ '__/ _ \| '_ \| |/ _ \ '_ ` _ \ \n" \
                        "| |  | | | (_) | |_) | |  __/ | | | | |\n" \
                        "\_|  |_|  \___/|_.__/|_|\___|_| |_| |_|\n" \
                        "\n" \
                        "Usage:\n" \
                        "   By default, this script will calculate TSP using default algorithm on 5 nodes." \
                        " You can change it using: \n" \
                        "   1. '-n' to specify quantity of nodes,\n" \
                        "   2. '-d' to specify distances between nodes (NOTE: remember about proper formatting)"
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
