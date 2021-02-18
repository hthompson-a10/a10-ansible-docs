.. _a10_license_manager_host_module:


a10_license_manager_host -- Configures A10 license-manager.host
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure license manager host






Parameters
----------

+-----------------------+-------------------------------+----------------------------------------------------+
| Parameters            | Choices/Defaults              | Comment                                            |
|                       |                               |                                                    |
|                       |                               |                                                    |
+=======================+===============================+====================================================+
| state                 | ['noop', 'present', 'absent'] | State of the object to be created.                 |
|                       |                               |                                                    |
| /required             |                               |                                                    |
+-----------------------+-------------------------------+----------------------------------------------------+
| ansible_host          |                               | Host for AXAPI authentication                      |
|                       |                               |                                                    |
| /required             |                               |                                                    |
+-----------------------+-------------------------------+----------------------------------------------------+
| ansible_username      |                               | Username for AXAPI authentication                  |
|                       |                               |                                                    |
| /required             |                               |                                                    |
+-----------------------+-------------------------------+----------------------------------------------------+
| ansible_password      |                               | Password for AXAPI authentication                  |
|                       |                               |                                                    |
| /required             |                               |                                                    |
+-----------------------+-------------------------------+----------------------------------------------------+
| ansible_port          |                               | Port for AXAPI authentication                      |
|                       |                               |                                                    |
| /required             |                               |                                                    |
+-----------------------+-------------------------------+----------------------------------------------------+
| a10_device_context_id | ['1-8']                       | Device ID for aVCS configuration                   |
|                       |                               |                                                    |
|                       |                               |                                                    |
+-----------------------+-------------------------------+----------------------------------------------------+
| a10_partition         |                               | Destination/target partition for object/command    |
|                       |                               |                                                    |
|                       |                               |                                                    |
+-----------------------+-------------------------------+----------------------------------------------------+
| host_ipv4             |                               | license server ip address (length=1-31)            |
|                       |                               |                                                    |
| /required             |                               |                                                    |
+-----------------------+-------------------------------+----------------------------------------------------+
| host_ipv6             |                               | Configure license manager server ipv6-address      |
|                       |                               |                                                    |
| /required             |                               |                                                    |
+-----------------------+-------------------------------+----------------------------------------------------+
| port                  |                               | Configure the license manager port, default is 443 |
|                       |                               |                                                    |
|                       |                               |                                                    |
+-----------------------+-------------------------------+----------------------------------------------------+
| uuid                  |                               | uuid of the object                                 |
|                       |                               |                                                    |
|                       |                               |                                                    |
+-----------------------+-------------------------------+----------------------------------------------------+







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

