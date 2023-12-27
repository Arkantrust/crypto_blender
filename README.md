# Crypto Blender

Slow python generator for strong passwords and hashed keys using SHA256 and SHA512. Made with python, fastapi and react.

You can run the generator by CLI or web UI.

## Prerequisites

- [Python](https://www.python.org/downloads/)
- [Docker](https://docs.docker.com/get-docker/) (for web UI only)

## CLI

To run the CLI app just create the venv, download packages and run the [`gen.py`](./backend/gen.py) file.

``` bash
cd backend

python3 -m venv .venv # maybe python if you're on windows

source .venv/bin/activate

pip install --upgrade -r requirements.txt

python3 gen.py
```

## Web UI

To run the web app you just need to have docker installed and run the [`compose.yaml`](./compose.yaml) file.

## License

[MIT](./LICENSE)
