.. _a10_sys_ut_state_next_state_case_action_l3_ip_module:


a10_sys_ut_state_next_state_case_action_l3_ip -- Configures A10 sys-ut.state.next.state.case.action.l3.ip
=========================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

IP address






Parameters
----------

  ipv6_address (False, any, None)
    Ipv6 address


  ve (False, any, None)
    Virtual Ethernet interface


  ansible_username (True, any, None)
    Username for AXAPI authentication


  case_number (optional, any, None)
    Key to identify parent object


  ipv4_address (False, any, None)
    IP address


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


  name (optional, any, None)
    Key to identify parent object


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  state_name (optional, any, None)
    Key to identify parent object


  src_dst (True, any, None)
    'dest'= dest; 'src'= src;


  state (True, any, None)
    State of the object to be created.


  action_direction (optional, any, None)
    Key to identify parent object


  ethernet (False, any, None)
    Ethernet interface


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

