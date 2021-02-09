.. _a10_file_system_backup_module:


a10_file_system_backup -- Configures A10 file.system-backup
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Backup system files






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  file_handle (False, any, None)
    full path of the uploaded file


  ansible_username (True, any, None)
    Username for AXAPI authentication


  file_content (False, any, None)
    Content of the uploaded file


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

