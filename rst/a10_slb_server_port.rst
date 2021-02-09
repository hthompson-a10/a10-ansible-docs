.. _a10_slb_server_port_module:


a10_slb_server_port -- Configures A10 slb.server.port
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Real Server Port






Parameters
----------

  oper (False, any, None)
    Field oper


    down_grace_period_allowed (optional, any, None)
      Field down_grace_period_allowed


    protocol (optional, any, None)
      'tcp'= TCP Port; 'udp'= UDP Port;


    ip (optional, any, None)
      Field ip


    hm_index (optional, any, None)
      Field hm_index


    port_number (optional, any, None)
      Port Number


    ports_freed_total (optional, any, None)
      Field ports_freed_total


    ports_consumed_total (optional, any, None)
      Field ports_consumed_total


    aflow_queue_size (optional, any, None)
      Field aflow_queue_size


    current_time (optional, any, None)
      Field current_time


    alloc_failed (optional, any, None)
      Field alloc_failed


    vrid (optional, any, None)
      Field vrid


    state (optional, any, None)
      Field state


    hm_key (optional, any, None)
      Field hm_key


    ipv6 (optional, any, None)
      Field ipv6


    slow_start_conn_limit (optional, any, None)
      Field slow_start_conn_limit


    resv_conn (optional, any, None)
      Field resv_conn


    drs_auto_nat_list (optional, any, None)
      Field drs_auto_nat_list


    pool_name (optional, any, None)
      Field pool_name


    down_time_grace_period (optional, any, None)
      Field down_time_grace_period


    inband_hm_reassign_num (optional, any, None)
      Field inband_hm_reassign_num


    ports_consumed (optional, any, None)
      Field ports_consumed


    curr_observe_rate (optional, any, None)
      Field curr_observe_rate


    curr_conn_rate (optional, any, None)
      Field curr_conn_rate


    disable (optional, any, None)
      Field disable


    drs_ip_nat_list (optional, any, None)
      Field drs_ip_nat_list


    aflow_conn_limit (optional, any, None)
      Field aflow_conn_limit


    diameter_enabled (optional, any, None)
      Field diameter_enabled


    soft_down_time (optional, any, None)
      Field soft_down_time


    ha_group_id (optional, any, None)
      Field ha_group_id


    es_resp_time (optional, any, None)
      Field es_resp_time


    conn_rate_unit (optional, any, None)
      Field conn_rate_unit


    nat_pool_addr_list (optional, any, None)
      Field nat_pool_addr_list



  protocol (True, any, None)
    'tcp'= TCP Port; 'udp'= UDP Port;


  weight (False, any, None)
    Port Weight (Connection Weight)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  template_server_ssl (False, any, None)
    Server side SSL template (Server side SSL Name)


  health_check (False, any, None)
    Health Check (Monitor Name)


  port_number (True, any, None)
    Port Number


  template_port (False, any, None)
    Port template (Port template name)


  follow_port_protocol (False, any, None)
    'tcp'= TCP Port; 'udp'= UDP Port;


  shared_rport_health_check (False, any, None)
    Reference a health-check from shared partition


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'curr_req'= Current requests; 'total_req'= Total Requests; 'total_req_succ'= Total requests succ; 'total_fwd_bytes'= Bytes processed in forward direction; 'total_fwd_pkts'= Packets processed in forward direction; 'total_rev_bytes'= Bytes processed in reverse direction; 'total_rev_pkts'= Packets processed in reverse direction; 'total_conn'= Total connections; 'last_total_conn'= Last total connections; 'peak_conn'= Peak connections; 'es_resp_200'= Response status 200; 'es_resp_300'= Response status 300; 'es_resp_400'= Response status 400; 'es_resp_500'= Response status 500; 'es_resp_other'= Response status other; 'es_req_count'= Total proxy requests; 'es_resp_count'= Total proxy response; 'es_resp_invalid_http'= Total non-http response; 'total_rev_pkts_inspected'= Total reverse packets inspected; 'total_rev_pkts_inspected_good_status_code'= Total reverse packets with good status code inspected; 'response_time'= Response time; 'fastest_rsp_time'= Fastest response time; 'slowest_rsp_time'= Slowest response time; 'curr_ssl_conn'= Current SSL connections; 'total_ssl_conn'= Total SSL connections; 'resp-count'= Total Response Count; 'resp-1xx'= Response status 1xx; 'resp-2xx'= Response status 2xx; 'resp-3xx'= Response status 3xx; 'resp-4xx'= Response status 4xx; 'resp-5xx'= Response status 5xx; 'resp-other'= Response status Other; 'resp-latency'= Time to First Response Byte; 'curr_pconn'= Current persistent connections;



  stats (False, any, None)
    Field stats


    es_resp_invalid_http (optional, any, None)
      Total non-http response


    curr_req (optional, any, None)
      Current requests


    resp_other (optional, any, None)
      Response status Other


    resp_3xx (optional, any, None)
      Response status 3xx


    total_rev_pkts_inspected_good_status_code (optional, any, None)
      Total reverse packets with good status code inspected


    resp_2xx (optional, any, None)
      Response status 2xx


    curr_ssl_conn (optional, any, None)
      Current SSL connections


    port_number (optional, any, None)
      Port Number


    es_resp_count (optional, any, None)
      Total proxy response


    protocol (optional, any, None)
      'tcp'= TCP Port; 'udp'= UDP Port;


    total_fwd_bytes (optional, any, None)
      Bytes processed in forward direction


    resp_4xx (optional, any, None)
      Response status 4xx


    resp_1xx (optional, any, None)
      Response status 1xx


    es_resp_other (optional, any, None)
      Response status other


    fastest_rsp_time (optional, any, None)
      Fastest response time


    total_fwd_pkts (optional, any, None)
      Packets processed in forward direction


    resp_count (optional, any, None)
      Total Response Count


    es_req_count (optional, any, None)
      Total proxy requests


    es_resp_500 (optional, any, None)
      Response status 500


    peak_conn (optional, any, None)
      Peak connections


    resp_latency (optional, any, None)
      Time to First Response Byte


    total_req (optional, any, None)
      Total Requests


    es_resp_400 (optional, any, None)
      Response status 400


    es_resp_300 (optional, any, None)
      Response status 300


    curr_pconn (optional, any, None)
      Current persistent connections


    curr_conn (optional, any, None)
      Current connections


    es_resp_200 (optional, any, None)
      Response status 200


    total_rev_bytes (optional, any, None)
      Bytes processed in reverse direction


    response_time (optional, any, None)
      Response time


    resp_5xx (optional, any, None)
      Response status 5xx


    total_ssl_conn (optional, any, None)
      Total SSL connections


    total_conn (optional, any, None)
      Total connections


    total_rev_pkts (optional, any, None)
      Packets processed in reverse direction


    total_req_succ (optional, any, None)
      Total requests succ


    last_total_conn (optional, any, None)
      Last total connections


    total_rev_pkts_inspected (optional, any, None)
      Total reverse packets inspected


    slowest_rsp_time (optional, any, None)
      Slowest response time



  uuid (False, any, None)
    uuid of the object


  server_name (optional, any, None)
    Key to identify parent object


  extended_stats (False, any, None)
    Enable extended statistics on real server port


  state (True, any, None)
    State of the object to be created.


  health_check_follow_port (False, any, None)
    Specify which port to follow for health status (Port Number)


  conn_resume (False, any, None)
    Connection Resume


  rport_health_check_shared (False, any, None)
    Health Check (Monitor Name)


  support_http2 (False, any, None)
    Starting HTTP/2 with Prior Knowledge


  stats_data_action (False, any, None)
    'stats-data-enable'= Enable statistical data collection for real server port; 'stats-data-disable'= Disable statistical data collection for real server port;


  ansible_port (True, any, None)
    Port for AXAPI authentication


  conn_limit (False, any, None)
    Connection Limit


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  health_check_disable (False, any, None)
    Disable health check


  alternate_port (False, any, None)
    Field alternate_port


    alternate (optional, any, None)
      Alternate Server Number


    alternate_name (optional, any, None)
      Alternate Name


    alternate_server_port (optional, any, None)
      Port (Alternate Server Port Value)



  no_ssl (False, any, None)
    No SSL


  ansible_password (True, any, None)
    Password for AXAPI authentication


  range (False, any, None)
    Port range (Port range value - used for vip-to-rport-mapping and vport-rport range mapping)


  action (False, any, None)
    'enable'= enable; 'disable'= disable; 'disable-with-health-check'= disable port, but health check work;


  no_logging (False, any, None)
    Do not log connection over limit event


  user_tag (False, any, None)
    Customized tag


  auth_cfg (False, any, None)
    Field auth_cfg


    service_principal_name (optional, any, None)
      Service Principal Name (Kerberos principal name)










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

