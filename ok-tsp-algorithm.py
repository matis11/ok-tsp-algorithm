#!/usr/bin/env python
# coding=utf-8
import argparse
import subprocess
import sys
import webbrowser

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

argparser = argparse.ArgumentParser()
argparser.add_argument("-p",
                       "--port",
                       help="Server port")

args = argparser.parse_args()


# def shutdown_server():
#     func = request.environ.get('werkzeug.server.shutdown')
#     if func is None:
#         raise RuntimeError('Not running with the Werkzeug Server')
#     func()
#
#
# def shutdown():
#     shutdown_server()
#     return 'Server shutting down...'
#
#
# @app.route("/submit", methods=["POST"])
# def save():
#     data = request.form["output"]
#
#     config = open(config_path, "w+")
#     config.write(data)
#     config.close()
#
#     shutdown()
#
#     return render_template('closed.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<path:file>')
def get_file(file):
    filename = file
    cache_timeout = app.get_send_file_max_age(filename)
    return send_from_directory(app.template_folder, filename,
                               cache_timeout=cache_timeout)


def main():
    # if not (os.path.exists(config_path)):
    #     print("Config file for " + app_tag + " does not exists!")
    #     return 0

    url = "http://127.0.0.1:8000"

    if sys.platform == 'darwin':  # in case of OS X
        subprocess.Popen(['open', url])
    else:
        webbrowser.open_new_tab(url)

    app.run(port=8000)


if __name__ == "__main__":
    main()
