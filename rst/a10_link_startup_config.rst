.. _a10_link_startup_config_module:


a10_link_startup_config -- Configures A10 link.startup-config
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Startup Configuration






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  default (False, any, None)
    Default startup-config


  file_name (False, any, None)
    Local Configuration Profile Name


  primary (False, any, None)
    Create link in primary partition


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  secondary (False, any, None)
    Create link in secondary partition


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  all_partitions (False, any, None)
    All-partitions









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

