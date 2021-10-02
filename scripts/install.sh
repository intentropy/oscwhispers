#!/bin/bash 
#
#   Install OSC Whispers via setup.py

python3 setup.py clean && \
python3 setup.py bdist && \
python3 setup.py install && \
python3 setup.py clean