.. _a10_system_fpga_core_crc_module:


a10_system_fpga_core_crc -- Configures A10 system.fpga-core-crc
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

FPGA Core CRC check Global Commands






Parameters
----------

  monitor_disable (False, any, None)
    Disable FPGA Core CRC error monitoring and act on it


  oper (False, any, None)
    Field oper


    reboot_val (optional, any, None)
      Field reboot_val


    crc_error_present (optional, any, None)
      Field crc_error_present


    enable_val (optional, any, None)
      Field enable_val



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


  reboot_enable (False, any, None)
    Enable system reboot if system encounters FPGA Core CRC error









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

