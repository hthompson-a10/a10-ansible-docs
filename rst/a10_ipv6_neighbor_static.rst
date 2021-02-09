.. _a10_ipv6_neighbor_static_module:


a10_ipv6_neighbor_static -- Configures A10 ipv6.neighbor.static
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

static IPv6 Neighbor commands






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  tunnel (False, any, None)
    Tunnel interface


  ansible_password (True, any, None)
    Password for AXAPI authentication


  vlan (True, any, None)
    VLAN ID


  ipv6_addr (True, any, None)
    IPV6 address


  mac (False, any, None)
    MAC Address


  state (True, any, None)
    State of the object to be created.


  trunk (False, any, None)
    Trunk group


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  ethernet (False, any, None)
    Ethernet port (Port Value)


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

