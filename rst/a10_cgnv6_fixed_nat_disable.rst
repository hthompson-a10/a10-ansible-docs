.. _a10_cgnv6_fixed_nat_disable_module:


a10_cgnv6_fixed_nat_disable -- Configures A10 cgnv6.fixed.nat.disable
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Disable fixed-nat configuration (Operation)






Parameters
----------

+------------------------+---------------------+-------------------------------------------------+
| Parameters             | Choices/Defaults    | Comment                                         |
|                        |                     |                                                 |
|                        |                     |                                                 |
+========================+=====================+=================================================+
| state                  | ['noop', 'present'] | State of the object to be created.              |
|                        |                     |                                                 |
| /required              |                     |                                                 |
+------------------------+---------------------+-------------------------------------------------+
| ansible_host           |                     | Host for AXAPI authentication                   |
|                        |                     |                                                 |
| /required              |                     |                                                 |
+------------------------+---------------------+-------------------------------------------------+
| ansible_username       |                     | Username for AXAPI authentication               |
|                        |                     |                                                 |
| /required              |                     |                                                 |
+------------------------+---------------------+-------------------------------------------------+
| ansible_password       |                     | Password for AXAPI authentication               |
|                        |                     |                                                 |
| /required              |                     |                                                 |
+------------------------+---------------------+-------------------------------------------------+
| ansible_port           |                     | Port for AXAPI authentication                   |
|                        |                     |                                                 |
| /required              |                     |                                                 |
+------------------------+---------------------+-------------------------------------------------+
| a10_device_context_id  | ['1-8']             | Device ID for aVCS configuration                |
|                        |                     |                                                 |
|                        |                     |                                                 |
+------------------------+---------------------+-------------------------------------------------+
| a10_partition          |                     | Destination/target partition for object/command |
|                        |                     |                                                 |
|                        |                     |                                                 |
+------------------------+---------------------+-------------------------------------------------+
| inside_start_v4address |                     | IPv4 Inside User Start Address                  |
|                        |                     |                                                 |
|                        |                     |                                                 |
+------------------------+---------------------+-------------------------------------------------+
| inside_end_v4address   |                     | IPv4 Inside User End Address                    |
|                        |                     |                                                 |
|                        |                     |                                                 |
+------------------------+---------------------+-------------------------------------------------+
| v4_netmask             |                     | IPv4 Netmask                                    |
|                        |                     |                                                 |
|                        |                     |                                                 |
+------------------------+---------------------+-------------------------------------------------+
| inside_start_v6address |                     | IPv6 Inside User Start Address                  |
|                        |                     |                                                 |
|                        |                     |                                                 |
+------------------------+---------------------+-------------------------------------------------+
| inside_end_v6address   |                     | IPv6 Inside User End Address                    |
|                        |                     |                                                 |
|                        |                     |                                                 |
+------------------------+---------------------+-------------------------------------------------+
| v6_netmask             |                     | Inside User IPv6 Netmask                        |
|                        |                     |                                                 |
|                        |                     |                                                 |
+------------------------+---------------------+-------------------------------------------------+
| ip_list                |                     | Name of IP List used to specify Inside Users    |
|                        |                     |                                                 |
|                        |                     |                                                 |
+------------------------+---------------------+-------------------------------------------------+
| partition              |                     | Inside User Partition (Partition Name)          |
|                        |                     |                                                 |
|                        |                     |                                                 |
+------------------------+---------------------+-------------------------------------------------+
| clear_session          |                     | Clear all sessions                              |
|                        |                     |                                                 |
|                        |                     |                                                 |
+------------------------+---------------------+-------------------------------------------------+







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

