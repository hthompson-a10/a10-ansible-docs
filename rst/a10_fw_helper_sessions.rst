.. _a10_fw_helper_sessions_module:


a10_fw_helper_sessions -- Configures A10 fw.helper-sessions
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure firewall helper-session (TAC use only)






Parameters
----------

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


  idle_timeout (False, any, None)
    helper-sessions idle-timeout time (Idle-timeout in minutes (default= 1 minute))


  limit (False, any, None)
    Limit number of helper-sessions (Limit helper-sessions number)


  mode (False, any, None)
    'disable'= Disable helper-sessions;


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

