.. _a10_system_apps_global_module:


a10_system_apps_global -- Configures A10 system.apps-global
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Global application generic configuration






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


  log_session_on_established (False, any, None)
    Send TCP session creation log on completion of 3-way handshake


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  msl_time (False, any, None)
    Configure maximum session life, default is 2 seconds (1-40 seconds, default is 2 seconds)









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

