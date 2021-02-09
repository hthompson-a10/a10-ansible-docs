.. _a10_ip_nat_nat_global_module:


a10_ip_nat_nat_global -- Configures A10 ip.nat.nat-global
=========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Debug statistics for IP NAT






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'cross_cpu_helper_created'= Cross CPU Helper Created; 'cross_cpu_helper_free'= Cross CPU Helper Free; 'cross_cpu_sent'= Cross CPU Helper Packets Sent; 'cross_cpu_rcv'= Cross CPU Helper Packets Received; 'cross_cpu_helper_nat_pool_standby'= Cross CPU Helper Standby; 'cross_cpu_helper_cpu_mismatch'= Cross CPU Helper CPU Mismatch; 'cross_cpu_bad_l3'= Cross CPU Unsupported L3; 'cross_cpu_bad_l4'= Cross CPU Unsupported L4; 'cross_cpu_no_session'= Cross CPU No Session Found; 'cross_cpu_helper_deleted'= Cross CPU Helper Deleted; 'cross_cpu_helper_free_retry_lookup'= Cross CPU Helper Free Retry Lookup; 'cross_cpu_helper_free_not_found'= Cross CPU Helper Free Not Found;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


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

