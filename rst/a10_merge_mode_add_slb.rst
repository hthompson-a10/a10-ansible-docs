.. _a10_merge_mode_add_slb_module:


a10_merge_mode_add_slb -- Configures A10 merge.mode.add.slb
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Control block-merge mode behavior for slb objects






Parameters
----------

+-----------------------+-------------------------------+-----------------------------------------------------------+
| Parameters            | Choices/Defaults              | Comment                                                   |
|                       |                               |                                                           |
|                       |                               |                                                           |
+=======================+===============================+===========================================================+
| state                 | ['noop', 'present', 'absent'] | State of the object to be created.                        |
|                       |                               |                                                           |
| /required             |                               |                                                           |
+-----------------------+-------------------------------+-----------------------------------------------------------+
| ansible_host          |                               | Host for AXAPI authentication                             |
|                       |                               |                                                           |
| /required             |                               |                                                           |
+-----------------------+-------------------------------+-----------------------------------------------------------+
| ansible_username      |                               | Username for AXAPI authentication                         |
|                       |                               |                                                           |
| /required             |                               |                                                           |
+-----------------------+-------------------------------+-----------------------------------------------------------+
| ansible_password      |                               | Password for AXAPI authentication                         |
|                       |                               |                                                           |
| /required             |                               |                                                           |
+-----------------------+-------------------------------+-----------------------------------------------------------+
| ansible_port          |                               | Port for AXAPI authentication                             |
|                       |                               |                                                           |
| /required             |                               |                                                           |
+-----------------------+-------------------------------+-----------------------------------------------------------+
| a10_device_context_id | ['1-8']                       | Device ID for aVCS configuration                          |
|                       |                               |                                                           |
|                       |                               |                                                           |
+-----------------------+-------------------------------+-----------------------------------------------------------+
| a10_partition         |                               | Destination/target partition for object/command           |
|                       |                               |                                                           |
|                       |                               |                                                           |
+-----------------------+-------------------------------+-----------------------------------------------------------+
| server_port           |                               | Control block-merge behavior for slb server port          |
|                       |                               |                                                           |
|                       |                               |                                                           |
+-----------------------+-------------------------------+-----------------------------------------------------------+
| member                |                               | Control block-merge behavior for slb service-group member |
|                       |                               |                                                           |
|                       |                               |                                                           |
+-----------------------+-------------------------------+-----------------------------------------------------------+
| virtual_server_port   |                               | Control block-merge behavior for slb virtual-server port  |
|                       |                               |                                                           |
|                       |                               |                                                           |
+-----------------------+-------------------------------+-----------------------------------------------------------+
| uuid                  |                               | uuid of the object                                        |
|                       |                               |                                                           |
|                       |                               |                                                           |
+-----------------------+-------------------------------+-----------------------------------------------------------+







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

