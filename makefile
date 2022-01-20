.PHONY: all docs

all: install README.md docs

env: environment.yml
	(echo "Creating stringcompare environment..."; conda env create -f environment.yml) || (echo "Updating stringcompare environment...\n"; conda env update -f environment.yml)

install: $(shell find stringcompare -type f) setup.py pyproject.toml
	pip install -e .

README.md: $(shell find stringcompare -type f) README.ipynb
	jupyter nbconvert --to markdown README.ipynb
	m2r README.md

clean:
	find . -name "*.so" -delete
	find . -name "__pycache__" | xargs rm -rf
	rm -rf build
	rm -rf stringcompare.egg-info
	rm -rf .pytest_cache
	rm -rf dist

SPHINXOPTS    =
SPHINXBUILD   = python -msphinx
SPHINXPROJ    = stringcompare
SOURCEDIR     = documentation
BUILDDIR      = .

docs:
	rm -rf docs
	sphinx-apidoc -f -o documentation/source stringcompare stringcompare/distance/
	m2r README.md
	mv README.rst documentation/README.rst
	$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	mv html docs
	rm -rf doctrees
	touch docs/.nojekyll


