.. _a10_network_arp_static_module:


a10_network_arp_static -- Configures A10 network.arp.static
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

static ARP Commands






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ip_addr (True, any, None)
    IP address


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  vlan (True, any, None)
    VLAN ID


  state (True, any, None)
    State of the object to be created.


  mac_addr (False, any, None)
    MAC address


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

