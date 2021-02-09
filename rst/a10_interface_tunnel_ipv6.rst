.. _a10_interface_tunnel_ipv6_module:


a10_interface_tunnel_ipv6 -- Configures A10 interface.tunnel.ipv6
=================================================================

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


  address_cfg (False, any, None)
    Field address_cfg


    ipv6_addr (optional, any, None)
      Set the IPv6 address of an interface


    address_type (optional, any, None)
      'anycast'= Configure an IPv6 anycast address; 'link-local'= Configure an IPv6 link local address;



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


    network_list (optional, any, None)
      Field network_list


    neighbor_cfg (optional, any, None)
      Field neighbor_cfg


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


  ipv6_enable (False, any, None)
    Enable IPv6 processing


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  tunnel_ifnum (optional, any, None)
    Key to identify parent object


  router (False, any, None)
    Field router


    ripng (optional, any, None)
      Field ripng


    ospf (optional, any, None)
      Field ospf



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

