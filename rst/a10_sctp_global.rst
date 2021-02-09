.. _a10_sctp_global_module:


a10_sctp_global -- Configures A10 sctp.global
=============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

SCTP Statistics






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'sctp-static-nat-session-created'= SCTP Static NAT Session Created; 'sctp-static-nat-session-deleted'= SCTP Static NAT Session Deleted; 'sctp-fw- session-created'= SCTP Firewall Session Created; 'sctp-fw-session-deleted'= SCTP Firewall Session Deleted; 'pkt-err-drop'= Packet Error Drop; 'bad-csum'= Bad Checksum; 'bad-payload-drop'= Bad Payload Drop; 'bad-alignment-drop'= Bad Alignment Drop; 'oos-pkt-drop'= Out-of-state Packet Drop; 'max-multi-home- drop'= Maximum Multi-homing IP Addresses Drop; 'multi-home-remove-ip-skip'= Multi-homing Remove IP Parameter Skip; 'multi-home-addr-not-found-drop'= Multi- homing IP Address Not Found Drop; 'static-nat-cfg-not-found'= Static NAT Config Not Found Drop; 'cfg-err-drop'= Configuration Error Drop; 'vrrp-standby-drop'= NAT Resource VRRP-A Standby Drop; 'invalid-frag-chunk-drop'= Invalid Fragmented Chunks Drop; 'disallowed-chunk-filtered'= Disallowed Chunk Filtered; 'disallowed-pkt-drop'= Disallowed Packet Drop; 'rate-limit-drop'= Rate-limit Drop; 'sby-session-created'= Standby Session Created; 'sby-session-create- fail'= Standby Session Create Failed; 'sby-session-updated'= Standby Session Updated; 'sby-session-update-fail'= Standby Session Update Failed; 'sby-static- nat-cfg-not-found'= Static NAT Config Not Found on Standby; 'sctp-out-of- system-memory'= Out of System Memory; 'conn_ext_size_max'= Max Conn Extension Size; 'bad-csum-shadow'= Bad Checksum Shadow; 'bad-payload-drop-shadow'= Bad Packet Payload Drop Shadow; 'bad-alignment-drop-shadow'= Bad Packet Alignment Drop Shadow;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    sctp_fw_session_created (optional, any, None)
      SCTP Firewall Session Created


    rate_limit_drop (optional, any, None)
      Rate-limit Drop


    bad_payload_drop (optional, any, None)
      Bad Payload Drop


    sctp_fw_session_deleted (optional, any, None)
      SCTP Firewall Session Deleted


    sby_session_create_fail (optional, any, None)
      Standby Session Create Failed


    vrrp_standby_drop (optional, any, None)
      NAT Resource VRRP-A Standby Drop


    sctp_static_nat_session_deleted (optional, any, None)
      SCTP Static NAT Session Deleted


    oos_pkt_drop (optional, any, None)
      Out-of-state Packet Drop


    disallowed_chunk_filtered (optional, any, None)
      Disallowed Chunk Filtered


    multi_home_addr_not_found_drop (optional, any, None)
      Multi-homing IP Address Not Found Drop


    sby_session_created (optional, any, None)
      Standby Session Created


    invalid_frag_chunk_drop (optional, any, None)
      Invalid Fragmented Chunks Drop


    sby_session_updated (optional, any, None)
      Standby Session Updated


    sctp_static_nat_session_created (optional, any, None)
      SCTP Static NAT Session Created


    multi_home_remove_ip_skip (optional, any, None)
      Multi-homing Remove IP Parameter Skip


    sby_session_update_fail (optional, any, None)
      Standby Session Update Failed


    max_multi_home_drop (optional, any, None)
      Maximum Multi-homing IP Addresses Drop


    pkt_err_drop (optional, any, None)
      Packet Error Drop


    bad_csum (optional, any, None)
      Bad Checksum


    sby_static_nat_cfg_not_found (optional, any, None)
      Static NAT Config Not Found on Standby


    bad_alignment_drop (optional, any, None)
      Bad Alignment Drop


    disallowed_pkt_drop (optional, any, None)
      Disallowed Packet Drop


    static_nat_cfg_not_found (optional, any, None)
      Static NAT Config Not Found Drop


    cfg_err_drop (optional, any, None)
      Configuration Error Drop



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

