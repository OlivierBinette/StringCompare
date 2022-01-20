.PHONY: all

all: install docs README.md

env: environment.yml
	(echo "Creating stringcompare environment..."; conda env create -f environment.yml) || (echo "Updating stringcompare environment...\n"; conda env update -f environment.yml)

install: $(shell find stringcompare -type f) setup.py pyproject.toml
	pip install -e .

README.md: $(shell find stringcompare -type f) README.ipynb
	jupyter nbconvert --to markdown README.ipynb
	m2r README.md

docs: $(shell find stringcompare -type f)
	sphinx-apidoc -f -o docs/source stringcompare stringcompare/distance/
	m2r README.md
	mv README.rst docs/README.rst

clean:
	find . -name "*.so" -delete
	find . -name "__pycache__" | xargs rm -rf
	rm -rf build
	rm -rf stringcompare.egg-info
	rm -rf .pytest_cache
	rm -rf dist
	rm -rf docs/_build