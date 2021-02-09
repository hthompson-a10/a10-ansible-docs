.. _a10_reload_module:


a10_reload -- Configures A10 reload
===================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Reload the system without rebooting






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  all (False, any, None)
    Reload all devices when VCS is enabled, or only this device itself if VCS is not enabled


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  device (False, any, None)
    Reload a specific device when VCS is enabled (device id)


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

