.PHONY: all

all: install test README.md

conda: environment.yml
	(echo "Creating environment stringcompare..."; conda env create -f environment.yml) || (echo "Updating stringcompare...\n"; conda env update -f environment.yml)

install: $(shell find stringcompare -type f) pypackage.toml setup.cfg setup.py
	pip install -e .

test: $(shell find stringcompare -type f)
	pytest --doctest-modules

README.md: $(shell find stringcompare -type f) README.ipynb
	jupyter nbconvert --to markdown README.ipynb

clean:
	find . -name "*.so" -delete
	rm -rf build
	rm -rf stringcompare.egg-info
	rm -rf .pytest_cache
	rm -rf dist

reinstall:
	make clean
	pip uninstall stringcompare
	pip install -e .