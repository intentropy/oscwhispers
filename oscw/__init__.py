#!/usr/bin/env python3
"""
OSC Whispers
    OSCWhispers

    Written By:
        Shane Hutter


    Description:
        This is the __init__.py module for storing globally importable variables, and methods.
"""

from os import envrion

ZERO , ONE  = int( False ) , int( True )


# Global indices
GLOBAL_INDICES  = {
        "only"  : ZERO  ,
        "first" : ZERO  ,
        }

# Program CONSTANTS
PROG_NAME           = "oscwhispers"
PROG_VERSION        = "0.0.0"
PROG_AUTHOR         = "Shane Hutter"
PROG_AUTHOR_EMAIL   = "contact@shanehutter.com"
PROG_DESC           = """"""
PROG_PACKAGES       = [ "OSCWhispers" , ]

# System CONSTANTS
PATH_DELIMITER  = ':'
PATHS           = environ[ "PATH" ].split( PATH_DELIMITER )
PREFERED_PATHS  = (
        "/usr/bin"          ,
        "/usr/local/bin"    ,
        "/bin"              ,
        )
PATH = None
for path in PATHS:
    if path in PREFERED_PATHS:
        PATH    = path
        break
if not PATH:
    PATH    = PATHS[
            GLOBAL_INDICES[ "first" ]
            ]

# Systemd CONSTANTS
SYSTEMD_UNIT_DIR        = "/usr/lib/systemd/system"
SYSTEMD_SERVICE_UNIT    = "oscwhispers.service"
