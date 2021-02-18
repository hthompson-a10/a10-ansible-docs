.. _a10_import_health_external_module:


a10_import_health_external -- Configures A10 import.health-external
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Address the External Script Program






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
| externalfilename      |                               | Specify the Program Name                        |
|                       |                               |                                                 |
|                       |                               |                                                 |
+-----------------------+-------------------------------+-------------------------------------------------+
| description           |                               | Describe the Program Function briefly           |
|                       |                               |                                                 |
|                       |                               |                                                 |
+-----------------------+-------------------------------+-------------------------------------------------+
| overwrite             |                               | Overwrite existing file                         |
|                       |                               |                                                 |
|                       |                               |                                                 |
+-----------------------+-------------------------------+-------------------------------------------------+
| use_mgmt_port         |                               | Use management port as source port              |
|                       |                               |                                                 |
|                       |                               |                                                 |
+-----------------------+-------------------------------+-------------------------------------------------+
| remote_file           |                               | Field remote_file                               |
|                       |                               |                                                 |
|                       |                               |                                                 |
+-----------------------+-------------------------------+-------------------------------------------------+
| password              |                               | password for the remote site                    |
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

