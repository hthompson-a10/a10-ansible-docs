.. _a10_sys_ut_template_module:


a10_sys_ut_template -- Configures A10 sys-ut.template
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Packet config template






Parameters
----------

  udp (False, any, None)
    Field udp


    length (optional, any, None)
      Total packet length starting at UDP header


    src_port_range (optional, any, None)
      Field src_port_range


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



  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  tcp (False, any, None)
    Field tcp


    src_port_range (optional, any, None)
      Field src_port_range


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


  name (True, any, None)
    template name


  ignore_validation (False, any, None)
    Field ignore_validation


    all (optional, any, None)
      Skip validation


    l2 (optional, any, None)
      Dont validate L2 header


    uuid (optional, any, None)
      uuid of the object


    l1 (optional, any, None)
      Dont validate TX descriptor. This includes Tx port, Len & vlan


    l4 (optional, any, None)
      Dont validate L4 header


    l3 (optional, any, None)
      Dont validate L3 header



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



  l1 (False, any, None)
    Field l1


    length (optional, any, None)
      packet length


    trunk_list (optional, any, None)
      Field trunk_list


    eth_list (optional, any, None)
      Field eth_list


    uuid (optional, any, None)
      uuid of the object


    auto (optional, any, None)
      Auto calculate pkt len


    drop (optional, any, None)
      Packet drop. Only allowed for output spec


    value (optional, any, None)
      Total packet length starting at L2 header



  user_tag (False, any, None)
    Customized tag









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

