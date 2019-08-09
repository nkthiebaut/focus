# Focus

[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://docs.python.org/3/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Python API for models predictions.

Install package with ``pip install -e .``, or create docker image with ``docker build -t focus .`` from the project root folder. 
To run this image the DUMMY environment variable must be provided to the container: ``docker run -e DUMMY="$DUMMY" -p 5000:5000 focus``.


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

## Training

Follow instructions in the `train.ipynb` Jupyter notebook.

## Testing

