.. _a10_router_ipv6_ospf_default_information_module:


a10_router_ipv6_ospf_default_information -- Configures A10 router.ipv6.ospf.default-information
===============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Control distribution of default information






Parameters
----------

+-----------------------+-------------------------------+----------------------------------------------------+
| Parameters            | Choices/Defaults              | Comment                                            |
|                       |                               |                                                    |
|                       |                               |                                                    |
+=======================+===============================+====================================================+
| state                 | ['noop', 'present', 'absent'] | State of the object to be created.                 |
|                       |                               |                                                    |
| /required             |                               |                                                    |
+-----------------------+-------------------------------+----------------------------------------------------+
| ansible_host          |                               | Host for AXAPI authentication                      |
|                       |                               |                                                    |
| /required             |                               |                                                    |
+-----------------------+-------------------------------+----------------------------------------------------+
| ansible_username      |                               | Username for AXAPI authentication                  |
|                       |                               |                                                    |
| /required             |                               |                                                    |
+-----------------------+-------------------------------+----------------------------------------------------+
| ansible_password      |                               | Password for AXAPI authentication                  |
|                       |                               |                                                    |
| /required             |                               |                                                    |
+-----------------------+-------------------------------+----------------------------------------------------+
| ansible_port          |                               | Port for AXAPI authentication                      |
|                       |                               |                                                    |
| /required             |                               |                                                    |
+-----------------------+-------------------------------+----------------------------------------------------+
| a10_device_context_id | ['1-8']                       | Device ID for aVCS configuration                   |
|                       |                               |                                                    |
|                       |                               |                                                    |
+-----------------------+-------------------------------+----------------------------------------------------+
| a10_partition         |                               | Destination/target partition for object/command    |
|                       |                               |                                                    |
|                       |                               |                                                    |
+-----------------------+-------------------------------+----------------------------------------------------+
| ospf_process_id       |                               | Key to identify parent object                      |
|                       |                               |                                                    |
|                       |                               |                                                    |
+-----------------------+-------------------------------+----------------------------------------------------+
| originate             |                               | Distribute a default route                         |
|                       |                               |                                                    |
|                       |                               |                                                    |
+-----------------------+-------------------------------+----------------------------------------------------+
| always                |                               | Always advertise default route                     |
|                       |                               |                                                    |
|                       |                               |                                                    |
+-----------------------+-------------------------------+----------------------------------------------------+
| metric                |                               | OSPF default metric (OSPF metric)                  |
|                       |                               |                                                    |
|                       |                               |                                                    |
+-----------------------+-------------------------------+----------------------------------------------------+
| metric_type           |                               | OSPF metric type for default routes                |
|                       |                               |                                                    |
|                       |                               |                                                    |
+-----------------------+-------------------------------+----------------------------------------------------+
| route_map             |                               | Route map reference (Pointer to route-map entries) |
|                       |                               |                                                    |
|                       |                               |                                                    |
+-----------------------+-------------------------------+----------------------------------------------------+
| uuid                  |                               | uuid of the object                                 |
|                       |                               |                                                    |
|                       |                               |                                                    |
+-----------------------+-------------------------------+----------------------------------------------------+







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

