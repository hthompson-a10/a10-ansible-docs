.. _a10_sys_ut_run_suite_module:


a10_sys_ut_run_suite -- Configures A10 sys.ut.run-suite
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Generate test cases and run them






Parameters
----------

+-----------------------+---------------------+-------------------------------------------------+
| Parameters            | Choices/Defaults    | Comment                                         |
|                       |                     |                                                 |
|                       |                     |                                                 |
+=======================+=====================+=================================================+
| state                 | ['noop', 'present'] | State of the object to be created.              |
|                       |                     |                                                 |
| /required             |                     |                                                 |
+-----------------------+---------------------+-------------------------------------------------+
| ansible_host          |                     | Host for AXAPI authentication                   |
|                       |                     |                                                 |
| /required             |                     |                                                 |
+-----------------------+---------------------+-------------------------------------------------+
| ansible_username      |                     | Username for AXAPI authentication               |
|                       |                     |                                                 |
| /required             |                     |                                                 |
+-----------------------+---------------------+-------------------------------------------------+
| ansible_password      |                     | Password for AXAPI authentication               |
|                       |                     |                                                 |
| /required             |                     |                                                 |
+-----------------------+---------------------+-------------------------------------------------+
| ansible_port          |                     | Port for AXAPI authentication                   |
|                       |                     |                                                 |
| /required             |                     |                                                 |
+-----------------------+---------------------+-------------------------------------------------+
| a10_device_context_id | ['1-8']             | Device ID for aVCS configuration                |
|                       |                     |                                                 |
|                       |                     |                                                 |
+-----------------------+---------------------+-------------------------------------------------+
| a10_partition         |                     | Destination/target partition for object/command |
|                       |                     |                                                 |
|                       |                     |                                                 |
+-----------------------+---------------------+-------------------------------------------------+







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

