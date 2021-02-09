.. _a10_health_monitor_method_tacplus_module:


a10_health_monitor_method_tacplus -- Configures A10 health.monitor.method.tacplus
=================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

TACACS+ type






Parameters
----------

  tacplus_port (False, any, None)
    Specify the TACACS+ port, default 49 (Port number (default 49))


  ansible_username (True, any, None)
    Username for AXAPI authentication


  tacplus_secret_string (False, any, None)
    Shared Crypto Key


  ansible_password (True, any, None)
    Password for AXAPI authentication


  tacplus_secret (False, any, None)
    Specify the shared secret of TACACS+ server


  tacplus_password_string (False, any, None)
    Configure password, '' means empty password


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  tacplus_type (False, any, None)
    'inbound-ascii-login'= Specify Inbound ASCII Login type;


  monitor_name (optional, any, None)
    Key to identify parent object


  tacplus_password (False, any, None)
    Specify the user password


  tacplus_username (False, any, None)
    Specify the username


  state (True, any, None)
    State of the object to be created.


  tacplus (False, any, None)
    TACACS+ type


  tacplus_encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)


  secret_encrypted (False, any, None)
    Field secret_encrypted









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

