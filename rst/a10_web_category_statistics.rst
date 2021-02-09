.. _a10_web_category_statistics_module:


a10_web_category_statistics -- Configures A10 web.category.statistics
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Statistics






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'db-lookup'= db-lookup; 'cloud-cache-lookup'= cloud-cache-lookup; 'cloud-lookup'= cloud-lookup; 'rtu-lookup'= rtu-lookup; 'lookup-latency'= lookup-latency; 'db-mem'= db-mem; 'rtu-cache-mem'= rtu-cache-mem; 'lookup- cache-mem'= lookup-cache-mem;



  oper (False, any, None)
    Field oper


    total_req_dropped (optional, any, None)
      Field total_req_dropped


    total_req_processed (optional, any, None)
      Field total_req_processed


    per_cpu_list (optional, any, None)
      Field per_cpu_list


    total_req_lookup_processed (optional, any, None)
      Field total_req_lookup_processed


    total_req_queue (optional, any, None)
      Field total_req_queue


    num_dplane_threads (optional, any, None)
      Field num_dplane_threads


    num_lookup_threads (optional, any, None)
      Field num_lookup_threads



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    lookup_latency (optional, any, None)
      Field lookup_latency


    cloud_lookup (optional, any, None)
      Field cloud_lookup


    db_lookup (optional, any, None)
      Field db_lookup


    lookup_cache_mem (optional, any, None)
      Field lookup_cache_mem


    db_mem (optional, any, None)
      Field db_mem


    rtu_lookup (optional, any, None)
      Field rtu_lookup


    cloud_cache_lookup (optional, any, None)
      Field cloud_cache_lookup


    rtu_cache_mem (optional, any, None)
      Field rtu_cache_mem



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

