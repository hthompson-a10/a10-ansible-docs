.. _a10_link_startup_config_module:


a10_link_startup_config -- Configures A10 link.startup-config
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Startup Configuration






Parameters
----------

+-----------------------+-------------------------------+-------------------------------------------------+
| Parameters            | Choices/Defaults              | Comment                                         |
|                       |                               |                                                 |
|                       |                               |                                                 |
+=======================+===============================+=================================================+
| state                 | ['noop', 'present', 'absent'] | State of the object to be created.              |
|                       |                               |                                                 |
| /required             |                               |                                                 |
+-----------------------+-------------------------------+-------------------------------------------------+
| ansible_host          |                               | Host for AXAPI authentication                   |
|                       |                               |                                                 |
| /required             |                               |                                                 |
+-----------------------+-------------------------------+-------------------------------------------------+
| ansible_username      |                               | Username for AXAPI authentication               |
|                       |                               |                                                 |
| /required             |                               |                                                 |
+-----------------------+-------------------------------+-------------------------------------------------+
| ansible_password      |                               | Password for AXAPI authentication               |
|                       |                               |                                                 |
| /required             |                               |                                                 |
+-----------------------+-------------------------------+-------------------------------------------------+
| ansible_port          |                               | Port for AXAPI authentication                   |
|                       |                               |                                                 |
| /required             |                               |                                                 |
+-----------------------+-------------------------------+-------------------------------------------------+
| a10_device_context_id | ['1-8']                       | Device ID for aVCS configuration                |
|                       |                               |                                                 |
|                       |                               |                                                 |
+-----------------------+-------------------------------+-------------------------------------------------+
| a10_partition         |                               | Destination/target partition for object/command |
|                       |                               |                                                 |
|                       |                               |                                                 |
+-----------------------+-------------------------------+-------------------------------------------------+
| default               |                               | Default startup-config                          |
|                       |                               |                                                 |
|                       |                               |                                                 |
+-----------------------+-------------------------------+-------------------------------------------------+
| file_name             |                               | Local Configuration Profile Name                |
|                       |                               |                                                 |
|                       |                               |                                                 |
+-----------------------+-------------------------------+-------------------------------------------------+
| primary               |                               | Create link in primary partition                |
|                       |                               |                                                 |
|                       |                               |                                                 |
+-----------------------+-------------------------------+-------------------------------------------------+
| secondary             |                               | Create link in secondary partition              |
|                       |                               |                                                 |
|                       |                               |                                                 |
+-----------------------+-------------------------------+-------------------------------------------------+
| all_partitions        |                               | All-partitions                                  |
|                       |                               |                                                 |
|                       |                               |                                                 |
+-----------------------+-------------------------------+-------------------------------------------------+







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

