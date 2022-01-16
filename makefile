.PHONY: all

all: install README.md

env: environment.yml
	(echo "Creating stringcompare environment..."; conda env create -f environment.yml) || (echo "Updating stringcompare environment...\n"; conda env update -f environment.yml)

install: $(shell find stringcompare -type f) setup.py setup.cfg pypackage.toml
	pip install -e .

README.md: $(shell find stringcompare -type f) README.ipynb
	jupyter nbconvert --to markdown README.ipynb

clean:
	find . -name "*.so" -delete
	rm -rf build
	rm -rf stringcompare.egg-info
	rm -rf .pytest_cache
	rm -rf dist