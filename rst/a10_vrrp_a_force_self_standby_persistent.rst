.. _a10_vrrp_a_force_self_standby_persistent_module:


a10_vrrp_a_force_self_standby_persistent -- Configures A10 vrrp-a.force-self-standby-persistent
===============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

HA VRRP-A Configured  Command to force the unit or a group to HA standby state






Parameters
----------

+-----------------------+-------------------------------+-----------------------------------------------------+
| Parameters            | Choices/Defaults              | Comment                                             |
|                       |                               |                                                     |
|                       |                               |                                                     |
+=======================+===============================+=====================================================+
| state                 | ['noop', 'present', 'absent'] | State of the object to be created.                  |
|                       |                               |                                                     |
| /required             |                               |                                                     |
+-----------------------+-------------------------------+-----------------------------------------------------+
| ansible_host          |                               | Host for AXAPI authentication                       |
|                       |                               |                                                     |
| /required             |                               |                                                     |
+-----------------------+-------------------------------+-----------------------------------------------------+
| ansible_username      |                               | Username for AXAPI authentication                   |
|                       |                               |                                                     |
| /required             |                               |                                                     |
+-----------------------+-------------------------------+-----------------------------------------------------+
| ansible_password      |                               | Password for AXAPI authentication                   |
|                       |                               |                                                     |
| /required             |                               |                                                     |
+-----------------------+-------------------------------+-----------------------------------------------------+
| ansible_port          |                               | Port for AXAPI authentication                       |
|                       |                               |                                                     |
| /required             |                               |                                                     |
+-----------------------+-------------------------------+-----------------------------------------------------+
| a10_device_context_id | ['1-8']                       | Device ID for aVCS configuration                    |
|                       |                               |                                                     |
|                       |                               |                                                     |
+-----------------------+-------------------------------+-----------------------------------------------------+
| a10_partition         |                               | Destination/target partition for object/command     |
|                       |                               |                                                     |
|                       |                               |                                                     |
+-----------------------+-------------------------------+-----------------------------------------------------+
| vrid                  |                               | Specify one VRRP-A vrid to force into standby state |
|                       |                               |                                                     |
| /required             |                               |                                                     |
+-----------------------+-------------------------------+-----------------------------------------------------+
| uuid                  |                               | uuid of the object                                  |
|                       |                               |                                                     |
|                       |                               |                                                     |
+-----------------------+-------------------------------+-----------------------------------------------------+







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

