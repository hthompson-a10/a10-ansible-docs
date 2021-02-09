.. _a10_cgnv6_lsn_alg_rtsp_module:


a10_cgnv6_lsn_alg_rtsp -- Configures A10 cgnv6.lsn.alg.rtsp
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Change LSN RTSP ALG Settings






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'streams-created'= Streams Created; 'streams-freed'= Streams Freed; 'stream-creation-failure'= Stream Creation Failures; 'ports-allocated'= Stream Client Ports Allocated; 'ports-freed'= Stream Client Ports Freed; 'port- allocation-failure'= Stream Client Port Allocation Failures; 'unknown-client- port-from-server'= Server Replies With Unknown Client Ports; 'data-session- created'= Data Session Created; 'data-session-freed'= Data Session Freed; 'no- session-mem'= Data Session Creation Failures; 'ha-sent'= HA Sent; 'ha-rcv'= HA RCV; 'smp-inserted'= SMP Session Inserted; 'smp-removed'= SMP Session Removed; 'smp-reused'= SMP Session Reused; 'nat-pool-standby'= New Session NAT Pool Standby; 'smp-deleted'= New Session SMP Already Deleted; 'control-closed'= New Session Closed; 'data-session-exists'= New Session Already Exists; 'data- session-creation-failure'= New Data Session Creation Failure; 'rtp-reversed'= RTP Reverse Creation; 'rtcp-reversed'= RTCP Reverse Creation; 'cross-cpu-sent'= Cross CPU Sent; 'cross-cpu-rcv'= Cross CPU Received; 'cross-cpu-no-session'= Cross CPU No Session Found; 'cross-cpu-created'= Cross CPU Creation; 'cross- cpu-rcv-failure'= Cross CPU Receive Failure; 'data-free-smp-retry-lookup'= Data Session Free SMP Retry Lookup; 'data-free-smp-not-found'= Data Session Free SMP Not Found; 'ha-streams-sent'= HA Streams Sent; 'ha-streams-rcv'= HA Streams Received; 'ha-stream-incompatible'= HA Incompatible Streams Received; 'ha- stream-exists'= HA Stream Already Exists; 'ha-port-allocation-failure'= HA Stream Port Allocation Failure; 'ha-data-session-sent'= HA Data Session Sent; 'ha-data-session-rcv'= HA Data Session Received; 'ha-data-no-smp'= HA Data Session SMP Not Found; 'ha-control-closed'= HA New Data Control Session Closed; 'ha-data-exists'= HA New Data Session Already Exists; 'ha-extension-failure'= HA Conn Extension Failure; 'ha-stream-smp-reused'= HA SMP Session Reused; 'ha- stream-smp-acquire-failure'= HA SMP Session Acquire Failure; 'smp-app-type- mismatch'= SMP ALG App Type Mismatch;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    data_session_freed (optional, any, None)
      Data Session Freed


    ports_freed (optional, any, None)
      Stream Client Ports Freed


    unknown_client_port_from_server (optional, any, None)
      Server Replies With Unknown Client Ports


    streams_freed (optional, any, None)
      Streams Freed


    no_session_mem (optional, any, None)
      Data Session Creation Failures


    port_allocation_failure (optional, any, None)
      Stream Client Port Allocation Failures


    data_session_created (optional, any, None)
      Data Session Created


    streams_created (optional, any, None)
      Streams Created


    stream_creation_failure (optional, any, None)
      Stream Creation Failures


    ports_allocated (optional, any, None)
      Stream Client Ports Allocated



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  rtsp_value (False, any, None)
    'enable'= Enable RTSP ALG for LSN;


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

