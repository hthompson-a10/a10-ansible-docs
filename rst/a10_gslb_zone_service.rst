.. _a10_gslb_zone_service_module:


a10_gslb_zone_service -- Configures A10 gslb.zone.service
=========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Service information for the GSLB zone






Parameters
----------

  oper (False, any, None)
    Field oper


    total_sessions (optional, any, None)
      Field total_sessions


    service_port (optional, any, None)
      Port number of the service


    cache_list (optional, any, None)
      Field cache_list


    state (optional, any, None)
      Field state


    dns_mx_record_list (optional, any, None)
      Field dns_mx_record_list


    service_name (optional, any, None)
      Specify the service name for the zone, * for wildcard


    dns_ns_record_list (optional, any, None)
      Field dns_ns_record_list


    session_list (optional, any, None)
      Field session_list


    matched (optional, any, None)
      Field matched



  dns_record_list (False, any, None)
    Field dns_record_list


    ntype (optional, any, None)
      Specify DNS Type


    data (optional, any, None)
      Specify DNS Data


    uuid (optional, any, None)
      uuid of the object



  ansible_username (True, any, None)
    Username for AXAPI authentication


  service_name (True, any, None)
    Specify the service name for the zone, * for wildcard


  health_check_port (False, any, None)
    Field health_check_port


    health_check_port (optional, any, None)
      Check Related Port Status (Port Number)



  health_check_gateway (False, any, None)
    'enable'= Enable Gateway Status Check; 'disable'= Disable Gateway Status Check;


  dns_ns_record_list (False, any, None)
    Field dns_ns_record_list


    sampling_enable (optional, any, None)
      Field sampling_enable


    ns_name (optional, any, None)
      Specify Domain Name


    uuid (optional, any, None)
      uuid of the object


    ttl (optional, any, None)
      Specify TTL



  disable (False, any, None)
    Disable


  service_port (True, any, None)
    Port number of the service


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  zone_name (optional, any, None)
    Key to identify parent object


  dns_cname_record_list (False, any, None)
    Field dns_cname_record_list


    sampling_enable (optional, any, None)
      Field sampling_enable


    as_backup (optional, any, None)
      As backup when fail


    uuid (optional, any, None)
      uuid of the object


    weight (optional, any, None)
      Specify Weight, default is 1


    admin_preference (optional, any, None)
      Specify Administrative Preference, default is 100


    alias_name (optional, any, None)
      Specify the alias name



  ansible_host (True, any, None)
    Host for AXAPI authentication


  dns_srv_record_list (False, any, None)
    Field dns_srv_record_list


    sampling_enable (optional, any, None)
      Field sampling_enable


    priority (optional, any, None)
      Specify Priority


    uuid (optional, any, None)
      uuid of the object


    weight (optional, any, None)
      Specify Weight, default is 10


    srv_name (optional, any, None)
      Specify Domain Name


    ttl (optional, any, None)
      Specify TTL


    port (optional, any, None)
      Specify Port (Port Number)



  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'received-query'= Number of DNS queries received for the service; 'sent-response'= Number of DNS replies sent to clients for the service; 'proxy- mode-response'= Number of DNS replies sent to clients by the ACOS device as a DNS proxy for the service; 'cache-mode-response'= Number of cached DNS replies sent to clients by the ACOS device for the service. (This statistic applies only if the DNS cache; 'server-mode-response'= Number of DNS replies sent to clients by the ACOS device as a DNS server for the service. (This statistic applies only if the D; 'sticky-mode-response'= Number of DNS replies sent to clients by the ACOS device to keep the clients on the same site. (This statistic applies only if; 'backup-mode-response'= help Number of DNS replies sent to clients by the ACOS device in backup mode;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    received_query (optional, any, None)
      Number of DNS queries received for the service


    dns_naptr_record_list (optional, any, None)
      Field dns_naptr_record_list


    sent_response (optional, any, None)
      Number of DNS replies sent to clients for the service


    sticky_mode_response (optional, any, None)
      Number of DNS replies sent to clients by the ACOS device to keep the clients on the same site. (This statistic applies only if


    backup_mode_response (optional, any, None)
      help Number of DNS replies sent to clients by the ACOS device in backup mode


    service_port (optional, any, None)
      Port number of the service


    dns_cname_record_list (optional, any, None)
      Field dns_cname_record_list


    dns_srv_record_list (optional, any, None)
      Field dns_srv_record_list


    proxy_mode_response (optional, any, None)
      Number of DNS replies sent to clients by the ACOS device as a DNS proxy for the service


    cache_mode_response (optional, any, None)
      Number of cached DNS replies sent to clients by the ACOS device for the service. (This statistic applies only if the DNS cache


    dns_a_record (optional, any, None)
      Field dns_a_record


    server_mode_response (optional, any, None)
      Number of DNS replies sent to clients by the ACOS device as a DNS server for the service. (This statistic applies only if the D


    dns_ptr_record_list (optional, any, None)
      Field dns_ptr_record_list


    dns_txt_record_list (optional, any, None)
      Field dns_txt_record_list


    dns_mx_record_list (optional, any, None)
      Field dns_mx_record_list


    service_name (optional, any, None)
      Specify the service name for the zone, * for wildcard


    dns_ns_record_list (optional, any, None)
      Field dns_ns_record_list



  uuid (False, any, None)
    uuid of the object


  dns_a_record (False, any, None)
    Field dns_a_record


    dns_a_record_ipv6_list (optional, any, None)
      Field dns_a_record_ipv6_list


    dns_a_record_ipv4_list (optional, any, None)
      Field dns_a_record_ipv4_list


    dns_a_record_srv_list (optional, any, None)
      Field dns_a_record_srv_list



  a10_partition (False, any, None)
    Destination/target partition for object/command


  geo_location_list (False, any, None)
    Field geo_location_list


    uuid (optional, any, None)
      uuid of the object


    alias (optional, any, None)
      Field alias


    action_type (optional, any, None)
      'allow'= Allow query from this geo-location; 'drop'= Drop query from this geo- location; 'forward'= Forward packet for this geo-location; 'ignore'= Send empty response to this geo-location; 'reject'= Send refuse response to this geo- location;


    policy (optional, any, None)
      Policy for this geo-location (Specify the policy name)


    user_tag (optional, any, None)
      Customized tag


    action (optional, any, None)
      Action for this geo-location


    forward_type (optional, any, None)
      'both'= Forward both query and response; 'query'= Forward query from this geo- location; 'response'= Forward response to this geo-location;


    geo_name (optional, any, None)
      Specify the geo-location



  action (False, any, None)
    'drop'= Drop query; 'forward'= Forward packet; 'ignore'= Send empty response; 'reject'= Send refuse response;


  state (True, any, None)
    State of the object to be created.


  dns_ptr_record_list (False, any, None)
    Field dns_ptr_record_list


    sampling_enable (optional, any, None)
      Field sampling_enable


    ptr_name (optional, any, None)
      Specify Domain Name


    uuid (optional, any, None)
      uuid of the object


    ttl (optional, any, None)
      Specify TTL



  dns_txt_record_list (False, any, None)
    Field dns_txt_record_list


    sampling_enable (optional, any, None)
      Field sampling_enable


    txt_data (optional, any, None)
      Specify TXT Data


    record_name (optional, any, None)
      Specify the Object Name for TXT Data


    uuid (optional, any, None)
      uuid of the object


    ttl (optional, any, None)
      Specify TTL



  dns_mx_record_list (False, any, None)
    Field dns_mx_record_list


    mx_name (optional, any, None)
      Specify Domain Name


    priority (optional, any, None)
      Specify Priority


    ttl (optional, any, None)
      Specify TTL


    uuid (optional, any, None)
      uuid of the object


    sampling_enable (optional, any, None)
      Field sampling_enable



  dns_naptr_record_list (False, any, None)
    Field dns_naptr_record_list


    sampling_enable (optional, any, None)
      Field sampling_enable


    service_proto (optional, any, None)
      Specify Service and Protocol


    uuid (optional, any, None)
      uuid of the object


    naptr_target (optional, any, None)
      Specify the replacement or regular expression


    flag (optional, any, None)
      Specify the flag (e.g., a, s). Default is empty flag


    preference (optional, any, None)
      Specify Preference


    ttl (optional, any, None)
      Specify TTL


    regexp (optional, any, None)
      Return the regular expression


    order (optional, any, None)
      Specify Order



  policy (False, any, None)
    Specify policy for this service (Specify policy name)


  user_tag (False, any, None)
    Customized tag


  ansible_password (True, any, None)
    Password for AXAPI authentication


  forward_type (False, any, None)
    'both'= Forward both query and response; 'query'= Forward query; 'response'= Forward response;









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

