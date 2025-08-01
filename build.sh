#!/bin/bash


pip install --upgrade build twine

python -m build

twine upload dist/*
