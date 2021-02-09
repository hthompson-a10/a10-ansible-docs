.. _a10_backup_log_module:


a10_backup_log -- Configures A10 backup.log
===========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Backup log files






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


  use_mgmt_port (False, any, None)
    Use management port as source port


  date (False, any, None)
    specify number of days


  password (False, any, None)
    password for the remote site


  a10_partition (False, any, None)
    Destination/target partition for object/command


  day (False, any, None)
    Most recent day


  expedite (False, any, None)
    Expedite the Backup


  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  ansible_host (True, any, None)
    Host for AXAPI authentication


  store_name (False, any, None)
    Save backup store information


  state (True, any, None)
    State of the object to be created.


  remote_file (False, any, None)
    profile name for remote url


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

