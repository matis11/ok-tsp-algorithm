#!/usr/bin/env python
# coding=utf-8
import argparse
import webbrowser
from random import randint

from flask import Flask, render_template, send_from_directory, request

from tsp import *

app = Flask(__name__)

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
nodes = ""
edges = ""


def parse_distances():
    global graph, nodes, edges
    nodes = ""
    edges = ""
    graph = [[0 for x in range(graph_size)] for x in range(graph_size)]
    for i in range(0, graph_size):
        if i == 0:
            nodes += "{id: 0,  label: '0', color: '#F22613'},"
        else:
            nodes += "{id: " + str(i) + ",  label: '" + str(i) + "' },"
        for j in range(i + 1, graph_size):
            value = distances.pop(0)
            graph[i][j] = value
            graph[j][i] = value
    nodes = nodes[:-1]


def generate_random_graph():
    edges_count = (graph_size * (graph_size - 1)) / 2
    edges_count = int(round(edges_count))
    global distances
    distances = [randint(1, 20) for x in range(edges_count)]
    parse_distances()


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


def shutdown():
    shutdown_server()
    return 'Server shutting down...'


@app.route('/')
def index():
    return render_template('index.html', edges=edges, nodes=nodes)


@app.route('/<path:file>')
def get_file(file):
    filename = file
    cache_timeout = app.get_send_file_max_age(filename)
    return send_from_directory(app.template_folder, filename,
                               cache_timeout=cache_timeout)


def main():
    global edges
    if args.distances is None:
        generate_random_graph()
    else:
        parse_distances()

    load_graph(graph)
    print("Using BruteForce algorithm")
    edges = brute_force()
    edges = edges[:-1]

    url = "http://127.0.0.1:8000"
    webbrowser.open_new_tab(url)
    app.run(port=8000)


if __name__ == "__main__":
    main()
