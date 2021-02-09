.. _a10_interface_loopback_module:


a10_interface_loopback -- Configures A10 interface.loopback
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Loopback interface






Parameters
----------

  oper (False, any, None)
    Field oper


    ipv6_list (optional, any, None)
      Field ipv6_list


    line_protocol (optional, any, None)
      Field line_protocol


    ipv6_link_local (optional, any, None)
      Field ipv6_link_local


    ipv6_link_local_scope (optional, any, None)
      Field ipv6_link_local_scope


    state (optional, any, None)
      Field state


    ipv6_link_local_prefix (optional, any, None)
      Field ipv6_link_local_prefix


    ipv4_addr_count (optional, any, None)
      Field ipv4_addr_count


    ipv6_link_local_type (optional, any, None)
      Field ipv6_link_local_type


    ipv4_address (optional, any, None)
      IP address


    ifnum (optional, any, None)
      Loopback interface number


    ipv6_addr_count (optional, any, None)
      Field ipv6_addr_count


    ipv4_netmask (optional, any, None)
      IP subnet mask


    ipv4_list (optional, any, None)
      Field ipv4_list



  ansible_username (True, any, None)
    Username for AXAPI authentication


  ip (False, any, None)
    Field ip


    router (optional, any, None)
      Field router


    ospf (optional, any, None)
      Field ospf


    uuid (optional, any, None)
      uuid of the object


    rip (optional, any, None)
      Field rip


    address_list (optional, any, None)
      Field address_list



  snmp_server (False, any, None)
    Field snmp_server


    trap_source (optional, any, None)
      The trap source



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


  isis (False, any, None)
    Field isis


    mesh_group (optional, any, None)
      Field mesh_group


    bfd_cfg (optional, any, None)
      Field bfd_cfg


    password_list (optional, any, None)
      Field password_list


    lsp_interval (optional, any, None)
      Set LSP transmission interval (LSP transmission interval (milliseconds))


    padding (optional, any, None)
      Add padding to IS-IS hello packets


    csnp_interval_list (optional, any, None)
      Field csnp_interval_list


    hello_multiplier_list (optional, any, None)
      Field hello_multiplier_list


    priority_list (optional, any, None)
      Field priority_list


    wide_metric_list (optional, any, None)
      Field wide_metric_list


    retransmit_interval (optional, any, None)
      Set per-LSP retransmission interval (Interval between retransmissions of the same LSP (seconds))


    metric_list (optional, any, None)
      Field metric_list


    uuid (optional, any, None)
      uuid of the object


    circuit_type (optional, any, None)
      'level-1'= Level-1 only adjacencies are formed; 'level-1-2'= Level-1-2 adjacencies are formed; 'level-2-only'= Level-2 only adjacencies are formed;


    hello_interval_list (optional, any, None)
      Field hello_interval_list


    authentication (optional, any, None)
      Field authentication


    hello_interval_minimal_list (optional, any, None)
      Field hello_interval_minimal_list



  name (False, any, None)
    Name for the interface


  user_tag (False, any, None)
    Customized tag


  state (True, any, None)
    State of the object to be created.


  ifnum (True, any, None)
    Loopback interface number


  ipv6 (False, any, None)
    Field ipv6


    ipv6_enable (optional, any, None)
      Enable IPv6 processing


    uuid (optional, any, None)
      uuid of the object


    router (optional, any, None)
      Field router


    ospf (optional, any, None)
      Field ospf


    rip (optional, any, None)
      Field rip


    address_list (optional, any, None)
      Field address_list



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

