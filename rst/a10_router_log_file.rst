.. _a10_router_log_file_module:


a10_router_log_file -- Configures A10 router.log.file
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Logging to file






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  rotate (False, any, None)
    Log file rotation (Number of backup files)


  name (False, any, None)
    Logging filename (File name)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  per_protocol (False, any, None)
    Per protocol


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  size (False, any, None)
    Log file maximum size (File size in MBytes)


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uuid (False, any, None)
    uuid of the object









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

