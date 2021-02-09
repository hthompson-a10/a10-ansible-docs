.. _a10_cgnv6_global_module:


a10_cgnv6_global -- Configures A10 cgnv6.global
===============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

CGN global paramters






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'tcp-total-ports-allocated'= Total TCP ports allocated; 'udp-total- ports-allocated'= Total UDP ports allocated; 'icmp-total-ports-allocated'= Total ICMP ports allocated;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    udp_total_ports_allocated (optional, any, None)
      Total UDP ports allocated


    icmp_total_ports_allocated (optional, any, None)
      Total ICMP ports allocated


    tcp_total_ports_allocated (optional, any, None)
      Total TCP ports allocated



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

