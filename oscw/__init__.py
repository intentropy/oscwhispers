#!/usr/bin/env python3
"""OSCW Package __init__
"""

from os.path    import exists


## Setup variables for installation/packaging
# Determine init system here
"""
    For now I'm only working with systemd
"""
_systemd_unit = (
    "/usr/lib/systemd/system",
    [
        "service/oscwhispers.service",
        ],
    )
_service_file = _systemd_unit

_data_files = [
    (   # Executables
        "/usr/bin",
        [
            "oscwhispers",
            ],
        ),
    (   # Documentation
        _docs_dir,
        [
            "README.md",
            "LICENSE",
            ],
        ),
    (   # Config
        "/etc",
        [
            "conf/oscwhispers.yml",
            ],
        ),
    _service_file,  # Systemd or OpenRC init script
    ]

_packages = [ "oscw" ]

_version = "0.0.1"
_description = "An Open Sound Control proxying server"

_url = "https://intentropycs.com"
_author = "Shane Hutter"
_email = "shane@intentropycs.com"

_setup = {
    "name": "oscwhispers",
    "version": _version,
    "author": _author,
    "author_email": _email,
    "maintainer": _author,
    "maintainer_email": _email,
    "description": _description,
    "license": "GNU GPL v3.0",
    "packages": _packages,
    "data_files": _data_files,
    "download_url": "https://intentropycs.com",
    "platforms": [ "any" ],
    "classifiers": [ "Development Status :: Alpha" ]
    }