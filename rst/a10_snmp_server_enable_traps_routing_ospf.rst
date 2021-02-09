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

  ospfLsdbOverflow (False, any, None)
    Enable ospfLsdbOverflow traps


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ospfVirtIfAuthFailure (False, any, None)
    Enable ospfVirtIfAuthFailure traps


  ospfVirtIfRxBadPacket (False, any, None)
    Enable ospfVirtIfRxBadPacket traps


  ospfTxRetransmit (False, any, None)
    Enable ospfTxRetransmit traps


  ospfIfAuthFailure (False, any, None)
    Enable ospfIfAuthFailure traps


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ospfOriginateLsa (False, any, None)
    Enable ospfOriginateLsa traps


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ospfNbrStateChange (False, any, None)
    Enable ospfNbrStateChange traps


  ospfVirtIfTxRetransmit (False, any, None)
    Enable ospfVirtIfTxRetransmit traps


  ospfVirtNbrStateChange (False, any, None)
    Enable ospfVirtNbrStateChange traps


  ospfIfConfigError (False, any, None)
    Enable ospfIfConfigError traps


  ospfVirtIfStateChange (False, any, None)
    Enable ospfVirtIfStateChange traps


  ospfVirtIfConfigError (False, any, None)
    Enable ospfVirtIfConfigError traps


  state (True, any, None)
    State of the object to be created.


  ospfIfStateChange (False, any, None)
    Enable ospfIfStateChange traps


  ospfMaxAgeLsa (False, any, None)
    Enable ospfMaxAgeLsa traps


  ospfIfRxBadPacket (False, any, None)
    Enable ospfIfRxBadPacket traps


  ospfLsdbApproachingOverflow (False, any, None)
    Enable ospfLsdbApproachingOverflow traps


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

