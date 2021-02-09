.. _a10_chassis_infra_module:


a10_chassis_infra -- Configures A10 chassis-infra
=================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Chassis infrastructure commands






Parameters
----------

  detailed (False, any, None)
    Give Chassis filesystem info( USED BY TAC ONLY )


  debug_enable (False, any, None)
    Enable chassis infrastruture debugging


  ansible_port (True, any, None)
    Port for AXAPI authentication


  system_sync_verify (False, any, None)
    Validate chassis filesytem synchronization status (For A10 TAC Use Only)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  sys_sync (False, any, None)
    Synchronize the Master and Blade filesystems (For A10 TAC Use Only)


  debug_status (False, any, None)
    Show chassis infrastruture debugging status


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  debug_disable (False, any, None)
    Disable chassis infrastruture debugging









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

