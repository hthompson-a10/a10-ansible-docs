.. _a10_slb_server_module:


a10_slb_server -- Configures A10 slb.server
===========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Server






Parameters
----------

  oper (False, any, None)
    Field oper


    drs_list (optional, any, None)
      Field drs_list


    name (optional, any, None)
      Server Name


    dns_update_time (optional, any, None)
      Field dns_update_time


    state (optional, any, None)
      Field state


    creation_type (optional, any, None)
      Field creation_type


    server_ttl (optional, any, None)
      Field server_ttl


    curr_observe_rate (optional, any, None)
      Field curr_observe_rate


    curr_conn_rate (optional, any, None)
      Field curr_conn_rate


    conn_rate_unit (optional, any, None)
      Field conn_rate_unit


    disable (optional, any, None)
      Field disable


    port_list (optional, any, None)
      Field port_list


    slow_start_conn_limit (optional, any, None)
      Field slow_start_conn_limit


    is_autocreate (optional, any, None)
      Field is_autocreate


    srv_gateway_arp (optional, any, None)
      Field srv_gateway_arp



  weight (False, any, None)
    Weight for this Real Server (Connection Weight)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  slow_start (False, any, None)
    Slowly ramp up the connection number after server is up (start from 128, then double every 10 sec till 4096)


  resolve_as (False, any, None)
    'resolve-to-ipv4'= Use A Query only to resolve FQDN; 'resolve-to-ipv6'= Use AAAA Query only to resolve FQDN; 'resolve-to-ipv4-and-ipv6'= Use A as well as AAAA Query to resolve FQDN;


  health_check (False, any, None)
    Health Check Monitor (Health monitor name)


  spoofing_cache (False, any, None)
    This server is a spoofing cache


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'total-conn'= Total established connections; 'fwd-pkt'= Forward Packets Processed; 'rev-pkt'= Reverse Packets Processed; 'peak-conn'= Peak number of established connections; 'total_req'= Total Requests processed; 'total_req_succ'= Total Requests succeeded; 'curr_ssl_conn'= Current SSL connections established; 'total_ssl_conn'= Total SSL connections established; 'total_fwd_bytes'= Bytes processed in forward direction; 'total_rev_bytes'= Bytes processed in reverse direction; 'total_fwd_pkts'= Packets processed in forward direction; 'total_rev_pkts'= Packets processed in reverse direction; 'ip_only_lb_fwd_bytes'= IP-Only-LB Bytes processed in forward direction; 'ip_only_lb_rev_bytes'= IP-Only-LB Bytes processed in reverse direction; 'ip_only_lb_fwd_pkts'= IP-Only-LB Packets processed in forward direction; 'ip_only_lb_rev_pkts'= IP-Only-LB Packets processed in reverse direction;



  fqdn_name (False, any, None)
    Server hostname


  uuid (False, any, None)
    uuid of the object


  extended_stats (False, any, None)
    Enable extended statistics on real server


  state (True, any, None)
    State of the object to be created.


  ipv6 (False, any, None)
    IPv6 address Mapping of GSLB


  server_ipv6_addr (False, any, None)
    IPV6 address


  shared_partition_health_check (False, any, None)
    Reference a health-check from shared partition


  conn_resume (False, any, None)
    Connection Resume (Connection Resume (min active conn before resume taking new conn))


  stats_data_action (False, any, None)
    'stats-data-enable'= Enable statistical data collection for real server; 'stats-data-disable'= Disable statistical data collection for real server;


  conn_limit (False, any, None)
    Connection Limit


  action (False, any, None)
    'enable'= Enable this Real Server; 'disable'= Disable this Real Server; 'disable-with-health-check'= disable real server, but health check work;


  host (False, any, None)
    IP Address


  port_list (False, any, None)
    Field port_list


    conn_resume (optional, any, None)
      Connection Resume


    protocol (optional, any, None)
      'tcp'= TCP Port; 'udp'= UDP Port;


    weight (optional, any, None)
      Port Weight (Connection Weight)


    support_http2 (optional, any, None)
      Starting HTTP/2 with Prior Knowledge


    rport_health_check_shared (optional, any, None)
      Health Check (Monitor Name)


    template_server_ssl (optional, any, None)
      Server side SSL template (Server side SSL Name)


    health_check (optional, any, None)
      Health Check (Monitor Name)


    port_number (optional, any, None)
      Port Number


    template_port (optional, any, None)
      Port template (Port template name)


    follow_port_protocol (optional, any, None)
      'tcp'= TCP Port; 'udp'= UDP Port;


    shared_rport_health_check (optional, any, None)
      Reference a health-check from shared partition


    sampling_enable (optional, any, None)
      Field sampling_enable


    conn_limit (optional, any, None)
      Connection Limit


    alternate_port (optional, any, None)
      Field alternate_port


    no_ssl (optional, any, None)
      No SSL


    uuid (optional, any, None)
      uuid of the object


    extended_stats (optional, any, None)
      Enable extended statistics on real server port


    auth_cfg (optional, any, None)
      Field auth_cfg


    stats_data_action (optional, any, None)
      'stats-data-enable'= Enable statistical data collection for real server port; 'stats-data-disable'= Disable statistical data collection for real server port;


    range (optional, any, None)
      Port range (Port range value - used for vip-to-rport-mapping and vport-rport range mapping)


    health_check_disable (optional, any, None)
      Disable health check


    action (optional, any, None)
      'enable'= enable; 'disable'= disable; 'disable-with-health-check'= disable port, but health check work;


    no_logging (optional, any, None)
      Do not log connection over limit event


    user_tag (optional, any, None)
      Customized tag


    health_check_follow_port (optional, any, None)
      Specify which port to follow for health status (Port Number)



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  stats (False, any, None)
    Field stats


    peak_conn (optional, any, None)
      Peak number of established connections


    ip_only_lb_fwd_pkts (optional, any, None)
      IP-Only-LB Packets processed in forward direction


    fwd_pkt (optional, any, None)
      Forward Packets Processed


    total_req (optional, any, None)
      Total Requests processed


    total_rev_pkts (optional, any, None)
      Packets processed in reverse direction


    curr_ssl_conn (optional, any, None)
      Current SSL connections established


    curr_conn (optional, any, None)
      Current established connections


    port_list (optional, any, None)
      Field port_list


    rev_pkt (optional, any, None)
      Reverse Packets Processed


    total_rev_bytes (optional, any, None)
      Bytes processed in reverse direction


    name (optional, any, None)
      Server Name


    total_fwd_bytes (optional, any, None)
      Bytes processed in forward direction


    ip_only_lb_rev_pkts (optional, any, None)
      IP-Only-LB Packets processed in reverse direction


    total_ssl_conn (optional, any, None)
      Total SSL connections established


    total_conn (optional, any, None)
      Total established connections


    total_fwd_pkts (optional, any, None)
      Packets processed in forward direction


    ip_only_lb_fwd_bytes (optional, any, None)
      IP-Only-LB Bytes processed in forward direction


    total_req_succ (optional, any, None)
      Total Requests succeeded


    ip_only_lb_rev_bytes (optional, any, None)
      IP-Only-LB Bytes processed in reverse direction



  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  health_check_disable (False, any, None)
    Disable configured health check configuration


  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    Server Name


  external_ip (False, any, None)
    External IP address for NAT of GSLB


  ansible_password (True, any, None)
    Password for AXAPI authentication


  template_server (False, any, None)
    Server template (Server template name)


  alternate_server (False, any, None)
    Field alternate_server


    alternate (optional, any, None)
      Alternate Server (Alternate Server Number)


    alternate_name (optional, any, None)
      Alternate Name



  no_logging (False, any, None)
    Do not log connection over limit event


  health_check_shared (False, any, None)
    Health Check Monitor (Health monitor name)


  user_tag (False, any, None)
    Customized tag









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

