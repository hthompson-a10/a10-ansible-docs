.. _a10_route_map_module:


a10_route_map -- Configures A10 route-map
=========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure route-map






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  set (False, any, None)
    Field set


    extcommunity (optional, any, None)
      Field extcommunity


    origin (optional, any, None)
      Field origin


    weight (optional, any, None)
      Field weight


    ip (optional, any, None)
      Field ip


    metric (optional, any, None)
      Field metric


    as_path (optional, any, None)
      Field as_path


    community (optional, any, None)
      BGP community attribute


    ddos (optional, any, None)
      Field ddos


    tag (optional, any, None)
      Field tag


    originator_id (optional, any, None)
      Field originator_id


    metric_type (optional, any, None)
      Field metric_type


    dampening_cfg (optional, any, None)
      Field dampening_cfg


    uuid (optional, any, None)
      uuid of the object


    level (optional, any, None)
      Field level


    aggregator (optional, any, None)
      Field aggregator


    atomic_aggregate (optional, any, None)
      BGP atomic aggregate attribute


    local_preference (optional, any, None)
      Field local_preference


    ipv6 (optional, any, None)
      Field ipv6


    comm_list (optional, any, None)
      Field comm_list



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  sequence (True, any, None)
    Sequence to insert to/delete from existing route-map entry


  ansible_password (True, any, None)
    Password for AXAPI authentication


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  tag (True, any, None)
    Route map tag


  action (True, any, None)
    'permit'= Route map permits set operations; 'deny'= Route map denies set operations;


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  match (False, any, None)
    Field match


    extcommunity (optional, any, None)
      Field extcommunity


    origin (optional, any, None)
      Field origin


    group (optional, any, None)
      Field group


    uuid (optional, any, None)
      uuid of the object


    route_type (optional, any, None)
      Field route_type


    ip (optional, any, None)
      Field ip


    metric (optional, any, None)
      Field metric


    as_path (optional, any, None)
      Field as_path


    community (optional, any, None)
      Field community


    tag (optional, any, None)
      Field tag


    local_preference (optional, any, None)
      Field local_preference


    ipv6 (optional, any, None)
      Field ipv6


    interface (optional, any, None)
      Field interface


    scaleout (optional, any, None)
      Field scaleout










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

