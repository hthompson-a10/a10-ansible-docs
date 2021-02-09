.. _a10_sys_ut_event_action_l3_module:


a10_sys_ut_event_action_l3 -- Configures A10 sys.ut.event.action.l3
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

L3 packet paramters






Parameters
----------

  protocol (False, any, None)
    L4 Protocol


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ntype (False, any, None)
    'tcp'= tcp; 'udp'= udp; 'icmp'= icmp;


  ttl (False, any, None)
    Field ttl


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ip_list (False, any, None)
    Field ip_list


    ipv6_address (optional, any, None)
      Ipv6 address


    ve (optional, any, None)
      Virtual Ethernet interface


    src_dst (optional, any, None)
      'dest'= dest; 'src'= src;


    ipv4_address (optional, any, None)
      IP address


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



  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  event_number (optional, any, None)
    Key to identify parent object


  value (False, any, None)
    protocol number


  state (True, any, None)
    State of the object to be created.


  checksum (False, any, None)
    'valid'= valid; 'invalid'= invalid;


  action_direction (optional, any, None)
    Key to identify parent object


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

