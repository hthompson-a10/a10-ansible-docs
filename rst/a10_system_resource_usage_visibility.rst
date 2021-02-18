.. _a10_system_resource_usage_visibility_module:


a10_system_resource_usage_visibility -- Configures A10 system.resource.usage.visibility
=======================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure System Resource Usage for visibility






Parameters
----------

+------------------------+-------------------------------+---------------------------------------------------+
| Parameters             | Choices/Defaults              | Comment                                           |
|                        |                               |                                                   |
|                        |                               |                                                   |
+========================+===============================+===================================================+
| state                  | ['noop', 'present', 'absent'] | State of the object to be created.                |
|                        |                               |                                                   |
| /required              |                               |                                                   |
+------------------------+-------------------------------+---------------------------------------------------+
| ansible_host           |                               | Host for AXAPI authentication                     |
|                        |                               |                                                   |
| /required              |                               |                                                   |
+------------------------+-------------------------------+---------------------------------------------------+
| ansible_username       |                               | Username for AXAPI authentication                 |
|                        |                               |                                                   |
| /required              |                               |                                                   |
+------------------------+-------------------------------+---------------------------------------------------+
| ansible_password       |                               | Password for AXAPI authentication                 |
|                        |                               |                                                   |
| /required              |                               |                                                   |
+------------------------+-------------------------------+---------------------------------------------------+
| ansible_port           |                               | Port for AXAPI authentication                     |
|                        |                               |                                                   |
| /required              |                               |                                                   |
+------------------------+-------------------------------+---------------------------------------------------+
| a10_device_context_id  | ['1-8']                       | Device ID for aVCS configuration                  |
|                        |                               |                                                   |
|                        |                               |                                                   |
+------------------------+-------------------------------+---------------------------------------------------+
| a10_partition          |                               | Destination/target partition for object/command   |
|                        |                               |                                                   |
|                        |                               |                                                   |
+------------------------+-------------------------------+---------------------------------------------------+
| monitored_entity_count |                               | Total number of monitored entities for visibility |
|                        |                               |                                                   |
|                        |                               |                                                   |
+------------------------+-------------------------------+---------------------------------------------------+
| uuid                   |                               | uuid of the object                                |
|                        |                               |                                                   |
|                        |                               |                                                   |
+------------------------+-------------------------------+---------------------------------------------------+







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

