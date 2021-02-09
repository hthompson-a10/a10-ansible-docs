.. _a10_health_external_rename_module:


a10_health_external_rename -- Configures A10 health.external.rename
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Rename external health monitor script






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  dst_file (False, any, None)
    Destination external health monitor script file name


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  src_file (False, any, None)
    Source external health monitor script file name









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

