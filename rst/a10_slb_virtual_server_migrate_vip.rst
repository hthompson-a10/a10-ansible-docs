.. _a10_slb_virtual_server_migrate_vip_module:


a10_slb_virtual_server_migrate_vip -- Configures A10 slb.virtual.server.migrate-vip
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Migrate this virtual server






Parameters
----------

  oper (False, any, None)
    Field oper


    state (optional, any, None)
      Field state



  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  finish_migration (False, any, None)
    Complete the migration


  cancel_migration (False, any, None)
    Cancel migration


  state (True, any, None)
    State of the object to be created.


  target_data_cpu (False, any, None)
    Number of CPUs on the target platform


  virtual_server_name (optional, any, None)
    Key to identify parent object


  target_floating_ipv4 (False, any, None)
    Specify IP address


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

