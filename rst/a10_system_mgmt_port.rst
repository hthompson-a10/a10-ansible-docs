.. _a10_system_mgmt_port_module:


a10_system_mgmt_port -- Configures A10 system.mgmt-port
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

set management port






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
| port_index            |                               | port index to be configured (Specify port index) |
|                       |                               |                                                  |
|                       |                               |                                                  |
+-----------------------+-------------------------------+--------------------------------------------------+
| mac_address           |                               | mac-address to be configured as mgmt port        |
|                       |                               |                                                  |
|                       |                               |                                                  |
+-----------------------+-------------------------------+--------------------------------------------------+
| pci_address           |                               | pci-address to be configured as mgmt port        |
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

