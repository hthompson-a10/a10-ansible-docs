.. _a10_route_map_set_module:


a10_route_map_set -- Configures A10 route.map.set
=================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Set values in destination routing protocol






Parameters
----------

  extcommunity (False, any, None)
    Field extcommunity


    rt (optional, any, None)
      Field rt


    soo (optional, any, None)
      Field soo



  origin (False, any, None)
    Field origin


    egp (optional, any, None)
      remote EGP


    incomplete (optional, any, None)
      unknown heritage


    igp (optional, any, None)
      local IGP



  route_map_tag (optional, any, None)
    Key to identify parent object


  weight (False, any, None)
    Field weight


    weight_val (optional, any, None)
      Weight value



  ansible_username (True, any, None)
    Username for AXAPI authentication


  ip (False, any, None)
    Field ip


    next_hop (optional, any, None)
      Field next_hop



  metric (False, any, None)
    Field metric


    value (optional, any, None)
      Metric Value (from -4294967295 to 4294967295)



  sequence (optional, any, None)
    Key to identify parent object


  as_path (False, any, None)
    Field as_path


    num (optional, any, None)
      AS number


    num2 (optional, any, None)
      AS number


    prepend (optional, any, None)
      Prepend to the as-path (AS number)



  community (False, any, None)
    BGP community attribute


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  ddos (False, any, None)
    Field ddos


    class_list_name (optional, any, None)
      Class-List Name


    class_list_cid (optional, any, None)
      Class-List Cid


    zone (optional, any, None)
      Zone Name



  tag (False, any, None)
    Field tag


    value (optional, any, None)
      Tag value



  originator_id (False, any, None)
    Field originator_id


    originator_ip (optional, any, None)
      IP address of originator



  metric_type (False, any, None)
    Field metric_type


    value (optional, any, None)
      'external'= IS-IS external metric type; 'internal'= IS-IS internal metric type; 'type-1'= OSPF external type 1 metric; 'type-2'= OSPF external type 2 metric;



  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  dampening_cfg (False, any, None)
    Field dampening_cfg


    dampening_supress (optional, any, None)
      Value to start suppressing a route


    dampening (optional, any, None)
      Enable route-flap dampening


    dampening_reuse (optional, any, None)
      Value to start reusing a route


    dampening_half_time (optional, any, None)
      Reachability Half-life time for the penalty(minutes)


    dampening_penalty (optional, any, None)
      Un-reachability Half-life time for the penalty(minutes)


    dampening_max_supress (optional, any, None)
      Maximum duration to suppress a stable route(minutes)



  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  level (False, any, None)
    Field level


    value (optional, any, None)
      'level-1'= Export into a level-1 area; 'level-1-2'= Export into level-1 and level-2; 'level-2'= Export into level-2 sub-domain;



  aggregator (False, any, None)
    Field aggregator


    aggregator_as (optional, any, None)
      Field aggregator_as



  atomic_aggregate (False, any, None)
    BGP atomic aggregate attribute


  state (True, any, None)
    State of the object to be created.


  local_preference (False, any, None)
    Field local_preference


    val (optional, any, None)
      Preference value



  ipv6 (False, any, None)
    Field ipv6


    next_hop_1 (optional, any, None)
      Field next_hop_1



  action (optional, any, None)
    Key to identify parent object


  comm_list (False, any, None)
    Field comm_list


    name (optional, any, None)
      Community-list name


    v_std (optional, any, None)
      Community-list number (standard)


    v_exp (optional, any, None)
      Community-list number (expanded)


    v_exp_delete (optional, any, None)
      Delete matching communities


    name_delete (optional, any, None)
      Delete matching communities


    delete (optional, any, None)
      Delete matching communities



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

