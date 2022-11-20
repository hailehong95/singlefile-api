# SingleFile API

Simple Webservice for SingleFile

## Installation

- Docker install

    ```bash
    https://docs.docker.com/engine/install/
    ```

- Installation singlefile from Docker Hub

    ```bash
    # Ref: https://github.com/gildas-lormeau/single-file-cli
    $ docker pull capsulecode/singlefile
    ```

- Python package install:

    ```bash
    $ git clone https://github.com/hailehong95/singlefile-api.git
    $ cd singlefile-api/
    $ pip3 install -r requirements.txt
    ```

## Running SingleFile API

- Run server:

    ```bash
    $ python3 singlefile-server.py
    * Serving Flask app 'singlefile-server'
    * Debug mode: off
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    * Running on http://127.0.0.1:8080
    Press CTRL+C to quit
    ```

- Run client:

  - Using `curl`:

    ```bash
    $ curl -d 'url=https://www.wikipedia.org/' http://127.0.0.1:8080
    ```

  - Using `singlefile-client`:

    ```bash
    $ python3 singlefile-client.py
    Usage: singlefile-client.py [OPTIONS] COMMAND [ARGS]...

    A CLI for SingleFile Client

    Options:
    --help  Show this message and exit.

    Commands:
    bulk  Save list URL to each single HTML file
    save  Save a URL into a single HTML file
    ```

    ```bash
    # a url
    $ python3 singlefile-client.py save -u https://www.wikipedia.org/ -p tests/
    ```

    ```bash
    # list url
    $ cat list-url.txt
    https://www.wikipedia.org/
    https://github.com/

    $ python3 singlefile-client.py bulk -us list-url.txt -p tests/
    ```

    ```bash
    $ ls tests/
    github-lets-build-from-here-github.html  wikipedia.html
    ```
