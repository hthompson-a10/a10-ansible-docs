.. _a10_backup_periodic_module:


a10_backup_periodic -- Configures A10 backup-periodic
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure backup periodically






Parameters
----------

  week (False, any, None)
    Specify interval weeks


  ansible_username (True, any, None)
    Username for AXAPI authentication


  use_mgmt_port (False, any, None)
    Use management port as source port


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  fixed_nat (False, any, None)
    Backup fixed-nat port mapping files


  a10_partition (False, any, None)
    Destination/target partition for object/command


  day (False, any, None)
    Specify interval days


  uuid (False, any, None)
    uuid of the object


  ansible_port (True, any, None)
    Port for AXAPI authentication


  encrypt (False, any, None)
    Encrypt the backup file


  log (False, any, None)
    Backup log files


  hour (False, any, None)
    Specify interval hours


  ansible_password (True, any, None)
    Password for AXAPI authentication


  system (False, any, None)
    Backup system files


  ansible_host (True, any, None)
    Host for AXAPI authentication


  store_name (False, any, None)
    profile name to store remote url


  state (True, any, None)
    State of the object to be created.


  remote_file (False, any, None)
    profile name for remote url









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

