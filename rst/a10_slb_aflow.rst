.. _a10_slb_aflow_module:


a10_slb_aflow -- Configures A10 slb.aflow
=========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure aFlow






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'pause_conn'= Pause connection; 'pause_conn_fail'= Pause connection fail; 'resume_conn'= Resume connection; 'event_resume_conn'= Resume conn by event; 'timer_resume_conn'= Resume conn by timer; 'try_to_resume_conn'= Resume conn by trying; 'retry_resume_conn'= Resume conn by retry; 'error_resume_conn'= Resume conn by error; 'open_new_server_conn'= Open new server conn; 'reuse_server_idle_conn'= Reuse idle server conn; 'inc_aflow_limit'= Inc aFlow limit;



  oper (False, any, None)
    Field oper


    aflow_cpu_list (optional, any, None)
      Field aflow_cpu_list


    cpu_count (optional, any, None)
      Field cpu_count



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    open_new_server_conn (optional, any, None)
      Open new server conn


    reuse_server_idle_conn (optional, any, None)
      Reuse idle server conn


    inc_aflow_limit (optional, any, None)
      Inc aFlow limit


    pause_conn (optional, any, None)
      Pause connection


    pause_conn_fail (optional, any, None)
      Pause connection fail


    event_resume_conn (optional, any, None)
      Resume conn by event


    try_to_resume_conn (optional, any, None)
      Resume conn by trying


    resume_conn (optional, any, None)
      Resume connection


    retry_resume_conn (optional, any, None)
      Resume conn by retry


    error_resume_conn (optional, any, None)
      Resume conn by error


    timer_resume_conn (optional, any, None)
      Resume conn by timer



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

