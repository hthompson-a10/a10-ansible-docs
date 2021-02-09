.. _a10_sys_ut_state_next_state_case_action_module:


a10_sys_ut_state_next_state_case_action -- Configures A10 sys-ut.state.next.state.case.action
=============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Specify event parameters






Parameters
----------

  udp (False, any, None)
    Field udp


    length (optional, any, None)
      Total packet length starting at UDP header


    src_port (optional, any, None)
      Source port value


    uuid (optional, any, None)
      uuid of the object


    checksum (optional, any, None)
      'valid'= valid; 'invalid'= invalid;


    dest_port_value (optional, any, None)
      Dest port value


    nat_pool (optional, any, None)
      Nat pool port


    dest_port (optional, any, None)
      Dest port



  state_name (optional, any, None)
    Key to identify parent object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  direction (True, any, None)
    'send'= Test event; 'expect'= Expected result; 'wait'= Introduce a delay;


  tcp (False, any, None)
    Field tcp


    src_port (optional, any, None)
      Source port value


    uuid (optional, any, None)
      uuid of the object


    seq_number (optional, any, None)
      'valid'= valid; 'invalid'= invalid;


    checksum (optional, any, None)
      'valid'= valid; 'invalid'= invalid;


    dest_port_value (optional, any, None)
      Dest port value


    nat_pool (optional, any, None)
      Nat pool port


    urgent (optional, any, None)
      'valid'= valid; 'invalid'= invalid;


    window (optional, any, None)
      'valid'= valid; 'invalid'= invalid;


    ack_seq_number (optional, any, None)
      'valid'= valid; 'invalid'= invalid;


    flags (optional, any, None)
      Field flags


    options (optional, any, None)
      Field options


    dest_port (optional, any, None)
      Dest port



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


  drop (False, any, None)
    Packet drop. Only allowed for output spec


  delay (False, any, None)
    Delay in seconds


  state (True, any, None)
    State of the object to be created.


  l2 (False, any, None)
    Field l2


    protocol (optional, any, None)
      'arp'= arp; 'ipv4'= ipv4; 'ipv6'= ipv6;


    uuid (optional, any, None)
      uuid of the object


    ethertype (optional, any, None)
      L2 frame type


    vlan (optional, any, None)
      Vlan ID on the packet. 0 is untagged


    mac_list (optional, any, None)
      Field mac_list


    value (optional, any, None)
      ethertype number



  l3 (False, any, None)
    Field l3


    protocol (optional, any, None)
      L4 Protocol


    uuid (optional, any, None)
      uuid of the object


    ttl (optional, any, None)
      Field ttl


    checksum (optional, any, None)
      'valid'= valid; 'invalid'= invalid;


    ntype (optional, any, None)
      'tcp'= tcp; 'udp'= udp; 'icmp'= icmp;


    value (optional, any, None)
      protocol number


    ip_list (optional, any, None)
      Field ip_list



  template (False, any, None)
    Packet template


  l1 (False, any, None)
    Field l1


    length (optional, any, None)
      packet length


    eth_list (optional, any, None)
      Field eth_list


    uuid (optional, any, None)
      uuid of the object


    auto (optional, any, None)
      Auto calculate pkt len


    trunk_list (optional, any, None)
      Field trunk_list


    value (optional, any, None)
      Total packet length starting at L2 header



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

