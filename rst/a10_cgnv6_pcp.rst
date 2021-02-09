.. _a10_cgnv6_pcp_module:


a10_cgnv6_pcp -- Configures A10 cgnv6.pcp
=========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Set Port Control Protocol parameters






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'packets-rcv'= Packets Received; 'lsn-map-process-success'= PCP MAP Request Processing Success (NAT44); 'dslite-map-process-success'= PCP MAP Request Processing Success (DS-Lite); 'nat64-map-process-success'= PCP MAP Request Processing Success (NAT64); 'lsn-peer-process-success'= PCP PEER Request Processing Success (NAT44); 'dslite-peer-process-success'= PCP PEER Request Processing Success (DS-Lite); 'nat64-peer-process-success'= PCP PEER Request Processing Success (NAT64); 'lsn-announce-process-success'= PCP ANNOUNCE Request Processing Success (NAT44); 'dslite-announce-process-success'= PCP ANNOUNCE Request Processing Success (DS-Lite); 'nat64-announce-process- success'= PCP ANNOUNCE Request Processing Success (NAT64); 'pkt-not-request- drop'= Packet Not a PCP Request; 'pkt-too-short-drop'= Packet Too Short; 'noroute-drop'= Response No Route; 'unsupported-version'= Unsupported PCP version; 'not-authorized'= PCP Request Not Authorized; 'malform-request'= PCP Request Malformed; 'unsupp-opcode'= Unsupported PCP Opcode; 'unsupp-option'= Unsupported PCP Option; 'malform-option'= PCP Option Malformed; 'no-resources'= No System or NAT Resources; 'unsupp-protocol'= Unsupported Mapping Protocol; 'user-quota-exceeded'= User Quota Exceeded; 'cannot-provide-suggest'= Cannot Provide Suggested Port When PREFER_FAILURE; 'address-mismatch'= PCP Client Address Mismatch; 'excessive-remote-peers'= Excessive Remote Peers; 'pkt-not- from-nat-inside'= Packet Dropped For Not Coming From NAT Inside; 'l4-process- error'= L3/L4 Process Error; 'internal-error-drop'= Internal Error; 'unsol_ance_sent_succ'= Unsolicited Announce Sent; 'unsol_ance_sent_fail'= Unsolicited Announce Send Failure; 'ha_sync_epoch_sent'= HA Sync PCP Epoch Sent; 'ha_sync_epoch_rcv'= HA Sync PCP Epoch Recv; 'fullcone-ext-alloc'= PCP Fullcone Extension Alloc; 'fullcone-ext-free'= PCP Fullcone Extension Free; 'fullcone-ext-alloc-failure'= PCP Fullcone Extension Alloc Failure; 'fullcone- ext-notfound'= PCP Fullcone Extension Not Found; 'fullcone-ext-reuse'= PCP Fullcone Extension Reuse; 'client-nonce-mismatch'= PCP Client Nonce Mismatch; 'map-filter-set'= PCP MAP Filter Set; 'map-filter-deny'= PCP MAP Filter Deny Inbound; 'inter-board-pkts'= PCP Inter board packets;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    unsol_ance_sent_fail (optional, any, None)
      Unsolicited Announce Send Failure


    address_mismatch (optional, any, None)
      PCP Client Address Mismatch


    unsupp_option (optional, any, None)
      Unsupported PCP Option


    unsupported_version (optional, any, None)
      Unsupported PCP version


    dslite_map_process_success (optional, any, None)
      PCP MAP Request Processing Success (DS-Lite)


    pkt_not_request_drop (optional, any, None)
      Packet Not a PCP Request


    user_quota_exceeded (optional, any, None)
      User Quota Exceeded


    pkt_too_short_drop (optional, any, None)
      Packet Too Short


    dslite_announce_process_success (optional, any, None)
      PCP ANNOUNCE Request Processing Success (DS-Lite)


    lsn_announce_process_success (optional, any, None)
      PCP ANNOUNCE Request Processing Success (NAT44)


    packets_rcv (optional, any, None)
      Packets Received


    ha_sync_epoch_sent (optional, any, None)
      HA Sync PCP Epoch Sent


    l4_process_error (optional, any, None)
      L3/L4 Process Error


    nat64_peer_process_success (optional, any, None)
      PCP PEER Request Processing Success (NAT64)


    internal_error_drop (optional, any, None)
      Internal Error


    malform_request (optional, any, None)
      PCP Request Malformed


    nat64_map_process_success (optional, any, None)
      PCP MAP Request Processing Success (NAT64)


    not_authorized (optional, any, None)
      PCP Request Not Authorized


    cannot_provide_suggest (optional, any, None)
      Cannot Provide Suggested Port When PREFER_FAILURE


    pkt_not_from_nat_inside (optional, any, None)
      Packet Dropped For Not Coming From NAT Inside


    lsn_peer_process_success (optional, any, None)
      PCP PEER Request Processing Success (NAT44)


    unsupp_opcode (optional, any, None)
      Unsupported PCP Opcode


    unsupp_protocol (optional, any, None)
      Unsupported Mapping Protocol


    ha_sync_epoch_rcv (optional, any, None)
      HA Sync PCP Epoch Recv


    unsol_ance_sent_succ (optional, any, None)
      Unsolicited Announce Sent


    noroute_drop (optional, any, None)
      Response No Route


    malform_option (optional, any, None)
      PCP Option Malformed


    no_resources (optional, any, None)
      No System or NAT Resources


    dslite_peer_process_success (optional, any, None)
      PCP PEER Request Processing Success (DS-Lite)


    excessive_remote_peers (optional, any, None)
      Excessive Remote Peers


    nat64_announce_process_success (optional, any, None)
      PCP ANNOUNCE Request Processing Success (NAT64)


    lsn_map_process_success (optional, any, None)
      PCP MAP Request Processing Success (NAT44)



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  default_template (False, any, None)
    Bind the default template for PCP (Bind a PCP template)


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication









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

