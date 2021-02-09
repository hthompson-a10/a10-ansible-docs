.. _a10_system_module:


a10_system -- Configures A10 system
===================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure System Parameters






Parameters
----------

  cosq_show (False, any, None)
    Field cosq_show


    uuid (optional, any, None)
      uuid of the object



  app_performance (False, any, None)
    Field app_performance


    sampling_enable (optional, any, None)
      Field sampling_enable


    uuid (optional, any, None)
      uuid of the object



  management_interface_mode (False, any, None)
    Field management_interface_mode


    dedicated (optional, any, None)
      Set management interface in dedicated mode


    non_dedicated (optional, any, None)
      Set management interface in non-dedicated mode



  trunk_xaui_hw_hash (False, any, None)
    Field trunk_xaui_hw_hash


    mode (optional, any, None)
      Set HW hash mode, default is 6 (1=dst-mac 2=src-mac 3=src-dst-mac 4=src-ip 5=dst-ip 6=rtag6 7=rtag7)


    uuid (optional, any, None)
      uuid of the object



  timeout_value (False, any, None)
    Field timeout_value


    ftp (optional, any, None)
      set timeout to stop ftp transfer in seconds, 0 is no limit


    http (optional, any, None)
      set timeout to stop http transfer in seconds, 0 is no limit


    uuid (optional, any, None)
      uuid of the object


    https (optional, any, None)
      set timeout to stop https transfer in seconds, 0 is no limit


    tftp (optional, any, None)
      set timeout to stop tftp transfer in seconds, 0 is no limit


    scp (optional, any, None)
      set timeout to stop scp transfer in seconds, 0 is no limit


    sftp (optional, any, None)
      set timeout to stop sftp transfer in seconds, 0 is no limit



  tcp (False, any, None)
    Field tcp


    sampling_enable (optional, any, None)
      Field sampling_enable


    uuid (optional, any, None)
      uuid of the object



  modify_port (False, any, None)
    Field modify_port


    port_index (optional, any, None)
      port index to be configured (Specify port index)


    port_number (optional, any, None)
      port number to be configured (Specify port number)



  session_reclaim_limit (False, any, None)
    Field session_reclaim_limit


    nscan_limit (optional, any, None)
      smp session scan limit (number of smp sessions per scan)


    scan_freq (optional, any, None)
      smp session scan frequency (scan per second)


    uuid (optional, any, None)
      uuid of the object



  bandwidth (False, any, None)
    Field bandwidth


    sampling_enable (optional, any, None)
      Field sampling_enable


    uuid (optional, any, None)
      uuid of the object



  session (False, any, None)
    Field session


    sampling_enable (optional, any, None)
      Field sampling_enable


    uuid (optional, any, None)
      uuid of the object



  shutdown (False, any, None)
    Field shutdown


    uuid (optional, any, None)
      uuid of the object



  deep_hrxq (False, any, None)
    Field deep_hrxq


    enable (optional, any, None)
      Field enable



  add_port (False, any, None)
    Field add_port


    port_index (optional, any, None)
      port index to be configured (Specify port index)



  tcp_stats (False, any, None)
    Field tcp_stats


    sampling_enable (optional, any, None)
      Field sampling_enable


    uuid (optional, any, None)
      uuid of the object



  ip_stats (False, any, None)
    Field ip_stats


    sampling_enable (optional, any, None)
      Field sampling_enable


    uuid (optional, any, None)
      uuid of the object



  add_cpu_core (False, any, None)
    Field add_cpu_core


    core_index (optional, any, None)
      core index to be added (Specify core index)



  icmp_rate (False, any, None)
    Field icmp_rate


    sampling_enable (optional, any, None)
      Field sampling_enable


    uuid (optional, any, None)
      uuid of the object



  queuing_buffer (False, any, None)
    Field queuing_buffer


    enable (optional, any, None)
      Enable/Disable micro-burst traffic support


    uuid (optional, any, None)
      uuid of the object



  log_cpu_interval (False, any, None)
    Log high CPU interval (Specify consecutive seconds before logging high CPU)


  cm_update_file_name_ref (False, any, None)
    Field cm_update_file_name_ref


    source_name (optional, any, None)
      bind source name


    id (optional, any, None)
      Specify unique Partition id


    dest_name (optional, any, None)
      bind dest name



  ve_mac_scheme (False, any, None)
    Field ve_mac_scheme


    ve_mac_scheme_val (optional, any, None)
      'hash-based'= Hash-based using the VE number; 'round-robin'= Round Robin scheme; 'system-mac'= Use system MAC address;


    uuid (optional, any, None)
      uuid of the object



  all_vlan_limit (False, any, None)
    Field all_vlan_limit


    unknown_ucast (optional, any, None)
      unknown unicast packets (per second limit)


    bcast (optional, any, None)
      broadcast packets (per second limit)


    uuid (optional, any, None)
      uuid of the object


    ipmcast (optional, any, None)
      IP multicast packets (per second limit)


    mcast (optional, any, None)
      multicast packets (per second limit)



  shell_privileges (False, any, None)
    Field shell_privileges


    uuid (optional, any, None)
      uuid of the object



  environment (False, any, None)
    Field environment


    uuid (optional, any, None)
      uuid of the object



  attack (False, any, None)
    System Attack


  fpga_core_crc (False, any, None)
    Field fpga_core_crc


    monitor_disable (optional, any, None)
      Disable FPGA Core CRC error monitoring and act on it


    uuid (optional, any, None)
      uuid of the object


    reboot_enable (optional, any, None)
      Enable system reboot if system encounters FPGA Core CRC error



  memory (False, any, None)
    Field memory


    sampling_enable (optional, any, None)
      Field sampling_enable


    uuid (optional, any, None)
      uuid of the object



  io_cpu (False, any, None)
    Field io_cpu


    max_cores (optional, any, None)
      max number of IO cores (Specify number of cores)



  del_port (False, any, None)
    Field del_port


    port_index (optional, any, None)
      port index to be configured (Specify port index)



  src_ip_hash_enable (False, any, None)
    Enable source ip hash


  inuse_port_list (False, any, None)
    Field inuse_port_list


    uuid (optional, any, None)
      uuid of the object



  ndisc_ra (False, any, None)
    Field ndisc_ra


    sampling_enable (optional, any, None)
      Field sampling_enable


    uuid (optional, any, None)
      uuid of the object



  dns (False, any, None)
    Field dns


    sampling_enable (optional, any, None)
      Field sampling_enable


    uuid (optional, any, None)
      uuid of the object



  glid (False, any, None)
    Apply limits to the whole system


  link_monitor (False, any, None)
    Field link_monitor


    enable (optional, any, None)
      Enable Link Monitoring


    disable (optional, any, None)
      Disable Link Monitoring



  ipmi (False, any, None)
    Field ipmi


    reset (optional, any, None)
      Reset IPMI Controller


    ip (optional, any, None)
      Field ip


    ipsrc (optional, any, None)
      Field ipsrc


    tool (optional, any, None)
      Field tool


    user (optional, any, None)
      Field user



  spe_profile (False, any, None)
    Field spe_profile


    action (optional, any, None)
      'ipv4-only'= Enable IPv4 HW forward entries only; 'ipv6-only'= Enable IPv6 HW forward entries only; 'ipv4-ipv6'= Enable Both IPv4/IPv6 HW forward entries (shared);



  cpu_hyper_thread (False, any, None)
    Field cpu_hyper_thread


    enable (optional, any, None)
      Enable CPU Hyperthreading


    disable (optional, any, None)
      Disable CPU Hyperthreading



  port_list (False, any, None)
    Field port_list


    uuid (optional, any, None)
      uuid of the object



  trunk_hw_hash (False, any, None)
    Field trunk_hw_hash


    mode (optional, any, None)
      Set HW hash mode, default is 6 (1=dst-mac 2=src-mac 3=src-dst-mac 4=src-ip 5=dst-ip 6=rtag6 7=rtag7)


    uuid (optional, any, None)
      uuid of the object



  icmp (False, any, None)
    Field icmp


    sampling_enable (optional, any, None)
      Field sampling_enable


    uuid (optional, any, None)
      uuid of the object



  ip6_stats (False, any, None)
    Field ip6_stats


    sampling_enable (optional, any, None)
      Field sampling_enable


    uuid (optional, any, None)
      uuid of the object



  ipsec (False, any, None)
    Field ipsec


    fpga_decrypt (optional, any, None)
      Field fpga_decrypt


    crypto_core (optional, any, None)
      Crypto cores assigned for IPsec processing


    uuid (optional, any, None)
      uuid of the object


    packet_round_robin (optional, any, None)
      Enable packet round robin for IPsec packets


    crypto_mem (optional, any, None)
      Crypto memory percentage assigned for IPsec processing (rounded to increments of 10)



  ansible_port (True, any, None)
    Port for AXAPI authentication


  guest_file (False, any, None)
    Field guest_file


    uuid (optional, any, None)
      uuid of the object



  geoloc_name_helper (False, any, None)
    Field geoloc_name_helper


    sampling_enable (optional, any, None)
      Field sampling_enable


    uuid (optional, any, None)
      uuid of the object



  domain_list_hitcount_enable (False, any, None)
    Enable class list hit count


  attack_log (False, any, None)
    log attack anomalies


  syslog_time_msec (False, any, None)
    Field syslog_time_msec


    enable_flag (optional, any, None)
      Field enable_flag



  class_list_hitcount_enable (False, any, None)
    Enable class list hit count


  ddos_log (False, any, None)
    log DDoS attack anomalies


  probe_network_devices (False, any, None)
    Field probe_network_devices


  data_cpu (False, any, None)
    Field data_cpu


    uuid (optional, any, None)
      uuid of the object



  ports (False, any, None)
    Field ports


    link_detection_interval (optional, any, None)
      Link detection interval in msecs


    uuid (optional, any, None)
      uuid of the object



  hrxq_status (False, any, None)
    Field hrxq_status


    uuid (optional, any, None)
      uuid of the object



  geo_db_hitcount_enable (False, any, None)
    Enable Geolocation database hit count


  counter_lib_accounting (False, any, None)
    Field counter_lib_accounting


    uuid (optional, any, None)
      uuid of the object



  control_cpu (False, any, None)
    Field control_cpu


    uuid (optional, any, None)
      uuid of the object



  ansible_username (True, any, None)
    Username for AXAPI authentication


  multi_queue_support (False, any, None)
    Field multi_queue_support


    enable (optional, any, None)
      Enable Multi-Queue-Support



  domain_list_info (False, any, None)
    Field domain_list_info


    uuid (optional, any, None)
      uuid of the object



  promiscuous_mode (False, any, None)
    Run in promiscous mode settings


  geolocation_file (False, any, None)
    Field geolocation_file


    uuid (optional, any, None)
      uuid of the object


    error_info (optional, any, None)
      Field error_info



  hardware (False, any, None)
    Field hardware


    uuid (optional, any, None)
      uuid of the object



  radius (False, any, None)
    Field radius


    server (optional, any, None)
      Field server



  inuse_cpu_list (False, any, None)
    Field inuse_cpu_list


    uuid (optional, any, None)
      uuid of the object



  shared_poll_mode (False, any, None)
    Field shared_poll_mode


    enable (optional, any, None)
      Enable shared poll mode


    disable (optional, any, None)
      Disable shared poll mode



  password_policy (False, any, None)
    Field password_policy


    aging (optional, any, None)
      'Strict'= Strict= Max Age-60 Days; 'Medium'= Medium= Max Age- 90 Days; 'Simple'= Simple= Max Age-120 Days;


    complexity (optional, any, None)
      'Strict'= Strict= Min length=8, Min Lower Case=2, Min Upper Case=2, Min Numbers=2, Min Special Character=1; 'Medium'= Medium= Min length=6, Min Lower Case=2, Min Upper Case=2, Min Numbers=1, Min Special Character=1; 'Simple'= Simple= Min length=4, Min Lower Case=1, Min Upper Case=1, Min Numbers=1, Min Special Character=0;


    history (optional, any, None)
      'Strict'= Strict= Does not allow upto 5 old passwords; 'Medium'= Medium= Does not allow upto 4 old passwords; 'Simple'= Simple= Does not allow upto 3 old passwords;


    uuid (optional, any, None)
      uuid of the object


    min_pswd_len (optional, any, None)
      Configure custom password length



  port_info (False, any, None)
    Field port_info


    uuid (optional, any, None)
      uuid of the object



  link_capability (False, any, None)
    Field link_capability


    enable (optional, any, None)
      Enable/Disable link capabilities


    uuid (optional, any, None)
      uuid of the object



  resource_accounting (False, any, None)
    Field resource_accounting


    template_list (optional, any, None)
      Field template_list


    uuid (optional, any, None)
      uuid of the object



  cpu_load_sharing (False, any, None)
    Field cpu_load_sharing


    packets_per_second (optional, any, None)
      Field packets_per_second


    disable (optional, any, None)
      Disable CPU load sharing in overload situations


    cpu_usage (optional, any, None)
      Field cpu_usage


    uuid (optional, any, None)
      uuid of the object



  dynamic_service_dns_socket_pool (False, any, None)
    Enable socket pool for dynamic-service DNS


  geoloc_list_list (False, any, None)
    Field geoloc_list_list


    sampling_enable (optional, any, None)
      Field sampling_enable


    exclude_geoloc_name_list (optional, any, None)
      Field exclude_geoloc_name_list


    uuid (optional, any, None)
      uuid of the object


    shared (optional, any, None)
      Enable sharing with other partitions


    include_geoloc_name_list (optional, any, None)
      Field include_geoloc_name_list


    user_tag (optional, any, None)
      Customized tag


    name (optional, any, None)
      Specify name of Geolocation list



  gui_image_list (False, any, None)
    Field gui_image_list


    uuid (optional, any, None)
      uuid of the object



  template_bind (False, any, None)
    Field template_bind


    monitor_list (optional, any, None)
      Field monitor_list



  table_integrity_check (False, any, None)
    Field table_integrity_check


    action (optional, any, None)
      Enable table integrity check


    uuid (optional, any, None)
      uuid of the object



  telemetry_log (False, any, None)
    Field telemetry_log


    top_k_app_svc_list (optional, any, None)
      Field top_k_app_svc_list


    top_k_source_list (optional, any, None)
      Field top_k_source_list


    device_status (optional, any, None)
      Field device_status


    partition_metrics (optional, any, None)
      Field partition_metrics



  sockstress_disable (False, any, None)
    Disable sockstress protection


  reboot (False, any, None)
    Field reboot


    uuid (optional, any, None)
      uuid of the object



  hardware_forward (False, any, None)
    Field hardware_forward


    sampling_enable (optional, any, None)
      Field sampling_enable


    uuid (optional, any, None)
      uuid of the object



  per_vlan_limit (False, any, None)
    Field per_vlan_limit


    unknown_ucast (optional, any, None)
      unknown unicast packets (per second limit)


    bcast (optional, any, None)
      broadcast packets (per second limit)


    uuid (optional, any, None)
      uuid of the object


    ipmcast (optional, any, None)
      IP multicast packets (per second limit)


    mcast (optional, any, None)
      multicast packets (per second limit)



  state (True, any, None)
    State of the object to be created.


  geo_location (False, any, None)
    Field geo_location


    geoloc_load_file_list (optional, any, None)
      Field geoloc_load_file_list


    uuid (optional, any, None)
      uuid of the object


    geolite2_city_include_ipv6 (optional, any, None)
      Include IPv6 address


    geo_location_iana (optional, any, None)
      Load built-in IANA Database


    geo_location_geolite2_country (optional, any, None)
      Load built-in Maxmind GeoLite2-Country database. Database available from http=//www.maxmind.com


    geo_location_geolite2_city (optional, any, None)
      Load built-in Maxmind GeoLite2-City database. Database available from http=//www.maxmind.com


    entry_list (optional, any, None)
      Field entry_list


    geolite2_country_include_ipv6 (optional, any, None)
      Include IPv6 address



  cpu_map (False, any, None)
    Field cpu_map


    uuid (optional, any, None)
      uuid of the object



  ipmi_service (False, any, None)
    Field ipmi_service


    disable (optional, any, None)
      Disable IPMI on platform


    uuid (optional, any, None)
      uuid of the object



  template (False, any, None)
    Field template


    template_policy (optional, any, None)
      Apply policy template to the whole system (Policy template name)


    uuid (optional, any, None)
      uuid of the object



  upgrade_status (False, any, None)
    Field upgrade_status


    uuid (optional, any, None)
      uuid of the object



  module_ctrl_cpu (False, any, None)
    'high'= high cpu usage; 'low'= low cpu usage; 'medium'= medium cpu usage;


  anomaly_log (False, any, None)
    log system anomalies


  apps_global (False, any, None)
    Field apps_global


    log_session_on_established (optional, any, None)
      Send TCP session creation log on completion of 3-way handshake


    msl_time (optional, any, None)
      Configure maximum session life, default is 2 seconds (1-40 seconds, default is 2 seconds)


    uuid (optional, any, None)
      uuid of the object



  ssl_req_q (False, any, None)
    Field ssl_req_q


    sampling_enable (optional, any, None)
      Field sampling_enable


    uuid (optional, any, None)
      uuid of the object



  cpu_list (False, any, None)
    Field cpu_list


    uuid (optional, any, None)
      uuid of the object



  fw (False, any, None)
    Field fw


    basic_dpi_enable (optional, any, None)
      Enable basic dpi


    application_mempool (optional, any, None)
      Enable application memory pool


    application_flow (optional, any, None)
      Number of flows


    uuid (optional, any, None)
      uuid of the object



  dns_cache (False, any, None)
    Field dns_cache


    sampling_enable (optional, any, None)
      Field sampling_enable


    uuid (optional, any, None)
      uuid of the object



  resource_usage (False, any, None)
    Field resource_usage


    ssl_context_memory (optional, any, None)
      Total SSL context memory needed in units of MB. Will be rounded to closest multiple of 2MB


    nat_pool_addr_count (optional, any, None)
      Total configurable NAT Pool addresses in the System


    auth_portal_image_file_size (optional, any, None)
      Specify maximum image file size for default portal (in KB)


    max_aflex_authz_collection_number (optional, any, None)
      Specify the maximum number of collections supported by aFleX authorization


    max_aflex_file_size (optional, any, None)
      Set maximum aFleX file size (Maximum file size in KBytes, default is 32K)


    auth_portal_html_file_size (optional, any, None)
      Specify maximum html file size for each html page in auth portal (in KB)


    visibility (optional, any, None)
      Field visibility


    aflex_table_entry_count (optional, any, None)
      Total aFleX table entry in the system (Total aFlex entry in the system)


    authz_policy_number (optional, any, None)
      Specify the maximum number of authorization policies


    l4_session_count (optional, any, None)
      Total Sessions in the System


    class_list_ac_entry_count (optional, any, None)
      Total entries for AC class-list


    class_list_ipv6_addr_count (optional, any, None)
      Total IPv6 addresses for class-list


    radius_table_size (optional, any, None)
      Total configurable CGNV6 RADIUS Table entries


    ssl_dma_memory (optional, any, None)
      Total SSL DMA memory needed in units of MB. Will be rounded to closest multiple of 2MB


    uuid (optional, any, None)
      uuid of the object



  trunk (False, any, None)
    Field trunk


    load_balance (optional, any, None)
      Field load_balance



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  core (False, any, None)
    Field core


    uuid (optional, any, None)
      uuid of the object



  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ddos_attack (False, any, None)
    System DDoS Attack


  uuid (False, any, None)
    uuid of the object


  ip_dns_cache (False, any, None)
    Field ip_dns_cache


    uuid (optional, any, None)
      uuid of the object



  mgmt_port (False, any, None)
    Field mgmt_port


    port_index (optional, any, None)
      port index to be configured (Specify port index)


    pci_address (optional, any, None)
      pci-address to be configured as mgmt port


    mac_address (optional, any, None)
      mac-address to be configured as mgmt port



  geoloc (False, any, None)
    Field geoloc


    sampling_enable (optional, any, None)
      Field sampling_enable


    uuid (optional, any, None)
      uuid of the object



  spe_status (False, any, None)
    Field spe_status


    uuid (optional, any, None)
      uuid of the object



  bfd (False, any, None)
    Field bfd


    sampling_enable (optional, any, None)
      Field sampling_enable


    uuid (optional, any, None)
      uuid of the object



  icmp6 (False, any, None)
    Field icmp6


    sampling_enable (optional, any, None)
      Field sampling_enable


    uuid (optional, any, None)
      uuid of the object



  cosq_stats (False, any, None)
    Field cosq_stats


    uuid (optional, any, None)
      uuid of the object



  throughput (False, any, None)
    Field throughput


    sampling_enable (optional, any, None)
      Field sampling_enable


    uuid (optional, any, None)
      uuid of the object



  mon_template (False, any, None)
    Field mon_template


    monitor_list (optional, any, None)
      Field monitor_list



  ansible_password (True, any, None)
    Password for AXAPI authentication


  platformtype (False, any, None)
    Field platformtype


    uuid (optional, any, None)
      uuid of the object



  delete_cpu_core (False, any, None)
    Field delete_cpu_core


    core_index (optional, any, None)
      core index to be deleted (Specify core index)










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

