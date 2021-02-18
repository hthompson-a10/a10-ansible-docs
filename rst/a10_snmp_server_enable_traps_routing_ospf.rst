.. _a10_snmp_server_enable_traps_routing_ospf_module:


a10_snmp_server_enable_traps_routing_ospf -- Configures A10 snmp.server.enable.traps.routing.ospf
=================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Enable OSPFv2 traps






Parameters
----------

+-----------------------------+-------------------------------+-------------------------------------------------+
| Parameters                  | Choices/Defaults              | Comment                                         |
|                             |                               |                                                 |
|                             |                               |                                                 |
+=============================+===============================+=================================================+
| state                       | ['noop', 'present', 'absent'] | State of the object to be created.              |
|                             |                               |                                                 |
| /required                   |                               |                                                 |
+-----------------------------+-------------------------------+-------------------------------------------------+
| ansible_host                |                               | Host for AXAPI authentication                   |
|                             |                               |                                                 |
| /required                   |                               |                                                 |
+-----------------------------+-------------------------------+-------------------------------------------------+
| ansible_username            |                               | Username for AXAPI authentication               |
|                             |                               |                                                 |
| /required                   |                               |                                                 |
+-----------------------------+-------------------------------+-------------------------------------------------+
| ansible_password            |                               | Password for AXAPI authentication               |
|                             |                               |                                                 |
| /required                   |                               |                                                 |
+-----------------------------+-------------------------------+-------------------------------------------------+
| ansible_port                |                               | Port for AXAPI authentication                   |
|                             |                               |                                                 |
| /required                   |                               |                                                 |
+-----------------------------+-------------------------------+-------------------------------------------------+
| a10_device_context_id       | ['1-8']                       | Device ID for aVCS configuration                |
|                             |                               |                                                 |
|                             |                               |                                                 |
+-----------------------------+-------------------------------+-------------------------------------------------+
| a10_partition               |                               | Destination/target partition for object/command |
|                             |                               |                                                 |
|                             |                               |                                                 |
+-----------------------------+-------------------------------+-------------------------------------------------+
| ospfIfAuthFailure           |                               | Enable ospfIfAuthFailure traps                  |
|                             |                               |                                                 |
|                             |                               |                                                 |
+-----------------------------+-------------------------------+-------------------------------------------------+
| ospfIfConfigError           |                               | Enable ospfIfConfigError traps                  |
|                             |                               |                                                 |
|                             |                               |                                                 |
+-----------------------------+-------------------------------+-------------------------------------------------+
| ospfIfRxBadPacket           |                               | Enable ospfIfRxBadPacket traps                  |
|                             |                               |                                                 |
|                             |                               |                                                 |
+-----------------------------+-------------------------------+-------------------------------------------------+
| ospfIfStateChange           |                               | Enable ospfIfStateChange traps                  |
|                             |                               |                                                 |
|                             |                               |                                                 |
+-----------------------------+-------------------------------+-------------------------------------------------+
| ospfLsdbApproachingOverflow |                               | Enable ospfLsdbApproachingOverflow traps        |
|                             |                               |                                                 |
|                             |                               |                                                 |
+-----------------------------+-------------------------------+-------------------------------------------------+
| ospfLsdbOverflow            |                               | Enable ospfLsdbOverflow traps                   |
|                             |                               |                                                 |
|                             |                               |                                                 |
+-----------------------------+-------------------------------+-------------------------------------------------+
| ospfMaxAgeLsa               |                               | Enable ospfMaxAgeLsa traps                      |
|                             |                               |                                                 |
|                             |                               |                                                 |
+-----------------------------+-------------------------------+-------------------------------------------------+
| ospfNbrStateChange          |                               | Enable ospfNbrStateChange traps                 |
|                             |                               |                                                 |
|                             |                               |                                                 |
+-----------------------------+-------------------------------+-------------------------------------------------+
| ospfOriginateLsa            |                               | Enable ospfOriginateLsa traps                   |
|                             |                               |                                                 |
|                             |                               |                                                 |
+-----------------------------+-------------------------------+-------------------------------------------------+
| ospfTxRetransmit            |                               | Enable ospfTxRetransmit traps                   |
|                             |                               |                                                 |
|                             |                               |                                                 |
+-----------------------------+-------------------------------+-------------------------------------------------+
| ospfVirtIfAuthFailure       |                               | Enable ospfVirtIfAuthFailure traps              |
|                             |                               |                                                 |
|                             |                               |                                                 |
+-----------------------------+-------------------------------+-------------------------------------------------+
| ospfVirtIfConfigError       |                               | Enable ospfVirtIfConfigError traps              |
|                             |                               |                                                 |
|                             |                               |                                                 |
+-----------------------------+-------------------------------+-------------------------------------------------+
| ospfVirtIfRxBadPacket       |                               | Enable ospfVirtIfRxBadPacket traps              |
|                             |                               |                                                 |
|                             |                               |                                                 |
+-----------------------------+-------------------------------+-------------------------------------------------+
| ospfVirtIfStateChange       |                               | Enable ospfVirtIfStateChange traps              |
|                             |                               |                                                 |
|                             |                               |                                                 |
+-----------------------------+-------------------------------+-------------------------------------------------+
| ospfVirtIfTxRetransmit      |                               | Enable ospfVirtIfTxRetransmit traps             |
|                             |                               |                                                 |
|                             |                               |                                                 |
+-----------------------------+-------------------------------+-------------------------------------------------+
| ospfVirtNbrStateChange      |                               | Enable ospfVirtNbrStateChange traps             |
|                             |                               |                                                 |
|                             |                               |                                                 |
+-----------------------------+-------------------------------+-------------------------------------------------+
| uuid                        |                               | uuid of the object                              |
|                             |                               |                                                 |
|                             |                               |                                                 |
+-----------------------------+-------------------------------+-------------------------------------------------+







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

