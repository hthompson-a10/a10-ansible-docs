.. _a10_system_icmp_rate_module:


a10_system_icmp_rate -- Configures A10 system.icmp-rate
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Icmp rate limit statistics






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'over_limit_drop'= Over limit drops; 'limit_intf_drop'= Interfaces rate limit drops; 'limit_vserver_drop'= Virtual Server rate limit drops; 'limit_total_drop'= Total rate limit drops; 'lockup_time_left'= Lockup time left; 'curr_rate'= Current rate; 'v6_over_limit_drop'= Over limit drops (v6); 'v6_limit_intf_drop'= Interfaces rate limit drops (v6); 'v6_limit_vserver_drop'= Virtual Server rate limit drops (v6); 'v6_limit_total_drop'= Total rate limit drops (v6); 'v6_lockup_time_left'= Lockup time left (v6); 'v6_curr_rate'= Current rate (v6);



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    lockup_time_left (optional, any, None)
      Lockup time left


    v6_limit_intf_drop (optional, any, None)
      Interfaces rate limit drops (v6)


    limit_vserver_drop (optional, any, None)
      Virtual Server rate limit drops


    v6_limit_vserver_drop (optional, any, None)
      Virtual Server rate limit drops (v6)


    over_limit_drop (optional, any, None)
      Over limit drops


    v6_over_limit_drop (optional, any, None)
      Over limit drops (v6)


    v6_lockup_time_left (optional, any, None)
      Lockup time left (v6)


    v6_curr_rate (optional, any, None)
      Current rate (v6)


    limit_total_drop (optional, any, None)
      Total rate limit drops


    v6_limit_total_drop (optional, any, None)
      Total rate limit drops (v6)


    curr_rate (optional, any, None)
      Current rate


    limit_intf_drop (optional, any, None)
      Interfaces rate limit drops



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

