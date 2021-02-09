.. _a10_system_hardware_forward_module:


a10_system_hardware_forward -- Configures A10 system.hardware-forward
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Field hardware_forward






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'hit-counts'= Total packts hit counts; 'hit-index'= HW Fwd hit index; 'ipv4-forward-counts'= Total IPv4 hardware forwarded packets; 'ipv6-forward-counts'= Total IPv6 hardware forwarded packets; 'hw-fwd-module- status'= hardware forwarder status flags; 'hw-fwd-prog-reqs'= hardware forward programming requests; 'hw-fwd-prog-errors'= hardware forward programming Errors; 'hw-fwd-flow-singlebit-errors'= hardware forward singlebit Errors; 'hw- fwd-flow-tag-mismatch'= hardware forward tag mismatch errors; 'hw-fwd-flow-seq- mismatch'= hardware forward sequence mismatch errors; 'hw-fwd-ageout-drop- count'= hardware forward ageout drop count; 'hw-fwd-invalidation-drop'= hardware forward invalid drop count; 'hw-fwd-flow-hit-index'= hardware forward flow hit index; 'hw-fwd-flow-reason-flags'= hardware forward flow reason flags; 'hw-fwd-flow-drop-count'= hardware forward flow drop count; 'hw-fwd-flow-error- count'= hardware forward flow error count; 'hw-fwd-flow-unalign-count'= hardware forward flow unalign count; 'hw-fwd-flow-underflow-count'= hardware forward flow underflow count; 'hw-fwd-flow-tx-full-drop'= hardware forward flow tx full drop count; 'hw-fwd-flow-qdr-full-drop'= hardware forward flow qdr full drop count; 'hw-fwd-phyport-mismatch-drop'= hardware forward phyport mismatch count; 'hw-fwd-vlanid-mismatch-drop'= hardware forward vlanid mismatch count; 'hw-fwd-vmid-drop'= hardware forward vmid mismatch count; 'hw-fwd-protocol- mismatch-drop'= hardware forward protocol mismatch count; 'hw-fwd-avail- ipv4-entry'= hardware forward available ipv4 entries count; 'hw-fwd-avail- ipv6-entry'= hardware forward available ipv6 entries count; 'hw-fwd-entry- create'= Hardware Entries Created; 'hw-fwd-entry-create-failure'= Hardware Entries Created; 'hw-fwd-entry-create-fail-server-down'= Hardware Entries Created; 'hw-fwd-entry-create-fail-max-entry'= Hardware Entries Created; 'hw- fwd-entry-free'= Hardware Entries Freed; 'hw-fwd-entry-free-opp-entry'= Hardware Entries Free due to opposite tuple entry ageout event; 'hw-fwd-entry- free-no-hw-prog'= Hardware Entry Free no hw prog; 'hw-fwd-entry-free-no-conn'= Hardware Entry Free no matched conn; 'hw-fwd-entry-free-no-sw-entry'= Hardware Entry Free no software entry; 'hw-fwd-entry-counter'= Hardware Entry Count; 'hw-fwd-entry-age-out'= Hardware Entries Aged Out; 'hw-fwd-entry-age-out-idle'= Hardware Entries Aged Out Idle; 'hw-fwd-entry-age-out-tcp-fin'= Hardware Entries Aged Out TCP FIN; 'hw-fwd-entry-age-out-tcp-rst'= Hardware Entries Aged Out TCP RST; 'hw-fwd-entry-age-out-invalid-dst'= Hardware Entries Aged Out invalid dst; 'hw-fwd-entry-force-hw-invalidate'= Hardware Entries Force HW Invalidate; 'hw-fwd-entry-invalidate-server-down'= Hardware Entries Invalidate due to server down; 'hw-fwd-tcam-create'= TCAM Entries Created; 'hw-fwd-tcam- free'= TCAM Entries Freed; 'hw-fwd-tcam-counter'= TCAM Entry Count;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    hw_fwd_entry_age_out (optional, any, None)
      Hardware Entries Aged Out


    hw_fwd_avail_ipv4_entry (optional, any, None)
      hardware forward available ipv4 entries count


    hw_fwd_flow_drop_count (optional, any, None)
      hardware forward flow drop count


    hit_index (optional, any, None)
      HW Fwd hit index


    hw_fwd_flow_underflow_count (optional, any, None)
      hardware forward flow underflow count


    hw_fwd_entry_create_fail_server_down (optional, any, None)
      Hardware Entries Created


    hw_fwd_entry_force_hw_invalidate (optional, any, None)
      Hardware Entries Force HW Invalidate


    hw_fwd_flow_singlebit_errors (optional, any, None)
      hardware forward singlebit Errors


    hw_fwd_entry_age_out_tcp_fin (optional, any, None)
      Hardware Entries Aged Out TCP FIN


    hw_fwd_vmid_drop (optional, any, None)
      hardware forward vmid mismatch count


    hw_fwd_entry_create_fail_max_entry (optional, any, None)
      Hardware Entries Created


    hw_fwd_entry_create_failure (optional, any, None)
      Hardware Entries Created


    hw_fwd_entry_free_no_sw_entry (optional, any, None)
      Hardware Entry Free no software entry


    hw_fwd_ageout_drop_count (optional, any, None)
      hardware forward ageout drop count


    hw_fwd_entry_free (optional, any, None)
      Hardware Entries Freed


    hw_fwd_entry_create (optional, any, None)
      Hardware Entries Created


    hw_fwd_tcam_counter (optional, any, None)
      TCAM Entry Count


    hw_fwd_flow_error_count (optional, any, None)
      hardware forward flow error count


    hw_fwd_entry_age_out_idle (optional, any, None)
      Hardware Entries Aged Out Idle


    hw_fwd_flow_tx_full_drop (optional, any, None)
      hardware forward flow tx full drop count


    hw_fwd_phyport_mismatch_drop (optional, any, None)
      hardware forward phyport mismatch count


    hw_fwd_flow_unalign_count (optional, any, None)
      hardware forward flow unalign count


    hw_fwd_module_status (optional, any, None)
      hardware forwarder status flags


    hw_fwd_entry_free_no_conn (optional, any, None)
      Hardware Entry Free no matched conn


    hw_fwd_prog_errors (optional, any, None)
      hardware forward programming Errors


    hw_fwd_entry_age_out_invalid_dst (optional, any, None)
      Hardware Entries Aged Out invalid dst


    hw_fwd_vlanid_mismatch_drop (optional, any, None)
      hardware forward vlanid mismatch count


    hit_counts (optional, any, None)
      Total packts hit counts


    hw_fwd_entry_counter (optional, any, None)
      Hardware Entry Count


    hw_fwd_invalidation_drop (optional, any, None)
      hardware forward invalid drop count


    hw_fwd_flow_qdr_full_drop (optional, any, None)
      hardware forward flow qdr full drop count


    hw_fwd_flow_hit_index (optional, any, None)
      hardware forward flow hit index


    ipv4_forward_counts (optional, any, None)
      Total IPv4 hardware forwarded packets


    hw_fwd_entry_free_no_hw_prog (optional, any, None)
      Hardware Entry Free no hw prog


    hw_fwd_avail_ipv6_entry (optional, any, None)
      hardware forward available ipv6 entries count


    hw_fwd_protocol_mismatch_drop (optional, any, None)
      hardware forward protocol mismatch count


    hw_fwd_flow_seq_mismatch (optional, any, None)
      hardware forward sequence mismatch errors


    hw_fwd_entry_invalidate_server_down (optional, any, None)
      Hardware Entries Invalidate due to server down


    hw_fwd_prog_reqs (optional, any, None)
      hardware forward programming requests


    hw_fwd_tcam_create (optional, any, None)
      TCAM Entries Created


    hw_fwd_entry_free_opp_entry (optional, any, None)
      Hardware Entries Free due to opposite tuple entry ageout event


    ipv6_forward_counts (optional, any, None)
      Total IPv6 hardware forwarded packets


    hw_fwd_entry_age_out_tcp_rst (optional, any, None)
      Hardware Entries Aged Out TCP RST


    hw_fwd_flow_reason_flags (optional, any, None)
      hardware forward flow reason flags


    hw_fwd_flow_tag_mismatch (optional, any, None)
      hardware forward tag mismatch errors


    hw_fwd_tcam_free (optional, any, None)
      TCAM Entries Freed



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

