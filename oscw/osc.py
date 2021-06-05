#!/usr/bin/env python3
"""OSCW Open Sound Control server and client classes
"""

from oscw.exceptions    import *

from liblo  import ServerThread

class OSCServer( ServerThread ):
    def __init__( self , config ):
        """Instatiate oscw.osc.OSCSERVER

        Args:
            config: (Obj)   An oscw.config.Config object.
        """
        # Load configuration
        self._config = config.config
        if not self._config.get( "server" )\
            or not self._config.get( "routes" ):
            raise OSCWBadConfig()
        self._server_conf = self._config.get( "server" )
        self._routes = self._config.get( "routes" )
        if not self._server_conf.get( "port" ):
            raise OSCWBadConfig()
        # Init super
        super().__init__( 
            self._server_conf.get( "port" )
            )
        # Register forwarding method
        self.add_method( None , None , self.forward )
        return
    
    def __enter__( self ):
        """Start the OSCServer when entering `with`, and register configured routes"""
        self.start()
        return self
    
    def __exit__( self, *exception ):
        """Stop the OSCServer when exiting `with`"""
        self.stop()
        self.free()
        return

    def _top_level_dir( self, path ):
        """Determine the top level directory for a provided path

        Args:
            path: (str)     An OSC path

        Returns:
            A string of the top level directory in the path
        """
        return path.split( "/" )[ 1 ]

    def _trunc_top_level_dir( self, path ):
        """Remove the top level directory from a provided OSC path

        Args:
            path: (str)     An OSC path

        Returns:
            The OSC patch with the top level directory removed
        """
        return "/" + "/".join(
            path.split( "/" )[2:]
            )

    def forward( self , *args ):
        """Forward incoming messages"""
        _path , _values, _types, _Addr, _unsure = args
        if self._top_level_dir( _path ) in self._routes:
            for _route in self._routes.get(
                self._top_level_dir( _path )
                ):
                # Set path for message
                if _route.get( "truncate" ):
                    _path_trunc = self._trunc_top_level_dir( _path )
                else:
                    _path_trunc = _path
                # Set target for message
                _target = (
                    _route.get( "host" ),
                    _route.get( "port" ),
                    )
                # Set args for the message
                _args = []
                for _arg in zip( _types , _values ):
                    _args.append( _arg )
                # Forward the message
                self.send( _target, _path_trunc , *_args )