.. _a10_router_ipv6_rip_redistribute_module:


a10_router_ipv6_rip_redistribute -- Configures A10 router.ipv6.rip.redistribute
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Redistribute information from another routing protocol






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  vip_list (False, any, None)
    Field vip_list


    vip_route_map (optional, any, None)
      Route map reference (Pointer to route-map entries)


    vip_metric (optional, any, None)
      Metric for redistributed routes (metric value)


    vip_type (optional, any, None)
      'only-flagged'= Selected Virtual IP (VIP); 'only-not-flagged'= Only not flagged;



  redist_list (False, any, None)
    Field redist_list


    route_map (optional, any, None)
      Route map reference (Pointer to route-map entries)


    metric (optional, any, None)
      Metric for redistributed routes (metric value)


    ntype (optional, any, None)
      'bgp'= Border Gateway Protocol (BGP); 'connected'= Connected; 'floating-ip'= Floating IP; 'ip-nat-list'= IP NAT list; 'ip-nat'= IP NAT; 'isis'= ISO IS-IS; 'lw4o6'= LW4O6 Prefix; 'nat-map'= NAT MAP Prefix; 'nat64'= NAT64 Prefix; 'static-nat'= Static NAT; 'ospf'= Open Shortest Path First (OSPF); 'static'= Static routes;



  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


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

