.. _a10_system_view_show_monitor_module:


a10_system_view_show_monitor -- Configures A10 system.view.show-monitor
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show monitor threshold configuration






Parameters
----------

  oper (False, any, None)
    Field oper


    ctrl_cpu (optional, any, None)
      Field ctrl_cpu


    warn_temp (optional, any, None)
      Field warn_temp


    buff_value (optional, any, None)
      Field buff_value


    spm1 (optional, any, None)
      Field spm1


    buff_drop (optional, any, None)
      Field buff_drop


    spm4 (optional, any, None)
      Field spm4


    smp0 (optional, any, None)
      Field smp0


    smp1 (optional, any, None)
      Field smp1


    smp2 (optional, any, None)
      Field smp2


    smp3 (optional, any, None)
      Field smp3


    spm2 (optional, any, None)
      Field spm2


    spm3 (optional, any, None)
      Field spm3


    spm0 (optional, any, None)
      Field spm0


    disk_value (optional, any, None)
      Field disk_value


    mem_value (optional, any, None)
      Field mem_value


    smp4 (optional, any, None)
      Field smp4


    data_cpu (optional, any, None)
      Field data_cpu



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

