.. _a10_system_throughput_module:


a10_system_throughput -- Configures A10 system.throughput
=========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

System throughput






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'global-system-throughput-bits-per-sec'= Global System throughput in bits/sec; 'per-part-throughput-bits-per-sec'= Partition throughput in bits/sec;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    global_system_throughput_bits_per_sec (optional, any, None)
      Global System throughput in bits/sec


    per_part_throughput_bits_per_sec (optional, any, None)
      Partition throughput in bits/sec



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

