.. _a10_slb_virtual_server_module:


a10_slb_virtual_server -- Configures A10 slb.virtual-server
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create a Virtual Server






Parameters
----------

  oper (False, any, None)
    Field oper


    migration_status (optional, any, None)
      Field migration_status


    peak_conn (optional, any, None)
      Field peak_conn


    ip_only_lb_fwd_pkts (optional, any, None)
      Field ip_only_lb_fwd_pkts


    ip_only_lb_fwd_bytes (optional, any, None)
      Field ip_only_lb_fwd_bytes


    curr_conn_rate (optional, any, None)
      Field curr_conn_rate


    mac (optional, any, None)
      Field mac


    port_list (optional, any, None)
      Field port_list


    curr_icmpv6_rate (optional, any, None)
      Field curr_icmpv6_rate


    ip_address (optional, any, None)
      Field ip_address


    name (optional, any, None)
      SLB Virtual Server Name


    migrate_vip (optional, any, None)
      Field migrate_vip


    icmpv6_rate_over_limit_drop (optional, any, None)
      Field icmpv6_rate_over_limit_drop


    icmp_lockup_time_left (optional, any, None)
      Field icmp_lockup_time_left


    conn_rate_unit (optional, any, None)
      Field conn_rate_unit


    icmp_rate_over_limit_drop (optional, any, None)
      Field icmp_rate_over_limit_drop


    state (optional, any, None)
      Field state


    ip_only_lb_rev_bytes (optional, any, None)
      Field ip_only_lb_rev_bytes


    curr_conn_overflow (optional, any, None)
      Field curr_conn_overflow


    curr_icmp_rate (optional, any, None)
      Field curr_icmp_rate


    ip_only_lb_rev_pkts (optional, any, None)
      Field ip_only_lb_rev_pkts


    icmpv6_lockup_time_left (optional, any, None)
      Field icmpv6_lockup_time_left



  ipv6_address (False, any, None)
    IPV6 address


  ansible_username (True, any, None)
    Username for AXAPI authentication


  redistribute_route_map (False, any, None)
    Route map reference (Name of route-map)


  ipv6_acl (False, any, None)
    ipv6 acl name


  template_policy (False, any, None)
    Policy template (Policy template name)


  acl_id_shared (False, any, None)
    acl id


  use_if_ip (False, any, None)
    Use Interface IP


  vport_disable_action (False, any, None)
    'drop-packet'= Drop packet for disabled virtual-port;


  template_policy_shared (False, any, None)
    Policy Template Name


  uuid (False, any, None)
    uuid of the object


  a10_partition (False, any, None)
    Destination/target partition for object/command


  shared_partition_policy_template (False, any, None)
    Reference a policy template from shared partition


  vrid (False, any, None)
    Join a vrrp group (Specify ha VRRP-A vrid)


  redistribution_flagged (False, any, None)
    Flag VIP for special redistribution handling


  extended_stats (False, any, None)
    Enable extended statistics on virtual server


  state (True, any, None)
    State of the object to be created.


  acl_id (False, any, None)
    acl id


  description (False, any, None)
    Create a description for VIP


  acl_name (False, any, None)
    Access List name (IPv4 Access List Name)


  stats_data_action (False, any, None)
    'stats-data-enable'= Enable statistical data collection for virtual server; 'stats-data-disable'= Disable statistical data collection for virtual server;


  template_virtual_server (False, any, None)
    Virtual server template (Virtual server template name)


  template_logging (False, any, None)
    NAT Logging template (NAT Logging template name)


  netmask (False, any, None)
    IP subnet mask


  port_list (False, any, None)
    Field port_list


    shared_partition_http_template (optional, any, None)
      Reference a HTTP template from shared partition


    template_http_shared (optional, any, None)
      HTTP Template Name


    protocol (optional, any, None)
      'tcp'= TCP LB service; 'udp'= UDP Port; 'others'= for no tcp/udp protocol, do IP load balancing; 'diameter'= diameter port; 'dns-tcp'= DNS service over TCP; 'dns-udp'= DNS service over UDP; 'fast-http'= Fast HTTP Port; 'fix'= FIX Port; 'ftp'= File Transfer Protocol Port; 'ftp-proxy'= ftp proxy port; 'http'= HTTP Port; 'https'= HTTPS port; 'http2'= [Deprecated] HTTP2 Port; 'http2s'= [Deprecated] HTTP2 SSL port; 'imap'= imap proxy port; 'mlb'= Message based load balancing; 'mms'= Microsoft Multimedia Service Port; 'mysql'= mssql port; 'mssql'= mssql; 'pop3'= pop3 proxy port; 'radius'= RADIUS Port; 'rtsp'= Real Time Streaming Protocol Port; 'sip'= Session initiation protocol over UDP; 'sip-tcp'= Session initiation protocol over TCP; 'sips'= Session initiation protocol over TLS; 'smpp-tcp'= SMPP service over TCP; 'spdy'= spdy port; 'spdys'= spdys port; 'smtp'= SMTP Port; 'ssl-proxy'= Generic SSL proxy; 'ssli'= SSL insight; 'ssh'= SSH Port; 'tcp-proxy'= Generic TCP proxy; 'tftp'= TFTP Port; 'fast-fix'= Fast FIX port;


    precedence (optional, any, None)
      Set auto NAT pool as higher precedence for source NAT


    trunk_fwd (optional, any, None)
      Trunk interface number


    template_server_ssl (optional, any, None)
      Server Side SSL Template Name


    reset_on_server_selection_fail (optional, any, None)
      Send client reset when server selection fails


    template_server_ssh (optional, any, None)
      Server SSH Template (Server SSH Config Name)


    cpu_compute (optional, any, None)
      enable cpu compute on virtual port


    uuid (optional, any, None)
      uuid of the object


    req_fail (optional, any, None)
      Use alternate virtual port when L7 request fail


    extended_stats (optional, any, None)
      Enable extended statistics on virtual port


    no_auto_up_on_aflex (optional, any, None)
      Don't automatically mark vport up when aFleX is bound


    template_http_policy_shared (optional, any, None)
      Http Policy Template Name


    template_smtp (optional, any, None)
      SMTP Template (SMTP Config Name)


    redirect_to_https (optional, any, None)
      Redirect HTTP to HTTPS


    rtp_sip_call_id_match (optional, any, None)
      rtp traffic try to match the real server of sip smp call-id session


    support_http2 (optional, any, None)
      Support HTTP2


    stats_data_action (optional, any, None)
      'stats-data-enable'= Enable statistical data collection for virtual port; 'stats-data-disable'= Disable statistical data collection for virtual port;


    auto (optional, any, None)
      Configure auto NAT for the vport


    template_dns_shared (optional, any, None)
      DNS Template Name


    scaleout_device_group (optional, any, None)
      Device group id


    def_selection_if_pref_failed (optional, any, None)
      'def-selection-if-pref-failed'= Use default server selection method if prefer method failed; 'def-selection-if-pref-failed-disable'= Stop using default server selection method if prefer method failed;


    name (optional, any, None)
      SLB Virtual Service Name


    shared_partition_pool (optional, any, None)
      Specify NAT pool or pool group from shared partition


    port_number (optional, any, None)
      Port


    template_client_ssl_shared (optional, any, None)
      Client SSL Template Name


    eth_rev (optional, any, None)
      Ethernet interface number


    view (optional, any, None)
      Specify a GSLB View (ID)


    template_udp (optional, any, None)
      L4 UDP Template


    pool_shared (optional, any, None)
      Specify NAT pool or pool group


    template_tcp_proxy_server (optional, any, None)
      TCP Proxy Config Server (TCP Proxy Config name)


    use_alternate_port (optional, any, None)
      Use alternate virtual port


    template_file_inspection (optional, any, None)
      File Inspection service template (file-inspection template name)


    server_group (optional, any, None)
      Bind a use-rcv-hop-for-resp Server Group to this Virtual Server (Server Group Name)


    force_routing_mode (optional, any, None)
      Force routing mode


    template_client_ssh (optional, any, None)
      Client SSH Template (Client SSH Config Name)


    template_client_ssl (optional, any, None)
      Client SSL Template Name


    template_persist_cookie_shared (optional, any, None)
      Cookie Persistence Template Name


    template_http_policy (optional, any, None)
      http-policy template (http-policy template name)


    template_ftp (optional, any, None)
      FTP port template (Ftp template name)


    shared_partition_persist_source_ip_template (optional, any, None)
      Reference a persist source ip template from shared partition


    shared_partition_tcp (optional, any, None)
      Reference a tcp template from shared partition


    template_dynamic_service_shared (optional, any, None)
      Dynamic Service Template Name


    template_persist_destination_ip (optional, any, None)
      Destination IP persistence (Destination IP persistence template name)


    template_virtual_port_shared (optional, any, None)
      Virtual Port Template Name


    template_persist_destination_ip_shared (optional, any, None)
      Destination IP Persistence Template Name


    shared_partition_dns_template (optional, any, None)
      Reference a dns template from shared partition


    shared_partition_virtual_port_template (optional, any, None)
      Reference a Virtual Port template from shared partition


    template_udp_shared (optional, any, None)
      UDP Template Name


    template_dynamic_service (optional, any, None)
      Dynamic Service Template (dynamic-service template name)


    template_server_ssl_shared (optional, any, None)
      Server SSL Template Name


    skip_rev_hash (optional, any, None)
      Skip rev tuple hash insertion


    shared_partition_client_ssl_template (optional, any, None)
      Reference a Client SSL template from shared partition


    aflex_scripts (optional, any, None)
      Field aflex_scripts


    alternate_port (optional, any, None)
      Alternate Virtual Port


    acl_id_list (optional, any, None)
      Field acl_id_list


    shared_partition_persist_cookie_template (optional, any, None)
      Reference a persist cookie template from shared partition


    optimization_level (optional, any, None)
      '0'= No optimization; '1'= Optimization level 1 (Experimental);


    template_dblb (optional, any, None)
      DBLB Template (DBLB template name)


    range (optional, any, None)
      Virtual Port range (Virtual Port range value)


    template_external_service_shared (optional, any, None)
      External Service Template Name


    serv_sel_fail (optional, any, None)
      Use alternate virtual port when server selection failure


    action (optional, any, None)
      'enable'= Enable; 'disable'= Disable;


    no_logging (optional, any, None)
      Do not log connection over limit event


    template_respmod_icap (optional, any, None)
      ICAP respmod service template (respmod-icap template name)


    no_dest_nat (optional, any, None)
      Disable destination NAT, this option only supports in wildcard VIP or when a connection is operated in SSLi + EP mode


    template_connection_reuse_shared (optional, any, None)
      Connection Reuse Template Name


    shared_partition_connection_reuse_template (optional, any, None)
      Reference a connection reuse template from shared partition


    alt_protocol1 (optional, any, None)
      'http'= HTTP Port;


    alt_protocol2 (optional, any, None)
      'tcp'= TCP LB service;


    template_sip (optional, any, None)
      SIP template


    when_down (optional, any, None)
      Use alternate virtual port when down


    use_default_if_no_server (optional, any, None)
      Use default forwarding if server selection failed


    template_policy (optional, any, None)
      Policy Template (Policy template name)


    ipinip (optional, any, None)
      Enable IP in IP


    template_tcp_proxy_shared (optional, any, None)
      TCP Proxy Template name


    template_persist_source_ip (optional, any, None)
      Source IP persistence (Source IP persistence template name)


    sampling_enable (optional, any, None)
      Field sampling_enable


    template_diameter (optional, any, None)
      Diameter Template (diameter template name)


    ha_conn_mirror (optional, any, None)
      Enable for HA Conn sync


    template_policy_shared (optional, any, None)
      Policy Template Name


    shared_partition_cache_template (optional, any, None)
      Reference a Cache template from shared partition


    when_down_protocol2 (optional, any, None)
      Use alternate virtual port when down


    eth_fwd (optional, any, None)
      Ethernet interface number


    shared_partition_persist_ssl_sid_template (optional, any, None)
      Reference a persist SSL SID template from shared partition


    template_tcp (optional, any, None)
      TCP Template Name


    clientip_sticky_nat (optional, any, None)
      Prefer to use same source NAT address for a client


    pool (optional, any, None)
      Specify NAT pool or pool group


    on_syn (optional, any, None)
      Enable for HA Conn sync for l4 tcp sessions on SYN


    ip_only_lb (optional, any, None)
      Enable IP-Only LB mode


    template_http (optional, any, None)
      HTTP Template Name


    use_rcv_hop_group (optional, any, None)
      Set use-rcv-hop group


    template_connection_reuse (optional, any, None)
      Connection Reuse Template (Connection Reuse Template Name)


    l7_hardware_assist (optional, any, None)
      FPGA assist L7 packet parsing


    enable_playerid_check (optional, any, None)
      Enable playerid checks on UDP packets once the AX is in active mode


    shared_partition_http_policy_template (optional, any, None)
      Reference a http policy template from shared partition


    template_diameter_shared (optional, any, None)
      Diameter Template Name


    reset (optional, any, None)
      Send client reset when connection number over limit


    memory_compute (optional, any, None)
      enable dynamic memory compute on virtual port


    resolve_web_cat_list (optional, any, None)
      Web Category List name


    template_smpp (optional, any, None)
      SMPP template


    rate (optional, any, None)
      Specify the log message rate


    template_cache (optional, any, None)
      RAM caching template (Cache Template Name)


    template_persist_cookie (optional, any, None)
      Cookie persistence (Cookie persistence template name)


    persist_type (optional, any, None)
      'src-dst-ip-swap-persist'= Create persist session after source IP and destination IP swap; 'use-src-ip-for-dst-persist'= Use the source IP to create a destination persist session; 'use-dst-ip-for-src-persist'= Use the destination IP to create source IP persist session;


    use_rcv_hop_for_resp (optional, any, None)
      Use receive hop for response to client(For packets on default-vlan, also config 'vlan-global enable-def-vlan-l2-forwarding'.)


    scaleout_bucket_count (optional, any, None)
      Number of traffic buckets


    shared_partition_external_service_template (optional, any, None)
      Reference a external service template from shared partition


    trunk_rev (optional, any, None)
      Trunk interface number


    template_tcp_shared (optional, any, None)
      TCP Template Name


    acl_name_list (optional, any, None)
      Field acl_name_list


    template_dns (optional, any, None)
      DNS template (DNS template name)


    template_reqmod_icap (optional, any, None)
      ICAP reqmod template (reqmod-icap template name)


    template_external_service (optional, any, None)
      External service template (external-service template name)


    shared_partition_tcp_proxy_template (optional, any, None)
      Reference a TCP Proxy template from shared partition


    service_group (optional, any, None)
      Bind a Service Group to this Virtual Server (Service Group Name)


    shared_partition_policy_template (optional, any, None)
      Reference a policy template from shared partition


    waf_template (optional, any, None)
      WAF template (WAF Template Name)


    template_cache_shared (optional, any, None)
      Cache Template Name


    template_ssli (optional, any, None)
      SSLi template (SSLi Template Name)


    ip_map_list (optional, any, None)
      Enter name of IP Map List to be bound (IP Map List Name)


    use_cgnv6 (optional, any, None)
      Follow CGNv6 source NAT configuration


    shared_partition_dynamic_service_template (optional, any, None)
      Reference a dynamic service template from shared partition


    template_tcp_proxy (optional, any, None)
      TCP Proxy Template Name


    template_tcp_proxy_client (optional, any, None)
      TCP Proxy Config Client (TCP Proxy Config name)


    template_persist_ssl_sid (optional, any, None)
      SSL SID persistence (SSL SID persistence template name)


    gslb_enable (optional, any, None)
      Enable Global Server Load Balancing


    template_imap_pop3 (optional, any, None)
      IMAP/POP3 Template (IMAP/POP3 Config Name)


    shared_partition_server_ssl_template (optional, any, None)
      Reference a SSL Server template from shared partition


    shared_partition_persist_destination_ip_template (optional, any, None)
      Reference a persist destination ip template from shared partition


    conn_limit (optional, any, None)
      Connection Limit


    alternate_port_number (optional, any, None)
      Virtual Port


    snat_on_vip (optional, any, None)
      Enable source NAT traffic against VIP


    template_persist_source_ip_shared (optional, any, None)
      Source IP Persistence Template Name


    template_scaleout (optional, any, None)
      Scaleout template (Scaleout template name)


    message_switching (optional, any, None)
      Message switching


    expand (optional, any, None)
      expand syn-cookie with timestamp and wscale


    syn_cookie (optional, any, None)
      Enable syn-cookie


    template_fix (optional, any, None)
      FIX template (FIX Template Name)


    template_virtual_port (optional, any, None)
      Virtual port template (Virtual port template name)


    auth_cfg (optional, any, None)
      Field auth_cfg


    template_persist_ssl_sid_shared (optional, any, None)
      SSL SID Persistence Template Name


    shared_partition_diameter_template (optional, any, None)
      Reference a Diameter template from shared partition


    secs (optional, any, None)
      Specify the interval in seconds


    shared_partition_udp (optional, any, None)
      Reference a UDP template from shared partition


    user_tag (optional, any, None)
      Customized tag


    port_translation (optional, any, None)
      Enable port translation under no-dest-nat



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  template_scaleout (False, any, None)
    Scaleout template (Scaleout template name)


  ip_address (False, any, None)
    IP Address


  ansible_host (True, any, None)
    Host for AXAPI authentication


  name (True, any, None)
    SLB Virtual Server Name


  migrate_vip (False, any, None)
    Field migrate_vip


    cancel_migration (optional, any, None)
      Cancel migration


    finish_migration (optional, any, None)
      Complete the migration


    target_data_cpu (optional, any, None)
      Number of CPUs on the target platform


    target_floating_ipv4 (optional, any, None)
      Specify IP address


    uuid (optional, any, None)
      uuid of the object



  ansible_port (True, any, None)
    Port for AXAPI authentication


  disable_vip_adv (False, any, None)
    Disable virtual server GARP


  ha_dynamic (False, any, None)
    Dynamic failover based on vip status


  ansible_password (True, any, None)
    Password for AXAPI authentication


  acl_name_shared (False, any, None)
    Access List name (IPv4 Access List Name)


  arp_disable (False, any, None)
    Disable Respond to Virtual Server ARP request


  ipv6_acl_shared (False, any, None)
    ipv6 acl name


  ethernet (False, any, None)
    Ethernet interface


  user_tag (False, any, None)
    Customized tag


  enable_disable_action (False, any, None)
    'enable'= Enable Virtual Server (default); 'disable'= Disable Virtual Server; 'disable-when-all-ports-down'= Disable Virtual Server when all member ports are down; 'disable-when-any-port-down'= Disable Virtual Server when any member port is down;









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

