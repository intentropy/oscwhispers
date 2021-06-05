# oscwhispers
Open Sound Control message forwarding agent.

This is a replacement for the depricated version found in osctoolkit.

## Concept:
This is an OSC Proxy designed to allow a single client to control a mutlitude of devices.
The proxy acts as a single server, which then instatiates clients for various other servers.
The top level path in the OSC path is used to determine where an OSC message is forwarded.

## Requires:
Python3:
* pyliblo3
* pyyaml

Other:
*  liblo >= 0.28