.. _a10_erase_module:


a10_erase -- Configures A10 erase
=================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Erase Configuration






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  preserve_accounts (False, any, None)
    preserve admin accounts


  preserve_management (False, any, None)
    preserve managememt ip and default gateway


  state (True, any, None)
    State of the object to be created.


  reload (False, any, None)
    reload after erase


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  all_partitions (False, any, None)
    Wipe out all service config for all partitions









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

