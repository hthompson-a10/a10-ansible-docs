.. _a10_fw_status_module:


a10_fw_status -- Configures A10 fw.status
=========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Firewall status






Parameters
----------

  oper (False, any, None)
    Field oper


    most_recent_compilation_status (optional, any, None)
      Field most_recent_compilation_status


    current_active_rule_set (optional, any, None)
      Field current_active_rule_set


    most_recent_compilation_attempt (optional, any, None)
      Field most_recent_compilation_attempt


    previous_successful_compilation_attempt (optional, any, None)
      Field previous_successful_compilation_attempt


    internal (optional, any, None)
      Field internal


    previous_successful_compilation_duration (optional, any, None)
      Field previous_successful_compilation_duration



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

