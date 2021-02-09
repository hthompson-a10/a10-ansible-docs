.. _a10_system_per_vlan_limit_module:


a10_system_per_vlan_limit -- Configures A10 system.per-vlan-limit
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Per vlan flooding packet limit






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


  unknown_ucast (False, any, None)
    unknown unicast packets (per second limit)


  mcast (False, any, None)
    multicast packets (per second limit)


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  bcast (False, any, None)
    broadcast packets (per second limit)


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ipmcast (False, any, None)
    IP multicast packets (per second limit)









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

