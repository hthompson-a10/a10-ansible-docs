.. _a10_interface_tunnel_ip_module:


a10_interface_tunnel_ip -- Configures A10 interface.tunnel.ip
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Global IP configuration subcommands






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  generate_membership_query_val (False, any, None)
    1 - 255 (Default is 125)


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ospf (False, any, None)
    Field ospf


    ospf_global (optional, any, None)
      Field ospf_global


    ospf_ip_list (optional, any, None)
      Field ospf_ip_list



  max_resp_time (False, any, None)
    Max Response Time (Default is 100)


  ansible_password (True, any, None)
    Password for AXAPI authentication


  rip (False, any, None)
    Field rip


    split_horizon_cfg (optional, any, None)
      Field split_horizon_cfg


    receive_packet (optional, any, None)
      Enable receiving packet through the specified interface


    uuid (optional, any, None)
      uuid of the object


    receive_cfg (optional, any, None)
      Field receive_cfg


    authentication (optional, any, None)
      Field authentication


    send_packet (optional, any, None)
      Enable sending packets through the specified interface


    send_cfg (optional, any, None)
      Field send_cfg



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  address (False, any, None)
    Field address


    ip_cfg (optional, any, None)
      Field ip_cfg



  tunnel_ifnum (optional, any, None)
    Key to identify parent object


  generate_membership_query (False, any, None)
    Enable Membership Query


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

