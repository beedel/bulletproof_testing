# Bulletproof Testing in Python

This repo contains a guide to mocking in Python, and three exercises to help you learn how to use mocks.

## How to use this guide
We expect familiarity with Python, and some experience with unit testing. You should have Python 3 and pip installed on your system.

While this guide is geared towards bash environments (Mac, Linux), you should be able to follow along on Windows.

### Getting Started
First, clone this repo

```
git clone [REPO]
cd [REPO]
```

Then install the python dependencies in a virtual environment

```
python3 -m venv env
. env/bin/activate
pip install -r requirements.txt
```


Run the program with `python3 main.py ManufacturerName` (Ford, BMW, Honda, or Tesla)


Run tests with `python3 -m unittest tests/*Test.py`