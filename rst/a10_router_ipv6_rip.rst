.. _a10_router_ipv6_rip_module:


a10_router_ipv6_rip -- Configures A10 router.ipv6.rip
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Routing Information Protocol (RIPng)






Parameters
----------

  ansible_username (True, any, None)
    Username for AXAPI authentication


  default_metric (False, any, None)
    Set a metric of redistribute routes (Default metric)


  default_information (False, any, None)
    'originate'= originate;  (Distribute default route)


  redistribute (False, any, None)
    Field redistribute


    vip_list (optional, any, None)
      Field vip_list


    redist_list (optional, any, None)
      Field redist_list


    uuid (optional, any, None)
      uuid of the object



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


  ripng_neighbor (False, any, None)
    Field ripng_neighbor


    ripng_neighbor_cfg (optional, any, None)
      Field ripng_neighbor_cfg



  route_cfg (False, any, None)
    Field route_cfg


    route (optional, any, None)
      Static route advertisement (debugging purpose) (IP prefix)



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



  route_map (False, any, None)
    Field route_map


    map_cfg (optional, any, None)
      Field map_cfg


    uuid (optional, any, None)
      uuid of the object



  distribute_list (False, any, None)
    Field distribute_list


    acl_cfg (optional, any, None)
      Field acl_cfg


    prefix (optional, any, None)
      Field prefix


    uuid (optional, any, None)
      uuid of the object



  state (True, any, None)
    State of the object to be created.


  cisco_metric_behavior (False, any, None)
    'enable'= Enables updating metric consistent with Cisco; 'disable'= Disables updating metric consistent with Cisco;  (Enable/Disable updating metric consistent with Cisco)


  aggregate_address_cfg (False, any, None)
    Field aggregate_address_cfg


    aggregate_address (optional, any, None)
      Set aggregate RIP route announcement (Aggregate network)



  timers (False, any, None)
    Field timers


    timers_cfg (optional, any, None)
      Field timers_cfg



  recv_buffer_size (False, any, None)
    Set the RIPNG UDP receive buffer size (the RIPNG UDP receive buffer size value)


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

