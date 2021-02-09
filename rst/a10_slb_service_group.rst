.. _a10_slb_service_group_module:


a10_slb_service_group -- Configures A10 slb.service-group
=========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Service Group






Parameters
----------

  oper (False, any, None)
    Field oper


    pri_affinity_priority (optional, any, None)
      Field pri_affinity_priority


    name (optional, any, None)
      SLB Service Name


    sgm_list (optional, any, None)
      Field sgm_list


    stateless_current_rate (optional, any, None)
      Field stateless_current_rate


    servers_down (optional, any, None)
      Field servers_down


    stateless_state (optional, any, None)
      Field stateless_state


    servers_disable (optional, any, None)
      Field servers_disable


    filter (optional, any, None)
      Field filter


    stateless_type (optional, any, None)
      Field stateless_type


    servers_total (optional, any, None)
      Field servers_total


    state (optional, any, None)
      Field state


    member_list (optional, any, None)
      Field member_list


    servers_up (optional, any, None)
      Field servers_up


    stateless_current_usage (optional, any, None)
      Field stateless_current_usage


    hm_dsr_enable_all_vip (optional, any, None)
      Field hm_dsr_enable_all_vip



  rpt_ext_server (False, any, None)
    Report top 10 fastest/slowest servers


  protocol (False, any, None)
    'tcp'= TCP LB service; 'udp'= UDP LB service;


  ansible_username (True, any, None)
    Username for AXAPI authentication


  lc_method (False, any, None)
    'least-connection'= Least connection on server level; 'service-least- connection'= Least connection on service port level; 'weighted-least- connection'= Weighted least connection on server level; 'service-weighted- least-connection'= Weighted least connection on service port level;


  l4_session_usage_revert_rate (False, any, None)
    Usage to revert to statelful method


  extended_stats (False, any, None)
    Enable extended statistics on service group


  reset_on_server_selection_fail (False, any, None)
    Send reset to client if server selection fails


  stateless_lb_method2 (False, any, None)
    'stateless-dst-ip-hash'= Stateless load-balancing based on Dst IP and Dst port hash; 'stateless-per-pkt-round-robin'= Stateless load-balancing using per- packet round-robin; 'stateless-src-dst-ip-hash'= Stateless load-balancing based on IP and port hash for both Src and Dst; 'stateless-src-dst-ip-only-hash'= Stateless load-balancing based on only IP hash for both Src and Dst; 'stateless-src-ip-hash'= Stateless load-balancing based on Src IP and Src port hash; 'stateless-src-ip-only-hash'= Stateless load-balancing based on only Src IP hash;


  template_policy (False, any, None)
    Policy template (Policy template name)


  template_port (False, any, None)
    Port template (Port template name)


  backup_server_event_log (False, any, None)
    Send log info on back up server events


  conn_rate_duration (False, any, None)
    Period that trigger condition consistently happens(seconds)


  traffic_replication_mirror_sa_repl (False, any, None)
    Replace Source MAC


  top_slowest (False, any, None)
    Report top 10 slowest servers


  sample_rsp_time (False, any, None)
    sample server response time


  pseudo_round_robin (False, any, None)
    PRR, select the oldest node for sub-select


  traffic_replication_mirror_da_repl (False, any, None)
    Replace Destination MAC


  template_policy_shared (False, any, None)
    Policy template


  stats (False, any, None)
    Field stats


    service_resp_2xx (optional, any, None)
      Service Group response 2xx count


    service_unhealthy_host (optional, any, None)
      Service Group unhealthy host count


    service_curr_conn_overflow (optional, any, None)
      Current connection counter overflow count


    name (optional, any, None)
      SLB Service Name


    server_selection_fail_drop (optional, any, None)
      Drops due to Service selection failure


    service_healthy_host (optional, any, None)
      Service Group healthy host count


    service_resp_count (optional, any, None)
      Service Group response count


    member_list (optional, any, None)
      Field member_list


    service_req_count (optional, any, None)
      Service Group request count


    service_resp_4xx (optional, any, None)
      Service Group response 4xx count


    service_peak_conn (optional, any, None)
      Peak connection count for the Service Group


    server_selection_fail_reset (optional, any, None)
      Resets sent out for Service selection failure


    service_resp_3xx (optional, any, None)
      Service Group response 3xx count


    service_resp_5xx (optional, any, None)
      Service Group response 5xx count



  uuid (False, any, None)
    uuid of the object


  shared_partition_policy_template (False, any, None)
    Reference a policy template from shared partition


  conn_revert_rate (False, any, None)
    Rate to revert to statelful method (conn/sec)


  persist_scoring (False, any, None)
    'global'= Use Global Configuration; 'enable'= Enable persist-scoring; 'disable'= Disable persist-scoring;


  member_list (False, any, None)
    Field member_list


    sampling_enable (optional, any, None)
      Field sampling_enable


    fqdn_name (optional, any, None)
      Server hostname - Not applicable if real server is already defined


    name (optional, any, None)
      Member name


    member_priority (optional, any, None)
      Priority of Port in the Group (Priority of Port in the Group, default is 1)


    resolve_as (optional, any, None)
      'resolve-to-ipv4'= Use A Query only to resolve FQDN; 'resolve-to-ipv6'= Use AAAA Query only to resolve FQDN; 'resolve-to-ipv4-and-ipv6'= Use A as well as AAAA Query to resolve FQDN;


    host (optional, any, None)
      IP Address - Not applicable if real server is already defined


    member_stats_data_disable (optional, any, None)
      Disable statistical data collection


    member_template (optional, any, None)
      Real server port template (Real server port template name)


    member_state (optional, any, None)
      'enable'= Enable member service port; 'disable'= Disable member service port; 'disable-with-health-check'= disable member service port, but health check work;


    server_ipv6_addr (optional, any, None)
      IPV6 Address - Not applicable if real server is already defined


    user_tag (optional, any, None)
      Customized tag


    port (optional, any, None)
      Port number


    uuid (optional, any, None)
      uuid of the object



  conn_rate_revert_duration (False, any, None)
    Period that revert condition consistently happens(seconds)


  stateless_lb_method (False, any, None)
    'stateless-dst-ip-hash'= Stateless load-balancing based on Dst IP and Dst port hash; 'stateless-per-pkt-round-robin'= Stateless load-balancing using per- packet round-robin; 'stateless-src-dst-ip-hash'= Stateless load-balancing based on IP and port hash for both Src and Dst; 'stateless-src-dst-ip-only-hash'= Stateless load-balancing based on only IP hash for both Src and Dst; 'stateless-src-ip-hash'= Stateless load-balancing based on Src IP and Src port hash; 'stateless-src-ip-only-hash'= Stateless load-balancing based on only Src IP hash;


  l4_session_usage_grace_period (False, any, None)
    Define the grace period during transition (Define the grace period during transition(seconds))


  svcgrp_health_check_shared (False, any, None)
    Health Check (Monitor Name)


  lb_method (False, any, None)
    'dst-ip-hash'= Load-balancing based on only Dst IP and Port hash; 'dst-ip-only- hash'= Load-balancing based on only Dst IP hash; 'fastest-response'= Fastest response time on service port level; 'least-request'= Least request on service port level; 'src-ip-hash'= Load-balancing based on only Src IP and Port hash; 'src-ip-only-hash'= Load-balancing based on only Src IP hash; 'weighted-rr'= Weighted round robin on server level; 'service-weighted-rr'= Weighted round robin on service port level; 'round-robin'= Round robin on server level; 'round-robin-strict'= Strict mode round robin on server level; 'odd-even-hash'= odd/even hash based of client src-ip;


  state (True, any, None)
    State of the object to be created.


  stats_data_action (False, any, None)
    'stats-data-enable'= Enable statistical data collection for service group; 'stats-data-disable'= Disable statistical data collection for service group;


  l4_session_usage_log (False, any, None)
    Send log if transition happens


  l4_session_revert_duration (False, any, None)
    Period that revert condition consistently happens(seconds)


  stateless_auto_switch (False, any, None)
    Enable auto stateless method


  ansible_password (True, any, None)
    Password for AXAPI authentication


  l4_session_usage_duration (False, any, None)
    Period that trigger condition consistently happens(seconds)


  min_active_member_action (False, any, None)
    'dynamic-priority'= dynamic change member priority to met the min-active-member requirement; 'skip-pri-set'= Skip Current Priority Set If Min not met;


  shared_partition_svcgrp_health_check (False, any, None)
    Reference a health-check from shared partition


  l4_session_usage (False, any, None)
    Dynamically enable stateless method by session usage (Usage to trigger stateless method)


  report_delay (False, any, None)
    Reporting frequency (in minutes)


  strict_select (False, any, None)
    strict selection


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  conn_rate (False, any, None)
    Dynamically enable stateless method by conn-rate (Rate to trigger stateless method(conn/sec))


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  health_check_disable (False, any, None)
    Disable health check


  reset (False, any, None)
    Field reset


    auto_switch (optional, any, None)
      Reset auto stateless state



  ansible_port (True, any, None)
    Port for AXAPI authentication


  reset_priority_affinity (False, any, None)
    Reset


  name (True, any, None)
    SLB Service Name


  traffic_replication_mirror (False, any, None)
    Mirror Bi-directional Packet


  traffic_replication_mirror_sa_da_repl (False, any, None)
    Replace Source MAC and Destination MAC


  priorities (False, any, None)
    Field priorities


    priority (optional, any, None)
      Priority option. Define different action for each priority node. (Priority in the Group)


    priority_action (optional, any, None)
      'drop'= Drop request when all priority nodes fail; 'drop-if-exceed-limit'= Drop request when connection over limit; 'proceed'= Proceed to next priority when all priority nodes fail(default); 'reset'= Send client reset when all priority nodes fail; 'reset-if-exceed-limit'= Send client reset when connection over limit;



  conn_rate_grace_period (False, any, None)
    Define the grace period during transition (Define the grace period during transition(seconds))


  conn_rate_log (False, any, None)
    Send log if transition happens


  health_check (False, any, None)
    Health Check (Monitor Name)


  priority_affinity (False, any, None)
    Priority affinity. Persist to the same priority if possible.


  traffic_replication_mirror_ip_repl (False, any, None)
    Replaces IP with server-IP


  min_active_member (False, any, None)
    Minimum Active Member Per Priority (Minimum Active Member before Action)


  user_tag (False, any, None)
    Customized tag


  top_fastest (False, any, None)
    Report top 10 fastest servers


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'server_selection_fail_drop'= Drops due to Service selection failure; 'server_selection_fail_reset'= Resets sent out for Service selection failure; 'service_peak_conn'= Peak connection count for the Service Group; 'service_healthy_host'= Service Group healthy host count; 'service_unhealthy_host'= Service Group unhealthy host count; 'service_req_count'= Service Group request count; 'service_resp_count'= Service Group response count; 'service_resp_2xx'= Service Group response 2xx count; 'service_resp_3xx'= Service Group response 3xx count; 'service_resp_4xx'= Service Group response 4xx count; 'service_resp_5xx'= Service Group response 5xx count; 'service_curr_conn_overflow'= Current connection counter overflow count;










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

