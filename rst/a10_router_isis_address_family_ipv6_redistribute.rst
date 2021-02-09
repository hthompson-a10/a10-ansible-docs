.. _a10_router_isis_address_family_ipv6_redistribute_module:


a10_router_isis_address_family_ipv6_redistribute -- Configures A10 router.isis.address.family.ipv6.redistribute
===============================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Redistribute information from another routing protocol






Parameters
----------

  isis_tag (optional, any, None)
    Key to identify parent object


  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  isis (False, any, None)
    Field isis


    level_2_from (optional, any, None)
      Field level_2_from


    level_1_from (optional, any, None)
      Field level_1_from



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  vip_list (False, any, None)
    Field vip_list


    vip_metric_type (optional, any, None)
      'external'= Set IS-IS External metric type; 'internal'= Set IS-IS Internal metric type;


    vip_route_map (optional, any, None)
      Route map reference (Pointer to route-map entries)


    vip_metric (optional, any, None)
      Metric for redistributed routes (IS-IS default metric)


    vip_type (optional, any, None)
      'only-flagged'= Selected Virtual IP (VIP); 'only-not-flagged'= Only not flagged;


    vip_level (optional, any, None)
      'level-1'= IS-IS level-1 routes only; 'level-1-2'= IS-IS level-1 and level-2 routes; 'level-2'= IS-IS level-2 routes only;



  redist_list (False, any, None)
    Field redist_list


    metric_type (optional, any, None)
      'external'= Set IS-IS External metric type; 'internal'= Set IS-IS Internal metric type;


    route_map (optional, any, None)
      Route map reference (Pointer to route-map entries)


    metric (optional, any, None)
      Metric for redistributed routes (IS-IS default metric)


    ntype (optional, any, None)
      'bgp'= Border Gateway Protocol (BGP); 'connected'= Connected; 'floating-ip'= Floating IP; 'ip-nat-list'= IP NAT list; 'ip-nat'= IP NAT; 'lw4o6'= LW4O6 Prefix; 'nat-map'= NAT MAP Prefix; 'static-nat'= Static NAT; 'nat64'= NAT64 Prefix; 'ospf'= Open Shortest Path First (OSPF); 'rip'= Routing Information Protocol (RIP); 'static'= Static routes;


    level (optional, any, None)
      'level-1'= IS-IS level-1 routes only; 'level-1-2'= IS-IS level-1 and level-2 routes; 'level-2'= IS-IS level-2 routes only;



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

