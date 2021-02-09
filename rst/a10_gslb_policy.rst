.. _a10_gslb_policy_module:


a10_gslb_policy -- Configures A10 gslb.policy
=============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Policy for GSLB zone, service or geo-location






Parameters
----------

  oper (False, any, None)
    Field oper


    metric_list (optional, any, None)
      Field metric_list


    name (optional, any, None)
      Specify policy name



  bw_cost_enable (False, any, None)
    Enable bw cost


  ansible_username (True, any, None)
    Username for AXAPI authentication


  active_servers_fail_break (False, any, None)
    Break when no active server


  weighted_alias (False, any, None)
    Select alias name by weighted preference


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  health_check (False, any, None)
    Select Service-IP by health status


  admin_ip_enable (False, any, None)
    Enable admin ip


  edns (False, any, None)
    Field edns


    uuid (optional, any, None)
      uuid of the object


    client_subnet_geographic (optional, any, None)
      Use client subnet for geo-location



  health_preference_top (False, any, None)
    Only keep top n


  weighted_ip_total_hits (False, any, None)
    Weighted by total hits


  alias_admin_preference (False, any, None)
    Select alias name having maximum admin preference


  capacity (False, any, None)
    Field capacity


    threshold (optional, any, None)
      Specify capacity threshold, default is 90


    capacity_enable (optional, any, None)
      Enable capacity


    capacity_fail_break (optional, any, None)
      Break when exceed threshold


    uuid (optional, any, None)
      uuid of the object



  weighted_site_total_hits (False, any, None)
    Weighted by total hits


  metric_force_check (False, any, None)
    Always check Service-IP for all enabled metrics


  a10_partition (False, any, None)
    Destination/target partition for object/command


  geo_location_match (False, any, None)
    Field geo_location_match


    geo_type_overlap (optional, any, None)
      'global'= Global Geo-location; 'policy'= Policy Geo-location;


    match_first (optional, any, None)
      'global'= Global Geo-location; 'policy'= Policy Geo-location;


    uuid (optional, any, None)
      uuid of the object


    overlap (optional, any, None)
      Enable overlap mode to do longest match



  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  dns (False, any, None)
    Field dns


    server_sec (optional, any, None)
      Provide DNSSEC support


    geoloc_alias (optional, any, None)
      Return alias name by geo-location


    sticky (optional, any, None)
      Make DNS Record sticky for certain time


    block_value (optional, any, None)
      Field block_value


    backup_server (optional, any, None)
      Return fallback server when fail


    proxy_block_port_range_list (optional, any, None)
      Field proxy_block_port_range_list


    server_naptr (optional, any, None)
      Provide NAPTR Records


    delegation (optional, any, None)
      Zone Delegation


    selected_only (optional, any, None)
      Only keep selected servers


    server_cname (optional, any, None)
      Provide CNAME Records


    ttl (optional, any, None)
      Specify the TTL value contained in DNS record (TTL value, unit= second, default is 10)


    server_ptr (optional, any, None)
      Provide PTR Records


    aging_time (optional, any, None)
      Specify aging-time, default is TTL in DNS record, unit= second (Aging time, default 0 means using TTL in DNS record as aging time)


    geoloc_action (optional, any, None)
      Apply DNS action by geo-location


    uuid (optional, any, None)
      uuid of the object


    server_any_with_metric (optional, any, None)
      Provide All Records with GSLB Metrics applied to A/AAAA Records


    external_soa (optional, any, None)
      Return DNS response with external SOA Record


    server_any (optional, any, None)
      Provide All Records


    selected_only_value (optional, any, None)
      Answer Number


    cache (optional, any, None)
      Cache DNS Server response


    server_authoritative (optional, any, None)
      As authoritative server


    server_auto_ptr (optional, any, None)
      Provide PTR Records automatically


    server_mx (optional, any, None)
      Provide MX Records


    template (optional, any, None)
      Logging template (Logging Template Name)


    ipv6 (optional, any, None)
      Field ipv6


    dynamic_weight (optional, any, None)
      dynamically change the weight


    server_auto_ns (optional, any, None)
      Provide A-Records for NS-Records automatically


    use_server_ttl (optional, any, None)
      Use DNS Server Response TTL value in GSLB Proxy mode


    block_type (optional, any, None)
      Field block_type


    dns_auto_map (optional, any, None)
      Automatically build DNS Infrastructure


    dns_addition_mx (optional, any, None)
      Append MX Records in Addition Section


    active_only_fail_safe (optional, any, None)
      Continue if no candidate


    geoloc_policy (optional, any, None)
      Apply different policy by geo-location


    server_full_list (optional, any, None)
      Append All A Records in Authoritative Section


    ip_replace (optional, any, None)
      Replace DNS Server Response with GSLB Service-IPs


    sticky_ipv6_mask (optional, any, None)
      Specify IPv6 mask length, default is 128


    dynamic_preference (optional, any, None)
      Make dynamically change the preference


    sticky_aging_time (optional, any, None)
      Specify aging-time, unit= min, default is 5 (Aging time)


    server_addition_mx (optional, any, None)
      Append MX Records in Addition Section


    active_only (optional, any, None)
      Only keep active servers


    backup_alias (optional, any, None)
      Return alias name when fail


    logging (optional, any, None)
      'none'= None; 'query'= DNS Query; 'response'= DNS Response; 'both'= Both DNS Query and Response;


    server_ns_list (optional, any, None)
      Append All NS Records in Authoritative Section


    external_ip (optional, any, None)
      Return DNS response with external IP address


    cname_detect (optional, any, None)
      Apply GSLB for DNS Server response when service is Canonical Name (CNAME)


    hint (optional, any, None)
      'none'= None; 'answer'= Append Hint Records in DNS Answer Section; 'addition'= Append Hint Records in DNS Addition Section;


    server_txt (optional, any, None)
      Provide TXT Records


    server (optional, any, None)
      Run GSLB as DNS server mode


    server_srv (optional, any, None)
      Provide SRV Records


    block_action (optional, any, None)
      Specify Action


    server_mode_only (optional, any, None)
      Only run GSLB as DNS server mode


    action_type (optional, any, None)
      'drop'= Drop query; 'reject'= Send refuse response; 'ignore'= Send empty response;


    action (optional, any, None)
      Apply DNS action for service


    server_ns (optional, any, None)
      Provide NS Records


    sticky_mask (optional, any, None)
      Specify IP mask, default is /32



  weighted_site_enable (False, any, None)
    Enable Select Service-IP by weighted site preference


  bw_cost_fail_break (False, any, None)
    Break when exceed limit


  num_session_tolerance (False, any, None)
    The difference between the available sessions, default is 10 (Tolerance)


  amount_first (False, any, None)
    Select record based on the amount of available service-ip


  active_rdt (False, any, None)
    Field active_rdt


    keep_tracking (optional, any, None)
      Keep tracking client even round-delay-time samples are ready


    enable (optional, any, None)
      Enable the active rdt


    timeout (optional, any, None)
      Specify timeout if round-delay-time samples are not ready (Specify timeout, unit=sec,default is 3)


    single_shot (optional, any, None)
      Single Shot RDT


    skip (optional, any, None)
      Skip query if round-delay-time samples are not ready (Specify maximum skip count,default is 3)


    ignore_id (optional, any, None)
      Ignore IP Address specified in IP List by ID


    controller (optional, any, None)
      Active round-delay-time by controller


    limit (optional, any, None)
      Limit of allowed RDT, default is 16383 (Limit, unit= millisecond)


    samples (optional, any, None)
      Specify samples number for round-delay-time (Number of samples,default is 5)


    proto_rdt_enable (optional, any, None)
      Enable the round-delay-time to the controller


    fail_break (optional, any, None)
      Break when no valid RDT


    difference (optional, any, None)
      The difference between the round-delay-time, default is 0


    tolerance (optional, any, None)
      The difference percentage between the round-delay-time, default is 10 (Tolerance)


    uuid (optional, any, None)
      uuid of the object



  ansible_port (True, any, None)
    Port for AXAPI authentication


  round_robin (False, any, None)
    Round robin selection, enabled by default


  health_check_preference_enable (False, any, None)
    Check health preference


  admin_preference (False, any, None)
    Select Service-IP for the device having maximum admin preference


  metric_type (False, any, None)
    Field metric_type


  active_servers_enable (False, any, None)
    Enable Select Service-IP with the highest number of active servers


  connection_load (False, any, None)
    Field connection_load


    connection_load_fail_break (optional, any, None)
      Break when exceed limit


    uuid (optional, any, None)
      uuid of the object


    limit (optional, any, None)
      Limit of maxinum connection load, default is unlimited


    connection_load_samples (optional, any, None)
      Specify samples for connection-load (Number of samples used to calculate the connection load, default is 5)


    connection_load_enable (optional, any, None)
      Enable connection-load


    connection_load_limit (optional, any, None)
      The value of the connection-load limit, default is unlimited


    connection_load_interval (optional, any, None)
      Interval between two samples, Unit= second (Interval value,default is 5)



  ordered_ip_top_only (False, any, None)
    Return highest priority server only


  ip_list (False, any, None)
    Specify IP List (IP List Name)


  least_response (False, any, None)
    Least response selection


  uuid (False, any, None)
    uuid of the object


  weighted_ip_enable (False, any, None)
    Enable Select Service-IP by weighted preference


  name (True, any, None)
    Specify policy name


  geo_location_list (False, any, None)
    Field geo_location_list


    ip_multiple_fields (optional, any, None)
      Field ip_multiple_fields


    ipv6_multiple_fields (optional, any, None)
      Field ipv6_multiple_fields


    user_tag (optional, any, None)
      Customized tag


    name (optional, any, None)
      Specify geo-location name, section range is (1-15)


    uuid (optional, any, None)
      uuid of the object



  metric_fail_break (False, any, None)
    Break if no valid Service-IP


  ansible_password (True, any, None)
    Password for AXAPI authentication


  metric_order (False, any, None)
    Specify order of metric


  auto_map (False, any, None)
    Field auto_map


    all (optional, any, None)
      All modules


    ttl (optional, any, None)
      Specify Auto Map TTL (TTL, default is 300)


    module_type (optional, any, None)
      Field module_type


    uuid (optional, any, None)
      uuid of the object


    module_disable (optional, any, None)
      Specify Disable Auto Map Module



  num_session_enable (False, any, None)
    Enable Select Service-IP for device having maximum number of available sessions


  admin_ip_top_only (False, any, None)
    Return highest priority server only


  geographic (False, any, None)
    Select Service-IP by geographic


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

