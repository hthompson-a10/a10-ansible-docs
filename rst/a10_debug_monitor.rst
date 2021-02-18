.. _a10_debug_monitor_module:


a10_debug_monitor -- Configures A10 debug.monitor
=================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Monitor debug output






Parameters
----------

+-----------------------+---------------------+-------------------------------------------------+
| Parameters            | Choices/Defaults    | Comment                                         |
|                       |                     |                                                 |
|                       |                     |                                                 |
+=======================+=====================+=================================================+
| state                 | ['noop', 'present'] | State of the object to be created.              |
|                       |                     |                                                 |
| /required             |                     |                                                 |
+-----------------------+---------------------+-------------------------------------------------+
| ansible_host          |                     | Host for AXAPI authentication                   |
|                       |                     |                                                 |
| /required             |                     |                                                 |
+-----------------------+---------------------+-------------------------------------------------+
| ansible_username      |                     | Username for AXAPI authentication               |
|                       |                     |                                                 |
| /required             |                     |                                                 |
+-----------------------+---------------------+-------------------------------------------------+
| ansible_password      |                     | Password for AXAPI authentication               |
|                       |                     |                                                 |
| /required             |                     |                                                 |
+-----------------------+---------------------+-------------------------------------------------+
| ansible_port          |                     | Port for AXAPI authentication                   |
|                       |                     |                                                 |
| /required             |                     |                                                 |
+-----------------------+---------------------+-------------------------------------------------+
| a10_device_context_id | ['1-8']             | Device ID for aVCS configuration                |
|                       |                     |                                                 |
|                       |                     |                                                 |
+-----------------------+---------------------+-------------------------------------------------+
| a10_partition         |                     | Destination/target partition for object/command |
|                       |                     |                                                 |
|                       |                     |                                                 |
+-----------------------+---------------------+-------------------------------------------------+
| filename              |                     | Filename to save debug output                   |
|                       |                     |                                                 |
|                       |                     |                                                 |
+-----------------------+---------------------+-------------------------------------------------+
| all_slots             |                     | Display debug output of both Master and Blade   |
|                       |                     |                                                 |
|                       |                     |                                                 |
+-----------------------+---------------------+-------------------------------------------------+
| cpuid                 |                     | CPU id to debug (0,1,...)                       |
|                       |                     |                                                 |
|                       |                     |                                                 |
+-----------------------+---------------------+-------------------------------------------------+
| uuid                  |                     | uuid of the object                              |
|                       |                     |                                                 |
|                       |                     |                                                 |
+-----------------------+---------------------+-------------------------------------------------+







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

