.. _a10_system_bandwidth_module:


a10_system_bandwidth -- Configures A10 system.bandwidth
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

System bandwidth information






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'input-bytes-per-sec'= In Bytes per second; 'output-bytes-per-sec'= Out Bytes per second;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    input_bytes_per_sec (optional, any, None)
      In Bytes per second


    output_bytes_per_sec (optional, any, None)
      Out Bytes per second



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

