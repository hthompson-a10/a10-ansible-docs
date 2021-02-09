.. _a10_sys_ut_state_next_state_case_action_l2_module:


a10_sys_ut_state_next_state_case_action_l2 -- Configures A10 sys.ut.state.next.state.case.action.l2
===================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

L2 packet paramters






Parameters
----------

  protocol (False, any, None)
    'arp'= arp; 'ipv4'= ipv4; 'ipv6'= ipv6;


  state_name (optional, any, None)
    Key to identify parent object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  vlan (False, any, None)
    Vlan ID on the packet. 0 is untagged


  ansible_password (True, any, None)
    Password for AXAPI authentication


  case_number (optional, any, None)
    Key to identify parent object


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (optional, any, None)
    Key to identify parent object


  ethertype (False, any, None)
    L2 frame type


  value (False, any, None)
    ethertype number


  state (True, any, None)
    State of the object to be created.


  action_direction (optional, any, None)
    Key to identify parent object


  mac_list (False, any, None)
    Field mac_list


    address_type (optional, any, None)
      'broadcast'= broadcast; 'multicast'= multicast;


    ve (optional, any, None)
      Virtual Ethernet interface


    src_dst (optional, any, None)
      'dest'= dest; 'src'= src;


    value (optional, any, None)
      Mac Address


    nat_pool (optional, any, None)
      Nat pool


    trunk (optional, any, None)
      Trunk number


    ethernet (optional, any, None)
      Ethernet interface


    virtual_server (optional, any, None)
      vip


    uuid (optional, any, None)
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

