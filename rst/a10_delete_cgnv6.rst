.. _a10_delete_cgnv6_module:


a10_delete_cgnv6 -- Configures A10 delete.cgnv6
===============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Delete cgnv6 related files






Parameters
----------

+-------------------------------------+-------------------------------+-------------------------------------------------+
| Parameters                          | Choices/Defaults              | Comment                                         |
|                                     |                               |                                                 |
|                                     |                               |                                                 |
+=====================================+===============================+=================================================+
| state                               | ['noop', 'present', 'absent'] | State of the object to be created.              |
|                                     |                               |                                                 |
| /required                           |                               |                                                 |
+-------------------------------------+-------------------------------+-------------------------------------------------+
| ansible_host                        |                               | Host for AXAPI authentication                   |
|                                     |                               |                                                 |
| /required                           |                               |                                                 |
+-------------------------------------+-------------------------------+-------------------------------------------------+
| ansible_username                    |                               | Username for AXAPI authentication               |
|                                     |                               |                                                 |
| /required                           |                               |                                                 |
+-------------------------------------+-------------------------------+-------------------------------------------------+
| ansible_password                    |                               | Password for AXAPI authentication               |
|                                     |                               |                                                 |
| /required                           |                               |                                                 |
+-------------------------------------+-------------------------------+-------------------------------------------------+
| ansible_port                        |                               | Port for AXAPI authentication                   |
|                                     |                               |                                                 |
| /required                           |                               |                                                 |
+-------------------------------------+-------------------------------+-------------------------------------------------+
| a10_device_context_id               | ['1-8']                       | Device ID for aVCS configuration                |
|                                     |                               |                                                 |
|                                     |                               |                                                 |
+-------------------------------------+-------------------------------+-------------------------------------------------+
| a10_partition                       |                               | Destination/target partition for object/command |
|                                     |                               |                                                 |
|                                     |                               |                                                 |
+-------------------------------------+-------------------------------+-------------------------------------------------+
| fixed_nat                           |                               | Delete fixed-nat port-mapping-file              |
|                                     |                               |                                                 |
|                                     |                               |                                                 |
+-------------------------------------+-------------------------------+-------------------------------------------------+
| lw_4o6_binding_table_validation_log |                               | LW-4O6 Binding Table validation log File        |
|                                     |                               |                                                 |
|                                     |                               |                                                 |
+-------------------------------------+-------------------------------+-------------------------------------------------+
| filename                            |                               | Specify the port-mapping-file to be deleted     |
|                                     |                               |                                                 |
|                                     |                               |                                                 |
+-------------------------------------+-------------------------------+-------------------------------------------------+
| lw_filename                         |                               | LW-4O6 Binding Table Validation Log File Name   |
|                                     |                               |                                                 |
|                                     |                               |                                                 |
+-------------------------------------+-------------------------------+-------------------------------------------------+







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

