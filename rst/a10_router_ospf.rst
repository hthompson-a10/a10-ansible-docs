.. _a10_router_ospf_module:


a10_router_ospf -- Configures A10 router.ospf
=============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Open Shortest Path First (OSPF)






Parameters
----------

  neighbor_list (False, any, None)
    Field neighbor_list


    priority (optional, any, None)
      OSPF priority of non-broadcast neighbor


    cost (optional, any, None)
      OSPF cost for point-to-multipoint neighbor (Metric)


    poll_interval (optional, any, None)
      OSPF dead-router polling interval (Seconds)


    address (optional, any, None)
      Neighbor address



  maximum_area (False, any, None)
    Maximum number of non-backbone areas (OSPF area limit)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  auto_cost_reference_bandwidth (False, any, None)
    Use reference bandwidth method to assign OSPF cost (The reference bandwidth in terms of Mbits per second)


  host_list (False, any, None)
    Field host_list


    area_cfg (optional, any, None)
      Field area_cfg


    host_address (optional, any, None)
      Host address



  log_adjacency_changes_cfg (False, any, None)
    Field log_adjacency_changes_cfg


    state (optional, any, None)
      'detail'= Log changes in adjacency state; 'disable'= Disable logging;



  distribute_lists (False, any, None)
    Field distribute_lists


    direction (optional, any, None)
      'in'= Filter incoming routing updates; 'out'= Filter outgoing routing updates;


    protocol (optional, any, None)
      'bgp'= Border Gateway Protocol (BGP); 'connected'= Connected; 'floating-ip'= Floating IP; 'lw4o6'= LW4O6 Prefix; 'ip-nat'= IP NAT; 'ip-nat-list'= IP NAT list; 'static-nat'= Static NAT; 'isis'= ISO IS-IS; 'ospf'= Open Shortest Path First (OSPF); 'rip'= Routing Information Protocol (RIP); 'static'= Static routes;


    option (optional, any, None)
      'only-flagged'= Selected Virtual IP (VIP); 'only-not-flagged'= Only not flagged;


    value (optional, any, None)
      Access-list name


    ospf_id (optional, any, None)
      OSPF process ID



  area_list (False, any, None)
    Field area_list


    range_list (optional, any, None)
      Field range_list


    uuid (optional, any, None)
      uuid of the object


    virtual_link_list (optional, any, None)
      Field virtual_link_list


    stub_cfg (optional, any, None)
      Field stub_cfg


    nssa_cfg (optional, any, None)
      Field nssa_cfg


    filter_lists (optional, any, None)
      Field filter_lists


    default_cost (optional, any, None)
      Set the summary-default cost of a NSSA or stub area (Stub's advertised default summary cost)


    area_ipv4 (optional, any, None)
      OSPF area ID in IP address format


    shortcut (optional, any, None)
      'default'= Set default shortcutting behavior; 'disable'= Disable shortcutting through the area; 'enable'= Enable shortcutting through the area;


    area_num (optional, any, None)
      OSPF area ID as a decimal value


    auth_cfg (optional, any, None)
      Field auth_cfg



  bfd_all_interfaces (False, any, None)
    Enable BFD on all interfaces


  distribute_internal_list (False, any, None)
    Field distribute_internal_list


    di_cost (optional, any, None)
      Cost of route


    di_type (optional, any, None)
      'lw4o6'= LW4O6 Prefix; 'floating-ip'= Floating IP; 'ip-nat'= IP NAT; 'ip-nat- list'= IP NAT list; 'static-nat'= Static NAT; 'vip'= Only not flagged Virtual IP (VIP); 'vip-only-flagged'= Selected Virtual IP (VIP);


    di_area_num (optional, any, None)
      OSPF area ID as a decimal value


    di_area_ipv4 (optional, any, None)
      OSPF area ID as a IP address format



  uuid (False, any, None)
    uuid of the object


  max_concurrent_dd (False, any, None)
    Maximum number allowed to process DD concurrently (Number of DD process)


  state (True, any, None)
    State of the object to be created.


  passive_interface (False, any, None)
    Field passive_interface


    loopback_cfg (optional, any, None)
      Field loopback_cfg


    eth_cfg (optional, any, None)
      Field eth_cfg


    ve_cfg (optional, any, None)
      Field ve_cfg


    trunk_cfg (optional, any, None)
      Field trunk_cfg


    lif_cfg (optional, any, None)
      Field lif_cfg


    tunnel_cfg (optional, any, None)
      Field tunnel_cfg



  router_id (False, any, None)
    Field router_id


    value (optional, any, None)
      OSPF router-id in IPv4 address format



  default_metric (False, any, None)
    Set metric of redistributed routes (Default metric)


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


  ospf_1 (False, any, None)
    Field ospf_1


    abr_type (optional, any, None)
      Field abr_type



  process_id (True, any, None)
    OSPF process ID


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  overflow (False, any, None)
    Field overflow


    database (optional, any, None)
      Field database



  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  distance (False, any, None)
    Field distance


    distance_value (optional, any, None)
      OSPF Administrative distance


    distance_ospf (optional, any, None)
      Field distance_ospf



  redistribute (False, any, None)
    Field redistribute


    uuid (optional, any, None)
      uuid of the object


    metric_type_ip_nat (optional, any, None)
      '1'= Set OSPF External Type 1 metrics; '2'= Set OSPF External Type 2 metrics;


    vip_floating_list (optional, any, None)
      Field vip_floating_list


    redist_list (optional, any, None)
      Field redist_list


    route_map_ip_nat (optional, any, None)
      Route map reference (Pointer to route-map entries)


    ospf_list (optional, any, None)
      Field ospf_list


    metric_ip_nat (optional, any, None)
      OSPF default metric (OSPF metric)


    tag_ip_nat (optional, any, None)
      Set tag for routes redistributed into OSPF (32-bit tag value)


    ip_nat_floating_list (optional, any, None)
      Field ip_nat_floating_list


    vip_list (optional, any, None)
      Field vip_list


    ip_nat (optional, any, None)
      IP-NAT



  ha_standby_extra_cost (False, any, None)
    Field ha_standby_extra_cost


    extra_cost (optional, any, None)
      The extra cost value


    group (optional, any, None)
      Group (Group ID)



  ansible_password (True, any, None)
    Password for AXAPI authentication


  network_list (False, any, None)
    Field network_list


    network_ipv4 (optional, any, None)
      Network number


    network_ipv4_mask (optional, any, None)
      OSPF wild card bits


    network_ipv4_cidr (optional, any, None)
      OSPF network prefix


    network_area (optional, any, None)
      Field network_area



  summary_address_list (False, any, None)
    Field summary_address_list


    tag (optional, any, None)
      Set tag (32-bit tag value)


    not_advertise (optional, any, None)
      Suppress routes that match the prefix


    summary_address (optional, any, None)
      Configure IP address summaries (Summary prefix)



  timers (False, any, None)
    Field timers


    spf (optional, any, None)
      Field spf



  rfc1583_compatible (False, any, None)
    Compatible with RFC 1583


  user_tag (False, any, None)
    Customized tag









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

