.. _a10_system_app_performance_module:


a10_system_app_performance -- Configures A10 system.app-performance
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Application perfomance stats






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'total-throughput-bits-per-sec'= Total Throughput in bits/sec; 'l4-conns-per-sec'= L4 Connections/sec; 'l7-conns-per-sec'= L7 Connections/sec; 'l7-trans-per-sec'= L7 Transactions/sec; 'ssl-conns-per-sec'= SSL Connections/sec; 'ip-nat-conns-per-sec'= IP NAT Connections/sec; 'total-new- conns-per-sec'= Total New Connections Established/sec; 'total-curr-conns'= Total Current Established Connections; 'l4-bandwidth'= L4 Bandwidth in bits/sec; 'l7-bandwidth'= L7 Bandwidth in bits/sec; 'serv-ssl-conns-per-sec'= Server SSL Connections/sec; 'fw-conns-per-sec'= FW Connections/sec; 'gifw- conns-per-sec'= GiFW Connections/sec;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    total_new_conns_per_sec (optional, any, None)
      Total New Connections Established/sec


    gifw_conns_per_sec (optional, any, None)
      GiFW Connections/sec


    l7_trans_per_sec (optional, any, None)
      L7 Transactions/sec


    l4_conns_per_sec (optional, any, None)
      L4 Connections/sec


    fw_conns_per_sec (optional, any, None)
      FW Connections/sec


    total_curr_conns (optional, any, None)
      Total Current Established Connections


    ssl_conns_per_sec (optional, any, None)
      SSL Connections/sec


    ip_nat_conns_per_sec (optional, any, None)
      IP NAT Connections/sec


    total_throughput_bits_per_sec (optional, any, None)
      Total Throughput in bits/sec


    l4_bandwidth (optional, any, None)
      L4 Bandwidth in bits/sec


    serv_ssl_conns_per_sec (optional, any, None)
      Server SSL Connections/sec


    l7_conns_per_sec (optional, any, None)
      L7 Connections/sec


    l7_bandwidth (optional, any, None)
      L7 Bandwidth in bits/sec



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

