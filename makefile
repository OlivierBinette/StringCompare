.PHONY: all docs dockertest

all: install README.md docs

env: pixi.toml
	pixi install

install: $(shell find stringcompare -type f) setup.py pyproject.toml
	pixi install

README.md: $(shell find stringcompare -type f) README.ipynb
	pixi run jupyter nbconvert --execute --to markdown README.ipynb
	pixi run m2r README.md

clean:
	find . -name "*.so" -delete
	find . -name "__pycache__" | xargs rm -rf
	rm -rf build
	rm -rf stringcompare.egg-info
	rm -rf .pytest_cache
	rm -rf dist
	rm -rf build/

SPHINXOPTS    =
SPHINXBUILD   = python -msphinx
SPHINXPROJ    = stringcompare
SOURCEDIR     = documentation
BUILDDIR      = .

docs: README.md
	rm -rf docs
	pixi run sphinx-apidoc -M -f -o documentation/source stringcompare stringcompare stringcompare/distance/
	pixi run m2r README.md
	mv README.rst documentation/README.rst
	pixi run $(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	mv html docs
	rm -rf doctrees
	touch docs/.nojekyll
