.. _a10_router_ipv6_rip_route_map_module:


a10_router_ipv6_rip_route_map -- Configures A10 router.ipv6.rip.route-map
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Route map set






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  map_cfg (False, any, None)
    Field map_cfg


    map (optional, any, None)
      Route map name


    route_map_direction (optional, any, None)
      'in'= Route map set for input filtering; 'out'= Route map set for output filtering;


    loopback (optional, any, None)
      Loopback interface (Port number)


    tunnel (optional, any, None)
      Tunnel interface (Tunnel interface number)


    ethernet (optional, any, None)
      Ethernet interface (Port number)


    trunk (optional, any, None)
      Trunk interface (Trunk interface number)


    ve (optional, any, None)
      Virtual ethernet interface (Virtual ethernet interface number)



  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication









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

