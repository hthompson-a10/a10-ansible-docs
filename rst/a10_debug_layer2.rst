.. _a10_debug_layer2_module:


a10_debug_layer2 -- Configures A10 debug.layer2
===============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Layer2 module parameters






Parameters
----------

  arp (False, any, None)
    Layer2 debug arp switch


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  trace (False, any, None)
    Layer2 debug trace switch


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  vlan (False, any, None)
    Layer2 debug vlan switch


  misc (False, any, None)
    Layer2 debug misc switch


  all (False, any, None)
    Layer2 all debug switch


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  interface (False, any, None)
    Layer2 debug interface switch


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

