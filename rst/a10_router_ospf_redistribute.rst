.. _a10_router_ospf_redistribute_module:


a10_router_ospf_redistribute -- Configures A10 router.ospf.redistribute
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Redistribute information from another routing protocol






Parameters
----------

  ansible_username (True, any, None)
    Username for AXAPI authentication


  redist_list (False, any, None)
    Field redist_list


    metric_type (optional, any, None)
      '1'= Set OSPF External Type 1 metrics; '2'= Set OSPF External Type 2 metrics;


    route_map (optional, any, None)
      Route map reference (Pointer to route-map entries)


    metric (optional, any, None)
      OSPF default metric (OSPF metric)


    ntype (optional, any, None)
      'bgp'= Border Gateway Protocol (BGP); 'connected'= Connected; 'floating-ip'= Floating IP; 'ip-nat-list'= IP NAT list; 'lw4o6'= LW4O6 Prefix; 'nat-map'= NAT MAP Prefix; 'static-nat'= Static NAT; 'isis'= ISO IS-IS; 'rip'= Routing Information Protocol (RIP); 'static'= Static routes;


    tag (optional, any, None)
      Set tag for routes redistributed into OSPF (32-bit tag value)



  route_map_ip_nat (False, any, None)
    Route map reference (Pointer to route-map entries)


  ospf_list (False, any, None)
    Field ospf_list


    metric_type_ospf (optional, any, None)
      '1'= Set OSPF External Type 1 metrics; '2'= Set OSPF External Type 2 metrics;


    tag_ospf (optional, any, None)
      Set tag for routes redistributed into OSPF (32-bit tag value)


    route_map_ospf (optional, any, None)
      Route map reference (Pointer to route-map entries)


    process_id (optional, any, None)
      OSPF process ID


    ospf (optional, any, None)
      Open Shortest Path First (OSPF)


    metric_ospf (optional, any, None)
      OSPF default metric (OSPF metric)



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  ospf_process_id (optional, any, None)
    Key to identify parent object


  tag_ip_nat (False, any, None)
    Set tag for routes redistributed into OSPF (32-bit tag value)


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ip_nat (False, any, None)
    IP-NAT


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_password (True, any, None)
    Password for AXAPI authentication


  metric_type_ip_nat (False, any, None)
    '1'= Set OSPF External Type 1 metrics; '2'= Set OSPF External Type 2 metrics;


  vip_floating_list (False, any, None)
    Field vip_floating_list


    vip_address (optional, any, None)
      Address


    vip_floating_IP_forward (optional, any, None)
      Floating-IP as forward address



  state (True, any, None)
    State of the object to be created.


  metric_ip_nat (False, any, None)
    OSPF default metric (OSPF metric)


  vip_list (False, any, None)
    Field vip_list


    type_vip (optional, any, None)
      'only-flagged'= Selected Virtual IP (VIP); 'only-not-flagged'= Only not flagged;


    metric_type_vip (optional, any, None)
      '1'= Set OSPF External Type 1 metrics; '2'= Set OSPF External Type 2 metrics;


    route_map_vip (optional, any, None)
      Route map reference (Pointer to route-map entries)


    metric_vip (optional, any, None)
      OSPF default metric (OSPF metric)


    tag_vip (optional, any, None)
      Set tag for routes redistributed into OSPF (32-bit tag value)



  ip_nat_floating_list (False, any, None)
    Field ip_nat_floating_list


    ip_nat_floating_IP_forward (optional, any, None)
      Floating-IP as forward address


    ip_nat_prefix (optional, any, None)
      Address










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

