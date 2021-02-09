.. _a10_debug_ipv6_ospf_events_module:


a10_debug_ipv6_ospf_events -- Configures A10 debug.ipv6.ospf.events
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

OSPFv3 event






Parameters
----------

  asbr (False, any, None)
    OSPF ASBR events


  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  a10_partition (False, any, None)
    Destination/target partition for object/command


  state (True, any, None)
    State of the object to be created.


  abr (False, any, None)
    OSPF ABR events


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  router (False, any, None)
    Other router events


  vlink (False, any, None)
    Virtual-Link event


  os (False, any, None)
    OS events


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

