#!/usr/bin/env python3
"""OSCW Configuration file parsing
"""

from yaml   import safe_load

class Config():
    """Load an OSCW configuration file"""
    def __init__( self, config ):
        """Init for Config class

        Args:
            config: (str)   Location for OSCW configuration file
        """
        self.config_file = config
        return

    def __enter__( self ):
        """Load config upon entering `with`"""
        self.load_conf( self.config_file )
        return self

    def __exit__( self, *exception ):
        """Close the config upon exiting `with`"""
        self.close_conf()
        return

    def load_conf( self , config ):
        """Load the configuration file"""
        self._conf = open(
            self.config_file,
            "r",
            )
        self.config = safe_load(
            self._conf.read()
            )
        return

    def close_conf( self ):
        """Close the config file"""
        self._conf.close()
        return