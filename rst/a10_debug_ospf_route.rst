.. _a10_debug_ospf_route_module:


a10_debug_ospf_route -- Configures A10 debug.ospf.route
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

OSPFv3 route information






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ase (False, any, None)
    External route calculation information


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  install (False, any, None)
    Route installation information


  ia (False, any, None)
    Inter-Area route calculation information


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  spf (False, any, None)
    SPF calculation information


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

