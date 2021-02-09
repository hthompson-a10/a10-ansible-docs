.. _a10_interface_lif_ip_module:


a10_interface_lif_ip -- Configures A10 interface.lif.ip
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Global IP configuration subcommands






Parameters
----------

  ansible_username (True, any, None)
    Username for AXAPI authentication


  max_resp_time (False, any, None)
    Maximum Response Time (Max Response Time (Default is 100))


  lif_ifnum (optional, any, None)
    Key to identify parent object


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



  state (True, any, None)
    State of the object to be created.


  dhcp (False, any, None)
    Use DHCP to configure IP address


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_password (True, any, None)
    Password for AXAPI authentication


  inside (False, any, None)
    Configure interface as inside


  cache_spoofing_port (False, any, None)
    This interface connects to spoofing cache


  outside (False, any, None)
    Configure interface as outside


  allow_promiscuous_vip (False, any, None)
    Allow traffic to be associated with promiscuous VIP


  generate_membership_query (False, any, None)
    Enable Membership Query


  router (False, any, None)
    Field router


    isis (optional, any, None)
      Field isis



  query_interval (False, any, None)
    1 - 255 (Default is 125)


  ospf (False, any, None)
    Field ospf


    ospf_global (optional, any, None)
      Field ospf_global


    ospf_ip_list (optional, any, None)
      Field ospf_ip_list



  address_list (False, any, None)
    Field address_list


    ipv4_address (optional, any, None)
      IP address


    ipv4_netmask (optional, any, None)
      IP subnet mask










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

