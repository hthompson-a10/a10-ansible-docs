.. _a10_file_log_backup_module:


a10_file_log_backup -- Configures A10 file.log-backup
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Backup system files






Parameters
----------

  week (False, any, None)
    Most recent week


  all (False, any, None)
    all log


  ansible_username (True, any, None)
    Username for AXAPI authentication


  period (False, any, None)
    Specify backup period


  month (False, any, None)
     Most recent month


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  date (False, any, None)
    specify number of days


  a10_partition (False, any, None)
    Destination/target partition for object/command


  day (False, any, None)
    Most recent day


  expedite (False, any, None)
    Expedite the Backup


  ansible_port (True, any, None)
    Port for AXAPI authentication


  file_handle (False, any, None)
    full path of the uploaded file


  file_content (False, any, None)
    Content of the uploaded file


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  ansible_password (True, any, None)
    Password for AXAPI authentication


  stats_data (False, any, None)
    Backup web statistical data









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

