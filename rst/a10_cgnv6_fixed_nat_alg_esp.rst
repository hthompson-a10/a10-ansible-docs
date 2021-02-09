.. _a10_cgnv6_fixed_nat_alg_esp_module:


a10_cgnv6_fixed_nat_alg_esp -- Configures A10 cgnv6.fixed.nat.alg.esp
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Change Fixed NAT ESP ALG Settings






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'session-created'= ESP Sessions Created; 'placeholder-debug'= Placeholder Debug;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    session_created (optional, any, None)
      ESP Sessions Created



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

