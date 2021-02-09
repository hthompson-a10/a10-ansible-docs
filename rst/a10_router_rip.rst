.. _a10_router_rip_module:


a10_router_rip -- Configures A10 router.rip
===========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Routing Information Protocol (RIP)






Parameters
----------

  ansible_username (True, any, None)
    Username for AXAPI authentication


  default_metric (False, any, None)
    Set a metric of redistribute routes (Default metric)


  default_information (False, any, None)
    'originate'= originate;  (Distribute default route)


  ansible_port (True, any, None)
    Port for AXAPI authentication


  network_interface_list_cfg (False, any, None)
    Field network_interface_list_cfg


    tunnel (optional, any, None)
      Tunnel interface (Tunnel interface number)


    ethernet (optional, any, None)
      Ethernet interface (Port number)


    loopback (optional, any, None)
      Loopback interface (Port number)


    ve (optional, any, None)
      Virtual ethernet interface (Virtual ethernet interface number)


    trunk (optional, any, None)
      Trunk interface (Trunk interface number)



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  rip_maximum_prefix_cfg (False, any, None)
    Field rip_maximum_prefix_cfg


    maximum_prefix_thres (optional, any, None)
      Percentage of maximum routes to generate a warning (Default 75%)


    maximum_prefix (optional, any, None)
      Set the maximum number of RIP routes



  ansible_host (True, any, None)
    Host for AXAPI authentication


  route_cfg (False, any, None)
    Field route_cfg


    route (optional, any, None)
      Static route advertisement (debugging purpose) (IP prefix network/length)



  redistribute (False, any, None)
    Field redistribute


    vip_list (optional, any, None)
      Field vip_list


    redist_list (optional, any, None)
      Field redist_list


    uuid (optional, any, None)
      uuid of the object



  uuid (False, any, None)
    uuid of the object


  distance_list_cfg (False, any, None)
    Field distance_list_cfg


    distance (optional, any, None)
      Administrative distance (Distance value)


    distance_ipv4_mask (optional, any, None)
      IP source prefix


    distance_acl (optional, any, None)
      Access list name



  passive_interface_list (False, any, None)
    Field passive_interface_list


    tunnel (optional, any, None)
      Tunnel interface (Tunnel interface number)


    ethernet (optional, any, None)
      Ethernet interface (Port number)


    loopback (optional, any, None)
      Loopback interface (Port number)


    ve (optional, any, None)
      Virtual ethernet interface (Virtual ethernet interface number)


    trunk (optional, any, None)
      Trunk interface (Trunk interface number)



  a10_partition (False, any, None)
    Destination/target partition for object/command


  distribute_list (False, any, None)
    Field distribute_list


    acl_cfg (optional, any, None)
      Field acl_cfg


    prefix (optional, any, None)
      Field prefix


    uuid (optional, any, None)
      uuid of the object



  network_addresses (False, any, None)
    Field network_addresses


    network_ipv4_mask (optional, any, None)
      IP prefix network/length, e.g., 35.0.0.0/8



  cisco_metric_behavior (False, any, None)
    'enable'= Enables updating metric consistent with Cisco; 'disable'= Disables updating metric consistent with Cisco;  (Enable/Disable updating metric consistent with Cisco)


  state (True, any, None)
    State of the object to be created.


  version (False, any, None)
    Set routing protocol version (RIP version)


  timers (False, any, None)
    Field timers


    timers_cfg (optional, any, None)
      Field timers_cfg



  neighbor (False, any, None)
    Field neighbor


    value (optional, any, None)
      Neighbor address



  recv_buffer_size (False, any, None)
    Set the RIP UDP receive buffer size (the RIP UDP receive buffer size value)


  ansible_password (True, any, None)
    Password for AXAPI authentication


  offset_list (False, any, None)
    Field offset_list


    acl_cfg (optional, any, None)
      Field acl_cfg


    uuid (optional, any, None)
      uuid of the object










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

