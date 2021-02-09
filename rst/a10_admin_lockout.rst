.. _a10_admin_lockout_module:


a10_admin_lockout -- Configures A10 admin-lockout
=================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Admin user lockout configuration






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  enable (False, any, None)
    Enable admin user lockout


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  reset_time (False, any, None)
    After how long to reset the lockout counter, in minutes, by default 10 (Time in minutes after which to reset the lockout counter)


  ansible_password (True, any, None)
    Password for AXAPI authentication


  threshold (False, any, None)
    Admin user lockout threshold, by default 5


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  duration (False, any, None)
    Admin user lockout duration, in minutes, by default 10 (Admin user lockout duration in minutes, 0 means forever)


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

