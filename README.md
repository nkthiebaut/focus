# Focus

[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://docs.python.org/3/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Python API for models predictions.

Install package with ``pip install -e .``, or create docker image with ``docker build -t focus .`` from the project root folder. 
To run this image the DUMMY environment variable must be provided to the container: ``docker run -e DUMMY="$DUMMY" -p 5000:5000 focus``.

## API

The API accepts `POST` queries with a `JSON` body that contains a `text` field. Here is an example of a valid request (using `curl`):

```
curl -X POST \
  http://localhost:5000/explain \
  -H 'Accept: */*' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Host: localhost:5000' \
  -H 'Postman-Token: f0816fe4-a36e-4c78-b594-d6fa692f6a2f,c14b014b-685b-4118-9cd3-4fc46e307b82' \
  -H 'User-Agent: PostmanRuntime/7.15.0' \
  -H 'accept-encoding: gzip, deflate' \
  -H 'cache-control: no-cache' \
  -H 'content-length: 27' \
  -d '{
    "text": "this is my text"
}'
```

## Installation

After first cloning the repo, run the following commands:

 ```bash
 virtualenv venv
 source venv/bin/activate
 pip install -r requirements.txt
 pip install -e .
 pre-commit install
 ```

## Development

You can try the API with `python focus/api.py` from the root folder.

## Training

Follow instructions in the `train.ipynb` Jupyter notebook.

## Testing

Run `pytest` from the root folder.