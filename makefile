.PHONY: all

all: install test README.md

install: $(shell find stringcompare -type f) pypackage.toml setup.cfg setup.py
	pip install -e .

test: $(shell find stringcompare -type f)
	pytest --doctest-modules

README.md: $(shell find stringcompare -type f) README.ipynb
	jupyter nbconvert --to markdown README.ipynb
