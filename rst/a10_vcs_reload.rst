.. _a10_vcs_reload_module:


a10_vcs_reload -- Configures A10 vcs.reload
===========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

VCS reload






Parameters
----------

+-----------------------+---------------------+---------------------------------------------------------+
| Parameters            | Choices/Defaults    | Comment                                                 |
|                       |                     |                                                         |
|                       |                     |                                                         |
+=======================+=====================+=========================================================+
| state                 | ['noop', 'present'] | State of the object to be created.                      |
|                       |                     |                                                         |
| /required             |                     |                                                         |
+-----------------------+---------------------+---------------------------------------------------------+
| ansible_host          |                     | Host for AXAPI authentication                           |
|                       |                     |                                                         |
| /required             |                     |                                                         |
+-----------------------+---------------------+---------------------------------------------------------+
| ansible_username      |                     | Username for AXAPI authentication                       |
|                       |                     |                                                         |
| /required             |                     |                                                         |
+-----------------------+---------------------+---------------------------------------------------------+
| ansible_password      |                     | Password for AXAPI authentication                       |
|                       |                     |                                                         |
| /required             |                     |                                                         |
+-----------------------+---------------------+---------------------------------------------------------+
| ansible_port          |                     | Port for AXAPI authentication                           |
|                       |                     |                                                         |
| /required             |                     |                                                         |
+-----------------------+---------------------+---------------------------------------------------------+
| a10_device_context_id | ['1-8']             | Device ID for aVCS configuration                        |
|                       |                     |                                                         |
|                       |                     |                                                         |
+-----------------------+---------------------+---------------------------------------------------------+
| a10_partition         |                     | Destination/target partition for object/command         |
|                       |                     |                                                         |
|                       |                     |                                                         |
+-----------------------+---------------------+---------------------------------------------------------+
| disable_merge         |                     | don't merge this vBlade's configuration to aVCS chassis |
|                       |                     |                                                         |
|                       |                     |                                                         |
+-----------------------+---------------------+---------------------------------------------------------+







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

