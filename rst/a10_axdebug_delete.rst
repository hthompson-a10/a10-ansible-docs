.. _a10_axdebug_delete_module:


a10_axdebug_delete -- Configures A10 axdebug.delete
===================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

delete axdebug file






Parameters
----------

+-----------------------+-------------------------------+----------------------------------------------------------------+
| Parameters            | Choices/Defaults              | Comment                                                        |
|                       |                               |                                                                |
|                       |                               |                                                                |
+=======================+===============================+================================================================+
| state                 | ['noop', 'present', 'absent'] | State of the object to be created.                             |
|                       |                               |                                                                |
| /required             |                               |                                                                |
+-----------------------+-------------------------------+----------------------------------------------------------------+
| ansible_host          |                               | Host for AXAPI authentication                                  |
|                       |                               |                                                                |
| /required             |                               |                                                                |
+-----------------------+-------------------------------+----------------------------------------------------------------+
| ansible_username      |                               | Username for AXAPI authentication                              |
|                       |                               |                                                                |
| /required             |                               |                                                                |
+-----------------------+-------------------------------+----------------------------------------------------------------+
| ansible_password      |                               | Password for AXAPI authentication                              |
|                       |                               |                                                                |
| /required             |                               |                                                                |
+-----------------------+-------------------------------+----------------------------------------------------------------+
| ansible_port          |                               | Port for AXAPI authentication                                  |
|                       |                               |                                                                |
| /required             |                               |                                                                |
+-----------------------+-------------------------------+----------------------------------------------------------------+
| a10_device_context_id | ['1-8']                       | Device ID for aVCS configuration                               |
|                       |                               |                                                                |
|                       |                               |                                                                |
+-----------------------+-------------------------------+----------------------------------------------------------------+
| a10_partition         |                               | Destination/target partition for object/command                |
|                       |                               |                                                                |
|                       |                               |                                                                |
+-----------------------+-------------------------------+----------------------------------------------------------------+
| capture_file          |                               | Delete a capture file (Specify target filename to change)      |
|                       |                               |                                                                |
|                       |                               |                                                                |
+-----------------------+-------------------------------+----------------------------------------------------------------+
| config_file           |                               | Delete AXDebug config file (Specify target filename to change) |
|                       |                               |                                                                |
|                       |                               |                                                                |
+-----------------------+-------------------------------+----------------------------------------------------------------+







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

