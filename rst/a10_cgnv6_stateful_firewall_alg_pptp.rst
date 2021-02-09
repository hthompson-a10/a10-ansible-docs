.. _a10_cgnv6_stateful_firewall_alg_pptp_module:


a10_cgnv6_stateful_firewall_alg_pptp -- Configures A10 cgnv6.stateful.firewall.alg.pptp
=======================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure PPTP ALG for NAT stateful firewall (default= enabled)






Parameters
----------

  pptp_value (False, any, None)
    'disable'= Disable ALG;


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'calls-established'= Calls Established; 'call-req-pns-call-id- mismatch'= Call ID Mismatch on Call Request; 'call-reply-pns-call-id-mismatch'= Call ID Mismatch on Call Reply; 'gre-session-created'= GRE Session Created; 'gre-session-freed'= GRE Session Freed; 'call-req-retransmit'= Call Request Retransmit; 'call-req-new'= Call Request New; 'call-req-ext-alloc-failure'= Call Request Ext Alloc Failure; 'call-reply-call-id-unknown'= Call Reply Unknown Client Call ID; 'call-reply-retransmit'= Call Reply Retransmit; 'call- reply-ext-ext-alloc-failure'= Call Request Ext Alloc Failure; 'smp-app-type- mismatch'= SMP App Type Mismatch; 'smp-client-call-id-mismatch'= SMP Client Call ID Mismatch; 'smp-sessions-created'= SMP Session Created; 'smp-sessions- freed'= SMP Session Freed; 'smp-alloc-failure'= SMP Session Alloc Failure; 'gre-conn-creation-failure'= GRE Conn Alloc Failure; 'gre-conn-ext-creation- failure'= GRE Conn Ext Alloc Failure; 'gre-no-fwd-route'= GRE No Fwd Route; 'gre-no-rev-route'= GRE No Rev Route; 'gre-no-control-conn'= GRE No Control Conn; 'gre-conn-already-exists'= GRE Conn Already Exists; 'gre-free-no-ext'= GRE Free No Ext; 'gre-free-no-smp'= GRE Free No SMP; 'gre-free-smp-app-type- mismatch'= GRE Free SMP App Type Mismatch; 'control-freed'= Control Session Freed; 'control-free-no-ext'= Control Free No Ext; 'control-free-no-smp'= Control Free No SMP; 'control-free-smp-app-type-mismatch'= Control Free SMP App Type Mismatch;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    call_reply_pns_call_id_mismatch (optional, any, None)
      Call ID Mismatch on Call Reply


    calls_established (optional, any, None)
      Calls Established


    gre_session_created (optional, any, None)
      GRE Session Created


    gre_session_freed (optional, any, None)
      GRE Session Freed


    call_req_pns_call_id_mismatch (optional, any, None)
      Call ID Mismatch on Call Request



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


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

