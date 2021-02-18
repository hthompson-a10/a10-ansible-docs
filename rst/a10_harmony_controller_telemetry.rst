.. _a10_harmony_controller_telemetry_module:


a10_harmony_controller_telemetry -- Configures A10 harmony.controller.telemetry
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Harmony controller telemetry config






Parameters
----------

+-----------------------+-------------------------------+-------------------------------------------------------------+
| Parameters            | Choices/Defaults              | Comment                                                     |
|                       |                               |                                                             |
|                       |                               |                                                             |
+=======================+===============================+=============================================================+
| state                 | ['noop', 'present', 'absent'] | State of the object to be created.                          |
|                       |                               |                                                             |
| /required             |                               |                                                             |
+-----------------------+-------------------------------+-------------------------------------------------------------+
| ansible_host          |                               | Host for AXAPI authentication                               |
|                       |                               |                                                             |
| /required             |                               |                                                             |
+-----------------------+-------------------------------+-------------------------------------------------------------+
| ansible_username      |                               | Username for AXAPI authentication                           |
|                       |                               |                                                             |
| /required             |                               |                                                             |
+-----------------------+-------------------------------+-------------------------------------------------------------+
| ansible_password      |                               | Password for AXAPI authentication                           |
|                       |                               |                                                             |
| /required             |                               |                                                             |
+-----------------------+-------------------------------+-------------------------------------------------------------+
| ansible_port          |                               | Port for AXAPI authentication                               |
|                       |                               |                                                             |
| /required             |                               |                                                             |
+-----------------------+-------------------------------+-------------------------------------------------------------+
| a10_device_context_id | ['1-8']                       | Device ID for aVCS configuration                            |
|                       |                               |                                                             |
|                       |                               |                                                             |
+-----------------------+-------------------------------+-------------------------------------------------------------+
| a10_partition         |                               | Destination/target partition for object/command             |
|                       |                               |                                                             |
|                       |                               |                                                             |
+-----------------------+-------------------------------+-------------------------------------------------------------+
| log_rate              |                               | Max number of session logs sent by the partition per second |
|                       |                               |                                                             |
|                       |                               |                                                             |
+-----------------------+-------------------------------+-------------------------------------------------------------+
| uuid                  |                               | uuid of the object                                          |
|                       |                               |                                                             |
|                       |                               |                                                             |
+-----------------------+-------------------------------+-------------------------------------------------------------+







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

