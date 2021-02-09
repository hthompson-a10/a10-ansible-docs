.. _a10_cgnv6_server_port_module:


a10_cgnv6_server_port -- Configures A10 cgnv6.server.port
=========================================================

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


    inband_hm_reassign_num (optional, any, None)
      Field inband_hm_reassign_num


    ports_consumed (optional, any, None)
      Field ports_consumed


    hm_index (optional, any, None)
      Field hm_index


    curr_observe_rate (optional, any, None)
      Field curr_observe_rate


    curr_conn_rate (optional, any, None)
      Field curr_conn_rate


    disable (optional, any, None)
      Field disable


    port_number (optional, any, None)
      Port Number


    ports_freed_total (optional, any, None)
      Field ports_freed_total


    ports_consumed_total (optional, any, None)
      Field ports_consumed_total


    aflow_queue_size (optional, any, None)
      Field aflow_queue_size


    aflow_conn_limit (optional, any, None)
      Field aflow_conn_limit


    current_time (optional, any, None)
      Field current_time


    soft_down_time (optional, any, None)
      Field soft_down_time


    ha_group_id (optional, any, None)
      Field ha_group_id


    alloc_failed (optional, any, None)
      Field alloc_failed


    vrid (optional, any, None)
      Field vrid


    conn_rate_unit (optional, any, None)
      Field conn_rate_unit


    es_resp_time (optional, any, None)
      Field es_resp_time


    state (optional, any, None)
      Field state


    hm_key (optional, any, None)
      Field hm_key


    diameter_enabled (optional, any, None)
      Field diameter_enabled


    ipv6 (optional, any, None)
      Field ipv6


    down_time_grace_period (optional, any, None)
      Field down_time_grace_period


    slow_start_conn_limit (optional, any, None)
      Field slow_start_conn_limit


    resv_conn (optional, any, None)
      Field resv_conn



  health_check (False, any, None)
    Health Check (Monitor Name)


  protocol (True, any, None)
    'tcp'= TCP Port; 'udp'= UDP Port;


  ansible_username (True, any, None)
    Username for AXAPI authentication


  port_number (True, any, None)
    Port Number


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  follow_port_protocol (False, any, None)
    'tcp'= TCP Port; 'udp'= UDP Port;


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  health_check_disable (False, any, None)
    Disable health check


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'curr_conn'= Current connections; 'curr_req'= Current requests; 'total_req'= Total requests; 'total_req_succ'= Total request success; 'total_fwd_bytes'= Forward bytes; 'total_fwd_pkts'= Forward packets; 'total_rev_bytes'= Reverse bytes; 'total_rev_pkts'= Reverse packets; 'total_conn'= Total connections; 'last_total_conn'= Last total connections; 'peak_conn'= Peak connections; 'es_resp_200'= Response status 200; 'es_resp_300'= Response status 300; 'es_resp_400'= Response status 400; 'es_resp_500'= Response status 500; 'es_resp_other'= Response status other; 'es_req_count'= Total proxy request; 'es_resp_count'= Total proxy Response; 'es_resp_invalid_http'= Total non-http response; 'total_rev_pkts_inspected'= Total reverse packets inspected; 'total_rev_pkts_inspected_good_status_code'= Total reverse packets with good status code inspected; 'response_time'= Response time; 'fastest_rsp_time'= Fastest response time; 'slowest_rsp_time'= Slowest response time;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    es_resp_invalid_http (optional, any, None)
      Total non-http response


    curr_req (optional, any, None)
      Current requests


    protocol (optional, any, None)
      'tcp'= TCP Port; 'udp'= UDP Port;


    total_rev_pkts_inspected_good_status_code (optional, any, None)
      Total reverse packets with good status code inspected


    es_resp_500 (optional, any, None)
      Response status 500


    peak_conn (optional, any, None)
      Peak connections


    total_req (optional, any, None)
      Total requests


    es_resp_400 (optional, any, None)
      Response status 400


    es_resp_300 (optional, any, None)
      Response status 300


    port_number (optional, any, None)
      Port Number


    es_resp_count (optional, any, None)
      Total proxy Response


    es_resp_200 (optional, any, None)
      Response status 200


    total_fwd_bytes (optional, any, None)
      Forward bytes


    response_time (optional, any, None)
      Response time


    total_rev_bytes (optional, any, None)
      Reverse bytes


    curr_conn (optional, any, None)
      Current connections


    total_conn (optional, any, None)
      Total connections


    es_resp_other (optional, any, None)
      Response status other


    fastest_rsp_time (optional, any, None)
      Fastest response time


    total_fwd_pkts (optional, any, None)
      Forward packets


    total_rev_pkts (optional, any, None)
      Reverse packets


    total_req_succ (optional, any, None)
      Total request success


    last_total_conn (optional, any, None)
      Last total connections


    total_rev_pkts_inspected (optional, any, None)
      Total reverse packets inspected


    es_req_count (optional, any, None)
      Total proxy request


    slowest_rsp_time (optional, any, None)
      Slowest response time



  uuid (False, any, None)
    uuid of the object


  server_name (optional, any, None)
    Key to identify parent object


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  action (False, any, None)
    'enable'= enable; 'disable'= disable;


  user_tag (False, any, None)
    Customized tag


  health_check_follow_port (False, any, None)
    Specify which port to follow for health status (Port Number)









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

