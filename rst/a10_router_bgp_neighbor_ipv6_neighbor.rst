.. _a10_router_bgp_neighbor_ipv6_neighbor_module:


a10_router_bgp_neighbor_ipv6_neighbor -- Configures A10 router.bgp.neighbor.ipv6-neighbor
=========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Specify a ipv6 neighbor router






Parameters
----------

  default_originate (False, any, None)
    Originate default route to this neighbor


  neighbor_ipv6 (True, any, None)
    Neighbor IPv6 address


  dynamic (False, any, None)
    Advertise dynamic capability to this neighbor


  multihop (False, any, None)
    Enable multihop


  shutdown (False, any, None)
    Administratively shut down this neighbor


  next_hop_self (False, any, None)
    Disable the next hop calculation for this neighbor


  uuid (False, any, None)
    uuid of the object


  ebgp_multihop (False, any, None)
    Allow EBGP neighbors not on directly connected networks


  bfd (False, any, None)
    Bidirectional Forwarding Detection (BFD)


  a10_partition (False, any, None)
    Destination/target partition for object/command


  acos_application_only (False, any, None)
    Send BGP update to ACOS application


  allowas_in (False, any, None)
    Accept as-path with my AS present in it


  passive (False, any, None)
    Don't send open messages to this neighbor


  advertisement_interval (False, any, None)
    Minimum interval between sending BGP routing updates (time in seconds)


  timers_holdtime (False, any, None)
    Holdtime


  dont_capability_negotiate (False, any, None)
    Do not perform capability negotiation


  inbound (False, any, None)
    Allow inbound soft reconfiguration for this neighbor


  ansible_port (True, any, None)
    Port for AXAPI authentication


  timers_keepalive (False, any, None)
    Keepalive interval


  maximum_prefix_thres (False, any, None)
    threshold-value, 1 to 100 percent


  unsuppress_map (False, any, None)
    Route-map to selectively unsuppress suppressed routes (Name of route map)


  distribute_lists (False, any, None)
    Field distribute_lists


    distribute_list_direction (optional, any, None)
      'in'= in; 'out'= out;


    distribute_list (optional, any, None)
      Filter updates to/from this neighbor (IP standard/extended/named access list)



  key_type (False, any, None)
    'md5'= md5; 'meticulous-md5'= meticulous-md5; 'meticulous-sha1'= meticulous- sha1; 'sha1'= sha1; 'simple'= simple;  (Keyed MD5/Meticulous Keyed MD5/Meticulous Keyed SHA1/Keyed SHA1/Simple Password)


  route_refresh (False, any, None)
    Advertise route-refresh capability to this neighbor


  prefix_list_direction (False, any, None)
    'both'= both; 'receive'= receive; 'send'= send;


  nbr_remote_as (False, any, None)
    Specify AS number of BGP neighbor


  tunnel (False, any, None)
    Tunnel interface (Tunnel interface number)


  neighbor_prefix_lists (False, any, None)
    Field neighbor_prefix_lists


    nbr_prefix_list (optional, any, None)
      Filter updates to/from this neighbor (Name of a prefix list)


    nbr_prefix_list_direction (optional, any, None)
      'in'= in; 'out'= out;



  send_community_val (False, any, None)
    'both'= Send Standard and Extended Community attributes; 'none'= Disable Sending Community attributes; 'standard'= Send Standard Community attributes; 'extended'= Send Extended Community attributes;


  activate (False, any, None)
    Enable the Address Family for this Neighbor


  ve (False, any, None)
    Virtual ethernet interface (Virtual ethernet interface number)


  weight (False, any, None)
    Set default weight for routes from this neighbor


  ansible_username (True, any, None)
    Username for AXAPI authentication


  bgp_as_number (optional, any, None)
    Key to identify parent object


  allowas_in_count (False, any, None)
    Number of occurrences of AS number


  connect (False, any, None)
    BGP connect timer


  neighbor_filter_lists (False, any, None)
    Field neighbor_filter_lists


    filter_list (optional, any, None)
      Establish BGP filters (AS path access-list name)


    filter_list_direction (optional, any, None)
      'in'= in; 'out'= out;



  strict_capability_match (False, any, None)
    Strict capability negotiation match


  collide_established (False, any, None)
    Include Neighbor in Established State for Collision Detection


  remove_private_as (False, any, None)
    Remove private AS number from outbound updates


  lif (False, any, None)
    Logical interface (Lif interface number)


  update_source_ip (False, any, None)
    IP address


  override_capability (False, any, None)
    Override capability negotiation result


  loopback (False, any, None)
    Loopback interface (Port number)


  route_map (False, any, None)
    Route-map to specify criteria to originate default (route-map name)


  key_id (False, any, None)
    Key ID


  peer_group_name (False, any, None)
    Configure peer-group (peer-group name)


  state (True, any, None)
    State of the object to be created.


  maximum_prefix (False, any, None)
    Maximum number of prefix accept from this peer (maximum no. of prefix limit (various depends on model))


  pass_value (False, any, None)
    Key String


  enforce_multihop (False, any, None)
    Enforce EBGP neighbors to perform multihop


  as_origination_interval (False, any, None)
    Minimum interval between sending AS-origination routing updates (time in seconds)


  description (False, any, None)
    Neighbor specific description (Up to 80 characters describing this neighbor)


  bfd_value (False, any, None)
    Key String


  pass_encrypted (False, any, None)
    Field pass_encrypted


  trunk (False, any, None)
    Trunk interface (Trunk interface number)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  neighbor_route_map_lists (False, any, None)
    Field neighbor_route_map_lists


    nbr_rmap_direction (optional, any, None)
      'in'= in; 'out'= out;


    nbr_route_map (optional, any, None)
      Apply route map to neighbor (Name of route map)



  ebgp_multihop_hop_count (False, any, None)
    maximum hop count


  ansible_host (True, any, None)
    Host for AXAPI authentication


  update_source_ipv6 (False, any, None)
    IPv6 address


  bfd_encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)


  disallow_infinite_holdtime (False, any, None)
    BGP per neighbor disallow-infinite-holdtime


  ethernet (False, any, None)
    Ethernet interface (Port number)


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

