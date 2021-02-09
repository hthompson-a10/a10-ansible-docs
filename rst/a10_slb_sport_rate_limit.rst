.. _a10_slb_sport_rate_limit_module:


a10_slb_sport_rate_limit -- Configures A10 slb.sport-rate-limit
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure source port rate-limit






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'alloc_sport'= Alloc'd src port entry; 'alloc_sportip'= Alloc'd src port-ip entry; 'freed_sport'= Freed src port entry; 'freed_sportip'= Freed src port-ip entry; 'total_drop'= Total rate exceed drop; 'total_reset'= Total rate exceed reset; 'total_log'= Total log sent;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    total_reset (optional, any, None)
      Total rate exceed reset


    freed_sport (optional, any, None)
      Freed src port entry


    freed_sportip (optional, any, None)
      Freed src port-ip entry


    alloc_sportip (optional, any, None)
      Alloc'd src port-ip entry


    total_drop (optional, any, None)
      Total rate exceed drop


    alloc_sport (optional, any, None)
      Alloc'd src port entry


    total_log (optional, any, None)
      Total log sent



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

