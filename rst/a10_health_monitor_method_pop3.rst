.. _a10_health_monitor_method_pop3_module:


a10_health_monitor_method_pop3 -- Configures A10 health.monitor.method.pop3
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

POP3 type






Parameters
----------

  pop3_password (False, any, None)
    Specify the user password


  ansible_port (True, any, None)
    Port for AXAPI authentication


  pop3_encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  pop3 (False, any, None)
    POP3 type


  monitor_name (optional, any, None)
    Key to identify parent object


  pop3_port (False, any, None)
    Specify the POP3 port, default is 110 (Port Number (default 110))


  ansible_password (True, any, None)
    Password for AXAPI authentication


  pop3_password_string (False, any, None)
    Specify the user password, '' means empty password


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  pop3_username (False, any, None)
    Specify the username


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

