.. _a10_admin_password_module:


a10_admin_password -- Configures A10 admin.password
===================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Config admin user password






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  admin_user (optional, any, None)
    Key to identify parent object


  password_in_module (False, any, None)
    Config admin user password


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


  encrypted_in_module (False, any, None)
    Specify an ENCRYPTED password string (System admin user password)









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

