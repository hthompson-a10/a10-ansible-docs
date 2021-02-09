.. _a10_health_monitor_method_radius_module:


a10_health_monitor_method_radius -- Configures A10 health.monitor.method.radius
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

RADIUS type






Parameters
----------

  ansible_username (True, any, None)
    Username for AXAPI authentication


  radius_response_code (False, any, None)
    Specify response code range (e.g. 2,4-7) (Format is xx,xx-xx (xx between [1, 13]))


  radius_encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  radius (False, any, None)
    RADIUS type


  radius_password_string (False, any, None)
    Configure password, '' means empty password


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  radius_password (False, any, None)
    Specify the user password


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  monitor_name (optional, any, None)
    Key to identify parent object


  state (True, any, None)
    State of the object to be created.


  radius_username (False, any, None)
    Specify the username


  radius_port (False, any, None)
    Specify the RADIUS port, default is 1812 (Port number (default 1812))


  radius_secret (False, any, None)
    Specify the shared secret of RADIUS server (Shared Crypto Key)


  radius_expect (False, any, None)
    Specify what you expect from the response message


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

