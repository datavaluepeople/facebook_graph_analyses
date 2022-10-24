SHELL=/bin/bash


compile:
	pip-compile requirements.in

compile_upgrade:
	pip-compile --upgrade requirements.in
