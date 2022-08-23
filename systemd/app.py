#!/usr/bin/env python3

"""
This is a quick and dirty webhook receiver that will put a job into Redis for a
Docker container app to run.
"""

# Imports
import docker
from flask import Flask, request, Response
import requests
from rq import Queue
from systemd.worker import conn

# Docker instance
client = docker.from_env()

# Make instance of flask app
app = Flask(__name__)

# Make instance of redis queue
q = Queue(connection=conn)


# How to run that Docker container
def run_container(who_to_greet):
    """
    Runs a Docker container that greets a named user
    """
    container = client.containers.run(
        image="python:3.9",
        command="python3 -c \"print('Hello, {}!')\"".format(who_to_greet),
        detach=True,
    )


# Do the things
@app.route("/webhook", methods=["POST"])
def respond():
    who_to_greet = request.json["repository"]["owner"]["login"]
    job = q.enqueue_call(func=run_container, args=(), result_ttl=5000)
    return Response(status=201)
