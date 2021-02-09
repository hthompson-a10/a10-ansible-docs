.. _a10_interface_ethernet_ipv6_router_ripng_module:


a10_interface_ethernet_ipv6_router_ripng -- Configures A10 interface.ethernet.ipv6.router.ripng
===============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

ripng






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


  rip (False, any, None)
    RIP Routing for IPv6


  state (True, any, None)
    State of the object to be created.


  ethernet_ifnum (optional, any, None)
    Key to identify parent object


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


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

