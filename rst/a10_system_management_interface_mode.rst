.. _a10_system_management_interface_mode_module:


a10_system_management_interface_mode -- Configures A10 system.management-interface-mode
=======================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure management interface mode






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  dedicated (False, any, None)
    Set management interface in dedicated mode


  non_dedicated (False, any, None)
    Set management interface in non-dedicated mode


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

