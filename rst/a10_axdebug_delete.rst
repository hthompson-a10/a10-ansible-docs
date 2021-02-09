.. _a10_axdebug_delete_module:


a10_axdebug_delete -- Configures A10 axdebug.delete
===================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

delete axdebug file






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  config_file (False, any, None)
    Delete AXDebug config file (Specify target filename to change)


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


  capture_file (False, any, None)
    Delete a capture file (Specify target filename to change)









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

