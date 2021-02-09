.. _a10_configure_sync_module:


a10_configure_sync -- Configures A10 configure.sync
===================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Sync operation






Parameters
----------

  private_key (False, any, None)
    Use private key for authentication


  pwd_enc (False, any, None)
    Field pwd_enc


  auto_authentication (False, any, None)
    Authenticate with local username and password


  ntype (False, any, None)
    'running'= Sync local running to peer's running configuration; 'all'= Sync local running to peer's running configuration, and local startup to peer's startup configuration;


  pwd (False, any, None)
    Field pwd


  address (False, any, None)
    Specify the destination ip address to sync


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  partition_name (False, any, None)
    Partition name


  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  usr (False, any, None)
    Field usr


  shared (False, any, None)
    Shared partition


  ansible_password (True, any, None)
    Password for AXAPI authentication


  all_partitions (False, any, None)
    All partition configurations









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

