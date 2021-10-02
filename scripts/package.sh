#!/bin/bash 
#
#   Build OSC Whispers as RPM and tarball with setup.py

python3 setup.py clean      && \
python3 setup.py bdist_rpm  && \
python3 setup.py bdist_dumb && \
python3 setup.py clean