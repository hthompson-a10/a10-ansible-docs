.. _a10_cgnv6_one_to_one_global_module:


a10_cgnv6_one_to_one_global -- Configures A10 cgnv6.one.to.one.global
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Set one-to-one NAT config parameters






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'total-map-allocated'= Total One-to-One Address Mapping Allocated; 'total-map-freed'= Total One-to-One Address Mapping Freed; 'map-alloc-failure'= One-to-One Address Mapping Allocation Failure; 'map-dbl-free'= Address Mapping Double Free; 'alloc-map-race'= Mapping Exists When Allocating Address Mapping; 'map-not-found'= Mapping to be Released Not Found; 'ha-map-mismatch'= HA Standby Mapping Mismatch; 'ha-select-addr-failure'= HA Standby Allocate Address Failure; 'ha-alloc-map-conflicts'= HA Standby Allocate Mapping Conflicts;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    total_map_allocated (optional, any, None)
      Total One-to-One Address Mapping Allocated


    map_alloc_failure (optional, any, None)
      One-to-One Address Mapping Allocation Failure


    total_map_freed (optional, any, None)
      Total One-to-One Address Mapping Freed



  mapping_timeout (False, any, None)
    Configure timeout for the one-to-one NAT mapping (Timeout in minutes (default= 10 minutes))


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


  uuid (False, any, None)
    uuid of the object









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

