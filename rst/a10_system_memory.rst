.. _a10_system_memory_module:


a10_system_memory -- Configures A10 system.memory
=================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure System Parameters






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'usage-percentage'= Memory Usage percentage;



  oper (False, any, None)
    Field oper


    TCP_memory (optional, any, None)
      Field TCP_memory


    SSL_memory (optional, any, None)
      Field SSL_memory


    Cached (optional, any, None)
      Field Cached


    System_memory (optional, any, None)
      Field System_memory


    tcp_memory_counts (optional, any, None)
      Field tcp_memory_counts


    Used (optional, any, None)
      Field Used


    aflex_memory_counts (optional, any, None)
      Field aflex_memory_counts


    Usage (optional, any, None)
      Field Usage


    Shared (optional, any, None)
      Field Shared


    ssl_memory_counts (optional, any, None)
      Field ssl_memory_counts


    aFleX_memory (optional, any, None)
      Field aFleX_memory


    N2_memory (optional, any, None)
      Field N2_memory


    Free (optional, any, None)
      Field Free


    n2_memory_counts (optional, any, None)
      Field n2_memory_counts


    system_memory_counts (optional, any, None)
      Field system_memory_counts


    Total (optional, any, None)
      Field Total


    Buffers (optional, any, None)
      Field Buffers



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    usage_percentage (optional, any, None)
      Memory Usage percentage



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

