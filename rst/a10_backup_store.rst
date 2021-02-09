.. _a10_backup_store_module:


a10_backup_store -- Configures A10 backup.store
===============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Save backup store information






Parameters
----------

  creat_cfg (False, any, None)
    Field creat_cfg


    store_name (optional, any, None)
      profile name to store remote url


    create (optional, any, None)
      Create store


    remote_file (optional, any, None)
      profile name for remote url



  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  delete_cfg (False, any, None)
    Field delete_cfg


    delete (optional, any, None)
      Delete store


    store_name_del (optional, any, None)
      profile name for deleting



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

