#!/bin/bash 
#
# Description:
#   Build OSC Whispers as RPM and tarball with setup.py
#
# Requires:
#   - dh-python
#   - python3-stdeb

python3 setup.py clean                      && \
python3 setup.py check                      && \
python3 setup.py bdist_rpm                  \
    --use-bzip2 --binary-only               && \
python3 setup.py bdist_dumb                 \
    -f bztar                                && \
python3 setup.py                            \
    --command-packages=stdeb.command        \
    bdist_deb                               && \
python3 setup.py clean