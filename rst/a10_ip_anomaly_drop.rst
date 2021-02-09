.. _a10_ip_anomaly_drop_module:


a10_ip_anomaly_drop -- Configures A10 ip.anomaly-drop
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Set IP anomaly drop policy






Parameters
----------

  packet_deformity (False, any, None)
    Field packet_deformity


    packet_deformity_layer_3 (optional, any, None)
      drop packets with layer 3 anomaly


    packet_deformity_layer_4 (optional, any, None)
      drop packets with layer 4 anomaly



  frag (False, any, None)
    drop all fragmented packets


  ansible_username (True, any, None)
    Username for AXAPI authentication


  tcp_syn_fin (False, any, None)
    drop TCP packets with both syn and fin flags set


  security_attack (False, any, None)
    Field security_attack


    security_attack_layer_4 (optional, any, None)
      drop packets with layer 4 anomaly


    security_attack_layer_3 (optional, any, None)
      drop packets with layer 3 anomaly



  tcp_no_flag (False, any, None)
    drop TCP packets with no flag


  tcp_syn_frag (False, any, None)
    drop fragmented TCP packets with syn flag set


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  drop_all (False, any, None)
    drop all IP anomaly packets


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'land'= land; 'emp_frg'= emp_frg; 'emp_mic_frg'= emp_mic_frg; 'opt'= opt; 'frg'= frg; 'bad_ip_hdrlen'= bad_ip_hdrlen; 'bad_ip_flg'= bad_ip_flg; 'bad_ip_ttl'= bad_ip_ttl; 'no_ip_payload'= no_ip_payload; 'over_ip_payload'= over_ip_payload; 'bad_ip_payload_len'= bad_ip_payload_len; 'bad_ip_frg_offset'= bad_ip_frg_offset; 'csum'= csum; 'pod'= pod; 'bad_tcp_urg_offset'= bad_tcp_urg_offset; 'tcp_sht_hdr'= tcp_sht_hdr; 'tcp_bad_iplen'= tcp_bad_iplen; 'tcp_null_frg'= tcp_null_frg; 'tcp_null_scan'= tcp_null_scan; 'tcp_syn_fin'= tcp_syn_fin; 'tcp_xmas'= tcp_xmas; 'tcp_xmas_scan'= tcp_xmas_scan; 'tcp_syn_frg'= tcp_syn_frg; 'tcp_frg_hdr'= tcp_frg_hdr; 'tcp_bad_csum'= tcp_bad_csum; 'udp_srt_hdr'= udp_srt_hdr; 'udp_bad_len'= udp_bad_len; 'udp_kerb_frg'= udp_kerb_frg; 'udp_port_lb'= udp_port_lb; 'udp_bad_csum'= udp_bad_csum; 'runt_ip_hdr'= runt_ip_hdr; 'runt_tcp_udp_hdr'= runt_tcp_udp_hdr; 'ipip_tnl_msmtch'= ipip_tnl_msmtch; 'tcp_opt_err'= tcp_opt_err; 'ipip_tnl_err'= ipip_tnl_err; 'vxlan_err'= vxlan_err; 'nvgre_err'= nvgre_err; 'gre_pptp_err'= gre_pptp_err;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    tcp_frg_hdr (optional, any, None)
      Field tcp_frg_hdr


    tcp_null_frg (optional, any, None)
      Field tcp_null_frg


    over_ip_payload (optional, any, None)
      Field over_ip_payload


    udp_bad_csum (optional, any, None)
      Field udp_bad_csum


    nvgre_err (optional, any, None)
      Field nvgre_err


    tcp_syn_fin (optional, any, None)
      Field tcp_syn_fin


    udp_kerb_frg (optional, any, None)
      Field udp_kerb_frg


    tcp_syn_frg (optional, any, None)
      Field tcp_syn_frg


    tcp_bad_iplen (optional, any, None)
      Field tcp_bad_iplen


    ipip_tnl_err (optional, any, None)
      Field ipip_tnl_err


    csum (optional, any, None)
      Field csum


    tcp_xmas (optional, any, None)
      Field tcp_xmas


    pod (optional, any, None)
      Field pod


    tcp_bad_csum (optional, any, None)
      Field tcp_bad_csum


    emp_frg (optional, any, None)
      Field emp_frg


    frg (optional, any, None)
      Field frg


    bad_ip_ttl (optional, any, None)
      Field bad_ip_ttl


    bad_ip_frg_offset (optional, any, None)
      Field bad_ip_frg_offset


    tcp_sht_hdr (optional, any, None)
      Field tcp_sht_hdr


    tcp_xmas_scan (optional, any, None)
      Field tcp_xmas_scan


    no_ip_payload (optional, any, None)
      Field no_ip_payload


    udp_bad_len (optional, any, None)
      Field udp_bad_len


    opt (optional, any, None)
      Field opt


    vxlan_err (optional, any, None)
      Field vxlan_err


    bad_ip_payload_len (optional, any, None)
      Field bad_ip_payload_len


    runt_ip_hdr (optional, any, None)
      Field runt_ip_hdr


    runt_tcp_udp_hdr (optional, any, None)
      Field runt_tcp_udp_hdr


    emp_mic_frg (optional, any, None)
      Field emp_mic_frg


    bad_ip_hdrlen (optional, any, None)
      Field bad_ip_hdrlen


    tcp_null_scan (optional, any, None)
      Field tcp_null_scan


    land (optional, any, None)
      Field land


    tcp_opt_err (optional, any, None)
      Field tcp_opt_err


    bad_ip_flg (optional, any, None)
      Field bad_ip_flg


    udp_srt_hdr (optional, any, None)
      Field udp_srt_hdr


    udp_port_lb (optional, any, None)
      Field udp_port_lb


    bad_tcp_urg_offset (optional, any, None)
      Field bad_tcp_urg_offset


    gre_pptp_err (optional, any, None)
      Field gre_pptp_err


    ipip_tnl_msmtch (optional, any, None)
      Field ipip_tnl_msmtch



  uuid (False, any, None)
    uuid of the object


  zero_window (False, any, None)
    zero window size threshold (threshold value)


  ansible_password (True, any, None)
    Password for AXAPI authentication


  out_of_sequence (False, any, None)
    out of sequence packet threshold (threshold value)


  ping_of_death (False, any, None)
    drop oversize ICMP packets


  bad_content (False, any, None)
    bad content threshold (threshold value)


  state (True, any, None)
    State of the object to be created.


  land_attack (False, any, None)
    drop IP packets with the same source and destination addresses


  ip_option (False, any, None)
    drop packets with IP options









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

