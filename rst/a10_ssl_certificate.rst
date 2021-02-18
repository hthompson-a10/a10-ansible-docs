.. _a10_ssl_certificate_module:


a10_ssl_certificate -- Configures A10 ssl.certificate
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

ssl certificate file information and management commands






Parameters
----------

+-----------------------+-------------------------------+---------------------------------------------------+
| Parameters            | Choices/Defaults              | Comment                                           |
|                       |                               |                                                   |
|                       |                               |                                                   |
+=======================+===============================+===================================================+
| state                 | ['noop', 'present', 'absent'] | State of the object to be created.                |
|                       |                               |                                                   |
| /required             |                               |                                                   |
+-----------------------+-------------------------------+---------------------------------------------------+
| ansible_host          |                               | Host for AXAPI authentication                     |
|                       |                               |                                                   |
| /required             |                               |                                                   |
+-----------------------+-------------------------------+---------------------------------------------------+
| ansible_username      |                               | Username for AXAPI authentication                 |
|                       |                               |                                                   |
| /required             |                               |                                                   |
+-----------------------+-------------------------------+---------------------------------------------------+
| ansible_password      |                               | Password for AXAPI authentication                 |
|                       |                               |                                                   |
| /required             |                               |                                                   |
+-----------------------+-------------------------------+---------------------------------------------------+
| ansible_port          |                               | Port for AXAPI authentication                     |
|                       |                               |                                                   |
| /required             |                               |                                                   |
+-----------------------+-------------------------------+---------------------------------------------------+
| a10_device_context_id | ['1-8']                       | Device ID for aVCS configuration                  |
|                       |                               |                                                   |
|                       |                               |                                                   |
+-----------------------+-------------------------------+---------------------------------------------------+
| a10_partition         |                               | Destination/target partition for object/command   |
|                       |                               |                                                   |
|                       |                               |                                                   |
+-----------------------+-------------------------------+---------------------------------------------------+
| name                  |                               | ssl certificate local file name                   |
|                       |                               |                                                   |
| /required             |                               |                                                   |
+-----------------------+-------------------------------+---------------------------------------------------+
| public_key            |                               | Field public_key                                  |
|                       |                               |                                                   |
|                       |                               |                                                   |
+-----------------------+-------------------------------+---------------------------------------------------+
| certificate_type      |                               | 'pem'= pem; 'der'= der; 'pfx'= pfx; 'p7b'= p7b;   |
|                       |                               |                                                   |
|                       |                               |                                                   |
+-----------------------+-------------------------------+---------------------------------------------------+
| pfx_password          |                               | The password for certificate file (pfx type only) |
|                       |                               |                                                   |
|                       |                               |                                                   |
+-----------------------+-------------------------------+---------------------------------------------------+







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

