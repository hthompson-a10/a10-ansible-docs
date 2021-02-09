.. _a10_write_memory_module:


a10_write_memory -- Configures A10 write.memory
===============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Write memory






Parameters
----------

  profile (False, any, None)
    Local Configuration Profile Name


  ansible_port (True, any, None)
    Port for AXAPI authentication


  destination (False, any, None)
    'primary'= Write to default Primary Configuration; 'secondary'= Write to default Secondary Configuration; 'local'= Local Configuration Profile Name;


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  specified_partition (False, any, None)
    Specified partition


  partition (False, any, None)
    'all'= All partition configurations; 'shared'= Shared partition; 'specified'= Specified partition;


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

