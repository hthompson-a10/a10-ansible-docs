.. _a10_scaleout_cluster_service_config_module:


a10_scaleout_cluster_service_config -- Configures A10 scaleout.cluster.service-config
=====================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure scaleout templates for SLB, CGN and VRRP






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
| cluster_id            |                     | Key to identify parent object                   |
|                       |                     |                                                 |
|                       |                     |                                                 |
+-----------------------+---------------------+-------------------------------------------------+
| uuid                  |                     | uuid of the object                              |
|                       |                     |                                                 |
|                       |                     |                                                 |
+-----------------------+---------------------+-------------------------------------------------+
| template_list         |                     | Field template_list                             |
|                       |                     |                                                 |
|                       |                     |                                                 |
+---+-------------------+---------------------+-------------------------------------------------+
|   | name              |                     | Scaleout template Name                          |
|   |                   |                     |                                                 |
|   |                   |                     |                                                 |
+---+-------------------+---------------------+-------------------------------------------------+
|   | bucket_count      |                     | Number of traffic buckets                       |
|   |                   |                     |                                                 |
|   |                   |                     |                                                 |
+---+-------------------+---------------------+-------------------------------------------------+
|   | device_group      |                     | Device group id                                 |
|   |                   |                     |                                                 |
|   |                   |                     |                                                 |
+---+-------------------+---------------------+-------------------------------------------------+
|   | uuid              |                     | uuid of the object                              |
|   |                   |                     |                                                 |
|   |                   |                     |                                                 |
+---+-------------------+---------------------+-------------------------------------------------+
|   | user_tag          |                     | Customized tag                                  |
|   |                   |                     |                                                 |
|   |                   |                     |                                                 |
+---+-------------------+---------------------+-------------------------------------------------+







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

