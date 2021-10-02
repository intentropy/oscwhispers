#!/bin/bash 
#
#   Build OSC Whispers as RPM and tarball with setup.py

VERSION=`python3 -c "from oscw import _version; print( _version , end='' )"`
DESC=`python3 -c "from oscw import _description; print( _description , end='' )"`
TARBALL="dist/oscwhispers-${VERSION}.tar.bz2"

python3 setup.py clean              && \
python3 setup.py check              && \
python3 setup.py sdist              && \
python3 setup.py bdist_rpm          \
    --use-bzip2 --binary-only       && \
python3 setup.py bdist_dumb         \
    -f bztar                        && \
python3 setup.py clean              && \
sudo alien -d --target=amd64        \
    --version=$VERSION -k           \
    --description="$DESC"           \
    -g $TARBALL                     #&& \
#mv oscwhispers_$VERSION*.deb dist/.