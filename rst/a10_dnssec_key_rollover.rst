.. _a10_dnssec_key_rollover_module:


a10_dnssec_key_rollover -- Configures A10 dnssec.key-rollover
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

DNSSEC Key rollover






Parameters
----------

+-------------------------+-------------------------------+--------------------------------------------------+
| Parameters              | Choices/Defaults              | Comment                                          |
|                         |                               |                                                  |
|                         |                               |                                                  |
+=========================+===============================+==================================================+
| state                   | ['noop', 'present', 'absent'] | State of the object to be created.               |
|                         |                               |                                                  |
| /required               |                               |                                                  |
+-------------------------+-------------------------------+--------------------------------------------------+
| ansible_host            |                               | Host for AXAPI authentication                    |
|                         |                               |                                                  |
| /required               |                               |                                                  |
+-------------------------+-------------------------------+--------------------------------------------------+
| ansible_username        |                               | Username for AXAPI authentication                |
|                         |                               |                                                  |
| /required               |                               |                                                  |
+-------------------------+-------------------------------+--------------------------------------------------+
| ansible_password        |                               | Password for AXAPI authentication                |
|                         |                               |                                                  |
| /required               |                               |                                                  |
+-------------------------+-------------------------------+--------------------------------------------------+
| ansible_port            |                               | Port for AXAPI authentication                    |
|                         |                               |                                                  |
| /required               |                               |                                                  |
+-------------------------+-------------------------------+--------------------------------------------------+
| a10_device_context_id   | ['1-8']                       | Device ID for aVCS configuration                 |
|                         |                               |                                                  |
|                         |                               |                                                  |
+-------------------------+-------------------------------+--------------------------------------------------+
| a10_partition           |                               | Destination/target partition for object/command  |
|                         |                               |                                                  |
|                         |                               |                                                  |
+-------------------------+-------------------------------+--------------------------------------------------+
| zone_name               |                               | Specify the name for the DNS zone                |
|                         |                               |                                                  |
|                         |                               |                                                  |
+-------------------------+-------------------------------+--------------------------------------------------+
| dnssec_key_type         |                               | 'ZSK'= Zone Signing Key; 'KSK'= Key Signing Key; |
|                         |                               |                                                  |
|                         |                               |                                                  |
+-------------------------+-------------------------------+--------------------------------------------------+
| zsk_start               |                               | start ZSK rollover in emergency mode             |
|                         |                               |                                                  |
|                         |                               |                                                  |
+-------------------------+-------------------------------+--------------------------------------------------+
| ksk_start               |                               | start KSK rollover in emergency mode             |
|                         |                               |                                                  |
|                         |                               |                                                  |
+-------------------------+-------------------------------+--------------------------------------------------+
| ds_ready_in_parent_zone |                               | DS RR is already ready in the parent zone        |
|                         |                               |                                                  |
|                         |                               |                                                  |
+-------------------------+-------------------------------+--------------------------------------------------+







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

