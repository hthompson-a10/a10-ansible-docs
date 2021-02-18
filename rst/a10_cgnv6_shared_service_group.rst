.. _a10_cgnv6_shared_service_group_module:


a10_cgnv6_shared_service_group -- Configures A10 cgnv6.shared-service-group
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

CGNv6 Shared Service Group






Parameters
----------

+-------------------------------+-------------------------------+-------------------------------------------------+
| Parameters                    | Choices/Defaults              | Comment                                         |
|                               |                               |                                                 |
|                               |                               |                                                 |
+===============================+===============================+=================================================+
| state                         | ['noop', 'present', 'absent'] | State of the object to be created.              |
|                               |                               |                                                 |
| /required                     |                               |                                                 |
+-------------------------------+-------------------------------+-------------------------------------------------+
| ansible_host                  |                               | Host for AXAPI authentication                   |
|                               |                               |                                                 |
| /required                     |                               |                                                 |
+-------------------------------+-------------------------------+-------------------------------------------------+
| ansible_username              |                               | Username for AXAPI authentication               |
|                               |                               |                                                 |
| /required                     |                               |                                                 |
+-------------------------------+-------------------------------+-------------------------------------------------+
| ansible_password              |                               | Password for AXAPI authentication               |
|                               |                               |                                                 |
| /required                     |                               |                                                 |
+-------------------------------+-------------------------------+-------------------------------------------------+
| ansible_port                  |                               | Port for AXAPI authentication                   |
|                               |                               |                                                 |
| /required                     |                               |                                                 |
+-------------------------------+-------------------------------+-------------------------------------------------+
| a10_device_context_id         | ['1-8']                       | Device ID for aVCS configuration                |
|                               |                               |                                                 |
|                               |                               |                                                 |
+-------------------------------+-------------------------------+-------------------------------------------------+
| a10_partition                 |                               | Destination/target partition for object/command |
|                               |                               |                                                 |
|                               |                               |                                                 |
+-------------------------------+-------------------------------+-------------------------------------------------+
| uuid                          |                               | uuid of the object                              |
|                               |                               |                                                 |
|                               |                               |                                                 |
+-------------------------------+-------------------------------+-------------------------------------------------+
| oper                          |                               | Field oper                                      |
|                               |                               |                                                 |
|                               |                               |                                                 |
+---+---------------------------+-------------------------------+-------------------------------------------------+
|   | shared_service_group_list |                               | Field shared_service_group_list                 |
|   |                           |                               |                                                 |
|   |                           |                               |                                                 |
+---+---------------------------+-------------------------------+-------------------------------------------------+







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

