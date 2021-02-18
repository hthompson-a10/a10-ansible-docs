.. _a10_acos_events_rate_limit_remote_module:


a10_acos_events_rate_limit_remote -- Configures A10 acos.events.rate-limit-remote
=================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure rate limit for logs sent to remote via classic logging config






Parameters
----------

+-----------------------+-------------------------------+-------------------------------------------------------------------------+
| Parameters            | Choices/Defaults              | Comment                                                                 |
|                       |                               |                                                                         |
|                       |                               |                                                                         |
+=======================+===============================+=========================================================================+
| state                 | ['noop', 'present', 'absent'] | State of the object to be created.                                      |
|                       |                               |                                                                         |
| /required             |                               |                                                                         |
+-----------------------+-------------------------------+-------------------------------------------------------------------------+
| ansible_host          |                               | Host for AXAPI authentication                                           |
|                       |                               |                                                                         |
| /required             |                               |                                                                         |
+-----------------------+-------------------------------+-------------------------------------------------------------------------+
| ansible_username      |                               | Username for AXAPI authentication                                       |
|                       |                               |                                                                         |
| /required             |                               |                                                                         |
+-----------------------+-------------------------------+-------------------------------------------------------------------------+
| ansible_password      |                               | Password for AXAPI authentication                                       |
|                       |                               |                                                                         |
| /required             |                               |                                                                         |
+-----------------------+-------------------------------+-------------------------------------------------------------------------+
| ansible_port          |                               | Port for AXAPI authentication                                           |
|                       |                               |                                                                         |
| /required             |                               |                                                                         |
+-----------------------+-------------------------------+-------------------------------------------------------------------------+
| a10_device_context_id | ['1-8']                       | Device ID for aVCS configuration                                        |
|                       |                               |                                                                         |
|                       |                               |                                                                         |
+-----------------------+-------------------------------+-------------------------------------------------------------------------+
| a10_partition         |                               | Destination/target partition for object/command                         |
|                       |                               |                                                                         |
|                       |                               |                                                                         |
+-----------------------+-------------------------------+-------------------------------------------------------------------------+
| limit                 |                               | Configure rate limit for logs sent to remote via classic logging config |
|                       |                               |                                                                         |
|                       |                               |                                                                         |
+-----------------------+-------------------------------+-------------------------------------------------------------------------+
| uuid                  |                               | uuid of the object                                                      |
|                       |                               |                                                                         |
|                       |                               |                                                                         |
+-----------------------+-------------------------------+-------------------------------------------------------------------------+







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

