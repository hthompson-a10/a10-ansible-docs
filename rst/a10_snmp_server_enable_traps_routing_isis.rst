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

  isisOwnLSPPurge (False, any, None)
    Enable isisOwnLSPPurge traps


  isisSequenceNumberSkip (False, any, None)
    Enable isisSequenceNumberSkip traps


  isisAdjacencyChange (False, any, None)
    Enable isisAdjacencyChange traps


  ansible_username (True, any, None)
    Username for AXAPI authentication


  isisAreaMismatch (False, any, None)
    Enable isisAreaMismatch traps


  isisAttemptToExceedMaxSequence (False, any, None)
    Enable isisAttemptToExceedMaxSequence traps


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  isisVersionSkew (False, any, None)
    Enable isisVersionSkew traps


  isisManualAddressDrops (False, any, None)
    Enable isisManualAddressDrops traps


  isisCorruptedLSPDetected (False, any, None)
    Enable isisCorruptedLSPDetected traps


  ansible_port (True, any, None)
    Port for AXAPI authentication


  isisAuthenticationFailure (False, any, None)
    Enable isisAuthenticationFailure traps


  uuid (False, any, None)
    uuid of the object


  isisProtocolsSupportedMismatch (False, any, None)
    Enable isisProtocolsSupportedMismatch traps


  isisRejectedAdjacency (False, any, None)
    Enable isisRejectedAdjacency traps


  isisMaxAreaAddressesMismatch (False, any, None)
    Enable isisMaxAreaAddressesMismatch traps


  isisOriginatingLSPBufferSizeMismatch (False, any, None)
    Enable isisOriginatingLSPBufferSizeMismatch traps


  ansible_host (True, any, None)
    Host for AXAPI authentication


  isisLSPTooLargeToPropagate (False, any, None)
    Enable isisLSPTooLargeToPropagate traps


  isisDatabaseOverload (False, any, None)
    Enable isisDatabaseOverload traps


  state (True, any, None)
    State of the object to be created.


  isisIDLenMismatch (False, any, None)
    Enable isisIDLenMismatch traps


  isisAuthenticationTypeFailure (False, any, None)
    Enable isisAuthenticationTypeFailure traps


  ansible_password (True, any, None)
    Password for AXAPI authentication









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

