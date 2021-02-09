.. _a10_vcs_vblades_stat_module:


a10_vcs_vblades_stat -- Configures A10 vcs-vblades.stat
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show aVCS vBlade box statistics information






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'slave_recv_err'= vBlade Receive Errors counter of aVCS election; 'slave_send_err'= vBlade Send Errors counter of aVCS election; 'slave_recv_bytes'= vBlade Received Bytes counter of aVCS election; 'slave_sent_bytes'= vBlade Sent Bytes counter of aVCS election; 'slave_n_recv'= vBlade Received Messages counter of aVCS election; 'slave_n_sent'= vBlade Sent Messages counter of aVCS election; 'slave_msg_inval'= vBlade Invalid Messages counter of aVCS election; 'slave_keepalive'= vBlade Received Keepalives counter of aVCS election; 'slave_cfg_upd'= vBlade Received Configuration Updates counter of aVCS election; 'slave_cfg_upd_l1_fail'= vBlade Local Configuration Update Errors (1) counter of aVCS election; 'slave_cfg_upd_r_fail'= vBlade Remote Configuration Update Errors counter of aVCS election; 'slave_cfg_upd_l2_fail'= vBlade Local Configuration Update Errors (2) counter of aVCS election; 'slave_cfg_upd_notif_err'= vBlade Configuration Update Notif Errors counter of aVCS election; 'slave_cfg_upd_result_err'= vBlade Configuration Update Result Errors counter of aVCS election;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    slave_recv_bytes (optional, any, None)
      vBlade Received Bytes counter of aVCS election


    slave_cfg_upd_r_fail (optional, any, None)
      vBlade Remote Configuration Update Errors counter of aVCS election


    slave_cfg_upd_result_err (optional, any, None)
      vBlade Configuration Update Result Errors counter of aVCS election


    slave_cfg_upd (optional, any, None)
      vBlade Received Configuration Updates counter of aVCS election


    slave_msg_inval (optional, any, None)
      vBlade Invalid Messages counter of aVCS election


    slave_n_recv (optional, any, None)
      vBlade Received Messages counter of aVCS election


    slave_cfg_upd_notif_err (optional, any, None)
      vBlade Configuration Update Notif Errors counter of aVCS election


    slave_keepalive (optional, any, None)
      vBlade Received Keepalives counter of aVCS election


    slave_recv_err (optional, any, None)
      vBlade Receive Errors counter of aVCS election


    slave_n_sent (optional, any, None)
      vBlade Sent Messages counter of aVCS election


    slave_send_err (optional, any, None)
      vBlade Send Errors counter of aVCS election


    slave_cfg_upd_l1_fail (optional, any, None)
      vBlade Local Configuration Update Errors (1) counter of aVCS election


    slave_cfg_upd_l2_fail (optional, any, None)
      vBlade Local Configuration Update Errors (2) counter of aVCS election


    vblade_id (optional, any, None)
      vBlade-id


    slave_sent_bytes (optional, any, None)
      vBlade Sent Bytes counter of aVCS election



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  vblade_id (True, any, None)
    vBlade-id









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

