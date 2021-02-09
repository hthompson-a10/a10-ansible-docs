.. _a10_version_module:


a10_version -- Configures A10 version
=====================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Version Information






Parameters
----------

  oper (False, any, None)
    Field oper


    up_time (optional, any, None)
      Field up_time


    cots_sys_mfg (optional, any, None)
      Field cots_sys_mfg


    sw_version (optional, any, None)
      Field sw_version


    sys_poll_mode (optional, any, None)
      Field sys_poll_mode


    hw_platform (optional, any, None)
      Field hw_platform


    series_name (optional, any, None)
      Field series_name


    pri_gui_version (optional, any, None)
      Field pri_gui_version


    boot_from (optional, any, None)
      Field boot_from


    last_config_saved_time (optional, any, None)
      Field last_config_saved_time


    buff_size (optional, any, None)
      Field buff_size


    cots_sys_ver (optional, any, None)
      Field cots_sys_ver


    firmware_version (optional, any, None)
      Field firmware_version


    hd_sec (optional, any, None)
      Field hd_sec


    build_type (optional, any, None)
      Field build_type


    sec_gui_version (optional, any, None)
      Field sec_gui_version


    current_time (optional, any, None)
      Field current_time


    cots_sys_name (optional, any, None)
      Field cots_sys_name


    cf_sec (optional, any, None)
      Field cf_sec


    io_buff_enabled (optional, any, None)
      Field io_buff_enabled


    copyright (optional, any, None)
      Field copyright


    nun_ctrl_cpus (optional, any, None)
      Field nun_ctrl_cpus


    hostname (optional, any, None)
      Field hostname


    hd_pri (optional, any, None)
      Field hd_pri


    cf_pri (optional, any, None)
      Field cf_pri


    plat_features (optional, any, None)
      Field plat_features


    aflex_version (optional, any, None)
      Field aflex_version


    serial_number (optional, any, None)
      Field serial_number


    cylance_version (optional, any, None)
      Field cylance_version


    axapi_version (optional, any, None)
      Field axapi_version


    hw_code (optional, any, None)
      Field hw_code


    virtualization_type (optional, any, None)
      Field virtualization_type



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

