.. _a10_router_bgp_address_family_ipv6_module:


a10_router_bgp_address_family_ipv6 -- Configures A10 router.bgp.address.family.ipv6
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

ipv6 Address family






Parameters
----------

  ansible_username (True, any, None)
    Username for AXAPI authentication


  aggregate_address_list (False, any, None)
    Field aggregate_address_list


    summary_only (optional, any, None)
      Filter more specific routes from updates


    aggregate_address (optional, any, None)
      Configure BGP aggregate entries (Aggregate IPv6 prefix)


    as_set (optional, any, None)
      Generate AS set path information



  bgp_as_number (optional, any, None)
    Key to identify parent object


  redistribute (False, any, None)
    Field redistribute


    static_nat_cfg (optional, any, None)
      Field static_nat_cfg


    ip_nat_cfg (optional, any, None)
      Field ip_nat_cfg


    nat64_cfg (optional, any, None)
      Field nat64_cfg


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


    uuid (optional, any, None)
      uuid of the object



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


  network (False, any, None)
    Field network


    ipv6_network_list (optional, any, None)
      Field ipv6_network_list


    synchronization (optional, any, None)
      Field synchronization



  distance (False, any, None)
    Field distance


    distance_ext (optional, any, None)
      Distance for routes external to the AS


    distance_int (optional, any, None)
      Distance for routes internal to the AS


    distance_local (optional, any, None)
      Distance for local routes



  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  originate (False, any, None)
    Distribute an IPv6 default route


  auto_summary (False, any, None)
    Enable automatic network number summarization


  bgp (False, any, None)
    Field bgp


    dampening_start_reuse (optional, any, None)
      Value to start reusing a route


    dampening (optional, any, None)
      Enable route-flap dampening


    dampening_half (optional, any, None)
      Reachability Half-life time for the penalty(minutes)


    dampening_unreachability (optional, any, None)
      Un-reachability Half-life time for the penalty(minutes)


    route_map (optional, any, None)
      Route-map to specify criteria for dampening (Route-map name)


    dampening_max_supress (optional, any, None)
      Maximum duration to suppress a stable route(minutes)


    dampening_start_supress (optional, any, None)
      Value to start suppressing a route



  state (True, any, None)
    State of the object to be created.


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

