# SystemD implementation

## Usage

Pretty simple

1. Clone the repo and `cd` into the directory.
2. Start a vanilla redis server (or use one you already have).  Docker Desktop is fine for a demo.
3. Make sure the port number needed in :point_up: is in `worker.py`.
4. (Mac only) Set the environment variable needed for process forking.

    ```shell
    export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES
    ```

5. Start `worker.py` in the background.
6. Start `app.py` by launching flask.

    ```shell
    /usr/bin/env python3 -m flask run --host=0.0.0.0 --port=5000
    ```

7. If needed for external connectivity, launch `ngrok` and map it to whatever you have `app.py` listening on.
8. Look at the logs of the Docker container once it's done to see a nice "Hello world" message customized to your username! :tada:

There are 2 systemd unit files in this directory.  They launch `worker.py` and `app.py` in the background once redis is up.  You should check the name of the redis service in [app-queue.service](systemd/app-queue.service) to make sure it's correct to your distribution.
