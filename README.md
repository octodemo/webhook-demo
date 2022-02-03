# Webhook receiver

An example of a quick and dirty webhook receiver for where you can't use
`ngrok`, ironically using `ngrok` to demonstrate it on a Mac.  Use port forwarding in Codespaces instead.

:warning: Not for production.  Contains out of date dependencies in `requirements.txt`.

## Real world

Change the `app.py` function to do something useful ... whatever it was that you were really wanting to accomplish.  Update the requirements in `requirements.txt` first.  Consider moving off Werkzeug.

:information_source: Yes, the Redis container in `docker-compose.yml` does nothing at the moment, but it does in the [systemd](systemd) directory.  I had originally used this sort of program to kick off longer running tasks that couldn't be finished in time for the 10s webhook timeout in GitHub, so it'll return `201 - created` once the info from the webhook is put into Redis.
