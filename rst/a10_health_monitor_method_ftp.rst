.. _a10_health_monitor_method_ftp_module:


a10_health_monitor_method_ftp -- Configures A10 health.monitor.method.ftp
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

FTP type






Parameters
----------

  ftp (False, any, None)
    FTP type


  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  ftp_port (False, any, None)
    Specify FTP port (Specify port number, default is 21)


  ftp_username (False, any, None)
    Specify the username


  ftp_encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  monitor_name (optional, any, None)
    Key to identify parent object


  ftp_password_string (False, any, None)
    Specify the user password, '' means empty password


  ftp_password (False, any, None)
    Specify the user password


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


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

