FROM python:3.7-slim

ADD . /
RUN python -m pip install -e .
ENTRYPOINT python -m kaggle_graph
