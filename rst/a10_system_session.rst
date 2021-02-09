.. _a10_system_session_module:


a10_system_session -- Configures A10 system.session
===================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Session Entries






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'total_l4_conn'= Total L4 Count; 'conn_counter'= Conn Count; 'conn_freed_counter'= Conn Freed; 'total_l4_packet_count'= Total L4 Packet Count; 'total_l7_packet_count'= Total L7 Packet Count; 'total_l4_conn_proxy'= Total L4 Conn Proxy Count; 'total_l7_conn'= Total L7 Conn; 'total_tcp_conn'= Total TCP Conn; 'curr_free_conn'= Curr Free Conn; 'tcp_est_counter'= TCP Established; 'tcp_half_open_counter'= TCP Half Open; 'tcp_half_close_counter'= TCP Half Closed; 'udp_counter'= UDP Count; 'ip_counter'= IP Count; 'other_counter'= Non TCP/UDP IP sessions; 'reverse_nat_tcp_counter'= Reverse NAT TCP; 'reverse_nat_udp_counter'= Reverse NAT UDP; 'tcp_syn_half_open_counter'= TCP SYN Half Open; 'conn_smp_alloc_counter'= Conn SMP Alloc; 'conn_smp_free_counter'= Conn SMP Free; 'conn_smp_aged_counter'= Conn SMP Aged; 'ssl_count_curr'= Curr SSL Count; 'ssl_count_total'= Total SSL Count; 'server_ssl_count_curr'= Current SSL Server Count; 'server_ssl_count_total'= Total SSL Server Count; 'client_ssl_reuse_total'= Total SSL Client Reuse; 'server_ssl_reuse_total'= Total SSL Server Reuse; 'ssl_failed_total'= Total SSL Failures; 'ssl_failed_ca_verification'= SSL Cert Auth Verification Errors; 'ssl_server_cert_error'= SSL Server Cert Errors; 'ssl_client_cert_auth_fail'= SSL Client Cert Auth Failures; 'total_ip_nat_conn'= Total IP Nat Conn; 'total_l2l3_conn'= Totl L2/L3 Connections; 'client_ssl_ctx_malloc_failure'= Client SSL Ctx malloc Failures; 'conn_type_0_available'= Conn Type 0 Available; 'conn_type_1_available'= Conn Type 1 Available; 'conn_type_2_available'= Conn Type 2 Available; 'conn_type_3_available'= Conn Type 3 Available; 'conn_type_4_available'= Conn Type 4 Available; 'conn_smp_type_0_available'= Conn SMP Type 0 Available; 'conn_smp_type_1_available'= Conn SMP Type 1 Available; 'conn_smp_type_2_available'= Conn SMP Type 2 Available; 'conn_smp_type_3_available'= Conn SMP Type 3 Available; 'conn_smp_type_4_available'= Conn SMP Type 4 Available; 'sctp-half-open- counter'= SCTP Half Open; 'sctp-est-counter'= SCTP Established; 'nonssl_bypass'= NON SSL Bypass Count; 'ssl_failsafe_total'= Total SSL Failsafe Count; 'ssl_forward_proxy_failed_handshake_total'= Total SSL Forward Proxy Failed Handshake Count; 'ssl_forward_proxy_failed_tcp_total'= Total SSL Forward Proxy Failed TCP Count; 'ssl_forward_proxy_failed_crypto_total'= Total SSL Forward Proxy Failed Crypto Count; 'ssl_forward_proxy_failed_cert_verify_total'= Total SSL Forward Proxy Failed Certificate Verification Count; 'ssl_forward_proxy_invalid_ocsp_stapling_total'= Total SSL Forward Proxy Invalid OCSP Stapling Count; 'ssl_forward_proxy_revoked_ocsp_total'= Total SSL Forward Proxy Revoked OCSP Response Count; 'ssl_forward_proxy_failed_cert_signing_total'= Total SSL Forward Proxy Failed Certificate Signing Count; 'ssl_forward_proxy_failed_ssl_version_total'= Total SSL Forward Proxy Unsupported version Count; 'ssl_forward_proxy_sni_bypass_total'= Total SSL Forward Proxy SNI Bypass Count; 'ssl_forward_proxy_client_auth_bypass_total'= Total SSL Forward Proxy Client Auth Bypass Count; 'conn_app_smp_alloc_counter'= Conn APP SMP Alloc; 'diameter_conn_counter'= Diameter Conn Count; 'diameter_conn_freed_counter'= Diameter Conn Freed; 'debug_tcp_counter'= Hidden TCP sessions for CGNv6 Stateless Technologies; 'debug_udp_counter'= Hidden UDP sessions for CGNv6 Stateless Technologies; 'total_fw_conn'= Total Firewall Conn; 'total_local_conn'= Total Local Conn; 'total_curr_conn'= Total Curr Conn; 'client_ssl_fatal_alert'= client ssl fatal alert; 'client_ssl_fin_rst'= client ssl fin rst; 'fp_session_fin_rst'= FP Session FIN/RST; 'server_ssl_fatal_alert'= server ssl fatal alert; 'server_ssl_fin_rst'= server ssl fin rst; 'client_template_int_err'= client template internal error; 'client_template_unknown_err'= client template unknown error; 'server_template_int_err'= server template int error; 'server_template_unknown_err'= server template unknown error; 'total_debug_conn'= Total Debug Conn; 'ssl_forward_proxy_failed_aflex_total'= Total SSL Forward Proxy AFLEX Count; 'ssl_forward_proxy_cert_subject_bypass_total'= Total SSL Forward Proxy Certificate Subject Bypass Count; 'ssl_forward_proxy_cert_issuer_bypass_total'= Total SSL Forward Proxy Certificate Issuer Bypass Count; 'ssl_forward_proxy_cert_san_bypass_total'= Total SSL Forward Proxy Certificate SAN Bypass Count; 'ssl_forward_proxy_no_sni_bypass_total'= Total SSL Forward Proxy No SNI Bypass Count; 'ssl_forward_proxy_no_sni_reset_total'= Total SSL Forward Proxy No SNI reset Count; 'ssl_forward_proxy_username_bypass_total'= Total SSL Forward Proxy Username Bypass Count; 'ssl_forward_proxy_ad_grpup_bypass_total'= Total SSL Forward Proxy AD-Group Bypass Count; 'diameter_concurrent_user_sessions_counter'= Diameter Concurrent User-Sessions;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    total_curr_conn (optional, any, None)
      Total Curr Conn


    reverse_nat_tcp_counter (optional, any, None)
      Reverse NAT TCP


    total_l2l3_conn (optional, any, None)
      Totl L2/L3 Connections


    tcp_est_counter (optional, any, None)
      TCP Established


    server_template_int_err (optional, any, None)
      server template int error


    total_l4_packet_count (optional, any, None)
      Total L4 Packet Count


    client_ssl_reuse_total (optional, any, None)
      Total SSL Client Reuse


    sctp_est_counter (optional, any, None)
      SCTP Established


    server_ssl_count_total (optional, any, None)
      Total SSL Server Count


    ip_counter (optional, any, None)
      IP Count


    conn_freed_counter (optional, any, None)
      Conn Freed


    tcp_syn_half_open_counter (optional, any, None)
      TCP SYN Half Open


    other_counter (optional, any, None)
      Non TCP/UDP IP sessions


    conn_type_3_available (optional, any, None)
      Conn Type 3 Available


    client_template_int_err (optional, any, None)
      client template internal error


    client_ssl_fatal_alert (optional, any, None)
      client ssl fatal alert


    conn_type_4_available (optional, any, None)
      Conn Type 4 Available


    conn_app_smp_alloc_counter (optional, any, None)
      Conn APP SMP Alloc


    conn_type_2_available (optional, any, None)
      Conn Type 2 Available


    conn_smp_type_0_available (optional, any, None)
      Conn SMP Type 0 Available


    total_l7_packet_count (optional, any, None)
      Total L7 Packet Count


    total_tcp_conn (optional, any, None)
      Total TCP Conn


    tcp_half_open_counter (optional, any, None)
      TCP Half Open


    server_ssl_fatal_alert (optional, any, None)
      server ssl fatal alert


    conn_type_1_available (optional, any, None)
      Conn Type 1 Available


    client_ssl_fin_rst (optional, any, None)
      client ssl fin rst


    ssl_count_total (optional, any, None)
      Total SSL Count


    sctp_half_open_counter (optional, any, None)
      SCTP Half Open


    total_local_conn (optional, any, None)
      Total Local Conn


    conn_smp_free_counter (optional, any, None)
      Conn SMP Free


    server_ssl_reuse_total (optional, any, None)
      Total SSL Server Reuse


    total_fw_conn (optional, any, None)
      Total Firewall Conn


    curr_free_conn (optional, any, None)
      Curr Free Conn


    udp_counter (optional, any, None)
      UDP Count


    conn_smp_type_2_available (optional, any, None)
      Conn SMP Type 2 Available


    diameter_concurrent_user_sessions_counter (optional, any, None)
      Diameter Concurrent User-Sessions


    conn_smp_aged_counter (optional, any, None)
      Conn SMP Aged


    conn_smp_type_1_available (optional, any, None)
      Conn SMP Type 1 Available


    client_template_unknown_err (optional, any, None)
      client template unknown error


    conn_type_0_available (optional, any, None)
      Conn Type 0 Available


    server_template_unknown_err (optional, any, None)
      server template unknown error


    diameter_conn_freed_counter (optional, any, None)
      Diameter Conn Freed


    total_l4_conn_proxy (optional, any, None)
      Total L4 Conn Proxy Count


    conn_smp_type_3_available (optional, any, None)
      Conn SMP Type 3 Available


    conn_smp_alloc_counter (optional, any, None)
      Conn SMP Alloc


    conn_counter (optional, any, None)
      Conn Count


    server_ssl_fin_rst (optional, any, None)
      server ssl fin rst


    total_l7_conn (optional, any, None)
      Total L7 Conn


    server_ssl_count_curr (optional, any, None)
      Current SSL Server Count


    fp_session_fin_rst (optional, any, None)
      FP Session FIN/RST


    total_ip_nat_conn (optional, any, None)
      Total IP Nat Conn


    conn_smp_type_4_available (optional, any, None)
      Conn SMP Type 4 Available


    diameter_conn_counter (optional, any, None)
      Diameter Conn Count


    tcp_half_close_counter (optional, any, None)
      TCP Half Closed


    ssl_count_curr (optional, any, None)
      Curr SSL Count


    reverse_nat_udp_counter (optional, any, None)
      Reverse NAT UDP


    total_l4_conn (optional, any, None)
      Total L4 Count



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

