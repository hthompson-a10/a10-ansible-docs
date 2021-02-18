.. _a10_logging_lsn_port_unavailable_module:


a10_logging_lsn_port_unavailable -- Configures A10 logging.lsn.port-unavailable
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Set LSN system log policy when port unavailable occur






Parameters
----------

+-----------------------+-------------------------------+--------------------------------------------------------------+
| Parameters            | Choices/Defaults              | Comment                                                      |
|                       |                               |                                                              |
|                       |                               |                                                              |
+=======================+===============================+==============================================================+
| state                 | ['noop', 'present', 'absent'] | State of the object to be created.                           |
|                       |                               |                                                              |
| /required             |                               |                                                              |
+-----------------------+-------------------------------+--------------------------------------------------------------+
| ansible_host          |                               | Host for AXAPI authentication                                |
|                       |                               |                                                              |
| /required             |                               |                                                              |
+-----------------------+-------------------------------+--------------------------------------------------------------+
| ansible_username      |                               | Username for AXAPI authentication                            |
|                       |                               |                                                              |
| /required             |                               |                                                              |
+-----------------------+-------------------------------+--------------------------------------------------------------+
| ansible_password      |                               | Password for AXAPI authentication                            |
|                       |                               |                                                              |
| /required             |                               |                                                              |
+-----------------------+-------------------------------+--------------------------------------------------------------+
| ansible_port          |                               | Port for AXAPI authentication                                |
|                       |                               |                                                              |
| /required             |                               |                                                              |
+-----------------------+-------------------------------+--------------------------------------------------------------+
| a10_device_context_id | ['1-8']                       | Device ID for aVCS configuration                             |
|                       |                               |                                                              |
|                       |                               |                                                              |
+-----------------------+-------------------------------+--------------------------------------------------------------+
| a10_partition         |                               | Destination/target partition for object/command              |
|                       |                               |                                                              |
|                       |                               |                                                              |
+-----------------------+-------------------------------+--------------------------------------------------------------+
| ip_based              |                               | Log LSN port unavailable based on NAT IP (Default= disabled) |
|                       |                               |                                                              |
|                       |                               |                                                              |
+-----------------------+-------------------------------+--------------------------------------------------------------+
| uuid                  |                               | uuid of the object                                           |
|                       |                               |                                                              |
|                       |                               |                                                              |
+-----------------------+-------------------------------+--------------------------------------------------------------+







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

