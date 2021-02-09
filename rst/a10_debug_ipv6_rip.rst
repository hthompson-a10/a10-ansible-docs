.. _a10_debug_ipv6_rip_module:


a10_debug_ipv6_rip -- Configures A10 debug.ipv6.rip
===================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Routing Information Protocol (RIP) for IPv6






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  nsm (False, any, None)
    RIPng and NSM communication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  a10_partition (False, any, None)
    Destination/target partition for object/command


  detail (False, any, None)
    Detailed information display


  packet (False, any, None)
    RIPng packets


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  send (False, any, None)
    RIPng send packets


  all (False, any, None)
    Enable all debugging


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  recv (False, any, None)
    RIPng receive packets


  events (False, any, None)
    RIPng events









Examples
--------

.. code-block:: yaml+jinja

    





Status
------




- This module is not guaranteed to have a backwards compatible interface. *[preview]*


- This module is maintained by community.



Authors
~~~~~~~

- A10 Networks 2018

