.. _a10_slb_player_id_global_module:


a10_slb_player_id_global -- Configures A10 slb.player-id-global
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Player-id global commands






Parameters
----------

  oper (False, any, None)
    Field oper


    time_to_active (optional, any, None)
      Field time_to_active


    state (optional, any, None)
      Field state


    table_count (optional, any, None)
      Field table_count



  force_passive (False, any, None)
    Forces the device to be in passive mode (Only stats and no packet drops)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  pkt_activity_expiration (False, any, None)
    Packet activity record expiration value (default 5 minutes) (Packet activity record expiration time in minutes, default 5)


  abs_max_expiration (False, any, None)
    Absolute max record expiration value (default 10 minutes) (Absolute max record expiration time in minutes, default 10)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  enforcement_timer (False, any, None)
    Time to playerid enforcement after bootup (default 480 seconds) (Time to playerid enforcement in seconds, default 480)


  min_expiration (False, any, None)
    Minimum record expiration value (default 1 min) (Min record expiration time in minutes, default 1)


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'total_playerids_created'= Playerid records created; 'total_playerids_deleted'= Playerid records deleted; 'total_abs_max_age_outs'= Playerid records max time aged out; 'total_pkt_activity_age_outs'= Playerid records idle timeout; 'total_invalid_playerid_pkts'= Invalid playerid packets; 'total_invalid_playerid_drops'= Invalid playerid packet drops; 'total_valid_playerid_pkts'= Valid playerid packets;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    total_playerids_deleted (optional, any, None)
      Playerid records deleted


    total_playerids_created (optional, any, None)
      Playerid records created


    total_pkt_activity_age_outs (optional, any, None)
      Playerid records idle timeout


    total_invalid_playerid_drops (optional, any, None)
      Invalid playerid packet drops


    total_abs_max_age_outs (optional, any, None)
      Playerid records max time aged out


    total_valid_playerid_pkts (optional, any, None)
      Valid playerid packets


    total_invalid_playerid_pkts (optional, any, None)
      Invalid playerid packets



  uuid (False, any, None)
    uuid of the object


  enable_64bit_player_id (False, any, None)
    Enable 64 bit player id check. Default is 32 bit


  state (True, any, None)
    State of the object to be created.


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

