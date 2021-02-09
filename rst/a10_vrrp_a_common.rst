.. _a10_vrrp_a_common_module:


a10_vrrp_a_common -- Configures A10 vrrp.a.common
=================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

HA VRRP-A Global Commands






Parameters
----------

  track_event_delay (False, any, None)
    Delay before changing state after up/down event (Units of 100 milliseconds (default 30))


  dead_timer (False, any, None)
    VRRP-A dead timer in terms of how many hello messages missed, default is 5 (2-255, default is 5)


  inline_mode_cfg (False, any, None)
    Field inline_mode_cfg


    preferred_trunk (optional, any, None)
      Preferred trunk Port


    inline_mode (optional, any, None)
      Enable Layer 2 Inline Hot Standby Mode


    preferred_port (optional, any, None)
      Preferred ethernet Port



  disable_default_vrid (False, any, None)
    Disable default vrid


  ansible_username (True, any, None)
    Username for AXAPI authentication


  forward_l4_packet_on_standby (False, any, None)
    Enables Layer 2/3 forwarding of Layer 4 traffic on the Standby ACOS device


  restart_time (False, any, None)
    Time between restarting ports on standby system after transition


  hello_interval (False, any, None)
    VRRP-A Hello Interval (1-255, in unit of 100millisec, default is 2)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  device_id (False, any, None)
    Unique ID for each VRRP-A box (Device-id number)


  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    vrrp_common_dummy (optional, any, None)
      dummy counter



  uuid (False, any, None)
    uuid of the object


  arp_retry (False, any, None)
    Number of additional gratuitous ARPs sent out after HA failover (1-255, default is 4)


  get_ready_time (False, any, None)
    set get ready time after ax starting up (60-1200, in unit of 100millisec, default is 60)


  state (True, any, None)
    State of the object to be created.


  action (False, any, None)
    'enable'= enable vrrp-a; 'disable'= disable vrrp-a;


  preemption_delay (False, any, None)
    Delay before changing state from Active to Standby (1-255, in unit of 100millisec, default is 60)


  ansible_password (True, any, None)
    Password for AXAPI authentication


  hostid_append_to_vrid (False, any, None)
    Field hostid_append_to_vrid


    hostid_append_to_vrid_value (optional, any, None)
      hostid append to vrid num


    hostid_append_to_vrid_default (optional, any, None)
      hostid append to vrid default



  set_id (False, any, None)
    Set-ID for HA configuration (Set id from 1 to 15)









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

