.. _a10_import_periodic_ssl_cert_module:


a10_import_periodic_ssl_cert -- Configures A10 import-periodic.ssl-cert
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

SSL Cert File(enter bulk when import an archive file)






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
| ssl_cert              |                               | SSL Cert File(enter bulk when import an archive file) |
|                       |                               |                                                       |
| /required             |                               |                                                       |
+-----------------------+-------------------------------+-------------------------------------------------------+
| certificate_type      |                               | 'pem'= pem; 'der'= der; 'pfx'= pfx; 'p7b'= p7b;       |
|                       |                               |                                                       |
|                       |                               |                                                       |
+-----------------------+-------------------------------+-------------------------------------------------------+
| pfx_password          |                               | The password for certificate file (pfx type only)     |
|                       |                               |                                                       |
|                       |                               |                                                       |
+-----------------------+-------------------------------+-------------------------------------------------------+
| use_mgmt_port         |                               | Use management port as source port                    |
|                       |                               |                                                       |
|                       |                               |                                                       |
+-----------------------+-------------------------------+-------------------------------------------------------+
| remote_file           |                               | profile name for remote url                           |
|                       |                               |                                                       |
|                       |                               |                                                       |
+-----------------------+-------------------------------+-------------------------------------------------------+
| period                |                               | Specify the period in second                          |
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

