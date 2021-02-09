.. _a10_axdebug_save_config_module:


a10_axdebug_save_config -- Configures A10 axdebug.save-config
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

save AXDebug config file






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  config_file (False, any, None)
    config file name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  default (False, any, None)
    save to default config file


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

