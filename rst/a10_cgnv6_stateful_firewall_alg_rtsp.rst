.. _a10_cgnv6_stateful_firewall_alg_rtsp_module:


a10_cgnv6_stateful_firewall_alg_rtsp -- Configures A10 cgnv6.stateful.firewall.alg.rtsp
=======================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure RTSP ALG for NAT stateful firewall (default= enabled)






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'transport-inserted'= Transport Created; 'transport-freed'= Transport Freed; 'transport-alloc-failure'= Transport Alloc Failure; 'data- session-created'= Data Session Created; 'data-session-freed'= Data Session Freed; 'ext-creation-failure'= Extension Creation Failure; 'transport-add-to- ext'= Transport Added to Extension; 'transport-removed-from-ext'= Transport Removed from Extension; 'transport-too-many'= Too Many Transports for Control Conn; 'transport-already-in-ext'= Transport Already in Extension; 'transport- exists'= Transport Already Exists; 'transport-link-ext-failure-control'= Transport Link to Extension Failure Control; 'transport-link-ext-data'= Transport Link to Extension Data; 'transport-link-ext-failure-data'= Transport Link to Extension Failure Data; 'transport-inserted-shadow'= Transport Inserted Shadow; 'transport-creation-race'= Transport Create Race; 'transport-alloc- failure-shadow'= Transport Alloc Failure Shadow; 'transport-put-in-del-q'= Transport Put in Delete Queue; 'transport-freed-shadow'= Transport Freed Shadow; 'transport-acquired-from-control'= Transport Acquired Control; 'transport-found-from-prev-control'= Transport Found From Prev Control; 'transport-acquire-failure-from-control'= Transport Acquire Failure Control; 'transport-released-from-control'= Transport Released Control; 'transport- double-release-from-control'= Transport Double Release Control; 'transport- acquired-from-data'= Transport Acquired Data; 'transport-acquire-failure-from- data'= Transport Acquire Failure Data; 'transport-released-from-data'= Transport Released Data; 'transport-double-release-from-data'= Transport Double Release Data; 'transport-retry-lookup-on-data-free'= Transport Retry Lookup Data; 'transport-not-found-on-data-free'= Transport Not Found Data; 'data- session-created-shadow'= Data Session Created Shadow; 'data-session-freed- shadow'= Data Session Freed Shadow; 'ha-control-ext-creation-failure'= HA Control Extension Creation Failure; 'ha-control-session-created'= HA Control Session Created; 'ha-data-session-created'= HA Data Session Created;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    transport_inserted (optional, any, None)
      Transport Created


    transport_alloc_failure (optional, any, None)
      Transport Alloc Failure


    data_session_freed (optional, any, None)
      Data Session Freed


    data_session_created (optional, any, None)
      Data Session Created


    transport_freed (optional, any, None)
      Transport Freed



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  rtsp_value (False, any, None)
    'disable'= Disable ALG;


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

