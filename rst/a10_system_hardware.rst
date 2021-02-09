.. _a10_system_hardware_module:


a10_system_hardware -- Configures A10 system.hardware
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Field hardware






Parameters
----------

  oper (False, any, None)
    Field oper


    nvm_firmware_version (optional, any, None)
      Field nvm_firmware_version


    ssl_cards (optional, any, None)
      Field ssl_cards


    storage (optional, any, None)
      Field storage


    compression_cards (optional, any, None)
      Field compression_cards


    psu2_np15 (optional, any, None)
      Field psu2_np15


    disk_percentage (optional, any, None)
      Field disk_percentage


    serial (optional, any, None)
      Field serial


    bypass_pr (optional, any, None)
      Field bypass_pr


    cpu_cores (optional, any, None)
      Field cpu_cores


    psu1_np15 (optional, any, None)
      Field psu1_np15


    memory (optional, any, None)
      Field memory


    bios_version (optional, any, None)
      Field bios_version


    spe_present (optional, any, None)
      Field spe_present


    ipmi (optional, any, None)
      Field ipmi


    disk1_status (optional, any, None)
      Field disk1_status


    raid_present (optional, any, None)
      Field raid_present


    disk_total (optional, any, None)
      Field disk_total


    disk2_status (optional, any, None)
      Field disk2_status


    disk_free (optional, any, None)
      Field disk_free


    num_disks (optional, any, None)
      Field num_disks


    bypass_list (optional, any, None)
      Field bypass_list


    l23_asic (optional, any, None)
      Field l23_asic


    platform_description (optional, any, None)
      Field platform_description


    cpu_stepping (optional, any, None)
      Field cpu_stepping


    fpga_date (optional, any, None)
      Field fpga_date


    raid_list (optional, any, None)
      Field raid_list


    fpga_summary (optional, any, None)
      Field fpga_summary


    ports (optional, any, None)
      Field ports


    plat_flag (optional, any, None)
      Field plat_flag


    bios_release_date (optional, any, None)
      Field bios_release_date


    disk_used (optional, any, None)
      Field disk_used


    cpu (optional, any, None)
      Field cpu


    octeon (optional, any, None)
      Field octeon



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

