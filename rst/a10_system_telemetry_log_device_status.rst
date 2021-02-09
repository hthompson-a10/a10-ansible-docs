.. _a10_system_telemetry_log_device_status_module:


a10_system_telemetry_log_device_status -- Configures A10 system.telemetry.log.device-status
===========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Device status






Parameters
----------

  oper (False, any, None)
    Field oper


    control_cpu_usage (optional, any, None)
      Field control_cpu_usage


    total_bytes_in (optional, any, None)
      Field total_bytes_in


    total_bytes_out (optional, any, None)
      Field total_bytes_out


    memory_usage (optional, any, None)
      Field memory_usage


    ratio_session_count (optional, any, None)
      Field ratio_session_count


    ratio_buffer_count (optional, any, None)
      Field ratio_buffer_count


    cpu_usage_overall (optional, any, None)
      Field cpu_usage_overall



  ansible_port (True, any, None)
    Port for AXAPI authentication


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

