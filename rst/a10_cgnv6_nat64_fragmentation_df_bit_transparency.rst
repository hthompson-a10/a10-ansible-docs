.. _a10_cgnv6_nat64_fragmentation_df_bit_transparency_module:


a10_cgnv6_nat64_fragmentation_df_bit_transparency -- Configures A10 cgnv6.nat64.fragmentation.df-bit-transparency
=================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Add an empty IPv6 fragmentation header if IPv4 DF bit is zero (default=disabled)






Parameters
----------

+-----------------------+-------------------------------+--------------------------------------------------------------------------+
| Parameters            | Choices/Defaults              | Comment                                                                  |
|                       |                               |                                                                          |
|                       |                               |                                                                          |
+=======================+===============================+==========================================================================+
| state                 | ['noop', 'present', 'absent'] | State of the object to be created.                                       |
|                       |                               |                                                                          |
| /required             |                               |                                                                          |
+-----------------------+-------------------------------+--------------------------------------------------------------------------+
| ansible_host          |                               | Host for AXAPI authentication                                            |
|                       |                               |                                                                          |
| /required             |                               |                                                                          |
+-----------------------+-------------------------------+--------------------------------------------------------------------------+
| ansible_username      |                               | Username for AXAPI authentication                                        |
|                       |                               |                                                                          |
| /required             |                               |                                                                          |
+-----------------------+-------------------------------+--------------------------------------------------------------------------+
| ansible_password      |                               | Password for AXAPI authentication                                        |
|                       |                               |                                                                          |
| /required             |                               |                                                                          |
+-----------------------+-------------------------------+--------------------------------------------------------------------------+
| ansible_port          |                               | Port for AXAPI authentication                                            |
|                       |                               |                                                                          |
| /required             |                               |                                                                          |
+-----------------------+-------------------------------+--------------------------------------------------------------------------+
| a10_device_context_id | ['1-8']                       | Device ID for aVCS configuration                                         |
|                       |                               |                                                                          |
|                       |                               |                                                                          |
+-----------------------+-------------------------------+--------------------------------------------------------------------------+
| a10_partition         |                               | Destination/target partition for object/command                          |
|                       |                               |                                                                          |
|                       |                               |                                                                          |
+-----------------------+-------------------------------+--------------------------------------------------------------------------+
| df_bit_value          |                               | 'enable'= Add an empty IPv6 fragmentation header if IPv4 DF bit is zero; |
|                       |                               |                                                                          |
|                       |                               |                                                                          |
+-----------------------+-------------------------------+--------------------------------------------------------------------------+
| uuid                  |                               | uuid of the object                                                       |
|                       |                               |                                                                          |
|                       |                               |                                                                          |
+-----------------------+-------------------------------+--------------------------------------------------------------------------+







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

