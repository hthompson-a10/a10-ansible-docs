.. _a10_scaleout_cluster_cluster_devices_minimum_nodes_module:


a10_scaleout_cluster_cluster_devices_minimum_nodes -- Configures A10 scaleout.cluster.cluster.devices.minimum-nodes
===================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Minimum number of nodes to start scaleout






Parameters
----------

+-----------------------+-------------------------------+------------------------------------------------------------------+
| Parameters            | Choices/Defaults              | Comment                                                          |
|                       |                               |                                                                  |
|                       |                               |                                                                  |
+=======================+===============================+==================================================================+
| state                 | ['noop', 'present', 'absent'] | State of the object to be created.                               |
|                       |                               |                                                                  |
| /required             |                               |                                                                  |
+-----------------------+-------------------------------+------------------------------------------------------------------+
| ansible_host          |                               | Host for AXAPI authentication                                    |
|                       |                               |                                                                  |
| /required             |                               |                                                                  |
+-----------------------+-------------------------------+------------------------------------------------------------------+
| ansible_username      |                               | Username for AXAPI authentication                                |
|                       |                               |                                                                  |
| /required             |                               |                                                                  |
+-----------------------+-------------------------------+------------------------------------------------------------------+
| ansible_password      |                               | Password for AXAPI authentication                                |
|                       |                               |                                                                  |
| /required             |                               |                                                                  |
+-----------------------+-------------------------------+------------------------------------------------------------------+
| ansible_port          |                               | Port for AXAPI authentication                                    |
|                       |                               |                                                                  |
| /required             |                               |                                                                  |
+-----------------------+-------------------------------+------------------------------------------------------------------+
| a10_device_context_id | ['1-8']                       | Device ID for aVCS configuration                                 |
|                       |                               |                                                                  |
|                       |                               |                                                                  |
+-----------------------+-------------------------------+------------------------------------------------------------------+
| a10_partition         |                               | Destination/target partition for object/command                  |
|                       |                               |                                                                  |
|                       |                               |                                                                  |
+-----------------------+-------------------------------+------------------------------------------------------------------+
| cluster_id            |                               | Key to identify parent object                                    |
|                       |                               |                                                                  |
|                       |                               |                                                                  |
+-----------------------+-------------------------------+------------------------------------------------------------------+
| minimum_nodes_num     |                               | Specify the minimum number of the node required to start service |
|                       |                               |                                                                  |
|                       |                               |                                                                  |
+-----------------------+-------------------------------+------------------------------------------------------------------+
| uuid                  |                               | uuid of the object                                               |
|                       |                               |                                                                  |
|                       |                               |                                                                  |
+-----------------------+-------------------------------+------------------------------------------------------------------+







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

