#!/usr/bin/env python3

"""
This is a quick and dirty webhook receiver that will add an entry to a database
based on the webhook payload.
"""

# Imports
import psycopg2
from datetime import datetime
from flask import Flask, request, Response
from redis import Redis
from rq import Queue


# Make instance of flask app
app = Flask(__name__)

# Make instance of redis queue
q = Queue(connection=Redis(host="redis_cache", port=6379))


# Write the username and repo to the test table
def write_to_db(username, repo):
    """
    Writes the username, repo, and time to the test table
    """
    conn = psycopg2.connect(
        "host=database dbname=webhooks user=postgres password=mysecretpassword"
    )
    cur = conn.cursor()
    try:
        cur.execute(
            """
            INSERT INTO test_webhook (username, target_repo, event_timestamp) 
            VALUES (%s, %s, %s);
            """,
            (username, repo, datetime.now()),
        )
    except psycopg2.Error as e:
        print("Error: %s", e)
    conn.commit()
    cur.close()
    conn.close()


# Do the things
@app.route("/webhook", methods=["POST"])
def respond():
    username = request.json["repository"]["owner"]["login"]
    repo = request.json["repository"]["name"]
    write_to_db(username, repo)
    return Response(status=201)
    # TODO: add some business logic to do something else with the data, maybe
    # put it into redis to queue up something bigger?
