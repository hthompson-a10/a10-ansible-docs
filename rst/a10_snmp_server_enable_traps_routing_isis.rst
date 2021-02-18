.. _a10_snmp_server_enable_traps_routing_isis_module:


a10_snmp_server_enable_traps_routing_isis -- Configures A10 snmp.server.enable.traps.routing.isis
=================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Enable isis traps






Parameters
----------

+--------------------------------------+-------------------------------+---------------------------------------------------+
| Parameters                           | Choices/Defaults              | Comment                                           |
|                                      |                               |                                                   |
|                                      |                               |                                                   |
+======================================+===============================+===================================================+
| state                                | ['noop', 'present', 'absent'] | State of the object to be created.                |
|                                      |                               |                                                   |
| /required                            |                               |                                                   |
+--------------------------------------+-------------------------------+---------------------------------------------------+
| ansible_host                         |                               | Host for AXAPI authentication                     |
|                                      |                               |                                                   |
| /required                            |                               |                                                   |
+--------------------------------------+-------------------------------+---------------------------------------------------+
| ansible_username                     |                               | Username for AXAPI authentication                 |
|                                      |                               |                                                   |
| /required                            |                               |                                                   |
+--------------------------------------+-------------------------------+---------------------------------------------------+
| ansible_password                     |                               | Password for AXAPI authentication                 |
|                                      |                               |                                                   |
| /required                            |                               |                                                   |
+--------------------------------------+-------------------------------+---------------------------------------------------+
| ansible_port                         |                               | Port for AXAPI authentication                     |
|                                      |                               |                                                   |
| /required                            |                               |                                                   |
+--------------------------------------+-------------------------------+---------------------------------------------------+
| a10_device_context_id                | ['1-8']                       | Device ID for aVCS configuration                  |
|                                      |                               |                                                   |
|                                      |                               |                                                   |
+--------------------------------------+-------------------------------+---------------------------------------------------+
| a10_partition                        |                               | Destination/target partition for object/command   |
|                                      |                               |                                                   |
|                                      |                               |                                                   |
+--------------------------------------+-------------------------------+---------------------------------------------------+
| isisAdjacencyChange                  |                               | Enable isisAdjacencyChange traps                  |
|                                      |                               |                                                   |
|                                      |                               |                                                   |
+--------------------------------------+-------------------------------+---------------------------------------------------+
| isisAreaMismatch                     |                               | Enable isisAreaMismatch traps                     |
|                                      |                               |                                                   |
|                                      |                               |                                                   |
+--------------------------------------+-------------------------------+---------------------------------------------------+
| isisAttemptToExceedMaxSequence       |                               | Enable isisAttemptToExceedMaxSequence traps       |
|                                      |                               |                                                   |
|                                      |                               |                                                   |
+--------------------------------------+-------------------------------+---------------------------------------------------+
| isisAuthenticationFailure            |                               | Enable isisAuthenticationFailure traps            |
|                                      |                               |                                                   |
|                                      |                               |                                                   |
+--------------------------------------+-------------------------------+---------------------------------------------------+
| isisAuthenticationTypeFailure        |                               | Enable isisAuthenticationTypeFailure traps        |
|                                      |                               |                                                   |
|                                      |                               |                                                   |
+--------------------------------------+-------------------------------+---------------------------------------------------+
| isisCorruptedLSPDetected             |                               | Enable isisCorruptedLSPDetected traps             |
|                                      |                               |                                                   |
|                                      |                               |                                                   |
+--------------------------------------+-------------------------------+---------------------------------------------------+
| isisDatabaseOverload                 |                               | Enable isisDatabaseOverload traps                 |
|                                      |                               |                                                   |
|                                      |                               |                                                   |
+--------------------------------------+-------------------------------+---------------------------------------------------+
| isisIDLenMismatch                    |                               | Enable isisIDLenMismatch traps                    |
|                                      |                               |                                                   |
|                                      |                               |                                                   |
+--------------------------------------+-------------------------------+---------------------------------------------------+
| isisLSPTooLargeToPropagate           |                               | Enable isisLSPTooLargeToPropagate traps           |
|                                      |                               |                                                   |
|                                      |                               |                                                   |
+--------------------------------------+-------------------------------+---------------------------------------------------+
| isisManualAddressDrops               |                               | Enable isisManualAddressDrops traps               |
|                                      |                               |                                                   |
|                                      |                               |                                                   |
+--------------------------------------+-------------------------------+---------------------------------------------------+
| isisMaxAreaAddressesMismatch         |                               | Enable isisMaxAreaAddressesMismatch traps         |
|                                      |                               |                                                   |
|                                      |                               |                                                   |
+--------------------------------------+-------------------------------+---------------------------------------------------+
| isisOriginatingLSPBufferSizeMismatch |                               | Enable isisOriginatingLSPBufferSizeMismatch traps |
|                                      |                               |                                                   |
|                                      |                               |                                                   |
+--------------------------------------+-------------------------------+---------------------------------------------------+
| isisOwnLSPPurge                      |                               | Enable isisOwnLSPPurge traps                      |
|                                      |                               |                                                   |
|                                      |                               |                                                   |
+--------------------------------------+-------------------------------+---------------------------------------------------+
| isisProtocolsSupportedMismatch       |                               | Enable isisProtocolsSupportedMismatch traps       |
|                                      |                               |                                                   |
|                                      |                               |                                                   |
+--------------------------------------+-------------------------------+---------------------------------------------------+
| isisRejectedAdjacency                |                               | Enable isisRejectedAdjacency traps                |
|                                      |                               |                                                   |
|                                      |                               |                                                   |
+--------------------------------------+-------------------------------+---------------------------------------------------+
| isisSequenceNumberSkip               |                               | Enable isisSequenceNumberSkip traps               |
|                                      |                               |                                                   |
|                                      |                               |                                                   |
+--------------------------------------+-------------------------------+---------------------------------------------------+
| isisVersionSkew                      |                               | Enable isisVersionSkew traps                      |
|                                      |                               |                                                   |
|                                      |                               |                                                   |
+--------------------------------------+-------------------------------+---------------------------------------------------+
| uuid                                 |                               | uuid of the object                                |
|                                      |                               |                                                   |
|                                      |                               |                                                   |
+--------------------------------------+-------------------------------+---------------------------------------------------+







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

