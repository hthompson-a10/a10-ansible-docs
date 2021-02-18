.. _a10_logging_configure_module:


a10_logging_configure -- Configures A10 logging.configure
=========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Set logging configuration






Parameters
----------

+-------------------------+-------------------------------+-------------------------------------------------+
| Parameters              | Choices/Defaults              | Comment                                         |
|                         |                               |                                                 |
|                         |                               |                                                 |
+=========================+===============================+=================================================+
| state                   | ['noop', 'present', 'absent'] | State of the object to be created.              |
|                         |                               |                                                 |
| /required               |                               |                                                 |
+-------------------------+-------------------------------+-------------------------------------------------+
| ansible_host            |                               | Host for AXAPI authentication                   |
|                         |                               |                                                 |
| /required               |                               |                                                 |
+-------------------------+-------------------------------+-------------------------------------------------+
| ansible_username        |                               | Username for AXAPI authentication               |
|                         |                               |                                                 |
| /required               |                               |                                                 |
+-------------------------+-------------------------------+-------------------------------------------------+
| ansible_password        |                               | Password for AXAPI authentication               |
|                         |                               |                                                 |
| /required               |                               |                                                 |
+-------------------------+-------------------------------+-------------------------------------------------+
| ansible_port            |                               | Port for AXAPI authentication                   |
|                         |                               |                                                 |
| /required               |                               |                                                 |
+-------------------------+-------------------------------+-------------------------------------------------+
| a10_device_context_id   | ['1-8']                       | Device ID for aVCS configuration                |
|                         |                               |                                                 |
|                         |                               |                                                 |
+-------------------------+-------------------------------+-------------------------------------------------+
| a10_partition           |                               | Destination/target partition for object/command |
|                         |                               |                                                 |
|                         |                               |                                                 |
+-------------------------+-------------------------------+-------------------------------------------------+
| line_feed_in_udp_syslog |                               | Add newline for syslog over UDP                 |
|                         |                               |                                                 |
|                         |                               |                                                 |
+-------------------------+-------------------------------+-------------------------------------------------+
| uuid                    |                               | uuid of the object                              |
|                         |                               |                                                 |
|                         |                               |                                                 |
+-------------------------+-------------------------------+-------------------------------------------------+







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

