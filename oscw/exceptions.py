#!/usr/bin/env python3
"""OSCW Exceptions
"""

# Config
class OSCWNoConfig( Exception ):
    """MNo Config file has been loaded"""
    pass

class OSCWNoSuchFile( Exception ):
    """The specified configuration file does not exist"""
    pass

class OSCWBadConfig( Exception ):
    """The loaded configuration file is formated incorrectly"""
    pass