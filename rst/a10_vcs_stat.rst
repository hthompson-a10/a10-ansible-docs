.. _a10_vcs_stat_module:


a10_vcs_stat -- Configures A10 vcs.stat
=======================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show aVCS statistics information






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'elect_recv_err'= Receive error counter of aVCS election; 'elect_send_err'= Send error counter of aVCS election; 'elect_recv_byte'= Receive bytes counter of aVCS election; 'elect_send_byte'= Send bytes counter of aVCS election; 'elect_pdu_master_recv'= Received vMaster-PDU counter of aVCS election; 'elect_pdu_master_cand_recv'= Received MC-PDU counter of aVCS election; 'elect_pdu_slave_recv'= Received vBlade-PDU counter of aVCS election; 'elect_pdu_master_take_over_recv'= Received MTO-PDU counter of aVCS election; 'elect_pdu_unknown_recv'= Received Unknown-PDU counter of aVCS election; 'elect_pdu_master_sent'= Sent vMaster-PDU counter of aVCS election; 'elect_pdu_master_cand_sent'= Sent MC-PDU counter of aVCS election; 'elect_pdu_slave_sent'= Sent vBlade-PDU counter of aVCS election; 'elect_pdu_master_take_over_sent'= Sent MTO-PDU counter of aVCS election; 'elect_pdu_unknown_sent'= Sent Unknown-PDU counter of aVCS election; 'elect_pdu_inval'= Invalid PDU counter of aVCS election; 'elect_pdu_hw_mismatch'= PDU HW mismatch counter of aVCS election; 'elect_pdu_cluster_mismatch'= PDU Chassis-ID mismatch counter of aVCS election; 'elect_pdu_dev_id_collision'= PDU Device-ID collision counter of aVCS election; 'elect_mc_discard_master'= MC discarded vMaster-PDU counter of aVCS election; 'elect_mc_replace_master'= MC replaced vMaster-PDU counter of aVCS election; 'elect_mc_dup_masterr'= MC duplicate vMaster-PDU counter of aVCS election; 'elect_mc_reset_timer_by_mc'= MC timers reset by MC-PDU counter of aVCS election; 'elect_mc_reset_timer_by_mto'= MC timers reset by MTO-PDU counter of aVCS election; 'elect_slave_dup_master'= vBlade duplicate vMaster-PDU counter of aVCS election; 'elect_slave_discard_challenger'= vBlade discard challenger counter of aVCS election; 'elect_slave_replace_challenger'= vBlade replace challenger counter of aVCS election; 'elect_slave_dup_challenger'= vBlade duplicate challenger counter of aVCS election; 'elect_slave_discard_neighbour'= vBlade discard neighbour counter of aVCS election; 'elect_slave_too_many_neighbour'= vBlade too many neighbours counter of aVCS election; 'elect_slave_dup_neighbour'= send vBlade duplicate neighbours of aVCS election; 'elect_master_discard_challenger'= vMaster discard challenger counter of aVCS election; 'elect_master_new_challenger'= vMaster new challenger counter of aVCS election; 'elect_master_replace_challenger'= vMaster replace challenger counter of aVCS election; 'elect_master_dup_challenger'= vMaster duplicate challenger counter of aVCS election; 'elect_master_discard_neighbour'= vMaster discard neighbour counter of aVCS election; 'elect_master_too_many_neighbour'= vMaster too many neighbours counter of aVCS election; 'elect_master_dup_neighbour'= vMaster duplicate neighbours counter of aVCS election; 'elect_enter_master_cand_stat'= Enter MC counter of aVCS election; 'elect_enter_slave'= Enter vBlade counter of aVCS election; 'elect_enter_master'= Enter vMaster counter of aVCS election; 'elect_enter_master_take_over'= Enter MTO counter of aVCS election; 'elect_leave_master_cand'= Leave MC counter of aVCS election; 'elect_leave_slave'= Leave vBlade counter of aVCS election; 'elect_leave_master'= Leave vMaster counter of aVCS election; 'elect_leave_master_take_over'= Leave MTO counter of aVCS election; 'master_slave_start_err'= vMaster Start vBlade Errors counter of aVCS election; 'master_slave_start'= vMaster vBlades Started counter of aVCS election; 'master_slave_stop'= vMaster vBlades stopped counter of aVCS election; 'master_cfg_upd'= Received vMaster Configuration Updates counter of aVCS election; 'master_cfg_upd_l_fail'= vMaster Local Configuration Update Errors counter of aVCS election; 'master_cfg_upd_r_fail'= vMaster Remote Configuration Update Errors counter of aVCS election; 'master_cfg_upd_notif_err'= vMaster Configuration Update Notif Errors counter of aVCS election; 'master_cfg_upd_result_err'= vMaster Configuration Update Result Errors counter of aVCS election; 'slave_recv_err'= vBlade Receive Errors counter of aVCS election; 'slave_send_err'= vBlade Send Errors counter of aVCS election; 'slave_recv_bytes'= vBlade Received Bytes counter of aVCS election; 'slave_sent_bytes'= vBlade Sent Bytes counter of aVCS election; 'slave_n_recv'= vBlade Received Messages counter of aVCS election; 'slave_n_sent'= vBlade Sent Messages counter of aVCS election; 'slave_msg_inval'= vBlade Invalid Messages counter of aVCS election; 'slave_keepalive'= vBlade Received Keepalives counter of aVCS election; 'slave_cfg_upd'= vBlade Received Configuration Updates counter of aVCS election; 'slave_cfg_upd_fail'= vBlade Configuration Update Failures counter of aVCS election; 'daemon_n_elec_start'= times of aVCS election start; 'daemon_n_elec_stop'= times of aVCS election stop; 'daemon_recv_err'= counter of aVCS daemon receive error; 'daemon_send_err'= counter of aVCS daemon sent error; 'daemon_recv_bytes'= bytes of aVCS daemon receive; 'daemon_sent_bytes'= bytes of aVCS daemon sent; 'daemon_n_recv'= counter of aVCS daemon receive; 'daemon_n_sent'= counter of aVCS daemon sent; 'daemon_msg_inval'= counter of aVCS daemon invalid message; 'daemon_msg_handle_failure'= counter of aVCS daemon message handle failure;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    elect_master_discard_challenger (optional, any, None)
      vMaster discard challenger counter of aVCS election


    elect_pdu_slave_sent (optional, any, None)
      Sent vBlade-PDU counter of aVCS election


    elect_slave_too_many_neighbour (optional, any, None)
      vBlade too many neighbours counter of aVCS election


    elect_pdu_slave_recv (optional, any, None)
      Received vBlade-PDU counter of aVCS election


    daemon_n_elec_stop (optional, any, None)
      times of aVCS election stop


    elect_pdu_unknown_sent (optional, any, None)
      Sent Unknown-PDU counter of aVCS election


    slave_keepalive (optional, any, None)
      vBlade Received Keepalives counter of aVCS election


    elect_enter_master_take_over (optional, any, None)
      Enter MTO counter of aVCS election


    master_cfg_upd_notif_err (optional, any, None)
      vMaster Configuration Update Notif Errors counter of aVCS election


    elect_mc_discard_master (optional, any, None)
      MC discarded vMaster-PDU counter of aVCS election


    master_cfg_upd_r_fail (optional, any, None)
      vMaster Remote Configuration Update Errors counter of aVCS election


    slave_msg_inval (optional, any, None)
      vBlade Invalid Messages counter of aVCS election


    elect_master_new_challenger (optional, any, None)
      vMaster new challenger counter of aVCS election


    elect_mc_reset_timer_by_mto (optional, any, None)
      MC timers reset by MTO-PDU counter of aVCS election


    elect_pdu_master_take_over_sent (optional, any, None)
      Sent MTO-PDU counter of aVCS election


    elect_slave_discard_neighbour (optional, any, None)
      vBlade discard neighbour counter of aVCS election


    elect_slave_dup_master (optional, any, None)
      vBlade duplicate vMaster-PDU counter of aVCS election


    elect_pdu_master_cand_sent (optional, any, None)
      Sent MC-PDU counter of aVCS election


    elect_pdu_hw_mismatch (optional, any, None)
      PDU HW mismatch counter of aVCS election


    master_slave_stop (optional, any, None)
      vMaster vBlades stopped counter of aVCS election


    elect_master_replace_challenger (optional, any, None)
      vMaster replace challenger counter of aVCS election


    elect_master_too_many_neighbour (optional, any, None)
      vMaster too many neighbours counter of aVCS election


    slave_recv_err (optional, any, None)
      vBlade Receive Errors counter of aVCS election


    elect_enter_master (optional, any, None)
      Enter vMaster counter of aVCS election


    elect_mc_replace_master (optional, any, None)
      MC replaced vMaster-PDU counter of aVCS election


    elect_recv_err (optional, any, None)
      Receive error counter of aVCS election


    daemon_send_err (optional, any, None)
      counter of aVCS daemon sent error


    slave_n_sent (optional, any, None)
      vBlade Sent Messages counter of aVCS election


    master_cfg_upd_result_err (optional, any, None)
      vMaster Configuration Update Result Errors counter of aVCS election


    elect_master_dup_neighbour (optional, any, None)
      vMaster duplicate neighbours counter of aVCS election


    elect_mc_reset_timer_by_mc (optional, any, None)
      MC timers reset by MC-PDU counter of aVCS election


    slave_recv_bytes (optional, any, None)
      vBlade Received Bytes counter of aVCS election


    elect_slave_dup_neighbour (optional, any, None)
      send vBlade duplicate neighbours of aVCS election


    elect_pdu_unknown_recv (optional, any, None)
      Received Unknown-PDU counter of aVCS election


    slave_send_err (optional, any, None)
      vBlade Send Errors counter of aVCS election


    slave_cfg_upd_fail (optional, any, None)
      vBlade Configuration Update Failures counter of aVCS election


    elect_leave_master_take_over (optional, any, None)
      Leave MTO counter of aVCS election


    elect_pdu_master_sent (optional, any, None)
      Sent vMaster-PDU counter of aVCS election


    elect_pdu_cluster_mismatch (optional, any, None)
      PDU Chassis-ID mismatch counter of aVCS election


    daemon_sent_bytes (optional, any, None)
      bytes of aVCS daemon sent


    elect_recv_byte (optional, any, None)
      Receive bytes counter of aVCS election


    elect_mc_dup_masterr (optional, any, None)
      MC duplicate vMaster-PDU counter of aVCS election


    master_slave_start_err (optional, any, None)
      vMaster Start vBlade Errors counter of aVCS election


    elect_slave_discard_challenger (optional, any, None)
      vBlade discard challenger counter of aVCS election


    master_cfg_upd (optional, any, None)
      Received vMaster Configuration Updates counter of aVCS election


    daemon_recv_err (optional, any, None)
      counter of aVCS daemon receive error


    elect_pdu_master_recv (optional, any, None)
      Received vMaster-PDU counter of aVCS election


    slave_cfg_upd (optional, any, None)
      vBlade Received Configuration Updates counter of aVCS election


    elect_pdu_dev_id_collision (optional, any, None)
      PDU Device-ID collision counter of aVCS election


    slave_n_recv (optional, any, None)
      vBlade Received Messages counter of aVCS election


    master_slave_start (optional, any, None)
      vMaster vBlades Started counter of aVCS election


    elect_master_discard_neighbour (optional, any, None)
      vMaster discard neighbour counter of aVCS election


    elect_send_err (optional, any, None)
      Send error counter of aVCS election


    elect_slave_replace_challenger (optional, any, None)
      vBlade replace challenger counter of aVCS election


    elect_slave_dup_challenger (optional, any, None)
      vBlade duplicate challenger counter of aVCS election


    slave_sent_bytes (optional, any, None)
      vBlade Sent Bytes counter of aVCS election


    daemon_msg_inval (optional, any, None)
      counter of aVCS daemon invalid message


    elect_pdu_master_cand_recv (optional, any, None)
      Received MC-PDU counter of aVCS election


    elect_leave_master (optional, any, None)
      Leave vMaster counter of aVCS election


    elect_enter_master_cand_stat (optional, any, None)
      Enter MC counter of aVCS election


    elect_master_dup_challenger (optional, any, None)
      vMaster duplicate challenger counter of aVCS election


    daemon_n_elec_start (optional, any, None)
      times of aVCS election start


    master_cfg_upd_l_fail (optional, any, None)
      vMaster Local Configuration Update Errors counter of aVCS election


    elect_enter_slave (optional, any, None)
      Enter vBlade counter of aVCS election


    elect_send_byte (optional, any, None)
      Send bytes counter of aVCS election


    daemon_msg_handle_failure (optional, any, None)
      counter of aVCS daemon message handle failure


    daemon_n_sent (optional, any, None)
      counter of aVCS daemon sent


    daemon_n_recv (optional, any, None)
      counter of aVCS daemon receive


    elect_leave_master_cand (optional, any, None)
      Leave MC counter of aVCS election


    daemon_recv_bytes (optional, any, None)
      bytes of aVCS daemon receive


    elect_leave_slave (optional, any, None)
      Leave vBlade counter of aVCS election


    elect_pdu_master_take_over_recv (optional, any, None)
      Received MTO-PDU counter of aVCS election


    elect_pdu_inval (optional, any, None)
      Invalid PDU counter of aVCS election



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

