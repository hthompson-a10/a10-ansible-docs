.. _a10_cgnv6_stateful_firewall_vrid_module:


a10_cgnv6_stateful_firewall_vrid -- Configures A10 cgnv6.stateful.firewall.vrid
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Set VRRP-A vrid for stateful firewall






Parameters
----------

+-----------------------+-------------------------------+-------------------------------------------------------+
| Parameters            | Choices/Defaults              | Comment                                               |
|                       |                               |                                                       |
|                       |                               |                                                       |
+=======================+===============================+=======================================================+
| state                 | ['noop', 'present', 'absent'] | State of the object to be created.                    |
|                       |                               |                                                       |
| /required             |                               |                                                       |
+-----------------------+-------------------------------+-------------------------------------------------------+
| ansible_host          |                               | Host for AXAPI authentication                         |
|                       |                               |                                                       |
| /required             |                               |                                                       |
+-----------------------+-------------------------------+-------------------------------------------------------+
| ansible_username      |                               | Username for AXAPI authentication                     |
|                       |                               |                                                       |
| /required             |                               |                                                       |
+-----------------------+-------------------------------+-------------------------------------------------------+
| ansible_password      |                               | Password for AXAPI authentication                     |
|                       |                               |                                                       |
| /required             |                               |                                                       |
+-----------------------+-------------------------------+-------------------------------------------------------+
| ansible_port          |                               | Port for AXAPI authentication                         |
|                       |                               |                                                       |
| /required             |                               |                                                       |
+-----------------------+-------------------------------+-------------------------------------------------------+
| a10_device_context_id | ['1-8']                       | Device ID for aVCS configuration                      |
|                       |                               |                                                       |
|                       |                               |                                                       |
+-----------------------+-------------------------------+-------------------------------------------------------+
| a10_partition         |                               | Destination/target partition for object/command       |
|                       |                               |                                                       |
|                       |                               |                                                       |
+-----------------------+-------------------------------+-------------------------------------------------------+
| vrid_value            |                               | Set VRRP-A vrid for stateful firewall (IPv4 and IPv6) |
|                       |                               |                                                       |
|                       |                               |                                                       |
+-----------------------+-------------------------------+-------------------------------------------------------+
| uuid                  |                               | uuid of the object                                    |
|                       |                               |                                                       |
|                       |                               |                                                       |
+-----------------------+-------------------------------+-------------------------------------------------------+







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

