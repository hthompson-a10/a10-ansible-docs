.. _a10_gslb_zone_module:


a10_gslb_zone -- Configures A10 gslb.zone
=========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Specify the DNS zone name for which global SLB is provided






Parameters
----------

  oper (False, any, None)
    Field oper


    dns_ns_record_list (optional, any, None)
      Field dns_ns_record_list


    service_list (optional, any, None)
      Field service_list


    state (optional, any, None)
      Field state


    name (optional, any, None)
      Specify the name for the DNS zone


    dns_mx_record_list (optional, any, None)
      Field dns_mx_record_list



  use_server_ttl (False, any, None)
    Use DNS Server Response TTL value in GSLB Proxy mode


  dns_soa_record (False, any, None)
    Field dns_soa_record


    ex_expire (optional, any, None)
      Specify Expire Time Interval, default is 1209600


    retry (optional, any, None)
      Specify Retry Time Interval, default is 900


    ex_retry (optional, any, None)
      Specify Retry Time Interval, default is 900


    soa_ttl (optional, any, None)
      Specify Negative caching TTL, default is Zone TTL


    soa_name (optional, any, None)
      DNS Server Name


    refresh (optional, any, None)
      Specify Refresh Time Interval, default is 3600


    ex_serial (optional, any, None)
      Specify Serial Number, default is Current Time (Time Interval)


    ex_soa_ttl (optional, any, None)
      Specify Negative caching TTL, default is Zone TTL


    expire (optional, any, None)
      Specify Expire Time Interval, default is 1209600


    external (optional, any, None)
      Specify External SOA Record (DNS Server Name)


    ex_mail (optional, any, None)
      Mailbox


    mail (optional, any, None)
      Mailbox


    serial (optional, any, None)
      Specify Serial Number, default is Current Time (Time Interval)


    ex_refresh (optional, any, None)
      Specify Refresh Time Interval, default is 3600



  template (False, any, None)
    Field template


    dnssec (optional, any, None)
      Specify DNSSEC template (Specify template name)



  ansible_username (True, any, None)
    Username for AXAPI authentication


  service_list (False, any, None)
    Field service_list


    dns_record_list (optional, any, None)
      Field dns_record_list


    dns_naptr_record_list (optional, any, None)
      Field dns_naptr_record_list


    health_check_port (optional, any, None)
      Field health_check_port


    policy (optional, any, None)
      Specify policy for this service (Specify policy name)


    disable (optional, any, None)
      Disable


    health_check_gateway (optional, any, None)
      'enable'= Enable Gateway Status Check; 'disable'= Disable Gateway Status Check;


    dns_cname_record_list (optional, any, None)
      Field dns_cname_record_list


    action (optional, any, None)
      'drop'= Drop query; 'forward'= Forward packet; 'ignore'= Send empty response; 'reject'= Send refuse response;


    dns_srv_record_list (optional, any, None)
      Field dns_srv_record_list


    sampling_enable (optional, any, None)
      Field sampling_enable


    uuid (optional, any, None)
      uuid of the object


    dns_a_record (optional, any, None)
      Field dns_a_record


    service_port (optional, any, None)
      Port number of the service


    geo_location_list (optional, any, None)
      Field geo_location_list


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


    user_tag (optional, any, None)
      Customized tag


    forward_type (optional, any, None)
      'both'= Forward both query and response; 'query'= Forward query; 'response'= Forward response;



  policy (False, any, None)
    Specify the policy for this zone (Specify policy name)


  disable (False, any, None)
    Disable all services in the GSLB zone


  ttl (False, any, None)
    Specify the zone ttl value (TTL value, unit= second, default is 10)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  name (True, any, None)
    Specify the name for the DNS zone


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'received-query'= Total Number of DNS queries received for the zone; 'sent-response'= Total Number of DNS replies sent to clients for the zone; 'proxy-mode-response'= Total Number of DNS replies sent to clients by the ACOS device as a DNS proxy for the zone; 'cache-mode-response'= Total Number of cached DNS replies sent to clients by the ACOS device for the zone. (This statistic applies only if the DNS cac; 'server-mode-response'= Total Number of DNS replies sent to clients by the ACOS device as a DNS server for the zone. (This statistic applies only if th; 'sticky-mode-response'= Total Number of DNS replies sent to clients by the ACOS device to keep the clients on the same site. (This statistic applies on; 'backup-mode-response'= Total Number of DNS replies sent to clients by the ACOS device in backup mode;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    name (optional, any, None)
      Specify the name for the DNS zone


    received_query (optional, any, None)
      Total Number of DNS queries received for the zone


    proxy_mode_response (optional, any, None)
      Total Number of DNS replies sent to clients by the ACOS device as a DNS proxy for the zone


    service_list (optional, any, None)
      Field service_list


    cache_mode_response (optional, any, None)
      Total Number of cached DNS replies sent to clients by the ACOS device for the zone. (This statistic applies only if the DNS cac


    sent_response (optional, any, None)
      Total Number of DNS replies sent to clients for the zone


    sticky_mode_response (optional, any, None)
      Total Number of DNS replies sent to clients by the ACOS device to keep the clients on the same site. (This statistic applies on


    backup_mode_response (optional, any, None)
      Total Number of DNS replies sent to clients by the ACOS device in backup mode


    dns_mx_record_list (optional, any, None)
      Field dns_mx_record_list


    dns_ns_record_list (optional, any, None)
      Field dns_ns_record_list


    server_mode_response (optional, any, None)
      Total Number of DNS replies sent to clients by the ACOS device as a DNS server for the zone. (This statistic applies only if th



  uuid (False, any, None)
    uuid of the object


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


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

