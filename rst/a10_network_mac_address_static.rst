.. _a10_network_mac_address_static_module:


a10_network_mac_address_static -- Configures A10 network.mac.address.static
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Static MAC commands






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  dest (False, any, None)
    Trap MAC with this DA to CPU


  ansible_password (True, any, None)
    Password for AXAPI authentication


  vlan (True, any, None)
    VLAN Id


  state (True, any, None)
    State of the object to be created.


  ansible_host (True, any, None)
    Host for AXAPI authentication


  mac (True, any, None)
    Configure a Static MAC address


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  port (False, any, None)
    Ethernet Port on which the Address is applicable (Port Value)









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

