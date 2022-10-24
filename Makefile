.PHONY: all format help
SHELL=/bin/bash

# From
# https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

all: ## Run linting
all: lint

compile: ## Compile dependencies from requirements.in
	pip-compile requirements.in

compile_upgrade: ## Upgrade dependencies from requirements.in
	pip-compile --upgrade requirements.in

install: ## install facebook_graph_analyses
	pip install -r requirements.txt -e .

lint: ## run linting
	flake8 facebook_graph_analyses
	pydocstyle facebook_graph_analyses
	isort --check-only facebook_graph_analyses
	black --check facebook_graph_analyses
	mypy facebook_graph_analyses

format:
	isort phoenix tests
	black phoenix tests
