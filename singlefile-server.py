#!/usr/bin/env python

import docker

from flask import Flask, request, Response

server = Flask(__name__)
DOCKER_IMAGE = "capsulecode/singlefile"


@server.route("/", methods=["POST"])
def singlefile():
    try:
        url = request.form.get("url")
        if url:
            client = docker.from_env()
            singlefile_html = client.containers.run(DOCKER_IMAGE, url)
        else:
            return Response("Error: url parameter not found.", status=500)
    except Exception as ex:
        print(ex)
    else:
        return Response(singlefile_html, mimetype="text/html")


if __name__ == "__main__":
    server.run(port=8080)
