.. _a10_gslb_policy_geo_location_match_module:


a10_gslb_policy_geo_location_match -- Configures A10 gslb.policy.geo-location-match
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Specify match order of geographic






Parameters
----------

+-----------------------+-------------------------------+---------------------------------------------------------------+
| Parameters            | Choices/Defaults              | Comment                                                       |
|                       |                               |                                                               |
|                       |                               |                                                               |
+=======================+===============================+===============================================================+
| state                 | ['noop', 'present', 'absent'] | State of the object to be created.                            |
|                       |                               |                                                               |
| /required             |                               |                                                               |
+-----------------------+-------------------------------+---------------------------------------------------------------+
| ansible_host          |                               | Host for AXAPI authentication                                 |
|                       |                               |                                                               |
| /required             |                               |                                                               |
+-----------------------+-------------------------------+---------------------------------------------------------------+
| ansible_username      |                               | Username for AXAPI authentication                             |
|                       |                               |                                                               |
| /required             |                               |                                                               |
+-----------------------+-------------------------------+---------------------------------------------------------------+
| ansible_password      |                               | Password for AXAPI authentication                             |
|                       |                               |                                                               |
| /required             |                               |                                                               |
+-----------------------+-------------------------------+---------------------------------------------------------------+
| ansible_port          |                               | Port for AXAPI authentication                                 |
|                       |                               |                                                               |
| /required             |                               |                                                               |
+-----------------------+-------------------------------+---------------------------------------------------------------+
| a10_device_context_id | ['1-8']                       | Device ID for aVCS configuration                              |
|                       |                               |                                                               |
|                       |                               |                                                               |
+-----------------------+-------------------------------+---------------------------------------------------------------+
| a10_partition         |                               | Destination/target partition for object/command               |
|                       |                               |                                                               |
|                       |                               |                                                               |
+-----------------------+-------------------------------+---------------------------------------------------------------+
| policy_name           |                               | Key to identify parent object                                 |
|                       |                               |                                                               |
|                       |                               |                                                               |
+-----------------------+-------------------------------+---------------------------------------------------------------+
| overlap               |                               | Enable overlap mode to do longest match                       |
|                       |                               |                                                               |
|                       |                               |                                                               |
+-----------------------+-------------------------------+---------------------------------------------------------------+
| geo_type_overlap      |                               | 'global'= Global Geo-location; 'policy'= Policy Geo-location; |
|                       |                               |                                                               |
|                       |                               |                                                               |
+-----------------------+-------------------------------+---------------------------------------------------------------+
| match_first           |                               | 'global'= Global Geo-location; 'policy'= Policy Geo-location; |
|                       |                               |                                                               |
|                       |                               |                                                               |
+-----------------------+-------------------------------+---------------------------------------------------------------+
| uuid                  |                               | uuid of the object                                            |
|                       |                               |                                                               |
|                       |                               |                                                               |
+-----------------------+-------------------------------+---------------------------------------------------------------+







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

