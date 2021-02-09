.. _a10_slb_dns_response_rate_limiting_module:


a10_slb_dns_response_rate_limiting -- Configures A10 slb.dns-response-rate-limiting
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure DNS Response-Rate-Limiting






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'curr_entries'= Current Entry Count; 'total_created'= Total Entry Created; 'total_inserted'= Total Entry Inserted; 'total_withdrew'= Total Entry Withdrew; 'total_ready_to_free'= Total Entry Ready To Free; 'total_freed'= Total Entry Freed; 'total_logs'= Total Logs; 'total_overflow_entry_hits'= Total Overflow Entry Hits; 'total_refill'= Total Refills; 'total_credit_exceeded'= Total Credit Exceeded; 'other_thread_refill'= Other Thread Refilling; 'err_entry_create_failed'= Entry Creation Failure; 'err_entry_create_oom'= Entry Creation Out of Memory; 'err_entry_ext_create_oom'= Entry Extension Creation Out of Memory; 'err_entry_insert_failed'= Entry Insert Failed; 'err_vport_fail_match'= Failed to Match Vport;



  oper (False, any, None)
    Field oper


    dnsrrl_cpu_list (optional, any, None)
      Field dnsrrl_cpu_list


    cpu_count (optional, any, None)
      Field cpu_count



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    total_withdrew (optional, any, None)
      Total Entry Withdrew


    err_entry_ext_create_oom (optional, any, None)
      Entry Extension Creation Out of Memory


    err_vport_fail_match (optional, any, None)
      Failed to Match Vport


    total_refill (optional, any, None)
      Total Refills


    other_thread_refill (optional, any, None)
      Other Thread Refilling


    total_ready_to_free (optional, any, None)
      Total Entry Ready To Free


    curr_entries (optional, any, None)
      Current Entry Count


    total_logs (optional, any, None)
      Total Logs


    err_entry_create_oom (optional, any, None)
      Entry Creation Out of Memory


    total_freed (optional, any, None)
      Total Entry Freed


    total_inserted (optional, any, None)
      Total Entry Inserted


    total_created (optional, any, None)
      Total Entry Created


    total_overflow_entry_hits (optional, any, None)
      Total Overflow Entry Hits


    total_credit_exceeded (optional, any, None)
      Total Credit Exceeded


    err_entry_create_failed (optional, any, None)
      Entry Creation Failure


    err_entry_insert_failed (optional, any, None)
      Entry Insert Failed



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

