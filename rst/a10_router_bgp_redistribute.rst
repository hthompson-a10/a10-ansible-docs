.. _a10_router_bgp_redistribute_module:


a10_router_bgp_redistribute -- Configures A10 router.bgp.redistribute
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Redistribute information from another routing protocol






Parameters
----------

  ip_nat_cfg (False, any, None)
    Field ip_nat_cfg


    route_map (optional, any, None)
      Route map reference (Pointer to route-map entries)


    ip_nat (optional, any, None)
      IP NAT



  ansible_username (True, any, None)
    Username for AXAPI authentication


  bgp_as_number (optional, any, None)
    Key to identify parent object


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  vip (False, any, None)
    Field vip


    only_not_flagged_cfg (optional, any, None)
      Field only_not_flagged_cfg


    only_flagged_cfg (optional, any, None)
      Field only_flagged_cfg



  floating_ip_cfg (False, any, None)
    Field floating_ip_cfg


    route_map (optional, any, None)
      Route map reference (Pointer to route-map entries)


    floating_ip (optional, any, None)
      Floating IP



  lw4o6_cfg (False, any, None)
    Field lw4o6_cfg


    route_map (optional, any, None)
      Route map reference (Pointer to route-map entries)


    lw4o6 (optional, any, None)
      LW4O6 Prefix



  isis_cfg (False, any, None)
    Field isis_cfg


    route_map (optional, any, None)
      Route map reference (Pointer to route-map entries)


    isis (optional, any, None)
      ISO IS-IS



  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  static_cfg (False, any, None)
    Field static_cfg


    route_map (optional, any, None)
      Route map reference (Pointer to route-map entries)


    static (optional, any, None)
      Static routes



  ip_nat_list_cfg (False, any, None)
    Field ip_nat_list_cfg


    ip_nat_list (optional, any, None)
      IP NAT list


    route_map (optional, any, None)
      Route map reference (Pointer to route-map entries)



  connected_cfg (False, any, None)
    Field connected_cfg


    route_map (optional, any, None)
      Route map reference (Pointer to route-map entries)


    connected (optional, any, None)
      Connected



  state (True, any, None)
    State of the object to be created.


  ospf_cfg (False, any, None)
    Field ospf_cfg


    route_map (optional, any, None)
      Route map reference (Pointer to route-map entries)


    ospf (optional, any, None)
      Open Shortest Path First (OSPF)



  rip_cfg (False, any, None)
    Field rip_cfg


    route_map (optional, any, None)
      Route map reference (Pointer to route-map entries)


    rip (optional, any, None)
      Routing Information Protocol (RIP)



  nat_map_cfg (False, any, None)
    Field nat_map_cfg


    route_map (optional, any, None)
      Route map reference (Pointer to route-map entries)


    nat_map (optional, any, None)
      NAT MAP Prefix



  ansible_password (True, any, None)
    Password for AXAPI authentication


  static_nat_cfg (False, any, None)
    Field static_nat_cfg


    route_map (optional, any, None)
      Route map reference (Pointer to route-map entries)


    static_nat (optional, any, None)
      Static NAT Prefix










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

