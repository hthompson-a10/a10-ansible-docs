.. _a10_interface_ve_ip_stateful_firewall_module:


a10_interface_ve_ip_stateful_firewall -- Configures A10 interface.ve.ip.stateful-firewall
=========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure Stateful Firewall direction






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
| ve_ifnum              |                               | Key to identify parent object                    |
|                       |                               |                                                  |
|                       |                               |                                                  |
+-----------------------+-------------------------------+--------------------------------------------------+
| inside                |                               | Inside (private) interface for stateful firewall |
|                       |                               |                                                  |
|                       |                               |                                                  |
+-----------------------+-------------------------------+--------------------------------------------------+
| class_list            |                               | Class List (Class List Name)                     |
|                       |                               |                                                  |
|                       |                               |                                                  |
+-----------------------+-------------------------------+--------------------------------------------------+
| outside               |                               | Outside (public) interface for stateful firewall |
|                       |                               |                                                  |
|                       |                               |                                                  |
+-----------------------+-------------------------------+--------------------------------------------------+
| access_list           |                               | Access-list for traffic from the outside         |
|                       |                               |                                                  |
|                       |                               |                                                  |
+-----------------------+-------------------------------+--------------------------------------------------+
| acl_id                |                               | ACL id                                           |
|                       |                               |                                                  |
|                       |                               |                                                  |
+-----------------------+-------------------------------+--------------------------------------------------+
| uuid                  |                               | uuid of the object                               |
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

