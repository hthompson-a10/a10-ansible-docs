.. _a10_ip_nat_translation_service_timeout_module:


a10_ip_nat_translation_service_timeout -- Configures A10 ip.nat.translation.service-timeout
===========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Specify any custom service timeout






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
| service_type          |                               | 'tcp'= TCP Protocol; 'udp'= UDP Protocol;       |
|                       |                               |                                                 |
| /required             |                               |                                                 |
+-----------------------+-------------------------------+-------------------------------------------------+
| port                  |                               | Port Number                                     |
|                       |                               |                                                 |
| /required             |                               |                                                 |
+-----------------------+-------------------------------+-------------------------------------------------+
| timeout_type          |                               | 'age'= Expiration time; 'fast'= Use Fast aging; |
|                       |                               |                                                 |
|                       |                               |                                                 |
+-----------------------+-------------------------------+-------------------------------------------------+
| timeout_val           |                               | Timeout in seconds (Interval of 60 seconds)     |
|                       |                               |                                                 |
|                       |                               |                                                 |
+-----------------------+-------------------------------+-------------------------------------------------+
| uuid                  |                               | uuid of the object                              |
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

