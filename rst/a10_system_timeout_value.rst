.. _a10_system_timeout_value_module:


a10_system_timeout_value -- Configures A10 system.timeout-value
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

set the timeout to stop transferring a file






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
| ftp                   |                               | set timeout to stop ftp transfer in seconds, 0 is no limit   |
|                       |                               |                                                              |
|                       |                               |                                                              |
+-----------------------+-------------------------------+--------------------------------------------------------------+
| scp                   |                               | set timeout to stop scp transfer in seconds, 0 is no limit   |
|                       |                               |                                                              |
|                       |                               |                                                              |
+-----------------------+-------------------------------+--------------------------------------------------------------+
| sftp                  |                               | set timeout to stop sftp transfer in seconds, 0 is no limit  |
|                       |                               |                                                              |
|                       |                               |                                                              |
+-----------------------+-------------------------------+--------------------------------------------------------------+
| tftp                  |                               | set timeout to stop tftp transfer in seconds, 0 is no limit  |
|                       |                               |                                                              |
|                       |                               |                                                              |
+-----------------------+-------------------------------+--------------------------------------------------------------+
| http                  |                               | set timeout to stop http transfer in seconds, 0 is no limit  |
|                       |                               |                                                              |
|                       |                               |                                                              |
+-----------------------+-------------------------------+--------------------------------------------------------------+
| https                 |                               | set timeout to stop https transfer in seconds, 0 is no limit |
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

