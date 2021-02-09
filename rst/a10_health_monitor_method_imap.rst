.. _a10_health_monitor_method_imap_module:


a10_health_monitor_method_imap -- Configures A10 health.monitor.method.imap
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

IMAP type






Parameters
----------

  imap_port (False, any, None)
    Specify the IMAP port, default is 143 (Port Number (default 143))


  ansible_username (True, any, None)
    Username for AXAPI authentication


  imap_password_string (False, any, None)
    Configure password, '' means empty password


  imap_cram_md5 (False, any, None)
    Challenge-response authentication mechanism


  pwd_auth (False, any, None)
    Specify the Authentication method


  imap_password (False, any, None)
    Specify the user password


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  imap (False, any, None)
    IMAP type


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  monitor_name (optional, any, None)
    Key to identify parent object


  imap_encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)


  ansible_host (True, any, None)
    Host for AXAPI authentication


  imap_login (False, any, None)
    Simple login


  state (True, any, None)
    State of the object to be created.


  imap_username (False, any, None)
    Specify the username


  imap_plain (False, any, None)
    Plain text


  ansible_password (True, any, None)
    Password for AXAPI authentication









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

