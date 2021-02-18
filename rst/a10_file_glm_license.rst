.. _a10_file_glm_license_module:


a10_file_glm_license -- Configures A10 file.glm-license
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

glm license file information and management commands






Parameters
----------

+-----------------------+-------------------------------+--------------------------------------------------+
| Parameters            | Choices/Defaults              | Comment                                          |
|                       |                               |                                                  |
|                       |                               |                                                  |
+=======================+===============================+==================================================+
| state                 | ['noop', 'present', 'absent'] | State of the object to be created.               |
|                       |                               |                                                  |
| /required             |                               |                                                  |
+-----------------------+-------------------------------+--------------------------------------------------+
| ansible_host          |                               | Host for AXAPI authentication                    |
|                       |                               |                                                  |
| /required             |                               |                                                  |
+-----------------------+-------------------------------+--------------------------------------------------+
| ansible_username      |                               | Username for AXAPI authentication                |
|                       |                               |                                                  |
| /required             |                               |                                                  |
+-----------------------+-------------------------------+--------------------------------------------------+
| ansible_password      |                               | Password for AXAPI authentication                |
|                       |                               |                                                  |
| /required             |                               |                                                  |
+-----------------------+-------------------------------+--------------------------------------------------+
| ansible_port          |                               | Port for AXAPI authentication                    |
|                       |                               |                                                  |
| /required             |                               |                                                  |
+-----------------------+-------------------------------+--------------------------------------------------+
| a10_device_context_id | ['1-8']                       | Device ID for aVCS configuration                 |
|                       |                               |                                                  |
|                       |                               |                                                  |
+-----------------------+-------------------------------+--------------------------------------------------+
| a10_partition         |                               | Destination/target partition for object/command  |
|                       |                               |                                                  |
|                       |                               |                                                  |
+-----------------------+-------------------------------+--------------------------------------------------+
| file_content          |                               | Content of the uploaded file                     |
|                       |                               |                                                  |
|                       |                               |                                                  |
+-----------------------+-------------------------------+--------------------------------------------------+
| device                |                               | Device (Device ID)                               |
|                       |                               |                                                  |
|                       |                               |                                                  |
+-----------------------+-------------------------------+--------------------------------------------------+
| file                  |                               | glm license local file name                      |
|                       |                               |                                                  |
|                       |                               |                                                  |
+-----------------------+-------------------------------+--------------------------------------------------+
| file_handle           |                               | full path of the uploaded file                   |
|                       |                               |                                                  |
|                       |                               |                                                  |
+-----------------------+-------------------------------+--------------------------------------------------+
| action                |                               | 'import'= import;                                |
|                       |                               |                                                  |
|                       |                               |                                                  |
+-----------------------+-------------------------------+--------------------------------------------------+
| dst_file              |                               | destination file name for copy and rename action |
|                       |                               |                                                  |
|                       |                               |                                                  |
+-----------------------+-------------------------------+--------------------------------------------------+







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

