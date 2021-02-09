.. _a10_interface_ve_ip_ospf_ospf_ip_module:


a10_interface_ve_ip_ospf_ospf_ip -- Configures A10 interface.ve.ip.ospf.ospf-ip
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

IP address configuration for Open Shortest Path First for IPv4 (OSPF)






Parameters
----------

  cost (False, any, None)
    Interface cost


  ip_addr (True, any, None)
    Address of interface


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_port (True, any, None)
    Port for AXAPI authentication


  database_filter (False, any, None)
    'all'= Filter all LSA;


  message_digest_cfg (False, any, None)
    Field message_digest_cfg


    encrypted (optional, any, None)
      Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)


    md5_value (optional, any, None)
      The OSPF password (1-16)


    message_digest_key (optional, any, None)
      Message digest authentication password (key) (Key id)



  dead_interval (False, any, None)
    Interval after which a neighbor is declared dead (Seconds)


  hello_interval (False, any, None)
    Time between HELLO packets (Seconds)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  transmit_delay (False, any, None)
    Link state transmit delay (Seconds)


  out (False, any, None)
    Outgoing LSA


  retransmit_interval (False, any, None)
    Time between retransmitting lost link state advertisements (Seconds)


  uuid (False, any, None)
    uuid of the object


  authentication (False, any, None)
    Enable authentication


  value (False, any, None)
    'message-digest'= Use message-digest authentication; 'null'= Use no authentication;


  mtu_ignore (False, any, None)
    Ignores the MTU in DBD packets


  priority (False, any, None)
    Router priority


  state (True, any, None)
    State of the object to be created.


  ve_ifnum (optional, any, None)
    Key to identify parent object


  authentication_key (False, any, None)
    Authentication password (key) (The OSPF password (key))


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

