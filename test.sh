#! /usr/bin/bash
# docker run -v $(pwd):/stringcompare -w /stringcompare python:3.7.9 bash test.sh

make clean
pip install -e .
python -c "import stringcompare"
pip install pytest
pytest