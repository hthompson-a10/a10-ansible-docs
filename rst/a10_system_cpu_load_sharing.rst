.. _a10_system_cpu_load_sharing_module:


a10_system_cpu_load_sharing -- Configures A10 system.cpu-load-sharing
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Redistribute packets uniformly to all CPUs during overload situations






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  cpu_usage (False, any, None)
    Field cpu_usage


    high (optional, any, None)
      CPU usage threshold (percentage) that will trigger the redistribution (default= 75)


    low (optional, any, None)
      CPU usage threshold (percentage) that will restore the normal packet distribution (default= 60)



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  packets_per_second (False, any, None)
    Field packets_per_second


    min (optional, any, None)
      Minimum packets-per-second threshold (per CPU) before redistribution will take effect (Minimum packets-per-second threshold (per CPU) before redistribution will take effect (default= 100000))



  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  disable (False, any, None)
    Disable CPU load sharing in overload situations


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

