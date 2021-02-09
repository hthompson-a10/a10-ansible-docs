.. _a10_system_upgrade_status_module:


a10_system_upgrade_status -- Configures A10 system.upgrade-status
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Get upgrading status






Parameters
----------

  oper (False, any, None)
    Field oper


    status (optional, any, None)
      Field status


    message (optional, any, None)
      Field message


    rollback_pri (optional, any, None)
      Field rollback_pri


    rollback_sec (optional, any, None)
      Field rollback_sec



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

