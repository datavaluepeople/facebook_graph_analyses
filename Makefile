.PHONY: all format help test
SHELL=/bin/bash

# From
# https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

all: ## Run linting and tests
all: lint test

compile: ## Compile dependencies from requirements.in
	pip-compile requirements.in

compile_upgrade: ## Upgrade dependencies from requirements.in
	pip-compile --upgrade requirements.in

install: ## install facebook_graph_analyses
	pip install -r requirements.txt -e .

lint: ## run linting
	flake8 facebook_graph_analyses tests
	pydocstyle facebook_graph_analyses
	isort --check-only facebook_graph_analyses tests
	black --check facebook_graph_analyses tests
	mypy facebook_graph_analyses tests
 
format: ## format source code
	isort facebook_graph_analyses tests
	black facebook_graph_analyses tests

test:
	pytest tests
