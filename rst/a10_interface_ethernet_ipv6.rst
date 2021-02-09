.. _a10_interface_ethernet_ipv6_module:


a10_interface_ethernet_ipv6 -- Configures A10 interface.ethernet.ipv6
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Global IPv6 configuration subcommands






Parameters
----------

  ansible_username (True, any, None)
    Username for AXAPI authentication


  rip (False, any, None)
    Field rip


    split_horizon_cfg (optional, any, None)
      Field split_horizon_cfg


    uuid (optional, any, None)
      uuid of the object



  access_list_cfg (False, any, None)
    Field access_list_cfg


    inbound (optional, any, None)
      ACL applied on incoming packets to this interface


    v6_acl_name (optional, any, None)
      Apply ACL rules to incoming packets on this interface (Named Access List)



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  router_adver (False, any, None)
    Field router_adver


    min_interval (optional, any, None)
      Set Router Advertisement Min Interval (default= 200) (Min Router Advertisement Interval (seconds))


    default_lifetime (optional, any, None)
      Set Router Advertisement Default Lifetime (default= 1800) (Default Lifetime (seconds))


    floating_ip (optional, any, None)
      Use a floating IP as the source address for Router advertisements


    retransmit_timer (optional, any, None)
      Set Router Advertisement Retransmit Timer (default= 0)


    use_floating_ip (optional, any, None)
      Use a floating IP as the source address for Router advertisements


    action (optional, any, None)
      'enable'= Enable Router Advertisements on this interface; 'disable'= Disable Router Advertisements on this interface;


    max_interval (optional, any, None)
      Set Router Advertisement Max Interval (default= 600) (Max Router Advertisement Interval (seconds))


    use_floating_ip_default_vrid (optional, any, None)
      Use a floating IP as the source address for Router advertisements


    adver_mtu_disable (optional, any, None)
      Disable Router Advertisement MTU Option


    other_config_action (optional, any, None)
      'enable'= Enable the Other Stateful Configuration flag; 'disable'= Disable the Other Stateful Configuration flag (default);


    floating_ip_default_vrid (optional, any, None)
      Use a floating IP as the source address for Router advertisements


    adver_vrid (optional, any, None)
      Specify ha VRRP-A vrid


    prefix_list (optional, any, None)
      Field prefix_list


    rate_limit (optional, any, None)
      Rate Limit the processing of incoming Router Solicitations (Max Number of Router Solicitations to process per second)


    adver_vrid_default (optional, any, None)
      Default VRRP-A vrid


    adver_mtu (optional, any, None)
      Set Router Advertisement MTU Option


    reachable_time (optional, any, None)
      Set Router Advertisement Reachable ime (default= 0) (Reachable Time (milliseconds))


    hop_limit (optional, any, None)
      Set Router Advertisement Hop Limit (default= 255)


    managed_config_action (optional, any, None)
      'enable'= Enable the Managed Address Configuration flag; 'disable'= Disable the Managed Address Configuration flag (default);



  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_password (True, any, None)
    Password for AXAPI authentication


  inside (False, any, None)
    Configure interface as inside


  state (True, any, None)
    State of the object to be created.


  ipv6_enable (False, any, None)
    Enable IPv6 processing


  outside (False, any, None)
    Configure interface as outside


  ethernet_ifnum (optional, any, None)
    Key to identify parent object


  ttl_ignore (False, any, None)
    Ignore TTL decrement for a received packet before sending out


  router (False, any, None)
    Field router


    ripng (optional, any, None)
      Field ripng


    ospf (optional, any, None)
      Field ospf


    isis (optional, any, None)
      Field isis



  stateful_firewall (False, any, None)
    Field stateful_firewall


    class_list (optional, any, None)
      Class List (Class List Name)


    outside (optional, any, None)
      Outside (public) interface for stateful firewall


    uuid (optional, any, None)
      uuid of the object


    acl_name (optional, any, None)
      Access-list Name


    inside (optional, any, None)
      Inside (private) interface for stateful firewall


    access_list (optional, any, None)
      Access-list for traffic from the outside



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



  address_list (False, any, None)
    Field address_list


    ipv6_addr (optional, any, None)
      Set the IPv6 address of an interface


    address_type (optional, any, None)
      'anycast'= Configure an IPv6 anycast address; 'link-local'= Configure an IPv6 link local address;










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

