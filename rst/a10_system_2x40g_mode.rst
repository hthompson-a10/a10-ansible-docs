.. _a10_system_2x40g_mode_module:


a10_system_2x40g_mode -- Configures A10 system-2x40g-mode
=========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

To enable/disable 40G port to split into 2x40g ports






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  enable (False, any, None)
    Enable/Disable 100G port to split into 2x40g ports


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

