.. _a10_web_service_secure_generate_module:


a10_web_service_secure_generate -- Configures A10 web.service.secure.generate
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Web-service secure generate operation






Parameters
----------

+-----------------------+------------------+-------------------------------------------------+
| Parameters            | Choices/Defaults | Comment                                         |
|                       |                  |                                                 |
|                       |                  |                                                 |
+=======================+==================+=================================================+
| state                 |                  | The location                                    |
|                       |                  |                                                 |
|                       |                  |                                                 |
+-----------------------+------------------+-------------------------------------------------+
| ansible_host          |                  | Host for AXAPI authentication                   |
|                       |                  |                                                 |
| /required             |                  |                                                 |
+-----------------------+------------------+-------------------------------------------------+
| ansible_username      |                  | Username for AXAPI authentication               |
|                       |                  |                                                 |
| /required             |                  |                                                 |
+-----------------------+------------------+-------------------------------------------------+
| ansible_password      |                  | Password for AXAPI authentication               |
|                       |                  |                                                 |
| /required             |                  |                                                 |
+-----------------------+------------------+-------------------------------------------------+
| ansible_port          |                  | Port for AXAPI authentication                   |
|                       |                  |                                                 |
| /required             |                  |                                                 |
+-----------------------+------------------+-------------------------------------------------+
| a10_device_context_id | ['1-8']          | Device ID for aVCS configuration                |
|                       |                  |                                                 |
|                       |                  |                                                 |
+-----------------------+------------------+-------------------------------------------------+
| a10_partition         |                  | Destination/target partition for object/command |
|                       |                  |                                                 |
|                       |                  |                                                 |
+-----------------------+------------------+-------------------------------------------------+
| domain_name           |                  | The domain name                                 |
|                       |                  |                                                 |
|                       |                  |                                                 |
+-----------------------+------------------+-------------------------------------------------+
| country               |                  | The country name                                |
|                       |                  |                                                 |
|                       |                  |                                                 |
+-----------------------+------------------+-------------------------------------------------+







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

