.. _a10_ip_nat_alg_pptp_module:


a10_ip_nat_alg_pptp -- Configures A10 ip.nat.alg.pptp
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

PPTP ALG Settings






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'current-smp-sessions'= current-smp-sessions; 'current-gre- sessions'= current-gre-sessions; 'smp-session-creation-failure'= smp-session- creation-failure; 'truncated-pns-message'= truncated-pns-message; 'truncated- pac-message'= truncated-pac-message; 'mismatched-pns-call-id'= mismatched-pns- call-id; 'mismatched-pac-call-id'= mismatched-pac-call-id; 'retransmitted-pns- message'= retransmitted-pns-message; 'retransmitted-pac-message'= retransmitted-pac-message; 'truncated-gre-packet'= truncated-gre-packet; 'unknown-gre-version'= unknown-gre-version; 'no-matching-gre-session'= no- matching-gre-session;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    unknown_gre_version (optional, any, None)
      Field unknown_gre_version


    truncated_gre_packet (optional, any, None)
      Field truncated_gre_packet


    mismatched_pac_call_id (optional, any, None)
      Field mismatched_pac_call_id


    retransmitted_pac_message (optional, any, None)
      Field retransmitted_pac_message


    smp_session_creation_failure (optional, any, None)
      Field smp_session_creation_failure


    truncated_pac_message (optional, any, None)
      Field truncated_pac_message


    mismatched_pns_call_id (optional, any, None)
      Field mismatched_pns_call_id


    no_matching_gre_session (optional, any, None)
      Field no_matching_gre_session


    current_gre_sessions (optional, any, None)
      Field current_gre_sessions


    retransmitted_pns_message (optional, any, None)
      Field retransmitted_pns_message


    truncated_pns_message (optional, any, None)
      Field truncated_pns_message


    current_smp_sessions (optional, any, None)
      Field current_smp_sessions



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  pptp (False, any, None)
    'disable'= Disable PPTP NAT ALG; 'enable'= Enable PPTP NAT ALG;


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

