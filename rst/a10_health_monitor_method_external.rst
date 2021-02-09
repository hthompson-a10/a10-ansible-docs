.. _a10_health_monitor_method_external_module:


a10_health_monitor_method_external -- Configures A10 health.monitor.method.external
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

EXTERNAL type






Parameters
----------

  ext_preference (False, any, None)
    Get server's perference


  ansible_username (True, any, None)
    Username for AXAPI authentication


  external (False, any, None)
    EXTERNAL type


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  ext_program (False, any, None)
    Specify external application (Program name)


  a10_partition (False, any, None)
    Destination/target partition for object/command


  shared_partition_program (False, any, None)
    external application from shared partition


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  monitor_name (optional, any, None)
    Key to identify parent object


  ext_port (False, any, None)
    Specify the server port (Port Number)


  state (True, any, None)
    State of the object to be created.


  ext_program_shared (False, any, None)
    Specify external application (Program name)


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  ext_arguments (False, any, None)
    Specify external application's arguments (Application arguments)









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

