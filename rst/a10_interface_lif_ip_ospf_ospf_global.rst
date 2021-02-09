.. _a10_interface_lif_ip_ospf_ospf_global_module:


a10_interface_lif_ip_ospf_ospf_global -- Configures A10 interface.lif.ip.ospf.ospf-global
=========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Global setting for Open Shortest Path First for IPv4 (OSPF)






Parameters
----------

  cost (False, any, None)
    Interface cost


  ansible_username (True, any, None)
    Username for AXAPI authentication


  lif_ifnum (optional, any, None)
    Key to identify parent object


  message_digest_cfg (False, any, None)
    Field message_digest_cfg


    message_digest_key (optional, any, None)
      Message digest authentication password (key) (Key id)


    md5 (optional, any, None)
      Field md5



  dead_interval (False, any, None)
    Interval after which a neighbor is declared dead (Seconds)


  hello_interval (False, any, None)
    Time between HELLO packets (Seconds)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  mtu (False, any, None)
    OSPF interface MTU (MTU size)


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  transmit_delay (False, any, None)
    Link state transmit delay (Seconds)


  uuid (False, any, None)
    uuid of the object


  database_filter_cfg (False, any, None)
    Field database_filter_cfg


    database_filter (optional, any, None)
      'all'= Filter all LSA;


    out (optional, any, None)
      Outgoing LSA



  retransmit_interval (False, any, None)
    Time between retransmitting lost link state advertisements (Seconds)


  network (False, any, None)
    Field network


    broadcast (optional, any, None)
      Specify OSPF broadcast multi-access network


    non_broadcast (optional, any, None)
      Specify OSPF NBMA network


    p2mp_nbma (optional, any, None)
      Specify non-broadcast point-to-multipoint network


    point_to_multipoint (optional, any, None)
      Specify OSPF point-to-multipoint network


    point_to_point (optional, any, None)
      Specify OSPF point-to-point network



  mtu_ignore (False, any, None)
    Ignores the MTU in DBD packets


  priority (False, any, None)
    Router priority


  state (True, any, None)
    State of the object to be created.


  disable (False, any, None)
    'all'= All functionality;


  authentication_cfg (False, any, None)
    Field authentication_cfg


    authentication (optional, any, None)
      Enable authentication


    value (optional, any, None)
      'message-digest'= Use message-digest authentication; 'null'= Use no authentication;



  bfd_cfg (False, any, None)
    Field bfd_cfg


    disable (optional, any, None)
      Disable BFD


    bfd (optional, any, None)
      Bidirectional Forwarding Detection (BFD)



  authentication_key (False, any, None)
    Authentication password (key) (The OSPF password (key))


  ansible_password (True, any, None)
    Password for AXAPI authentication


  ansible_port (True, any, None)
    Port for AXAPI authentication









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

