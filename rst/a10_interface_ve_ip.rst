.. _a10_interface_ve_ip_module:


a10_interface_ve_ip -- Configures A10 interface.ve.ip
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Global IP configuration subcommands






Parameters
----------

  query_interval (False, any, None)
    1 - 255 (Default is 125)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  max_resp_time (False, any, None)
    Maximum Response Time (Max Response Time (Default is 100))


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


  router (False, any, None)
    Field router


    isis (optional, any, None)
      Field isis



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ve_ifnum (optional, any, None)
    Key to identify parent object


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  slb_partition_redirect (False, any, None)
    Redirect SLB traffic across partition


  ansible_password (True, any, None)
    Password for AXAPI authentication


  inside (False, any, None)
    Configure interface as inside


  allow_promiscuous_vip (False, any, None)
    Allow traffic to be associated with promiscuous VIP


  server (False, any, None)
    Server facing interface for IPv4/v6 traffic


  outside (False, any, None)
    Configure interface as outside


  client (False, any, None)
    Client facing interface for IPv4/v6 traffic


  ttl_ignore (False, any, None)
    Ignore TTL decrement for a received packet


  generate_membership_query (False, any, None)
    Enable Membership Query


  dhcp (False, any, None)
    Use DHCP to configure IP address


  stateful_firewall (False, any, None)
    Field stateful_firewall


    class_list (optional, any, None)
      Class List (Class List Name)


    outside (optional, any, None)
      Outside (public) interface for stateful firewall


    uuid (optional, any, None)
      uuid of the object


    inside (optional, any, None)
      Inside (private) interface for stateful firewall


    acl_id (optional, any, None)
      ACL id


    access_list (optional, any, None)
      Access-list for traffic from the outside



  address_list (False, any, None)
    Field address_list


    ipv4_address (optional, any, None)
      IP address


    ipv4_netmask (optional, any, None)
      IP subnet mask



  ospf (False, any, None)
    Field ospf


    ospf_global (optional, any, None)
      Field ospf_global


    ospf_ip_list (optional, any, None)
      Field ospf_ip_list



  helper_address_list (False, any, None)
    Field helper_address_list


    helper_address (optional, any, None)
      Helper address for DHCP packets (IP address)










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

