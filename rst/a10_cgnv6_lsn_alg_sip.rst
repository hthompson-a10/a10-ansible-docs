.. _a10_cgnv6_lsn_alg_sip_module:


a10_cgnv6_lsn_alg_sip -- Configures A10 cgnv6.lsn.alg.sip
=========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Change LSN SIP ALG Settings






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'method-register'= SIP Method REGISTER; 'method-invite'= SIP Method INVITE; 'method-ack'= SIP Method ACK; 'method-cancel'= SIP Method CANCEL; 'method-bye'= SIP Method BYE; 'method-options'= SIP Method OPTIONS; 'method- prack'= SIP Method PRACK; 'method-subscribe'= SIP Method SUBSCRIBE; 'method- notify'= SIP Method NOTIFY; 'method-publish'= SIP Method PUBLISH; 'method- info'= SIP Method INFO; 'method-refer'= SIP Method REFER; 'method-message'= SIP Method MESSAGE; 'method-update'= SIP Method UPDATE; 'method-unknown'= SIP Method UNKNOWN; 'parse-error'= SIP Message Parse Error; 'req-uri-op-failrue'= SIP Operate Request Uri Failure; 'via-hdr-op-failrue'= SIP Operate Via Header Failure; 'contact-hdr-op-failrue'= SIP Operate Contact Header Failure; 'from- hdr-op-failrue'= SIP Operate From Header Failure; 'to-hdr-op-failrue'= SIP Operate To Header Failure; 'route-hdr-op-failrue'= SIP Operate Route Header Failure; 'record-route-hdr-op-failrue'= SIP Operate Record-Route Header Failure; 'content-length-hdr-op-failrue'= SIP Operate Content-Length Failure; 'third-party-registration'= SIP Third-Party Registration; 'conn-ext-creation- failure'= SIP Create Connection Extension Failure; 'alloc-contact-port- failure'= SIP Alloc Contact Port Failure; 'outside-contact-port-mismatch'= SIP Outside Contact Port Mismatch NAT Port; 'inside-contact-port-mismatch'= SIP Inside Contact Port Mismatch; 'third-party-sdp'= SIP Third-Party SDP; 'sdp- process-candidate-failure'= SIP Operate SDP Media Candidate Attribute Failure; 'sdp-op-failure'= SIP Operate SDP Failure; 'sdp-alloc-port-map-success'= SIP Alloc SDP Port Map Success; 'sdp-alloc-port-map-failure'= SIP Alloc SDP Port Map Failure; 'modify-failure'= SIP Message Modify Failure; 'rewrite-failure'= SIP Message Rewrite Failure; 'tcp-out-of-order-drop'= TCP Out-of-Order Drop; 'smp-conn-alloc-failure'= SMP Helper Conn Alloc Failure; 'helper-found'= SMP Helper Conn Found; 'helper-created'= SMP Helper Conn Created; 'helper-deleted'= SMP Helper Conn Already Deleted; 'helper-freed'= SMP Helper Conn Freed; 'helper-failure'= SMP Helper Failure;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    method_notify (optional, any, None)
      SIP Method NOTIFY


    method_cancel (optional, any, None)
      SIP Method CANCEL


    method_unknown (optional, any, None)
      SIP Method UNKNOWN


    method_ack (optional, any, None)
      SIP Method ACK


    method_update (optional, any, None)
      SIP Method UPDATE


    method_refer (optional, any, None)
      SIP Method REFER


    method_bye (optional, any, None)
      SIP Method BYE


    method_subscribe (optional, any, None)
      SIP Method SUBSCRIBE


    method_prack (optional, any, None)
      SIP Method PRACK


    method_invite (optional, any, None)
      SIP Method INVITE


    method_publish (optional, any, None)
      SIP Method PUBLISH


    method_options (optional, any, None)
      SIP Method OPTIONS


    method_info (optional, any, None)
      SIP Method INFO


    method_register (optional, any, None)
      SIP Method REGISTER


    method_message (optional, any, None)
      SIP Method MESSAGE



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  rtp_stun_timeout (False, any, None)
    RTP/RTCP STUN timeout in minutes (Default is 5 minutes)


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  sip_value (False, any, None)
    'enable'= Enable SIP ALG for LSN;









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

