.. _a10_gslb_policy_dns_module:


a10_gslb_policy_dns -- Configures A10 gslb.policy.dns
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

DNS related policy






Parameters
----------

  server_sec (False, any, None)
    Provide DNSSEC support


  geoloc_alias (False, any, None)
    Return alias name by geo-location


  server_naptr (False, any, None)
    Provide NAPTR Records


  ansible_username (True, any, None)
    Username for AXAPI authentication


  block_value (False, any, None)
    Field block_value


    block_value (optional, any, None)
      Specify Type Number



  geoloc_policy (False, any, None)
    Apply different policy by geo-location


  proxy_block_port_range_list (False, any, None)
    Field proxy_block_port_range_list


    proxy_block_range_to (optional, any, None)
      To


    proxy_block_range_from (optional, any, None)
      Specify Type Range (From)



  sticky (False, any, None)
    Make DNS Record sticky for certain time


  delegation (False, any, None)
    Zone Delegation


  ip_replace (False, any, None)
    Replace DNS Server Response with GSLB Service-IPs


  server_cname (False, any, None)
    Provide CNAME Records


  ttl (False, any, None)
    Specify the TTL value contained in DNS record (TTL value, unit= second, default is 10)


  server_ptr (False, any, None)
    Provide PTR Records


  aging_time (False, any, None)
    Specify aging-time, default is TTL in DNS record, unit= second (Aging time, default 0 means using TTL in DNS record as aging time)


  geoloc_action (False, any, None)
    Apply DNS action by geo-location


  dynamic_preference (False, any, None)
    Make dynamically change the preference


  uuid (False, any, None)
    uuid of the object


  server_any_with_metric (False, any, None)
    Provide All Records with GSLB Metrics applied to A/AAAA Records


  external_soa (False, any, None)
    Return DNS response with external SOA Record


  server_any (False, any, None)
    Provide All Records


  selected_only_value (False, any, None)
    Answer Number


  cache (False, any, None)
    Cache DNS Server response


  state (True, any, None)
    State of the object to be created.


  server_auto_ptr (False, any, None)
    Provide PTR Records automatically


  server_mx (False, any, None)
    Provide MX Records


  server_authoritative (False, any, None)
    As authoritative server


  template (False, any, None)
    Logging template (Logging Template Name)


  ipv6 (False, any, None)
    Field ipv6


    dns_ipv6_option (optional, any, None)
      'mix'= Return both AAAA Record and A Record; 'smart'= Return AAAA Record by DNS Query Type; 'mapping'= Map A Record to AAAA Record;


    dns_ipv6_mapping_type (optional, any, None)
      'addition'= Append Mapped Record in DNS Addition Section; 'answer'= Append Mapped Record in DNS Answer Section; 'exclusive'= Only return AAAA Record; 'replace'= Replace Record with Mapped Record;



  dynamic_weight (False, any, None)
    dynamically change the weight


  ansible_host (True, any, None)
    Host for AXAPI authentication


  server_auto_ns (False, any, None)
    Provide A-Records for NS-Records automatically


  use_server_ttl (False, any, None)
    Use DNS Server Response TTL value in GSLB Proxy mode


  block_type (False, any, None)
    Field block_type


  dns_auto_map (False, any, None)
    Automatically build DNS Infrastructure


  dns_addition_mx (False, any, None)
    Append MX Records in Addition Section


  active_only_fail_safe (False, any, None)
    Continue if no candidate


  cname_detect (False, any, None)
    Apply GSLB for DNS Server response when service is Canonical Name (CNAME)


  backup_server (False, any, None)
    Return fallback server when fail


  server_full_list (False, any, None)
    Append All A Records in Authoritative Section


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  sticky_ipv6_mask (False, any, None)
    Specify IPv6 mask length, default is 128


  policy_name (optional, any, None)
    Key to identify parent object


  a10_partition (False, any, None)
    Destination/target partition for object/command


  sticky_aging_time (False, any, None)
    Specify aging-time, unit= min, default is 5 (Aging time)


  server_addition_mx (False, any, None)
    Append MX Records in Addition Section


  active_only (False, any, None)
    Only keep active servers


  ansible_port (True, any, None)
    Port for AXAPI authentication


  backup_alias (False, any, None)
    Return alias name when fail


  logging (False, any, None)
    'none'= None; 'query'= DNS Query; 'response'= DNS Response; 'both'= Both DNS Query and Response;


  server_ns_list (False, any, None)
    Append All NS Records in Authoritative Section


  selected_only (False, any, None)
    Only keep selected servers


  external_ip (False, any, None)
    Return DNS response with external IP address


  ansible_password (True, any, None)
    Password for AXAPI authentication


  hint (False, any, None)
    'none'= None; 'answer'= Append Hint Records in DNS Answer Section; 'addition'= Append Hint Records in DNS Addition Section;


  server_txt (False, any, None)
    Provide TXT Records


  server (False, any, None)
    Run GSLB as DNS server mode


  server_srv (False, any, None)
    Provide SRV Records


  block_action (False, any, None)
    Specify Action


  server_mode_only (False, any, None)
    Only run GSLB as DNS server mode


  action_type (False, any, None)
    'drop'= Drop query; 'reject'= Send refuse response; 'ignore'= Send empty response;


  action (False, any, None)
    Apply DNS action for service


  server_ns (False, any, None)
    Provide NS Records


  sticky_mask (False, any, None)
    Specify IP mask, default is /32









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

