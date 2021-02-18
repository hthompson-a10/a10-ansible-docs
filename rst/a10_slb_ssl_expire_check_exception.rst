.. _a10_slb_ssl_expire_check_exception_module:


a10_slb_ssl_expire_check_exception -- Configures A10 slb.ssl.expire.check.exception
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Config the exception which will not be checked






Parameters
----------

+-----------------------+---------------------+----------------------------------------------------------------------------------------+
| Parameters            | Choices/Defaults    | Comment                                                                                |
|                       |                     |                                                                                        |
|                       |                     |                                                                                        |
+=======================+=====================+========================================================================================+
| state                 | ['noop', 'present'] | State of the object to be created.                                                     |
|                       |                     |                                                                                        |
| /required             |                     |                                                                                        |
+-----------------------+---------------------+----------------------------------------------------------------------------------------+
| ansible_host          |                     | Host for AXAPI authentication                                                          |
|                       |                     |                                                                                        |
| /required             |                     |                                                                                        |
+-----------------------+---------------------+----------------------------------------------------------------------------------------+
| ansible_username      |                     | Username for AXAPI authentication                                                      |
|                       |                     |                                                                                        |
| /required             |                     |                                                                                        |
+-----------------------+---------------------+----------------------------------------------------------------------------------------+
| ansible_password      |                     | Password for AXAPI authentication                                                      |
|                       |                     |                                                                                        |
| /required             |                     |                                                                                        |
+-----------------------+---------------------+----------------------------------------------------------------------------------------+
| ansible_port          |                     | Port for AXAPI authentication                                                          |
|                       |                     |                                                                                        |
| /required             |                     |                                                                                        |
+-----------------------+---------------------+----------------------------------------------------------------------------------------+
| a10_device_context_id | ['1-8']             | Device ID for aVCS configuration                                                       |
|                       |                     |                                                                                        |
|                       |                     |                                                                                        |
+-----------------------+---------------------+----------------------------------------------------------------------------------------+
| a10_partition         |                     | Destination/target partition for object/command                                        |
|                       |                     |                                                                                        |
|                       |                     |                                                                                        |
+-----------------------+---------------------+----------------------------------------------------------------------------------------+
| action                |                     | 'add'= Add an exception; 'delete'= Delete an exception; 'clean'= Delete all exception; |
|                       |                     |                                                                                        |
|                       |                     |                                                                                        |
+-----------------------+---------------------+----------------------------------------------------------------------------------------+
| certificate_name      |                     | The certificate name                                                                   |
|                       |                     |                                                                                        |
|                       |                     |                                                                                        |
+-----------------------+---------------------+----------------------------------------------------------------------------------------+







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

