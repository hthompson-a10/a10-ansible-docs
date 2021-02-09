.. _a10_slb_crl_srcip_module:


a10_slb_crl_srcip -- Configures A10 slb.crl-srcip
=================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure connection rate limit






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'sessions_alloc'= Sessions allocated; 'sessions_freed'= Sessions freed; 'out_of_sessions'= Out of sessions; 'too_many_sessions'= Too many sessions consumed; 'called'= Threshold check count; 'permitted'= Honor threshold  count; 'threshold_exceed'= Threshold exceeded count; 'lockout_drop'= Lockout drops; 'log_msg_sent'= Log messages sent;



  oper (False, any, None)
    Field oper


    crl_srcip_lockedout_ips (optional, any, None)
      Field crl_srcip_lockedout_ips


    lockedout_ips_count (optional, any, None)
      Field lockedout_ips_count



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    threshold_exceed (optional, any, None)
      Threshold exceeded count


    lockout_drop (optional, any, None)
      Lockout drops


    called (optional, any, None)
      Threshold check count


    sessions_freed (optional, any, None)
      Sessions freed


    permitted (optional, any, None)
      Honor threshold  count


    log_msg_sent (optional, any, None)
      Log messages sent


    sessions_alloc (optional, any, None)
      Sessions allocated


    out_of_sessions (optional, any, None)
      Out of sessions


    too_many_sessions (optional, any, None)
      Too many sessions consumed



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication









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

