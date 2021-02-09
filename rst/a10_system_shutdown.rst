.. _a10_system_shutdown_module:


a10_system_shutdown -- Configures A10 system.shutdown
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Field shutdown






Parameters
----------

  oper (False, any, None)
    Field oper


    boot_now (optional, any, None)
      Field boot_now


    hour (optional, any, None)
      Field hour


    min (optional, any, None)
      Field min


    hostname (optional, any, None)
      Field hostname


    uname (optional, any, None)
      Field uname


    reason (optional, any, None)
      Field reason


    boot_scheduled (optional, any, None)
      Field boot_scheduled


    epoch_time (optional, any, None)
      Field epoch_time



  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


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

