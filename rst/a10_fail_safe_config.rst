.. _a10_fail_safe_config_module:


a10_fail_safe_config -- Configures A10 fail.safe.config
=======================================================

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


    sw_recovery_timeout (optional, any, None)
      Field sw_recovery_timeout


    sw_error_mon (optional, any, None)
      Field sw_error_mon


    fpga_mon_threshold (optional, any, None)
      Field fpga_mon_threshold


    hw_recovery_timeout (optional, any, None)
      Field hw_recovery_timeout


    fpga_mon_interval (optional, any, None)
      Field fpga_mon_interval


    fpga_mon_forced_reboot (optional, any, None)
      Field fpga_mon_forced_reboot


    fpga_mon_enable (optional, any, None)
      Field fpga_mon_enable


    mem_mon (optional, any, None)
      Field mem_mon


    hw_error_mon (optional, any, None)
      Field hw_error_mon



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

