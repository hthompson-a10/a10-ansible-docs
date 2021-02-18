.. _a10_slb_ssl_sni_automap_attributes_module:


a10_slb_ssl_sni_automap_attributes -- Configures A10 slb.ssl.sni-automap-attributes
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Server Name Automap global settings






Parameters
----------

+-----------------------+-------------------------------+-------------------------------------------------------------+
| Parameters            | Choices/Defaults              | Comment                                                     |
|                       |                               |                                                             |
|                       |                               |                                                             |
+=======================+===============================+=============================================================+
| state                 | ['noop', 'present', 'absent'] | State of the object to be created.                          |
|                       |                               |                                                             |
| /required             |                               |                                                             |
+-----------------------+-------------------------------+-------------------------------------------------------------+
| ansible_host          |                               | Host for AXAPI authentication                               |
|                       |                               |                                                             |
| /required             |                               |                                                             |
+-----------------------+-------------------------------+-------------------------------------------------------------+
| ansible_username      |                               | Username for AXAPI authentication                           |
|                       |                               |                                                             |
| /required             |                               |                                                             |
+-----------------------+-------------------------------+-------------------------------------------------------------+
| ansible_password      |                               | Password for AXAPI authentication                           |
|                       |                               |                                                             |
| /required             |                               |                                                             |
+-----------------------+-------------------------------+-------------------------------------------------------------+
| ansible_port          |                               | Port for AXAPI authentication                               |
|                       |                               |                                                             |
| /required             |                               |                                                             |
+-----------------------+-------------------------------+-------------------------------------------------------------+
| a10_device_context_id | ['1-8']                       | Device ID for aVCS configuration                            |
|                       |                               |                                                             |
|                       |                               |                                                             |
+-----------------------+-------------------------------+-------------------------------------------------------------+
| a10_partition         |                               | Destination/target partition for object/command             |
|                       |                               |                                                             |
|                       |                               |                                                             |
+-----------------------+-------------------------------+-------------------------------------------------------------+
| sni_lower_limit       |                               | Lower limit for free SNI contexts count. Default is 500     |
|                       |                               |                                                             |
|                       |                               |                                                             |
+-----------------------+-------------------------------+-------------------------------------------------------------+
| sni_upper_limit       |                               | Upper limit for free SNI contexts count. Default is 2000    |
|                       |                               |                                                             |
|                       |                               |                                                             |
+-----------------------+-------------------------------+-------------------------------------------------------------+
| sni_delete_factor     |                               | Contexts are deleted in groups of this value. Default is 50 |
|                       |                               |                                                             |
|                       |                               |                                                             |
+-----------------------+-------------------------------+-------------------------------------------------------------+
| uuid                  |                               | uuid of the object                                          |
|                       |                               |                                                             |
|                       |                               |                                                             |
+-----------------------+-------------------------------+-------------------------------------------------------------+







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

