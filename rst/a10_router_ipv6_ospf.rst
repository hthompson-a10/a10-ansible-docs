.. _a10_router_ipv6_ospf_module:


a10_router_ipv6_ospf -- Configures A10 router.ipv6.ospf
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Open Shortest Path First (OSPFv3)






Parameters
----------

  router_id (False, any, None)
    router-id for the OSPF process (OSPFv3 router-id in IPv4 address format)


  abr_type_option (False, any, None)
    'cisco'= Alternative ABR, Cisco implementation (RFC3509); 'ibm'= Alternative ABR, IBM implementation (RFC3509); 'standard'= Standard behavior (RFC2328);


  ansible_username (True, any, None)
    Username for AXAPI authentication


  default_metric (False, any, None)
    Set metric of redistributed routes (Default metric)


  auto_cost_reference_bandwidth (False, any, None)
    Use reference bandwidth method to assign OSPF cost (The reference bandwidth in terms of Mbits per second)


  default_information (False, any, None)
    Field default_information


    uuid (optional, any, None)
      uuid of the object


    route_map (optional, any, None)
      Route map reference (Pointer to route-map entries)


    metric_type (optional, any, None)
      OSPF metric type for default routes


    always (optional, any, None)
      Always advertise default route


    metric (optional, any, None)
      OSPF default metric (OSPF metric)


    originate (optional, any, None)
      Distribute a default route



  ansible_port (True, any, None)
    Port for AXAPI authentication


  log_adjacency_changes (False, any, None)
    'detail'= Log changes in adjacency state; 'disable'= Disable logging;


  area_list (False, any, None)
    Field area_list


    range_list (optional, any, None)
      Field range_list


    uuid (optional, any, None)
      uuid of the object


    virtual_link_list (optional, any, None)
      Field virtual_link_list


    area_ipv4 (optional, any, None)
      OSPFv3 area ID in IP address format


    stub (optional, any, None)
      Configure OSPFv3 area as stub


    default_cost (optional, any, None)
      Set the summary-default cost of a NSSA or stub area (Stub's advertised default summary cost)


    no_summary (optional, any, None)
      Do not inject inter-area routes into area


    area_num (optional, any, None)
      OSPFv3 area ID as a decimal value



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  bfd_all_interfaces (False, any, None)
    Enable BFD on all interfaces


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  distribute_internal_list (False, any, None)
    Field distribute_internal_list


    area_ipv4 (optional, any, None)
      OSPF area ID in IP address format


    ntype (optional, any, None)
      'lw4o6'= LW4O6 Prefix; 'nat64'= NAT64 Prefix; 'static-nat'= Static NAT; 'floating-ip'= Floating IP; 'ip-nat'= IP NAT; 'ip-nat-list'= IP NAT list; 'vip'= Only not flagged Virtual IP (VIP); 'vip-only-flagged'= Selected Virtual IP (VIP);


    cost (optional, any, None)
      Cost


    area_num (optional, any, None)
      OSPF area ID as a decimal value



  ha_standby_extra_cost (False, any, None)
    Field ha_standby_extra_cost


    extra_cost (optional, any, None)
      The extra cost value


    group (optional, any, None)
      Group (Group ID)



  redistribute (False, any, None)
    Field redistribute


    uuid (optional, any, None)
      uuid of the object


    metric_type_ip_nat (optional, any, None)
      '1'= Set OSPFV3 External Type 1 metrics; '2'= Set OSPFV3 External Type 2 metrics;


    vip_floating_list (optional, any, None)
      Field vip_floating_list


    redist_list (optional, any, None)
      Field redist_list


    route_map_ip_nat (optional, any, None)
      Route map reference (Pointer to route-map entries)


    ospf_list (optional, any, None)
      Field ospf_list


    metric_ip_nat (optional, any, None)
      OSPFV3 default metric (OSPFV3 metric)


    ip_nat_floating_list (optional, any, None)
      Field ip_nat_floating_list


    vip_list (optional, any, None)
      Field vip_list


    ip_nat (optional, any, None)
      IP-NAT



  uuid (False, any, None)
    uuid of the object


  max_concurrent_dd (False, any, None)
    Maximum number allowed to process DD concurrently (Number of DD process)


  user_tag (False, any, None)
    Customized tag


  distribute_list (False, any, None)
    Field distribute_list


    prefix_list (optional, any, None)
      Field prefix_list



  state (True, any, None)
    State of the object to be created.


  process_id (True, any, None)
    OSPFv3 process tag


  timers (False, any, None)
    Field timers


    spf (optional, any, None)
      Field spf



  passive_interface (False, any, None)
    Field passive_interface


    loopback_cfg (optional, any, None)
      Field loopback_cfg


    eth_cfg (optional, any, None)
      Field eth_cfg


    ve_cfg (optional, any, None)
      Field ve_cfg


    tunnel_cfg (optional, any, None)
      Field tunnel_cfg


    trunk_cfg (optional, any, None)
      Field trunk_cfg



  ansible_password (True, any, None)
    Password for AXAPI authentication









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

