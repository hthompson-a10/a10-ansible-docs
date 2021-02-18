.. _a10_scaleout_apps_skip_mac_overwrite_module:


a10_scaleout_apps_skip_mac_overwrite -- Configures A10 scaleout.apps.skip-mac-overwrite
=======================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Skips overwriting dest MAC of flooded packets on Active node






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
| enable                |                               | Skips overwriting dest MAC of flooded packets on Active node |
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

