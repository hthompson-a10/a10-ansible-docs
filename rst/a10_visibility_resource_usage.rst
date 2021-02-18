.. _a10_visibility_resource_usage_module:


a10_visibility_resource_usage -- Configures A10 visibility.resource-usage
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Visibility resoruces information






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
| uuid                  |                     | uuid of the object                              |
|                       |                     |                                                 |
|                       |                     |                                                 |
+-----------------------+---------------------+-------------------------------------------------+
| oper                  |                     | Field oper                                      |
|                       |                     |                                                 |
|                       |                     |                                                 |
+---+-------------------+---------------------+-------------------------------------------------+
|   | resource_list     |                     | Field resource_list                             |
|   |                   |                     |                                                 |
|   |                   |                     |                                                 |
+---+-------------------+---------------------+-------------------------------------------------+







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

