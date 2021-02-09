.. _a10_slb_virtual_server_port_module:


a10_slb_virtual_server_port -- Configures A10 slb.virtual-server.port
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Virtual Port






Parameters
----------

  shared_partition_http_template (False, any, None)
    Reference a HTTP template from shared partition


  template_http_shared (False, any, None)
    HTTP Template Name


  protocol (True, any, None)
    'tcp'= TCP LB service; 'udp'= UDP Port; 'others'= for no tcp/udp protocol, do IP load balancing; 'diameter'= diameter port; 'dns-tcp'= DNS service over TCP; 'dns-udp'= DNS service over UDP; 'fast-http'= Fast HTTP Port; 'fix'= FIX Port; 'ftp'= File Transfer Protocol Port; 'ftp-proxy'= ftp proxy port; 'http'= HTTP Port; 'https'= HTTPS port; 'http2'= [Deprecated] HTTP2 Port; 'http2s'= [Deprecated] HTTP2 SSL port; 'imap'= imap proxy port; 'mlb'= Message based load balancing; 'mms'= Microsoft Multimedia Service Port; 'mysql'= mssql port; 'mssql'= mssql; 'pop3'= pop3 proxy port; 'radius'= RADIUS Port; 'rtsp'= Real Time Streaming Protocol Port; 'sip'= Session initiation protocol over UDP; 'sip-tcp'= Session initiation protocol over TCP; 'sips'= Session initiation protocol over TLS; 'smpp-tcp'= SMPP service over TCP; 'spdy'= spdy port; 'spdys'= spdys port; 'smtp'= SMTP Port; 'ssl-proxy'= Generic SSL proxy; 'ssli'= SSL insight; 'ssh'= SSH Port; 'tcp-proxy'= Generic TCP proxy; 'tftp'= TFTP Port; 'fast-fix'= Fast FIX port;


  precedence (False, any, None)
    Set auto NAT pool as higher precedence for source NAT


  trunk_fwd (False, any, None)
    Trunk interface number


  template_server_ssl (False, any, None)
    Server Side SSL Template Name


  reset_on_server_selection_fail (False, any, None)
    Send client reset when server selection fails


  virtual_server_name (optional, any, None)
    Key to identify parent object


  template_server_ssh (False, any, None)
    Server SSH Template (Server SSH Config Name)


  cpu_compute (False, any, None)
    enable cpu compute on virtual port


  uuid (False, any, None)
    uuid of the object


  alt_protocol2 (False, any, None)
    'tcp'= TCP LB service;


  extended_stats (False, any, None)
    Enable extended statistics on virtual port


  no_auto_up_on_aflex (False, any, None)
    Don't automatically mark vport up when aFleX is bound


  template_http_policy_shared (False, any, None)
    Http Policy Template Name


  template_smtp (False, any, None)
    SMTP Template (SMTP Config Name)


  redirect_to_https (False, any, None)
    Redirect HTTP to HTTPS


  rtp_sip_call_id_match (False, any, None)
    rtp traffic try to match the real server of sip smp call-id session


  support_http2 (False, any, None)
    Support HTTP2


  stats_data_action (False, any, None)
    'stats-data-enable'= Enable statistical data collection for virtual port; 'stats-data-disable'= Disable statistical data collection for virtual port;


  auto (False, any, None)
    Configure auto NAT for the vport


  template_dns_shared (False, any, None)
    DNS Template Name


  scaleout_device_group (False, any, None)
    Device group id


  def_selection_if_pref_failed (False, any, None)
    'def-selection-if-pref-failed'= Use default server selection method if prefer method failed; 'def-selection-if-pref-failed-disable'= Stop using default server selection method if prefer method failed;


  name (False, any, None)
    SLB Virtual Service Name


  shared_partition_pool (False, any, None)
    Specify NAT pool or pool group from shared partition


  port_number (True, any, None)
    Port


  template_client_ssl_shared (False, any, None)
    Client SSL Template Name


  eth_rev (False, any, None)
    Ethernet interface number


  view (False, any, None)
    Specify a GSLB View (ID)


  reset (False, any, None)
    Send client reset when connection number over limit


  template_udp (False, any, None)
    L4 UDP Template


  pool_shared (False, any, None)
    Specify NAT pool or pool group


  template_tcp_proxy_server (False, any, None)
    TCP Proxy Config Server (TCP Proxy Config name)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  use_alternate_port (False, any, None)
    Use alternate virtual port


  template_file_inspection (False, any, None)
    File Inspection service template (file-inspection template name)


  server_group (False, any, None)
    Bind a use-rcv-hop-for-resp Server Group to this Virtual Server (Server Group Name)


  force_routing_mode (False, any, None)
    Force routing mode


  template_client_ssh (False, any, None)
    Client SSH Template (Client SSH Config Name)


  template_client_ssl (False, any, None)
    Client SSL Template Name


  template_persist_cookie_shared (False, any, None)
    Cookie Persistence Template Name


  template_http_policy (False, any, None)
    http-policy template (http-policy template name)


  template_ftp (False, any, None)
    FTP port template (Ftp template name)


  state (True, any, None)
    State of the object to be created.


  shared_partition_persist_source_ip_template (False, any, None)
    Reference a persist source ip template from shared partition


  shared_partition_tcp (False, any, None)
    Reference a tcp template from shared partition


  template_dynamic_service_shared (False, any, None)
    Dynamic Service Template Name


  template_persist_destination_ip (False, any, None)
    Destination IP persistence (Destination IP persistence template name)


  template_virtual_port_shared (False, any, None)
    Virtual Port Template Name


  shared_partition_dns_template (False, any, None)
    Reference a dns template from shared partition


  shared_partition_virtual_port_template (False, any, None)
    Reference a Virtual Port template from shared partition


  template_udp_shared (False, any, None)
    UDP Template Name


  template_dynamic_service (False, any, None)
    Dynamic Service Template (dynamic-service template name)


  template_server_ssl_shared (False, any, None)
    Server SSL Template Name


  skip_rev_hash (False, any, None)
    Skip rev tuple hash insertion


  shared_partition_client_ssl_template (False, any, None)
    Reference a Client SSL template from shared partition


  aflex_scripts (False, any, None)
    Field aflex_scripts


    aflex (optional, any, None)
      aFleX Script Name


    aflex_shared (optional, any, None)
      aFleX Script Name



  alternate_port (False, any, None)
    Alternate Virtual Port


  acl_id_list (False, any, None)
    Field acl_id_list


    v_acl_id_seq_num (optional, any, None)
      Specify ACL precedence (sequence-number)


    acl_id_src_nat_pool (optional, any, None)
      Policy based Source NAT (NAT Pool or Pool Group)


    v_shared_partition_pool_id (optional, any, None)
      Policy based Source NAT from shared partition


    acl_id (optional, any, None)
      ACL id VPORT


    v_acl_id_src_nat_pool_shared (optional, any, None)
      Policy based Source NAT (NAT Pool or Pool Group)


    acl_id_src_nat_pool_shared (optional, any, None)
      Policy based Source NAT (NAT Pool or Pool Group)


    v_acl_id_src_nat_pool (optional, any, None)
      Policy based Source NAT (NAT Pool or Pool Group)


    shared_partition_pool_id (optional, any, None)
      Policy based Source NAT from shared partition


    acl_id_seq_num (optional, any, None)
      Specify ACL precedence (sequence-number)


    acl_id_shared (optional, any, None)
      acl id


    acl_id_seq_num_shared (optional, any, None)
      Specify ACL precedence (sequence-number)


    v_acl_id_seq_num_shared (optional, any, None)
      Specify ACL precedence (sequence-number)



  shared_partition_persist_cookie_template (False, any, None)
    Reference a persist cookie template from shared partition


  optimization_level (False, any, None)
    '0'= No optimization; '1'= Optimization level 1 (Experimental);


  template_dblb (False, any, None)
    DBLB Template (DBLB template name)


  range (False, any, None)
    Virtual Port range (Virtual Port range value)


  template_external_service_shared (False, any, None)
    External Service Template Name


  serv_sel_fail (False, any, None)
    Use alternate virtual port when server selection failure


  action (False, any, None)
    'enable'= Enable; 'disable'= Disable;


  no_logging (False, any, None)
    Do not log connection over limit event


  template_respmod_icap (False, any, None)
    ICAP respmod service template (respmod-icap template name)


  no_dest_nat (False, any, None)
    Disable destination NAT, this option only supports in wildcard VIP or when a connection is operated in SSLi + EP mode


  template_connection_reuse_shared (False, any, None)
    Connection Reuse Template Name


  shared_partition_connection_reuse_template (False, any, None)
    Reference a connection reuse template from shared partition


  oper (False, any, None)
    Field oper


    protocol (optional, any, None)
      'tcp'= TCP LB service; 'udp'= UDP Port; 'others'= for no tcp/udp protocol, do IP load balancing; 'diameter'= diameter port; 'dns-tcp'= DNS service over TCP; 'dns-udp'= DNS service over UDP; 'fast-http'= Fast HTTP Port; 'fix'= FIX Port; 'ftp'= File Transfer Protocol Port; 'ftp-proxy'= ftp proxy port; 'http'= HTTP Port; 'https'= HTTPS port; 'http2'= [Deprecated] HTTP2 Port; 'http2s'= [Deprecated] HTTP2 SSL port; 'imap'= imap proxy port; 'mlb'= Message based load balancing; 'mms'= Microsoft Multimedia Service Port; 'mysql'= mssql port; 'mssql'= mssql; 'pop3'= pop3 proxy port; 'radius'= RADIUS Port; 'rtsp'= Real Time Streaming Protocol Port; 'sip'= Session initiation protocol over UDP; 'sip-tcp'= Session initiation protocol over TCP; 'sips'= Session initiation protocol over TLS; 'smpp-tcp'= SMPP service over TCP; 'spdy'= spdy port; 'spdys'= spdys port; 'smtp'= SMTP Port; 'ssl-proxy'= Generic SSL proxy; 'ssli'= SSL insight; 'ssh'= SSH Port; 'tcp-proxy'= Generic TCP proxy; 'tftp'= TFTP Port; 'fast-fix'= Fast FIX port;


    cpu_count (optional, any, None)
      Field cpu_count


    level_str (optional, any, None)
      Field level_str


    http_url_hits (optional, any, None)
      Field http_url_hits


    port_number (optional, any, None)
      Port


    real_curr_conn (optional, any, None)
      Field real_curr_conn


    http_vport_cpu_list (optional, any, None)
      Field http_vport_cpu_list


    http_hits_list (optional, any, None)
      Field http_hits_list


    loc_override (optional, any, None)
      Field loc_override


    http_host_hits (optional, any, None)
      Field http_host_hits


    loc_list (optional, any, None)
      Field loc_list


    http_vport (optional, any, None)
      Field http_vport


    loc_max_depth (optional, any, None)
      Field loc_max_depth


    loc_last (optional, any, None)
      Field loc_last


    state (optional, any, None)
      Field state


    geo_location (optional, any, None)
      Field geo_location


    loc_success (optional, any, None)
      Field loc_success


    loc_error (optional, any, None)
      Field loc_error


    group_id (optional, any, None)
      Field group_id



  alt_protocol1 (False, any, None)
    'http'= HTTP Port;


  req_fail (False, any, None)
    Use alternate virtual port when L7 request fail


  template_sip (False, any, None)
    SIP template


  when_down (False, any, None)
    Use alternate virtual port when down


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  use_default_if_no_server (False, any, None)
    Use default forwarding if server selection failed


  template_policy (False, any, None)
    Policy Template (Policy template name)


  ipinip (False, any, None)
    Enable IP in IP


  template_tcp_proxy_shared (False, any, None)
    TCP Proxy Template name


  template_persist_source_ip (False, any, None)
    Source IP persistence (Source IP persistence template name)


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'curr_conn'= Current established connections; 'total_l4_conn'= Total L4 connections established; 'total_l7_conn'= Total L7 connections established; 'total_tcp_conn'= Total TCP connections established; 'total_conn'= Total connections established; 'total_fwd_bytes'= Bytes processed in forward direction; 'total_fwd_pkts'= Packets processed in forward direction; 'total_rev_bytes'= Bytes processed in reverse direction; 'total_rev_pkts'= Packets processed in reverse direction; 'total_dns_pkts'= Total DNS packets processed; 'total_mf_dns_pkts'= Total MF DNS packets; 'es_total_failure_actions'= Total failure actions; 'compression_bytes_before'= Data into compression engine; 'compression_bytes_after'= Data out of compression engine; 'compression_hit'= Number of requests compressed; 'compression_miss'= Number of requests NOT compressed; 'compression_miss_no_client'= Compression miss no client; 'compression_miss_template_exclusion'= Compression miss template exclusion; 'curr_req'= Current requests; 'total_req'= Total requests; 'total_req_succ'= Total successful requests; 'peak_conn'= Peak connections; 'curr_conn_rate'= Current connection rate; 'last_rsp_time'= Last response time; 'fastest_rsp_time'= Fastest response time; 'slowest_rsp_time'= Slowest response time; 'loc_permit'= Geo-location Permit count; 'loc_deny'= Geo-location Deny count; 'loc_conn'= Geo-location Connection count; 'curr_ssl_conn'= Current SSL connections; 'total_ssl_conn'= Total SSL connections; 'backend-time-to-first- byte'= Backend Time from Request to Response First Byte; 'backend-time-to-last- byte'= Backend Time from Request to Response Last Byte; 'in-latency'= Request Latency at Thunder; 'out-latency'= Response Latency at Thunder; 'total_fwd_bytes_out'= Bytes processed in forward direction (outbound); 'total_fwd_pkts_out'= Packets processed in forward direction (outbound); 'total_rev_bytes_out'= Bytes processed in reverse direction (outbound); 'total_rev_pkts_out'= Packets processed in reverse direction (outbound); 'curr_req_rate'= Current request rate; 'curr_resp'= Current response; 'total_resp'= Total response; 'total_resp_succ'= Total successful responses; 'curr_resp_rate'= Current response rate; 'curr_conn_overflow'= Current connection counter overflow count; 'dnsrrl_total_allowed'= DNS Response-Rate- Limiting Total Responses Allowed; 'dnsrrl_total_dropped'= DNS Response-Rate- Limiting Total Responses Dropped; 'dnsrrl_total_slipped'= DNS Response-Rate- Limiting Total Responses Slipped; 'dnsrrl_bad_fqdn'= DNS Response-Rate-Limiting Bad FQDN; 'throughput-bits-per-sec'= Throughput in bits/sec; 'dynamic-memory- alloc'= dynamic memory (bytes) allocated by the vport; 'dynamic-memory-free'= dynamic memory (bytes) allocated by the vport; 'dynamic-memory'= dynamic memory (bytes) used by the vport(alloc-free); 'ip_only_lb_fwd_bytes'= IP-Only-LB Bytes processed in forward direction; 'ip_only_lb_rev_bytes'= IP-Only-LB Bytes processed in reverse direction; 'ip_only_lb_fwd_pkts'= IP-Only-LB Packets processed in forward direction; 'ip_only_lb_rev_pkts'= IP-Only-LB Packets processed in reverse direction;



  template_diameter (False, any, None)
    Diameter Template (diameter template name)


  ha_conn_mirror (False, any, None)
    Enable for HA Conn sync


  template_policy_shared (False, any, None)
    Policy Template Name


  shared_partition_cache_template (False, any, None)
    Reference a Cache template from shared partition


  when_down_protocol2 (False, any, None)
    Use alternate virtual port when down


  eth_fwd (False, any, None)
    Ethernet interface number


  shared_partition_persist_ssl_sid_template (False, any, None)
    Reference a persist SSL SID template from shared partition


  template_tcp (False, any, None)
    TCP Template Name


  message_switching (False, any, None)
    Message switching


  clientip_sticky_nat (False, any, None)
    Prefer to use same source NAT address for a client


  pool (False, any, None)
    Specify NAT pool or pool group


  on_syn (False, any, None)
    Enable for HA Conn sync for l4 tcp sessions on SYN


  ip_only_lb (False, any, None)
    Enable IP-Only LB mode


  template_http (False, any, None)
    HTTP Template Name


  use_rcv_hop_group (False, any, None)
    Set use-rcv-hop group


  template_connection_reuse (False, any, None)
    Connection Reuse Template (Connection Reuse Template Name)


  l7_hardware_assist (False, any, None)
    FPGA assist L7 packet parsing


  enable_playerid_check (False, any, None)
    Enable playerid checks on UDP packets once the AX is in active mode


  shared_partition_http_policy_template (False, any, None)
    Reference a http policy template from shared partition


  template_diameter_shared (False, any, None)
    Diameter Template Name


  template_persist_destination_ip_shared (False, any, None)
    Destination IP Persistence Template Name


  memory_compute (False, any, None)
    enable dynamic memory compute on virtual port


  ansible_port (True, any, None)
    Port for AXAPI authentication


  resolve_web_cat_list (False, any, None)
    Web Category List name


  template_smpp (False, any, None)
    SMPP template


  rate (False, any, None)
    Specify the log message rate


  template_cache (False, any, None)
    RAM caching template (Cache Template Name)


  template_persist_cookie (False, any, None)
    Cookie persistence (Cookie persistence template name)


  persist_type (False, any, None)
    'src-dst-ip-swap-persist'= Create persist session after source IP and destination IP swap; 'use-src-ip-for-dst-persist'= Use the source IP to create a destination persist session; 'use-dst-ip-for-src-persist'= Use the destination IP to create source IP persist session;


  use_rcv_hop_for_resp (False, any, None)
    Use receive hop for response to client(For packets on default-vlan, also config 'vlan-global enable-def-vlan-l2-forwarding'.)


  scaleout_bucket_count (False, any, None)
    Number of traffic buckets


  shared_partition_external_service_template (False, any, None)
    Reference a external service template from shared partition


  trunk_rev (False, any, None)
    Trunk interface number


  template_tcp_shared (False, any, None)
    TCP Template Name


  acl_name_list (False, any, None)
    Field acl_name_list


    v_acl_name_seq_num (optional, any, None)
      Specify ACL precedence (sequence-number)


    acl_name_seq_num (optional, any, None)
      Specify ACL precedence (sequence-number)


    acl_name_src_nat_pool_shared (optional, any, None)
      Policy based Source NAT (NAT Pool or Pool Group)


    acl_name (optional, any, None)
      Apply an access list name (Named Access List)


    acl_name_seq_num_shared (optional, any, None)
      Specify ACL precedence (sequence-number)


    shared_partition_pool_name (optional, any, None)
      Policy based Source NAT from shared partition


    v_acl_name_src_nat_pool (optional, any, None)
      Policy based Source NAT (NAT Pool or Pool Group)


    v_acl_name_seq_num_shared (optional, any, None)
      Specify ACL precedence (sequence-number)


    acl_name_src_nat_pool (optional, any, None)
      Policy based Source NAT (NAT Pool or Pool Group)


    acl_name_shared (optional, any, None)
      Apply an access list name (Named Access List)


    v_shared_partition_pool_name (optional, any, None)
      Policy based Source NAT from shared partition


    v_acl_name_src_nat_pool_shared (optional, any, None)
      Policy based Source NAT (NAT Pool or Pool Group)



  template_dns (False, any, None)
    DNS template (DNS template name)


  template_reqmod_icap (False, any, None)
    ICAP reqmod template (reqmod-icap template name)


  template_external_service (False, any, None)
    External service template (external-service template name)


  shared_partition_tcp_proxy_template (False, any, None)
    Reference a TCP Proxy template from shared partition


  service_group (False, any, None)
    Bind a Service Group to this Virtual Server (Service Group Name)


  shared_partition_policy_template (False, any, None)
    Reference a policy template from shared partition


  waf_template (False, any, None)
    WAF template (WAF Template Name)


  template_cache_shared (False, any, None)
    Cache Template Name


  template_ssli (False, any, None)
    SSLi template (SSLi Template Name)


  ip_map_list (False, any, None)
    Enter name of IP Map List to be bound (IP Map List Name)


  use_cgnv6 (False, any, None)
    Follow CGNv6 source NAT configuration


  shared_partition_dynamic_service_template (False, any, None)
    Reference a dynamic service template from shared partition


  template_tcp_proxy (False, any, None)
    TCP Proxy Template Name


  template_tcp_proxy_client (False, any, None)
    TCP Proxy Config Client (TCP Proxy Config name)


  template_persist_ssl_sid (False, any, None)
    SSL SID persistence (SSL SID persistence template name)


  gslb_enable (False, any, None)
    Enable Global Server Load Balancing


  template_imap_pop3 (False, any, None)
    IMAP/POP3 Template (IMAP/POP3 Config Name)


  shared_partition_server_ssl_template (False, any, None)
    Reference a SSL Server template from shared partition


  shared_partition_persist_destination_ip_template (False, any, None)
    Reference a persist destination ip template from shared partition


  conn_limit (False, any, None)
    Connection Limit


  alternate_port_number (False, any, None)
    Virtual Port


  snat_on_vip (False, any, None)
    Enable source NAT traffic against VIP


  template_persist_source_ip_shared (False, any, None)
    Source IP Persistence Template Name


  stats (False, any, None)
    Field stats


    curr_req (optional, any, None)
      Current requests


    protocol (optional, any, None)
      'tcp'= TCP LB service; 'udp'= UDP Port; 'others'= for no tcp/udp protocol, do IP load balancing; 'diameter'= diameter port; 'dns-tcp'= DNS service over TCP; 'dns-udp'= DNS service over UDP; 'fast-http'= Fast HTTP Port; 'fix'= FIX Port; 'ftp'= File Transfer Protocol Port; 'ftp-proxy'= ftp proxy port; 'http'= HTTP Port; 'https'= HTTPS port; 'http2'= [Deprecated] HTTP2 Port; 'http2s'= [Deprecated] HTTP2 SSL port; 'imap'= imap proxy port; 'mlb'= Message based load balancing; 'mms'= Microsoft Multimedia Service Port; 'mysql'= mssql port; 'mssql'= mssql; 'pop3'= pop3 proxy port; 'radius'= RADIUS Port; 'rtsp'= Real Time Streaming Protocol Port; 'sip'= Session initiation protocol over UDP; 'sip-tcp'= Session initiation protocol over TCP; 'sips'= Session initiation protocol over TLS; 'smpp-tcp'= SMPP service over TCP; 'spdy'= spdy port; 'spdys'= spdys port; 'smtp'= SMTP Port; 'ssl-proxy'= Generic SSL proxy; 'ssli'= SSL insight; 'ssh'= SSH Port; 'tcp-proxy'= Generic TCP proxy; 'tftp'= TFTP Port; 'fast-fix'= Fast FIX port;


    curr_req_rate (optional, any, None)
      Current request rate


    total_rev_bytes (optional, any, None)
      Bytes processed in reverse direction


    total_rev_pkts_out (optional, any, None)
      Packets processed in reverse direction (outbound)


    curr_ssl_conn (optional, any, None)
      Current SSL connections


    total_fwd_bytes_out (optional, any, None)
      Bytes processed in forward direction (outbound)


    loc_deny (optional, any, None)
      Geo-location Deny count


    out_latency (optional, any, None)
      Response Latency at Thunder


    curr_conn_rate (optional, any, None)
      Current connection rate


    curr_resp (optional, any, None)
      Current response


    total_fwd_bytes (optional, any, None)
      Bytes processed in forward direction


    curr_resp_rate (optional, any, None)
      Current response rate


    dnsrrl_total_slipped (optional, any, None)
      DNS Response-Rate-Limiting Total Responses Slipped


    total_resp_succ (optional, any, None)
      Total successful responses


    throughput_bits_per_sec (optional, any, None)
      Throughput in bits/sec


    compression_miss (optional, any, None)
      Number of requests NOT compressed


    loc_permit (optional, any, None)
      Geo-location Permit count


    peak_conn (optional, any, None)
      Peak connections


    fastest_rsp_time (optional, any, None)
      Fastest response time


    total_fwd_pkts (optional, any, None)
      Packets processed in forward direction


    total_tcp_conn (optional, any, None)
      Total TCP connections established


    total_mf_dns_pkts (optional, any, None)
      Total MF DNS packets


    dynamic_memory (optional, any, None)
      dynamic memory (bytes) used by the vport(alloc-free)


    curr_conn_overflow (optional, any, None)
      Current connection counter overflow count


    backend_time_to_last_byte (optional, any, None)
      Backend Time from Request to Response Last Byte


    dnsrrl_bad_fqdn (optional, any, None)
      DNS Response-Rate-Limiting Bad FQDN


    total_dns_pkts (optional, any, None)
      Total DNS packets processed


    loc_conn (optional, any, None)
      Geo-location Connection count


    ip_only_lb_fwd_pkts (optional, any, None)
      IP-Only-LB Packets processed in forward direction


    compression_bytes_after (optional, any, None)
      Data out of compression engine


    in_latency (optional, any, None)
      Request Latency at Thunder


    total_req (optional, any, None)
      Total requests


    ip_only_lb_fwd_bytes (optional, any, None)
      IP-Only-LB Bytes processed in forward direction


    compression_bytes_before (optional, any, None)
      Data into compression engine


    total_rev_bytes_out (optional, any, None)
      Bytes processed in reverse direction (outbound)


    last_rsp_time (optional, any, None)
      Last response time


    curr_conn (optional, any, None)
      Current established connections


    total_fwd_pkts_out (optional, any, None)
      Packets processed in forward direction (outbound)


    dnsrrl_total_dropped (optional, any, None)
      DNS Response-Rate-Limiting Total Responses Dropped


    dnsrrl_total_allowed (optional, any, None)
      DNS Response-Rate-Limiting Total Responses Allowed


    backend_time_to_first_byte (optional, any, None)
      Backend Time from Request to Response First Byte


    compression_miss_no_client (optional, any, None)
      Compression miss no client


    es_total_failure_actions (optional, any, None)
      Total failure actions


    ip_only_lb_rev_pkts (optional, any, None)
      IP-Only-LB Packets processed in reverse direction


    total_ssl_conn (optional, any, None)
      Total SSL connections


    compression_miss_template_exclusion (optional, any, None)
      Compression miss template exclusion


    total_rev_pkts (optional, any, None)
      Packets processed in reverse direction


    total_l7_conn (optional, any, None)
      Total L7 connections established


    total_req_succ (optional, any, None)
      Total successful requests


    ip_only_lb_rev_bytes (optional, any, None)
      IP-Only-LB Bytes processed in reverse direction


    total_resp (optional, any, None)
      Total response


    total_conn (optional, any, None)
      Total connections established


    port_number (optional, any, None)
      Port


    compression_hit (optional, any, None)
      Number of requests compressed


    slowest_rsp_time (optional, any, None)
      Slowest response time


    total_l4_conn (optional, any, None)
      Total L4 connections established



  template_scaleout (False, any, None)
    Scaleout template (Scaleout template name)


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  expand (False, any, None)
    expand syn-cookie with timestamp and wscale


  syn_cookie (False, any, None)
    Enable syn-cookie


  template_fix (False, any, None)
    FIX template (FIX Template Name)


  ansible_password (True, any, None)
    Password for AXAPI authentication


  template_virtual_port (False, any, None)
    Virtual port template (Virtual port template name)


  auth_cfg (False, any, None)
    Field auth_cfg


    aaa_policy (optional, any, None)
      Specify AAA policy name to bind to the virtual port



  template_persist_ssl_sid_shared (False, any, None)
    SSL SID Persistence Template Name


  shared_partition_diameter_template (False, any, None)
    Reference a Diameter template from shared partition


  secs (False, any, None)
    Specify the interval in seconds


  shared_partition_udp (False, any, None)
    Reference a UDP template from shared partition


  user_tag (False, any, None)
    Customized tag


  port_translation (False, any, None)
    Enable port translation under no-dest-nat









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

