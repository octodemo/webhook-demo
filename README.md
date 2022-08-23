# Webhook receiver

An example of a webhook receiver using [GitHub Codespaces](https://github.com/features/codespaces)!  Check out the [demo](demos.md) guide for a short guided tour.

> **Warning**
> Not for production.  May contain out of date dependencies in `requirements.txt`.  Also, it doesn't do anything useful - but you can probably modify it to do useful stuff on webhook receipt.

## Real world

Change the `app.py` function to do something useful ... whatever it was that you were really wanting to accomplish.  Update the requirements in `requirements.txt` first.  Consider moving off Werkzeug.

:information_source: Yes, the Redis container in `docker-compose.yml` does nothing at the moment, but it does in the [systemd](systemd) directory.  I had originally used this sort of program to kick off longer running tasks that couldn't be finished in time for the 10s webhook timeout in GitHub, so it'll return `201 - created` once the info from the webhook is put into Redis.
