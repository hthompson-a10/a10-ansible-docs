.. _a10_interface_ve_ipv6_router_isis_module:


a10_interface_ve_ipv6_router_isis -- Configures A10 interface.ve.ipv6.router.isis
=================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

IS-IS Routing for IP






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ve_ifnum (optional, any, None)
    Key to identify parent object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  tag (False, any, None)
    ISO routing area tag


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uuid (False, any, None)
    uuid of the object









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

