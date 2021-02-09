.. _a10_router_bgp_module:


a10_router_bgp -- Configures A10 router.bgp
===========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Border Gateway Protocol (BGP)






Parameters
----------

  as_number (True, any, None)
    AS number


  ansible_username (True, any, None)
    Username for AXAPI authentication


  aggregate_address_list (False, any, None)
    Field aggregate_address_list


    summary_only (optional, any, None)
      Filter more specific routes from updates


    aggregate_address (optional, any, None)
      Configure BGP aggregate entries (Aggregate prefix)


    as_set (optional, any, None)
      Generate AS set path information



  ansible_port (True, any, None)
    Port for AXAPI authentication


  synchronization (False, any, None)
    Perform IGP synchronization


  maximum_paths_value (False, any, None)
    Supported BGP multipath numbers


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  distance_list (False, any, None)
    Field distance_list


    acl_str (optional, any, None)
      Access list name


    local_routes_dist (optional, any, None)
      Distance for local routes


    src_prefix (optional, any, None)
      IP source prefix


    int_routes_dist (optional, any, None)
      Distance for routes internal to the AS


    ext_routes_dist (optional, any, None)
      Distance for routes external to the AS


    admin_distance (optional, any, None)
      Define an administrative distance



  redistribute (False, any, None)
    Field redistribute


    ip_nat_cfg (optional, any, None)
      Field ip_nat_cfg


    uuid (optional, any, None)
      uuid of the object


    static_cfg (optional, any, None)
      Field static_cfg


    ip_nat_list_cfg (optional, any, None)
      Field ip_nat_list_cfg


    connected_cfg (optional, any, None)
      Field connected_cfg


    vip (optional, any, None)
      Field vip


    ospf_cfg (optional, any, None)
      Field ospf_cfg


    rip_cfg (optional, any, None)
      Field rip_cfg


    nat_map_cfg (optional, any, None)
      Field nat_map_cfg


    lw4o6_cfg (optional, any, None)
      Field lw4o6_cfg


    isis_cfg (optional, any, None)
      Field isis_cfg


    floating_ip_cfg (optional, any, None)
      Field floating_ip_cfg


    static_nat_cfg (optional, any, None)
      Field static_nat_cfg



  address_family (False, any, None)
    Field address_family


    ipv6 (optional, any, None)
      Field ipv6



  user_tag (False, any, None)
    Customized tag


  originate (False, any, None)
    Distribute a default route


  auto_summary (False, any, None)
    Enable automatic network number summarization


  bgp (False, any, None)
    Field bgp


    router_id (optional, any, None)
      Override current router identifier (peers will reset) (Manually configured router identifier)


    deterministic_med (optional, any, None)
      Pick the best-MED path among paths advertised from the neighboring AS


    scan_time (optional, any, None)
      Configure background scan interval (Scan interval (sec) [Default=60 Disable=0])


    always_compare_med (optional, any, None)
      Allow comparing MED from different neighbors


    bestpath_cfg (optional, any, None)
      Field bestpath_cfg


    enforce_first_as (optional, any, None)
      Enforce the first AS for EBGP routes


    fast_external_failover (optional, any, None)
      Immediately reset session if a link to a directly connected external peer goes down


    override_validation (optional, any, None)
      override router-id validation


    nexthop_trigger_count (optional, any, None)
      BGP nexthop-tracking status (count)


    log_neighbor_changes (optional, any, None)
      Log neighbor up/down and reset reason


    local_preference_value (optional, any, None)
      Configure default local preference value


    dampening_cfg (optional, any, None)
      Field dampening_cfg



  network (False, any, None)
    Field network


    synchronization (optional, any, None)
      Field synchronization


    ip_cidr_list (optional, any, None)
      Field ip_cidr_list



  state (True, any, None)
    State of the object to be created.


  timers (False, any, None)
    Field timers


    bgp_holdtime (optional, any, None)
      Holdtime


    bgp_keepalive (optional, any, None)
      Keepalive interval



  neighbor (False, any, None)
    Field neighbor


    ipv6_neighbor_list (optional, any, None)
      Field ipv6_neighbor_list


    ipv4_neighbor_list (optional, any, None)
      Field ipv4_neighbor_list


    peer_group_neighbor_list (optional, any, None)
      Field peer_group_neighbor_list



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

