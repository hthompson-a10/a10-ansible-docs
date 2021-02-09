.. _a10_interface_loopback_ipv6_module:


a10_interface_loopback_ipv6 -- Configures A10 interface.loopback.ipv6
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Global IPv6 configuration subcommands






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ospf (False, any, None)
    Field ospf


    uuid (optional, any, None)
      uuid of the object


    bfd (optional, any, None)
      Bidirectional Forwarding Detection (BFD)


    hello_interval_cfg (optional, any, None)
      Field hello_interval_cfg


    cost_cfg (optional, any, None)
      Field cost_cfg


    dead_interval_cfg (optional, any, None)
      Field dead_interval_cfg


    transmit_delay_cfg (optional, any, None)
      Field transmit_delay_cfg


    disable (optional, any, None)
      Disable BFD


    mtu_ignore_cfg (optional, any, None)
      Field mtu_ignore_cfg


    priority_cfg (optional, any, None)
      Field priority_cfg


    retransmit_interval_cfg (optional, any, None)
      Field retransmit_interval_cfg



  ansible_password (True, any, None)
    Password for AXAPI authentication


  rip (False, any, None)
    Field rip


    split_horizon_cfg (optional, any, None)
      Field split_horizon_cfg


    uuid (optional, any, None)
      uuid of the object



  ipv6_enable (False, any, None)
    Enable IPv6 processing


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  router (False, any, None)
    Field router


    ripng (optional, any, None)
      Field ripng


    ospf (optional, any, None)
      Field ospf


    isis (optional, any, None)
      Field isis



  loopback_ifnum (optional, any, None)
    Key to identify parent object


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  address_list (False, any, None)
    Field address_list


    ipv6_addr (optional, any, None)
      Set the IPv6 address of an interface


    anycast (optional, any, None)
      Configure an IPv6 anycast address


    link_local (optional, any, None)
      Configure an IPv6 link local address










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

