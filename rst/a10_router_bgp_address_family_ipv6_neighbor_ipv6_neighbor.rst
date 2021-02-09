.. _a10_router_bgp_address_family_ipv6_neighbor_ipv6_neighbor_module:


a10_router_bgp_address_family_ipv6_neighbor_ipv6_neighbor -- Configures A10 router.bgp.address.family.ipv6-neighbor.ipv6.neighbor
=================================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Specify a peer-group neighbor router






Parameters
----------

  default_originate (False, any, None)
    Originate default route to this neighbor


  next_hop_self (False, any, None)
    Disable the next hop calculation for this neighbor


  activate (False, any, None)
    Enable the Address Family for this Neighbor


  weight (False, any, None)
    Set default weight for routes from this neighbor


  ansible_username (True, any, None)
    Username for AXAPI authentication


  inbound (False, any, None)
    Allow inbound soft reconfiguration for this neighbor


  neighbor_ipv6 (True, any, None)
    Neighbor IPv6 address


  peer_group_name (False, any, None)
    Configure peer-group (peer-group name)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  maximum_prefix_thres (False, any, None)
    threshold-value, 1 to 100 percent


  unsuppress_map (False, any, None)
    Route-map to selectively unsuppress suppressed routes (Name of route map)


  neighbor_filter_lists (False, any, None)
    Field neighbor_filter_lists


    filter_list (optional, any, None)
      Establish BGP filters (AS path access-list name)


    filter_list_direction (optional, any, None)
      'in'= in; 'out'= out;



  neighbor_route_map_lists (False, any, None)
    Field neighbor_route_map_lists


    nbr_rmap_direction (optional, any, None)
      'in'= in; 'out'= out;


    nbr_route_map (optional, any, None)
      Apply route map to neighbor (Name of route map)



  remove_private_as (False, any, None)
    Remove private AS number from outbound updates


  allowas_in_count (False, any, None)
    Number of occurrences of AS number


  bgp_as_number (optional, any, None)
    Key to identify parent object


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ansible_port (True, any, None)
    Port for AXAPI authentication


  prefix_list_direction (False, any, None)
    'both'= both; 'receive'= receive; 'send'= send;


  uuid (False, any, None)
    uuid of the object


  route_map (False, any, None)
    Route-map to specify criteria to originate default (route-map name)


  neighbor_prefix_lists (False, any, None)
    Field neighbor_prefix_lists


    nbr_prefix_list (optional, any, None)
      Filter updates to/from this neighbor (Name of a prefix list)


    nbr_prefix_list_direction (optional, any, None)
      'in'= in; 'out'= out;



  allowas_in (False, any, None)
    Accept as-path with my AS present in it


  state (True, any, None)
    State of the object to be created.


  maximum_prefix (False, any, None)
    Maximum number of prefix accept from this peer (maximum no. of prefix limit (various depends on model))


  distribute_lists (False, any, None)
    Field distribute_lists


    distribute_list_direction (optional, any, None)
      'in'= in; 'out'= out;


    distribute_list (optional, any, None)
      Filter updates to/from this neighbor (IP standard/extended/named access list)



  send_community_val (False, any, None)
    'both'= Send Standard and Extended Community attributes; 'none'= Disable Sending Community attributes; 'standard'= Send Standard Community attributes; 'extended'= Send Extended Community attributes;


  a10_partition (False, any, None)
    Destination/target partition for object/command


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

