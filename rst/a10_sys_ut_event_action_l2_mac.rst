.. _a10_sys_ut_event_action_l2_mac_module:


a10_sys_ut_event_action_l2_mac -- Configures A10 sys-ut.event.action.l2.mac
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Mac Address






Parameters
----------

  ve (False, any, None)
    Virtual Ethernet interface


  ansible_username (True, any, None)
    Username for AXAPI authentication


  nat_pool (False, any, None)
    Nat pool


  trunk (False, any, None)
    Trunk number


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  virtual_server (False, any, None)
    vip


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  event_number (optional, any, None)
    Key to identify parent object


  value (False, any, None)
    Mac Address


  state (True, any, None)
    State of the object to be created.


  src_dst (True, any, None)
    'dest'= dest; 'src'= src;


  action_direction (optional, any, None)
    Key to identify parent object


  ethernet (False, any, None)
    Ethernet interface


  address_type (False, any, None)
    'broadcast'= broadcast; 'multicast'= multicast;


  ansible_password (True, any, None)
    Password for AXAPI authentication









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

