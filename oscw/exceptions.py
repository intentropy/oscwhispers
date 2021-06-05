#!/usr/bin/env python3
"""OSCW Exceptions
"""

# Config
class OSCWNoConfig( Exception ):
    """No Config file has been loaded"""
    pass

class OSCWBadConfig( Exception ):
    """The loaded configuration file is formated incorrectly"""
    pass