.. _a10_slb_hw_compress_module:


a10_slb_hw_compress -- Configures A10 slb.hw-compress
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure HW compression






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'request_count'= Total request count; 'submit_count'= Total submit count; 'response_count'= Total response count; 'failure_count'= Total failure count; 'failure_code'= Last failure code; 'ring_full_count'= Compression queue full; 'max_outstanding_request_count'= Max queued request count; 'max_outstanding_submit_count'= Max queued submit count;



  oper (False, any, None)
    Field oper


    l4_cpu_list (optional, any, None)
      Field l4_cpu_list


    cpu_count (optional, any, None)
      Field cpu_count


    hw_compress_disabled (optional, any, None)
      Field hw_compress_disabled



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    max_outstanding_request_count (optional, any, None)
      Max queued request count


    failure_count (optional, any, None)
      Total failure count


    response_count (optional, any, None)
      Total response count


    ring_full_count (optional, any, None)
      Compression queue full


    submit_count (optional, any, None)
      Total submit count


    request_count (optional, any, None)
      Total request count


    max_outstanding_submit_count (optional, any, None)
      Max queued submit count


    failure_code (optional, any, None)
      Last failure code



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

