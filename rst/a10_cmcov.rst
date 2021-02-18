.. _a10_cmcov_module:


a10_cmcov -- Configures A10 cmcov
=================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

CM code coverage






Parameters
----------

+-----------------------+-------------------------------+--------------------------------------------------+
| Parameters            | Choices/Defaults              | Comment                                          |
|                       |                               |                                                  |
|                       |                               |                                                  |
+=======================+===============================+==================================================+
| state                 | ['noop', 'present', 'absent'] | State of the object to be created.               |
|                       |                               |                                                  |
| /required             |                               |                                                  |
+-----------------------+-------------------------------+--------------------------------------------------+
| ansible_host          |                               | Host for AXAPI authentication                    |
|                       |                               |                                                  |
| /required             |                               |                                                  |
+-----------------------+-------------------------------+--------------------------------------------------+
| ansible_username      |                               | Username for AXAPI authentication                |
|                       |                               |                                                  |
| /required             |                               |                                                  |
+-----------------------+-------------------------------+--------------------------------------------------+
| ansible_password      |                               | Password for AXAPI authentication                |
|                       |                               |                                                  |
| /required             |                               |                                                  |
+-----------------------+-------------------------------+--------------------------------------------------+
| ansible_port          |                               | Port for AXAPI authentication                    |
|                       |                               |                                                  |
| /required             |                               |                                                  |
+-----------------------+-------------------------------+--------------------------------------------------+
| a10_device_context_id | ['1-8']                       | Device ID for aVCS configuration                 |
|                       |                               |                                                  |
|                       |                               |                                                  |
+-----------------------+-------------------------------+--------------------------------------------------+
| a10_partition         |                               | Destination/target partition for object/command  |
|                       |                               |                                                  |
|                       |                               |                                                  |
+-----------------------+-------------------------------+--------------------------------------------------+
| dump                  |                               | Dump code coverage data and and generate report} |
|                       |                               |                                                  |
|                       |                               |                                                  |
+-----------------------+-------------------------------+--------------------------------------------------+
| export                |                               | Export code coverage report                      |
|                       |                               |                                                  |
|                       |                               |                                                  |
+-----------------------+-------------------------------+--------------------------------------------------+







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

