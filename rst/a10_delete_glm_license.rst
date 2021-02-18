.. _a10_delete_glm_license_module:


a10_delete_glm_license -- Configures A10 delete.glm-license
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Remove glm license






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
| cylance               |                               | only remove Cylance license                     |
|                       |                               |                                                 |
|                       |                               |                                                 |
+-----------------------+-------------------------------+-------------------------------------------------+
| threatstop            |                               | only remove ThreatSTOP license                  |
|                       |                               |                                                 |
|                       |                               |                                                 |
+-----------------------+-------------------------------+-------------------------------------------------+
| qosmos                |                               | only remove QOSMOS license                      |
|                       |                               |                                                 |
|                       |                               |                                                 |
+-----------------------+-------------------------------+-------------------------------------------------+
| webroot_ti            |                               | only remove Webroot Threat Intel license        |
|                       |                               |                                                 |
|                       |                               |                                                 |
+-----------------------+-------------------------------+-------------------------------------------------+
| ipsec_vpn             |                               | only remove IPSEC VPN license                   |
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

