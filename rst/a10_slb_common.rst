.. _a10_slb_common_module:


a10_slb_common -- Configures A10 slb.common
===========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

SLB related commands






Parameters
----------

  range_end (False, any, None)
    port range end


  oper (False, any, None)
    Field oper


    server_auto_reselect (optional, any, None)
      Field server_auto_reselect



  low_latency (False, any, None)
    Enable low latency mode


  msl_time (False, any, None)
    Configure maximum session life, default is 2 seconds (1-40 seconds, default is 2 seconds)


  entity (False, any, None)
    'server'= Graceful shutdown server/port only; 'virtual-server'= Graceful shutdown virtual server/port only;


  response_type (False, any, None)
    'single-answer'= Only cache DNS response with single answer; 'round-robin'= Round robin;


  dns_cache_enable (False, any, None)
    Enable DNS cache


  disable_port_masking (False, any, None)
    Disable masking of ports for CPU hashing


  max_http_header_count (False, any, None)
    Set maximum number of HTTP headers allowed


  dns_response_rate_limiting (False, any, None)
    Field dns_response_rate_limiting


    max_table_entries (optional, any, None)
      Maximum number of entries allowed


    uuid (optional, any, None)
      uuid of the object



  ecmp_hash (False, any, None)
    'system-default'= Use system default ecmp hashing algorithm; 'connection- based'= Use connection information for hashing;


  conn_rate_limit (False, any, None)
    Field conn_rate_limit


    src_ip_list (optional, any, None)
      Field src_ip_list



  compress_block_size (False, any, None)
    Set compression block size (Compression block size in bytes)


  max_buff_queued_per_conn (False, any, None)
    Set per connection buffer threshold (Buffer value range 128-4096)


  log_for_reset_unknown_conn (False, any, None)
    Log when rate exceed


  extended_stats (False, any, None)
    Enable global slb extended statistics


  ssli_sni_hash_enable (False, any, None)
    Enable SSLi SNI hash table


  no_auto_up_on_aflex (False, any, None)
    Don't automatically mark vport up when aFleX is bound


  graceful_shutdown (False, any, None)
    1-65535, in unit of seconds


  ddos_protection (False, any, None)
    Field ddos_protection


    packets_per_second (optional, any, None)
      Field packets_per_second


    logging (optional, any, None)
      Field logging


    ipd_enable_toggle (optional, any, None)
      'enable'= Enable SLB DDoS protection; 'disable'= Disable SLB DDoS protection (default);



  hw_compression (False, any, None)
    Use hardware compression


  fast_path_disable (False, any, None)
    Disable fast path in SLB processing


  ttl_threshold (False, any, None)
    Only cache DNS response with longer TTL


  gateway_health_check (False, any, None)
    Enable gateway health check


  dns_cache_age (False, any, None)
    Set DNS cache entry age, default is 300 seconds (1-1000000 seconds, default is 300 seconds)


  ansible_port (True, any, None)
    Port for AXAPI authentication


  buff_thresh (False, any, None)
    Set buffer threshold


  buff_thresh_hw_buff (False, any, None)
    Set hardware buffer threshold


  pkt_rate_for_reset_unknown_conn (False, any, None)
    Field pkt_rate_for_reset_unknown_conn


  timeout (False, any, None)
    Specify the healthcheck timeout value, default is 15 seconds (Timeout Value, in seconds (default 15))


  override_port (False, any, None)
    Enable override port in DSR health check mode


  snat_gwy_for_l3 (False, any, None)
    Use source NAT gateway for L3 traffic for transparent mode


  buff_thresh_relieve_thresh (False, any, None)
    Relieve threshold


  interval (False, any, None)
    Specify the healthcheck interval, default is 5 seconds (Interval Value, in seconds (default 5))


  honor_server_response_ttl (False, any, None)
    Honor the server reponse TTL


  dns_vip_stateless (False, any, None)
    Enable DNS VIP stateless mode


  ansible_username (True, any, None)
    Username for AXAPI authentication


  service_group_on_no_dest_nat_vports (False, any, None)
    'allow-same'= Allow the binding service-group on no-dest-nat virtual ports; 'enforce-different'= Enforce that the same service-group can not be bound on different no-dest-nat virtual ports;


  graceful_shutdown_enable (False, any, None)
    Enable graceful shutdown


  max_remote_rate (False, any, None)
    Set maximum remote rate


  hw_syn_rr (False, any, None)
    Configure hardware SYN round robin (range 1-500000)


  exclude_destination (False, any, None)
    'local'= Maximum local rate; 'remote'= Maximum remote rate;  (Maximum rates)


  dsr_health_check_enable (False, any, None)
    Enable dsr-health-check (direct server return health check)


  use_mss_tab (False, any, None)
    Use MSS based on internal table for SLB processing


  buff_thresh_sys_buff_low (False, any, None)
    Set low water mark of system buffer


  scale_out (False, any, None)
    Enable SLB scale out


  disable_persist_scoring (False, any, None)
    Disable Persist Scoring


  after_disable (False, any, None)
    Graceful shutdown after disable server/port and/or virtual server/port


  rate_limit_logging (False, any, None)
    Configure rate limit logging


  reset_stale_session (False, any, None)
    Send reset if session in delete queue receives a SYN packet


  ipv4_offset (False, any, None)
    IPv4 Octet Offset for Hash


  state (True, any, None)
    State of the object to be created.


  allow_in_gateway_mode (False, any, None)
    Use source NAT gateway for L3 traffic for gateway mode


  disable_server_auto_reselect (False, any, None)
    Disable auto reselection of server


  dns_cache_entry_size (False, any, None)
    Set DNS cache entry size, default is 256 bytes (1-4096 bytes, default is 256 bytes)


  player_id_check_enable (False, any, None)
    Enable the Player id check


  range_start (False, any, None)
    port range start


  max_local_rate (False, any, None)
    Set maximum local rate


  stats_data_disable (False, any, None)
    Disable global slb data statistics


  drop_icmp_to_vip_when_vip_down (False, any, None)
    Drop ICMP to VIP when VIP down


  snat_preserve (False, any, None)
    Field snat_preserve


    range (optional, any, None)
      Field range



  snat_on_vip (False, any, None)
    Enable source NAT traffic against VIP


  mss_table (False, any, None)
    Set MSS table (128-750, default is 536)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  resolve_port_conflict (False, any, None)
    Enable client port service port conflicts


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  enable_l7_req_acct (False, any, None)
    Enable L7 request accounting


  uuid (False, any, None)
    uuid of the object


  ansible_password (True, any, None)
    Password for AXAPI authentication


  l2l3_trunk_lb_disable (False, any, None)
    Disable L2/L3 trunk LB


  disable_adaptive_resource_check (False, any, None)
    Disable adaptive resource check based on buffer usage


  range (False, any, None)
    auto translate port range


  auto_nat_no_ip_refresh (False, any, None)
    'enable'= enable; 'disable'= disable;


  sort_res (False, any, None)
    Enable SLB sorting of resource names


  stateless_sg_multi_binding (False, any, None)
    Enable stateless service groups to be assigned to multiple L2/L3 DSR VIPs


  buff_thresh_sys_buff_high (False, any, None)
    Set high water mark of system buffer


  software (False, any, None)
    Software









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

