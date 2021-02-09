.. _a10_rule_set_module:


a10_rule_set -- Configures A10 rule-set
=======================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure Security policy Rule Set






Parameters
----------

  rule_list (False, any, None)
    Field rule_list


    cgnv6_lsn_lid (optional, any, None)
      LSN LID


    src_zone (optional, any, None)
      Zone name


    dst_domain_list (optional, any, None)
      Match destination IP against domain-list


    service_any (optional, any, None)
      'any'= any;


    src_zone_any (optional, any, None)
      'any'= any;


    src_threat_list (optional, any, None)
      Bind threat-list for source IP based filtering


    listen_on_port_lid (optional, any, None)
      Apply a Template LID


    fw_log (optional, any, None)
      Enable logging


    src_geoloc_name (optional, any, None)
      Single geolocation name


    track_application (optional, any, None)
      Enable application statistic


    dst_zone (optional, any, None)
      Zone name


    dst_zone_any (optional, any, None)
      'any'= any;


    src_geoloc_list (optional, any, None)
      Geolocation name list


    dst_ipv6_any (optional, any, None)
      'any'= Any IPv6 address;


    action (optional, any, None)
      'permit'= permit; 'deny'= deny; 'reset'= reset;


    lid (optional, any, None)
      Apply a Template LID


    dst_class_list (optional, any, None)
      Match destination IP against class-list


    src_ipv4_any (optional, any, None)
      'any'= Any IPv4 address;


    log (optional, any, None)
      Enable logging


    dest_list (optional, any, None)
      Field dest_list


    dst_geoloc_name (optional, any, None)
      Single geolocation name


    service_list (optional, any, None)
      Field service_list


    dst_ipv4_any (optional, any, None)
      'any'= Any IPv4 address;


    policy (optional, any, None)
      'cgnv6'= Apply CGNv6 policy; 'forward'= Forward packet;


    reset_lidlog (optional, any, None)
      Enable logging


    listen_on_port (optional, any, None)
      Listen on port


    status (optional, any, None)
      'enable'= Enable rule; 'disable'= Disable rule;


    lidlog (optional, any, None)
      Enable logging


    cgnv6_fixed_nat_log (optional, any, None)
      Enable logging


    app_list (optional, any, None)
      Field app_list


    source_list (optional, any, None)
      Field source_list


    src_geoloc_list_shared (optional, any, None)
      Use Geolocation list from shared partition


    src_class_list (optional, any, None)
      Match source IP against class-list


    idle_timeout (optional, any, None)
      TCP/UDP idle-timeout


    src_ipv6_any (optional, any, None)
      'any'= Any IPv6 address;


    move_rule (optional, any, None)
      Field move_rule


    application_any (optional, any, None)
      'any'= any;


    uuid (optional, any, None)
      uuid of the object


    cgnv6_lsn_log (optional, any, None)
      Enable logging


    remark (optional, any, None)
      Rule entry comment (Notes for this rule)


    name (optional, any, None)
      Rule name


    listen_on_port_lidlog (optional, any, None)
      Enable logging


    cgnv6_policy (optional, any, None)
      'lsn-lid'= Apply specified CGNv6 LSN LID; 'fixed-nat'= Apply CGNv6 Fixed NAT;


    cgnv6_log (optional, any, None)
      Enable logging


    fwlog (optional, any, None)
      Enable logging


    dst_threat_list (optional, any, None)
      Bind threat-list for destination IP based filtering


    forward_listen_on_port (optional, any, None)
      Listen on port


    dst_geoloc_list (optional, any, None)
      Geolocation name list


    dst_geoloc_list_shared (optional, any, None)
      Use Geolocation list from shared partition


    reset_lid (optional, any, None)
      Apply a Template LID


    forward_log (optional, any, None)
      Enable logging


    user_tag (optional, any, None)
      Customized tag


    ip_version (optional, any, None)
      'v4'= IPv4 rule; 'v6'= IPv6 rule;


    sampling_enable (optional, any, None)
      Field sampling_enable



  oper (False, any, None)
    Field oper


    rule_list (optional, any, None)
      Field rule_list


    total_active_others (optional, any, None)
      Field total_active_others


    total_reset_bytes (optional, any, None)
      Field total_reset_bytes


    total_active_icmp (optional, any, None)
      Field total_active_icmp


    policy_status (optional, any, None)
      Field policy_status


    total_deny_bytes (optional, any, None)
      Field total_deny_bytes


    policy_unmatched_drop (optional, any, None)
      Field policy_unmatched_drop


    total_permit_bytes (optional, any, None)
      Field total_permit_bytes


    policy_deny (optional, any, None)
      Field policy_deny


    total_bytes (optional, any, None)
      Field total_bytes


    total_reset_packets (optional, any, None)
      Field total_reset_packets


    track_app_rule_list (optional, any, None)
      Field track_app_rule_list


    rule_stats (optional, any, None)
      Field rule_stats


    total_active_udp (optional, any, None)
      Field total_active_udp


    name (optional, any, None)
      Rule set name


    policy_reset (optional, any, None)
      Field policy_reset


    topn_rules (optional, any, None)
      Field topn_rules


    total_hit (optional, any, None)
      Field total_hit


    total_deny_packets (optional, any, None)
      Field total_deny_packets


    application (optional, any, None)
      Field application


    total_permit_packets (optional, any, None)
      Field total_permit_packets


    total_packets (optional, any, None)
      Field total_packets


    show_total_stats (optional, any, None)
      Field show_total_stats


    policy_permit (optional, any, None)
      Field policy_permit


    policy_rule_count (optional, any, None)
      Field policy_rule_count


    total_active_tcp (optional, any, None)
      Field total_active_tcp


    rules_by_zone (optional, any, None)
      Field rules_by_zone



  ansible_username (True, any, None)
    Username for AXAPI authentication


  app (False, any, None)
    Field app


    uuid (optional, any, None)
      uuid of the object



  remark (False, any, None)
    Rule set entry comment (Notes for this rule set)


  tag (False, any, None)
    Field tag


    uuid (optional, any, None)
      uuid of the object



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  track_app_rule_list (False, any, None)
    Field track_app_rule_list


    uuid (optional, any, None)
      uuid of the object



  uuid (False, any, None)
    uuid of the object


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'unmatched-drops'= Unmatched drops counter; 'permit'= Permitted counter; 'deny'= Denied counter; 'reset'= Reset counter;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    reset (optional, any, None)
      Reset counter


    rule_list (optional, any, None)
      Field rule_list


    deny (optional, any, None)
      Denied counter


    name (optional, any, None)
      Rule set name


    app (optional, any, None)
      Field app


    tag (optional, any, None)
      Field tag


    permit (optional, any, None)
      Permitted counter


    rules_by_zone (optional, any, None)
      Field rules_by_zone


    track_app_rule_list (optional, any, None)
      Field track_app_rule_list


    unmatched_drops (optional, any, None)
      Unmatched drops counter



  name (True, any, None)
    Rule set name


  user_tag (False, any, None)
    Customized tag


  session_statistic (False, any, None)
    'enable'= Enable session based statistic (Default); 'disable'= Disable session based statistic;


  application (False, any, None)
    Field application


    uuid (optional, any, None)
      uuid of the object



  state (True, any, None)
    State of the object to be created.


  ansible_password (True, any, None)
    Password for AXAPI authentication


  rules_by_zone (False, any, None)
    Field rules_by_zone


    sampling_enable (optional, any, None)
      Field sampling_enable


    uuid (optional, any, None)
      uuid of the object










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

