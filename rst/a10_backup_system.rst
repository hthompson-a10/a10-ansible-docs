.. _a10_backup_system_module:


a10_backup_system -- Configures A10 backup.system
=================================================

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


  encrypt (False, any, None)
    Encrypt the backup file


  ansible_username (True, any, None)
    Username for AXAPI authentication


  remote_file (False, any, None)
    profile name for remote url


  ansible_password (True, any, None)
    Password for AXAPI authentication


  store_name (False, any, None)
    Save backup store information


  state (True, any, None)
    State of the object to be created.


  use_mgmt_port (False, any, None)
    Use management port as source port


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  password (False, any, None)
    password for the remote site


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

