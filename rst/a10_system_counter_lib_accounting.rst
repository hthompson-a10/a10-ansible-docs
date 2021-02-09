.. _a10_system_counter_lib_accounting_module:


a10_system_counter_lib_accounting -- Configures A10 system.counter-lib-accounting
=================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

System Counter library accounting






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    total_nodes_free_failed (optional, any, None)
      Total nodes free failed


    total_nodes_free (optional, any, None)
      Total nodes freed(sflow/history/telemetry/cpu-compute)


    total_ctr_in_system (optional, any, None)
      Total counters currently allocated in system


    total_ctr_in_rml (optional, any, None)
      Total counters put in rml queue


    total_blocks_in_rml_hash (optional, any, None)
      Total blocks in rml in hash table


    total_nodes_in_rml (optional, any, None)
      Total nodes put in rml queue


    total_ctr_alloc (optional, any, None)
      Total counters allocated


    total_nodes_in_system (optional, any, None)
      Total nodes currently allocated in system


    total_ctr_freed (optional, any, None)
      Total counters actually freed


    total_oper_free (optional, any, None)
      Total oper blocks freed


    total_oper_alloc (optional, any, None)
      Total oper blocks allocated


    total_nodes_unlink_failed (optional, any, None)
      Total nodes unlink failed


    total_memblocks_realloc_avro (optional, any, None)
      Total memory blocks realloc by avro lib


    total_nodes_alloc (optional, any, None)
      Total nodes allocated(sflow/history/telemetry/cpu-compute)


    total_blocks_in_hash (optional, any, None)
      Total blocks in hash table


    total_memblocks_alloc_avro (optional, any, None)
      Total memory blocks allocated by avro lib


    total_memblocks_free_avro (optional, any, None)
      Total memory blocks freed by avro lib



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

