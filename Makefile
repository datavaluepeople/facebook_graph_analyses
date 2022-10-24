.PHONY: all
SHELL=/bin/bash

all: lint

compile:
	pip-compile requirements.in

compile_upgrade:
	pip-compile --upgrade requirements.in

install:
	pip install -r requirements.txt -e .

lint:
	flake8 facebook_graph_analyses
	pydocstyle facebook_graph_analyses
	isort --check-only facebook_graph_analyses
	black --check facebook_graph_analyses
	mypy facebook_graph_analyses
