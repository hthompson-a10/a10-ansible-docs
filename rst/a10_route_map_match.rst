.. _a10_route_map_match_module:


a10_route_map_match -- Configures A10 route.map.match
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Match values from routing table






Parameters
----------

  extcommunity (False, any, None)
    Field extcommunity


    extcommunity_l_name (optional, any, None)
      Field extcommunity_l_name



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


  ansible_username (True, any, None)
    Username for AXAPI authentication


  route_type (False, any, None)
    Field route_type


    external (optional, any, None)
      Field external



  ip (False, any, None)
    Field ip


    peer (optional, any, None)
      Field peer


    next_hop (optional, any, None)
      Field next_hop


    address (optional, any, None)
      Field address



  metric (False, any, None)
    Field metric


    value (optional, any, None)
      Metric value



  as_path (False, any, None)
    Field as_path


    name (optional, any, None)
      AS path access-list name



  community (False, any, None)
    Field community


    name_cfg (optional, any, None)
      Field name_cfg



  interface (False, any, None)
    Field interface


    tunnel (optional, any, None)
      Tunnel interface (Tunnel interface number)


    ethernet (optional, any, None)
      Ethernet interface (Port number)


    loopback (optional, any, None)
      Loopback interface (Port number)


    ve (optional, any, None)
      Virtual ethernet interface (Virtual ethernet interface number)


    trunk (optional, any, None)
      Trunk Interface (Trunk interface number)



  tag (False, any, None)
    Field tag


    value (optional, any, None)
      Tag value



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  scaleout (False, any, None)
    Field scaleout


    cluster_id (optional, any, None)
      Scaleout Cluster-id


    operational_state (optional, any, None)
      'up'= Scaleout is up and running; 'down'= Scaleout is down or disabled;



  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ansible_port (True, any, None)
    Port for AXAPI authentication


  group (False, any, None)
    Field group


    group_id (optional, any, None)
      HA or VRRP-A group id


    ha_state (optional, any, None)
      'active'= HA or VRRP-A in Active State; 'standby'= HA or VRRP-A in Standby State;



  uuid (False, any, None)
    uuid of the object


  sequence (optional, any, None)
    Key to identify parent object


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


    address_1 (optional, any, None)
      Field address_1


    peer_1 (optional, any, None)
      Field peer_1



  action (optional, any, None)
    Key to identify parent object


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

