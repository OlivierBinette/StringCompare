#! /usr/bin/bash
# sudo docker run -v $(pwd):/stringcompare -w /stringcompare python:3.7.9 bash dockertest.sh

make clean
pip install -e .
python -c "import stringcompare"
pip install pytest
pytest