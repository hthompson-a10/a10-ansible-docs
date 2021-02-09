.. _a10_visibility_reporting_module:


a10_visibility_reporting -- Configures A10 visibility.reporting
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure reporting framework






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'log-transmit-failure'= Total log transmit failures; 'buffer-alloc- failure'= Total reporting buffer allocation failures; 'notif-jobs-in-queue'= Total notification jobs in queue; 'enqueue-fail'= Total enqueue jobs failed; 'enqueue-pass'= Total enqueue jobs passed; 'dequeued'= Total jobs dequeued;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    enqueue_pass (optional, any, None)
      Total enqueue jobs passed


    buffer_alloc_failure (optional, any, None)
      Total reporting buffer allocation failures


    dequeued (optional, any, None)
      Total jobs dequeued


    template (optional, any, None)
      Field template


    notif_jobs_in_queue (optional, any, None)
      Total notification jobs in queue


    log_transmit_failure (optional, any, None)
      Total log transmit failures


    enqueue_fail (optional, any, None)
      Total enqueue jobs failed



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  template (False, any, None)
    Field template


    notification (optional, any, None)
      Field notification



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  telemetry_export_interval (False, any, None)
    Field telemetry_export_interval


    uuid (optional, any, None)
      uuid of the object


    value (optional, any, None)
      Monitored entity telemetry data export interval in mins (Default 5 mins)










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

