.. _a10_slb_l4_module:


a10_slb_l4 -- Configures A10 slb.l4
===================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure L4






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'intcp'= TCP received; 'synreceived'= TCP SYN received; 'tcp_fwd_last_ack'= L4 rcv fwd last ACK; 'tcp_rev_last_ack'= L4 rcv rev last ACK; 'tcp_rev_fin'= L4 rcv rev FIN; 'tcp_fwd_fin'= L4 rcv fwd FIN; 'tcp_fwd_ackfin'= L4 rcv fwd FIN|ACK; 'inudp'= UDP received; 'syncookiessent'= TCP SYN cookie snt; 'syncookiessent_ts'= TCP SYN cookie snt ts; 'syncookiessentfailed'= TCP SYN cookie snt fail; 'outrst'= TCP out RST; 'outrst_nosyn'= TCP out RST no SYN; 'outrst_broker'= TCP out RST L4 proxy; 'outrst_ack_attack'= TCP out RST ACK attack; 'outrst_aflex'= TCP out RST aFleX; 'outrst_stale_sess'= TCP out RST stale sess; 'syn_stale_sess'= SYN stale sess drop; 'outrst_tcpproxy'= TCP out RST TCP proxy; 'svrselfail'= Server sel failure; 'noroute'= IP out noroute; 'snat_fail'= Source NAT failure; 'snat_no_fwd_route'= Source NAT no fwd route; 'snat_no_rev_route'= Source NAT no rev route; 'snat_icmp_error_process'= Source NAT ICMP Process; 'snat_icmp_no_match'= Source NAT ICMP No Match; 'smart_nat_id_mismatch'= Auto NAT id mismatch; 'syncookiescheckfailed'= TCP SYN cookie failed; 'novport_drop'= NAT no session drops; 'no_vport_drop'= vport not matching drops; 'nosyn_drop'= No SYN pkt drops; 'nosyn_drop_fin'= No SYN pkt drops - FIN; 'nosyn_drop_rst'= No SYN pkt drops - RST; 'nosyn_drop_ack'= No SYN pkt drops - ACK; 'connlimit_drop'= Conn Limit drops; 'connlimit_reset'= Conn Limit resets; 'conn_rate_limit_drop'= Conn rate limit drops; 'conn_rate_limit_reset'= Conn rate limit resets; 'proxy_nosock_drop'= Proxy no sock drops; 'drop_aflex'= aFleX drops; 'sess_aged_out'= Session aged out; 'tcp_sess_aged_out'= TCP Session aged out; 'udp_sess_aged_out'= UDP Session aged out; 'other_sess_aged_out'= Other Session aged out; 'tcp_no_slb'= TCP no SLB; 'udp_no_slb'= UDP no SLB; 'throttle_syn'= SYN Throttle; 'drop_gslb'= Drop GSLB; 'inband_hm_retry'= Inband HM retry; 'inband_hm_reassign'= Inband HM reassign; 'auto_reassign'= Auto-reselect server; 'fast_aging_set'= Fast aging set; 'fast_aging_reset'= Fast aging reset; 'dns_policy_drop'= DNS Policy Drop; 'tcp_invalid_drop'= TCP invalid drop; 'anomaly_out_seq'= Anomaly out of sequence; 'anomaly_zero_win'= Anomaly zero window; 'anomaly_bad_content'= Anomaly bad content; 'anomaly_pbslb_drop'= Anomaly pbslb drop; 'no_resourse_drop'= No resource drop; 'reset_unknown_conn'= Reset unknown conn; 'reset_l7_on_failover'= RST L7 on failover; 'ignore_msl'= ignore msl; 'l2_dsr'= L2 DSR received; 'l3_dsr'= L3 DSR received; 'port_preserve_attempt'= NAT Port Preserve Try; 'port_preserve_succ'= NAT Port Preserve Succ; 'tcpsyndata_drop'= TCP SYN With Data Drop; 'tcpotherflags_drop'= TCP SYN Other Flags Drop; 'bw_rate_limit_exceed'= BW-Limit Exceed drop; 'bw_watermark_drop'= BW-Watermark drop; 'l4_cps_exceed'= L4 CPS exceed drop; 'nat_cps_exceed'= NAT CPS exceed drop; 'l7_cps_exceed'= L7 CPS exceed drop; 'ssl_cps_exceed'= SSL CPS exceed drop; 'ssl_tpt_exceed'= SSL TPT exceed drop; 'ssl_watermark_drop'= SSL TPT- Watermark drop; 'concurrent_conn_exceed'= L3V Conn Limit Drop; 'svr_syn_handshake_fail'= L4 server handshake fail; 'stateless_conn_timeout'= L4 stateless Conn TO; 'tcp_ax_rexmit_syn'= L4 AX re-xmit SYN; 'tcp_syn_rcv_ack'= L4 rcv ACK on SYN; 'tcp_syn_rcv_rst'= L4 rcv RST on SYN; 'tcp_sess_noest_aged_out'= TCP no-Est Sess aged out; 'tcp_sess_noest_csyn_rcv_aged_out'= no-Est CSYN rcv aged out; 'tcp_sess_noest_ssyn_xmit_aged_out'= no-Est SSYN snt aged out; 'tcp_rexmit_syn'= L4 rcv rexmit SYN; 'tcp_rexmit_syn_delq'= L4 rcv rexmit SYN (delq); 'tcp_rexmit_synack'= L4 rcv rexmit SYN|ACK; 'tcp_rexmit_synack_delq'= L4 rcv rexmit SYN|ACK DQ; 'tcp_fwd_fin_dup'= L4 rcv fwd FIN dup; 'tcp_rev_fin_dup'= L4 rcv rev FIN dup; 'tcp_rev_ackfin'= L4 rcv rev FIN|ACK; 'tcp_fwd_rst'= L4 rcv fwd RST; 'tcp_rev_rst'= L4 rcv rev RST; 'udp_req_oneplus_no_resp'= L4 UDP reqs no rsp; 'udp_req_one_oneplus_resp'= L4 UDP req rsps; 'udp_req_resp_notmatch'= L4 UDP req/rsp not match; 'udp_req_more_resp'= L4 UDP req greater than rsps; 'udp_resp_more_req'= L4 UDP rsps greater than reqs; 'udp_req_oneplus'= L4 UDP reqs; 'udp_resp_oneplus'= L4 UDP rsps; 'out_seq_ack_drop'= Out of sequence ACK drop; 'tcp_est'= L4 TCP Established; 'synattack'= L4 SYN attack; 'syn_rate'= TCP SYN rate per sec; 'syncookie_buff_drop'= TCP SYN cookie buff drop; 'syncookie_buff_queue'= TCP SYN cookie buff queue; 'skip_insert_client_ip'= Skip Insert-client-ip; 'synreceived_hw'= TCP SYN (HW SYN cookie); 'dns_id_switch'= DNS query id switch; 'server_down_del'= Server Down Del switch; 'dnssec_switch'= DNSSEC SG switch; 'rate_drop_reset_unkn'= Rate Drop reset; 'tcp_connections_closed'= TCP Connections Closed; 'snat_force_preserve_alloc'= Snat port preserve allocated; 'snat_force_preserve_free'= Snat port preserve freed; 'snat_port_overload_fail'= Snat port overload fail;



  oper (False, any, None)
    Field oper


    l4_cpu_list (optional, any, None)
      Field l4_cpu_list


    cpu_count (optional, any, None)
      Field cpu_count



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    l7_cps_exceed (optional, any, None)
      L7 CPS exceed drop


    conn_rate_limit_drop (optional, any, None)
      Conn rate limit drops


    outrst_stale_sess (optional, any, None)
      TCP out RST stale sess


    concurrent_conn_exceed (optional, any, None)
      L3V Conn Limit Drop


    synattack (optional, any, None)
      L4 SYN attack


    drop_aflex (optional, any, None)
      aFleX drops


    snat_port_overload_fail (optional, any, None)
      Snat port overload fail


    tcp_sess_aged_out (optional, any, None)
      TCP Session aged out


    tcp_est (optional, any, None)
      L4 TCP Established


    bw_rate_limit_exceed (optional, any, None)
      BW-Limit Exceed drop


    no_vport_drop (optional, any, None)
      vport not matching drops


    snat_icmp_error_process (optional, any, None)
      Source NAT ICMP Process


    port_preserve_attempt (optional, any, None)
      NAT Port Preserve Try


    outrst_broker (optional, any, None)
      TCP out RST L4 proxy


    tcp_sess_noest_csyn_rcv_aged_out (optional, any, None)
      no-Est CSYN rcv aged out


    anomaly_pbslb_drop (optional, any, None)
      Anomaly pbslb drop


    proxy_nosock_drop (optional, any, None)
      Proxy no sock drops


    novport_drop (optional, any, None)
      NAT no session drops


    svr_syn_handshake_fail (optional, any, None)
      L4 server handshake fail


    udp_req_oneplus_no_resp (optional, any, None)
      L4 UDP reqs no rsp


    snat_icmp_no_match (optional, any, None)
      Source NAT ICMP No Match


    fast_aging_reset (optional, any, None)
      Fast aging reset


    drop_gslb (optional, any, None)
      Drop GSLB


    tcp_rexmit_syn (optional, any, None)
      L4 rcv rexmit SYN


    syncookiessent (optional, any, None)
      TCP SYN cookie snt


    outrst_aflex (optional, any, None)
      TCP out RST aFleX


    anomaly_zero_win (optional, any, None)
      Anomaly zero window


    tcp_ax_rexmit_syn (optional, any, None)
      L4 AX re-xmit SYN


    tcp_sess_noest_ssyn_xmit_aged_out (optional, any, None)
      no-Est SSYN snt aged out


    syncookie_buff_queue (optional, any, None)
      TCP SYN cookie buff queue


    sess_aged_out (optional, any, None)
      Session aged out


    throttle_syn (optional, any, None)
      SYN Throttle


    nosyn_drop (optional, any, None)
      No SYN pkt drops


    l4_cps_exceed (optional, any, None)
      L4 CPS exceed drop


    nosyn_drop_rst (optional, any, None)
      No SYN pkt drops - RST


    anomaly_bad_content (optional, any, None)
      Anomaly bad content


    snat_fail (optional, any, None)
      Source NAT failure


    no_resourse_drop (optional, any, None)
      No resource drop


    tcp_no_slb (optional, any, None)
      TCP no SLB


    inband_hm_retry (optional, any, None)
      Inband HM retry


    synreceived (optional, any, None)
      TCP SYN received


    ignore_msl (optional, any, None)
      ignore msl


    tcp_connections_closed (optional, any, None)
      TCP Connections Closed


    out_seq_ack_drop (optional, any, None)
      Out of sequence ACK drop


    outrst_nosyn (optional, any, None)
      TCP out RST no SYN


    udp_req_more_resp (optional, any, None)
      L4 UDP req greater than rsps


    nosyn_drop_fin (optional, any, None)
      No SYN pkt drops - FIN


    anomaly_out_seq (optional, any, None)
      Anomaly out of sequence


    tcp_rev_ackfin (optional, any, None)
      L4 rcv rev FIN|ACK


    rate_drop_reset_unkn (optional, any, None)
      Rate Drop reset


    tcp_rev_fin (optional, any, None)
      L4 rcv rev FIN


    conn_rate_limit_reset (optional, any, None)
      Conn rate limit resets


    nosyn_drop_ack (optional, any, None)
      No SYN pkt drops - ACK


    l2_dsr (optional, any, None)
      L2 DSR received


    nat_cps_exceed (optional, any, None)
      NAT CPS exceed drop


    snat_no_rev_route (optional, any, None)
      Source NAT no rev route


    tcp_fwd_rst (optional, any, None)
      L4 rcv fwd RST


    bw_watermark_drop (optional, any, None)
      BW-Watermark drop


    reset_l7_on_failover (optional, any, None)
      RST L7 on failover


    tcp_invalid_drop (optional, any, None)
      TCP invalid drop


    snat_force_preserve_free (optional, any, None)
      Snat port preserve freed


    syn_stale_sess (optional, any, None)
      SYN stale sess drop


    reset_unknown_conn (optional, any, None)
      Reset unknown conn


    syncookie_buff_drop (optional, any, None)
      TCP SYN cookie buff drop


    outrst_tcpproxy (optional, any, None)
      TCP out RST TCP proxy


    snat_no_fwd_route (optional, any, None)
      Source NAT no fwd route


    inudp (optional, any, None)
      UDP received


    tcp_rev_fin_dup (optional, any, None)
      L4 rcv rev FIN dup


    udp_req_resp_notmatch (optional, any, None)
      L4 UDP req/rsp not match


    tcpotherflags_drop (optional, any, None)
      TCP SYN Other Flags Drop


    svrselfail (optional, any, None)
      Server sel failure


    udp_sess_aged_out (optional, any, None)
      UDP Session aged out


    udp_no_slb (optional, any, None)
      UDP no SLB


    auto_reassign (optional, any, None)
      Auto-reselect server


    stateless_conn_timeout (optional, any, None)
      L4 stateless Conn TO


    connlimit_reset (optional, any, None)
      Conn Limit resets


    port_preserve_succ (optional, any, None)
      NAT Port Preserve Succ


    outrst_ack_attack (optional, any, None)
      TCP out RST ACK attack


    udp_resp_more_req (optional, any, None)
      L4 UDP rsps greater than reqs


    fast_aging_set (optional, any, None)
      Fast aging set


    connlimit_drop (optional, any, None)
      Conn Limit drops


    tcpsyndata_drop (optional, any, None)
      TCP SYN With Data Drop


    syncookiescheckfailed (optional, any, None)
      TCP SYN cookie failed


    udp_req_one_oneplus_resp (optional, any, None)
      L4 UDP req rsps


    tcp_rexmit_syn_delq (optional, any, None)
      L4 rcv rexmit SYN (delq)


    tcp_syn_rcv_rst (optional, any, None)
      L4 rcv RST on SYN


    dns_id_switch (optional, any, None)
      DNS query id switch


    ssl_cps_exceed (optional, any, None)
      SSL CPS exceed drop


    tcp_rev_rst (optional, any, None)
      L4 rcv rev RST


    noroute (optional, any, None)
      IP out noroute


    udp_resp_oneplus (optional, any, None)
      L4 UDP rsps


    syncookiessentfailed (optional, any, None)
      TCP SYN cookie snt fail


    intcp (optional, any, None)
      TCP received


    ssl_tpt_exceed (optional, any, None)
      SSL TPT exceed drop


    smart_nat_id_mismatch (optional, any, None)
      Auto NAT id mismatch


    udp_req_oneplus (optional, any, None)
      L4 UDP reqs


    tcp_rev_last_ack (optional, any, None)
      L4 rcv rev last ACK


    other_sess_aged_out (optional, any, None)
      Other Session aged out


    tcp_fwd_ackfin (optional, any, None)
      L4 rcv fwd FIN|ACK


    ssl_watermark_drop (optional, any, None)
      SSL TPT-Watermark drop


    tcp_rexmit_synack_delq (optional, any, None)
      L4 rcv rexmit SYN|ACK DQ


    tcp_fwd_fin (optional, any, None)
      L4 rcv fwd FIN


    dnssec_switch (optional, any, None)
      DNSSEC SG switch


    tcp_fwd_fin_dup (optional, any, None)
      L4 rcv fwd FIN dup


    inband_hm_reassign (optional, any, None)
      Inband HM reassign


    syncookiessent_ts (optional, any, None)
      TCP SYN cookie snt ts


    tcp_syn_rcv_ack (optional, any, None)
      L4 rcv ACK on SYN


    dns_policy_drop (optional, any, None)
      DNS Policy Drop


    tcp_fwd_last_ack (optional, any, None)
      L4 rcv fwd last ACK


    synreceived_hw (optional, any, None)
      TCP SYN (HW SYN cookie)


    tcp_rexmit_synack (optional, any, None)
      L4 rcv rexmit SYN|ACK


    outrst (optional, any, None)
      TCP out RST


    skip_insert_client_ip (optional, any, None)
      Skip Insert-client-ip


    server_down_del (optional, any, None)
      Server Down Del switch


    l3_dsr (optional, any, None)
      L3 DSR received


    snat_force_preserve_alloc (optional, any, None)
      Snat port preserve allocated


    tcp_sess_noest_aged_out (optional, any, None)
      TCP no-Est Sess aged out


    syn_rate (optional, any, None)
      TCP SYN rate per sec



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

