.. _a10_harmony_controller_profile_re_sync_module:


a10_harmony_controller_profile_re_sync -- Configures A10 harmony.controller.profile.re-sync
===========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Harmony controller profile






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  schema_registry (False, any, None)
    re-sync the schema registry


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


  analytics_bus (False, any, None)
    re-sync analtyics bus connections









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

