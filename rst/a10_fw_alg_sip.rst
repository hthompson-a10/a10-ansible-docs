.. _a10_fw_alg_sip_module:


a10_fw_alg_sip -- Configures A10 fw.alg.sip
===========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Change Firewall SIP ALG Settings






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'stat-request'= Request Received; 'stat-response'= Response Received; 'method-register'= Method REGISTER; 'method-invite'= Method INVITE; 'method-ack'= Method ACK; 'method-cancel'= Method CANCEL; 'method-bye'= Method BYE; 'method-options'= Method OPTIONS; 'method-prack'= Method PRACK; 'method- subscribe'= Method SUBSCRIBE; 'method-notify'= Method NOTIFY; 'method-publish'= Method PUBLISH; 'method-info'= Method INFO; 'method-refer'= Method REFER; 'method-message'= Method MESSAGE; 'method-update'= Method UPDATE; 'method- unknown'= Method Unknown; 'parse-error'= Message Parse Error; 'keep-alive'= Keep Alive; 'contact-error'= Contact Process Error; 'sdp-error'= SDP Process Error; 'rtp-port-no-op'= RTP Port No Op; 'rtp-rtcp-port-success'= RTP RTCP Port Success; 'rtp-port-failure'= RTP Port Failure; 'rtcp-port-failure'= RTCP Port Failure; 'contact-port-no-op'= Contact Port No Op; 'contact-port-success'= Contact Port Success; 'contact-port-failure'= Contact Port Failure; 'contact- new'= Contact Alloc; 'contact-alloc-failure'= Contact Alloc Failure; 'contact- eim'= Contact EIM; 'contact-eim-set'= Contact EIM Set; 'rtp-new'= RTP Alloc; 'rtp-alloc-failure'= RTP Alloc Failure; 'rtp-eim'= RTP EIM; 'helper-found'= SMP Helper Conn Found; 'helper-created'= SMP Helper Conn Created; 'helper-deleted'= SMP Helper Conn Already Deleted; 'helper-freed'= SMP Helper Conn Freed; 'helper-failure'= SMP Helper Failure;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    method_notify (optional, any, None)
      Method NOTIFY


    method_ack (optional, any, None)
      Method ACK


    method_update (optional, any, None)
      Method UPDATE


    method_refer (optional, any, None)
      Method REFER


    method_options (optional, any, None)
      Method OPTIONS


    method_prack (optional, any, None)
      Method PRACK


    method_publish (optional, any, None)
      Method PUBLISH


    method_register (optional, any, None)
      Method REGISTER


    method_cancel (optional, any, None)
      Method CANCEL


    method_unknown (optional, any, None)
      Method Unknown


    method_bye (optional, any, None)
      Method BYE


    stat_response (optional, any, None)
      Response Received


    method_subscribe (optional, any, None)
      Method SUBSCRIBE


    stat_request (optional, any, None)
      Request Received


    method_message (optional, any, None)
      Method MESSAGE


    method_invite (optional, any, None)
      Method INVITE


    method_info (optional, any, None)
      Method INFO



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  default_port_disable (False, any, None)
    'default-port-disable'= Disable SIP ALG default port 5060;


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


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

