#!/usr/bin/env python3
"""
OSC Whispers setup.py
    setup.py

    Written By:
        Shane Hutter
    
    Description:
        This is the setup.py for installing this software as a python package.
"""

from distutils.core     import setup
from oscw               import _setup

setup( **_setup )