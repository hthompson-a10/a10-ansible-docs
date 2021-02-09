.. _a10_fail_safe_module:


a10_fail_safe -- Configures A10 fail-safe
=========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Fail Safe Global Commands






Parameters
----------

  oper (False, any, None)
    Field oper


    total_system_memory (optional, any, None)
      Field total_system_memory


    fpga_buff_recovery_threshold (optional, any, None)
      Field fpga_buff_recovery_threshold


    total_free_fpga_buff (optional, any, None)
      Field total_free_fpga_buff


    fpga_stats_iochan (optional, any, None)
      Field fpga_stats_iochan


    total_fpga_buffers (optional, any, None)
      Field total_fpga_buffers


    free_fpga_buffers (optional, any, None)
      Field free_fpga_buffers


    fpga_stats_num_cntrs (optional, any, None)
      Field fpga_stats_num_cntrs


    free_session_memory (optional, any, None)
      Field free_session_memory


    avail_fpga_buff_domain1 (optional, any, None)
      Field avail_fpga_buff_domain1


    avail_fpga_buff_domain2 (optional, any, None)
      Field avail_fpga_buff_domain2


    total_session_memory (optional, any, None)
      Field total_session_memory


    config (optional, any, None)
      Field config


    sess_mem_recovery_threshold (optional, any, None)
      Field sess_mem_recovery_threshold



  hw_error_recovery_timeout (False, any, None)
    Hardware error recovery timeout (minutes) (waiting time of recovery from hardware errors (default 0))


  ansible_username (True, any, None)
    Username for AXAPI authentication


  fpga_buff_recovery_threshold (False, any, None)
    FPGA buffers recovery threshold (Units of 256 buffers (default 2))


  fpga_monitor_interval (False, any, None)
    FPGA monitor packet interval (seconds) (Numbers of seconds between sending packets (default 1))


  sw_error_monitor_enable (False, any, None)
    Enable fail-safe software error monitor


  ansible_password (True, any, None)
    Password for AXAPI authentication


  fpga_monitor_threshold (False, any, None)
    FPGA monitor packet missed for error condition (Numbers of missed monitor packets before setting error condition (default 3))


  kill (False, any, None)
    Stop the traffic and log the event


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  hw_error_monitor (False, any, None)
    'hw-error-monitor-disable'= Disable fail-safe hardware error monitor; 'hw- error-monitor-enable'= Enable fail-safe hardware error monitor;


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  sw_error_recovery_timeout (False, any, None)
    Software error recovery timeout (minutes) (waiting time of recovery from software errors (default 3))


  ansible_port (True, any, None)
    Port for AXAPI authentication


  fpga_monitor_forced_reboot (False, any, None)
    FPGA monitor forced reboot in error condition


  log (False, any, None)
    Log the event


  disable_failsafe (False, any, None)
    Field disable_failsafe


    action (optional, any, None)
      'all'= Disable All; 'io-buffer'= Disable I/O Buffer; 'session-memory'= Disable Session Memory; 'system-memory'= Disable System Memory;


    uuid (optional, any, None)
      uuid of the object



  fpga_monitor_enable (False, any, None)
    FPGA monitor feature enable


  total_memory_size_check (False, any, None)
    Check total memory size of current system (Size of memory (GB))


  state (True, any, None)
    State of the object to be created.


  hw_ssl_timeout_monitor (False, any, None)
    'hw-ssl-timeout-monitor-disable'= Disable fail-safe hardware SSL timeout monitor; 'hw-ssl-timeout-monitor-enable'= Enable fail-safe hardware SSL timeout monitor;


  config (False, any, None)
    Field config


    uuid (optional, any, None)
      uuid of the object



  session_mem_recovery_threshold (False, any, None)
    Session memory recovery threshold (percentage) (Percentage of available session memory (default 30%))









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

