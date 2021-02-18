.. _a10_fw_gtp_in_gtp_filtering_module:


a10_fw_gtp_in_gtp_filtering -- Configures A10 fw.gtp-in-gtp-filtering
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure GTP in GTP filtering






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
| gtp_in_gtp_value      |                               | 'disable'= Disable GTP in GTP filtering, (default=Enabled); |
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

