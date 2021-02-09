.. _a10_debug_cli_module:


a10_debug_cli -- Configures A10 debug.cli
=========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

CLI module parameters






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  parser (False, any, None)
    CLI debug parser switch


  all (False, any, None)
    CLI all debug switch


  state (True, any, None)
    State of the object to be created.


  io (False, any, None)
    CLI debug input-output switch


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

