.. _a10_slb_resource_usage_module:


a10_slb_resource_usage -- Configures A10 slb.resource-usage
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure SLB Resource Usage






Parameters
----------

  oper (False, any, None)
    Field oper


    real_port_max (optional, any, None)
      Field real_port_max


    health_monitor_count_min (optional, any, None)
      Field health_monitor_count_min


    fix_template_min (optional, any, None)
      Field fix_template_min


    persist_srcip_template_default (optional, any, None)
      Field persist_srcip_template_default


    gslb_site_count_min (optional, any, None)
      Field gslb_site_count_min


    server_ssl_template_min (optional, any, None)
      Field server_ssl_template_min


    gslb_template_count_min (optional, any, None)
      Field gslb_template_count_min


    fast_udp_template_min (optional, any, None)
      Field fast_udp_template_min


    gslb_service_ip_count_max (optional, any, None)
      Field gslb_service_ip_count_max


    virtual_port_default (optional, any, None)
      Field virtual_port_default


    gslb_svcgroup_count_max (optional, any, None)
      Field gslb_svcgroup_count_max


    cache_template_default (optional, any, None)
      Field cache_template_default


    http_template_min (optional, any, None)
      Field http_template_min


    fix_template_default (optional, any, None)
      Field fix_template_default


    gslb_policy_count_default (optional, any, None)
      Field gslb_policy_count_default


    server_ssl_template_default (optional, any, None)
      Field server_ssl_template_default


    gslb_svcgroup_count_default (optional, any, None)
      Field gslb_svcgroup_count_default


    gslb_geo_location_count_max (optional, any, None)
      Field gslb_geo_location_count_max


    gslb_service_count_max (optional, any, None)
      Field gslb_service_count_max


    virtual_server_min (optional, any, None)
      Field virtual_server_min


    gslb_service_count_min (optional, any, None)
      Field gslb_service_count_min


    gslb_service_count_default (optional, any, None)
      Field gslb_service_count_default


    gslb_zone_count_max (optional, any, None)
      Field gslb_zone_count_max


    gslb_service_port_count_default (optional, any, None)
      Field gslb_service_port_count_default


    proxy_template_default (optional, any, None)
      Field proxy_template_default


    gslb_geo_location_count_min (optional, any, None)
      Field gslb_geo_location_count_min


    http_template_max (optional, any, None)
      Field http_template_max


    pbslb_subnet_count_default (optional, any, None)
      Field pbslb_subnet_count_default


    gslb_device_count_default (optional, any, None)
      Field gslb_device_count_default


    stream_template_default (optional, any, None)
      Field stream_template_default


    gslb_device_count_min (optional, any, None)
      Field gslb_device_count_min


    pbslb_subnet_count_min (optional, any, None)
      Field pbslb_subnet_count_min


    gslb_site_count_default (optional, any, None)
      Field gslb_site_count_default


    virtual_server_max (optional, any, None)
      Field virtual_server_max


    client_ssl_template_max (optional, any, None)
      Field client_ssl_template_max


    nat_pool_addr_max (optional, any, None)
      Field nat_pool_addr_max


    nat_pool_addr_min (optional, any, None)
      Field nat_pool_addr_min


    conn_reuse_template_min (optional, any, None)
      Field conn_reuse_template_min


    service_group_max (optional, any, None)
      Field service_group_max


    client_ssl_template_min (optional, any, None)
      Field client_ssl_template_min


    gslb_service_ip_count_default (optional, any, None)
      Field gslb_service_ip_count_default


    conn_reuse_template_max (optional, any, None)
      Field conn_reuse_template_max


    gslb_zone_count_min (optional, any, None)
      Field gslb_zone_count_min


    gslb_ip_list_count_min (optional, any, None)
      Field gslb_ip_list_count_min


    gslb_geo_location_count_default (optional, any, None)
      Field gslb_geo_location_count_default


    health_monitor_count_max (optional, any, None)
      Field health_monitor_count_max


    virtual_server_default (optional, any, None)
      Field virtual_server_default


    pbslb_subnet_count_max (optional, any, None)
      Field pbslb_subnet_count_max


    conn_reuse_template_default (optional, any, None)
      Field conn_reuse_template_default


    gslb_device_count_max (optional, any, None)
      Field gslb_device_count_max


    gslb_service_port_count_min (optional, any, None)
      Field gslb_service_port_count_min


    client_ssl_template_default (optional, any, None)
      Field client_ssl_template_default


    gslb_policy_count_max (optional, any, None)
      Field gslb_policy_count_max


    stream_template_max (optional, any, None)
      Field stream_template_max


    real_server_max (optional, any, None)
      Field real_server_max


    gslb_policy_count_min (optional, any, None)
      Field gslb_policy_count_min


    fast_tcp_template_max (optional, any, None)
      Field fast_tcp_template_max


    fast_tcp_template_default (optional, any, None)
      Field fast_tcp_template_default


    service_group_min (optional, any, None)
      Field service_group_min


    persist_cookie_template_default (optional, any, None)
      Field persist_cookie_template_default


    gslb_zone_count_default (optional, any, None)
      Field gslb_zone_count_default


    fix_template_max (optional, any, None)
      Field fix_template_max


    slb_threshold_res_usage_max (optional, any, None)
      Field slb_threshold_res_usage_max


    proxy_template_max (optional, any, None)
      Field proxy_template_max


    http_template_default (optional, any, None)
      Field http_template_default


    gslb_template_count_default (optional, any, None)
      Field gslb_template_count_default


    proxy_template_min (optional, any, None)
      Field proxy_template_min


    nat_pool_addr_default (optional, any, None)
      Field nat_pool_addr_default


    gslb_svcgroup_count_min (optional, any, None)
      Field gslb_svcgroup_count_min


    gslb_ip_list_count_max (optional, any, None)
      Field gslb_ip_list_count_max


    health_monitor_count_default (optional, any, None)
      Field health_monitor_count_default


    gslb_service_port_count_max (optional, any, None)
      Field gslb_service_port_count_max


    persist_srcip_template_max (optional, any, None)
      Field persist_srcip_template_max


    persist_srcip_template_min (optional, any, None)
      Field persist_srcip_template_min


    stream_template_min (optional, any, None)
      Field stream_template_min


    slb_threshold_res_usage_min (optional, any, None)
      Field slb_threshold_res_usage_min


    service_group_default (optional, any, None)
      Field service_group_default


    cache_template_min (optional, any, None)
      Field cache_template_min


    fast_tcp_template_min (optional, any, None)
      Field fast_tcp_template_min


    real_server_min (optional, any, None)
      Field real_server_min


    real_port_default (optional, any, None)
      Field real_port_default


    gslb_service_ip_count_min (optional, any, None)
      Field gslb_service_ip_count_min


    gslb_template_count_max (optional, any, None)
      Field gslb_template_count_max


    gslb_ip_list_count_default (optional, any, None)
      Field gslb_ip_list_count_default


    gslb_site_count_max (optional, any, None)
      Field gslb_site_count_max


    server_ssl_template_max (optional, any, None)
      Field server_ssl_template_max


    fast_udp_template_max (optional, any, None)
      Field fast_udp_template_max


    fast_udp_template_default (optional, any, None)
      Field fast_udp_template_default


    real_port_min (optional, any, None)
      Field real_port_min


    persist_cookie_template_min (optional, any, None)
      Field persist_cookie_template_min


    virtual_port_max (optional, any, None)
      Field virtual_port_max


    slb_threshold_res_usage_default (optional, any, None)
      Field slb_threshold_res_usage_default


    cache_template_max (optional, any, None)
      Field cache_template_max


    virtual_port_min (optional, any, None)
      Field virtual_port_min


    persist_cookie_template_max (optional, any, None)
      Field persist_cookie_template_max


    real_server_default (optional, any, None)
      Field real_server_default



  cache_template_count (False, any, None)
    Total configurable HTTP Cache Templates in the System


  health_monitor_count (False, any, None)
    Total Health Monitors in the System


  server_ssl_template_count (False, any, None)
    Total configurable Server SSL Templates in the System


  ansible_username (True, any, None)
    Username for AXAPI authentication


  pbslb_subnet_count (False, any, None)
    Total PBSLB Subnets in the System


  persist_srcip_template_count (False, any, None)
    Total configurable Source IP Persistent Templates in the System


  real_port_count (False, any, None)
    Total Real Server Ports in the System


  virtual_server_count (False, any, None)
    Total Virtual Servers in the System


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  service_group_count (False, any, None)
    Total Service Groups in the System


  slb_threshold_res_usage_percent (False, any, None)
    Enter the threshold as a percentage (Threshold in percentage(default is 0%))


  ansible_port (True, any, None)
    Port for AXAPI authentication


  nat_pool_addr_count (False, any, None)
    Total configurable NAT Pool addresses in the System (deprecated)


  uuid (False, any, None)
    uuid of the object


  persist_cookie_template_count (False, any, None)
    Total configurable Persistent cookie Templates in the System


  ansible_password (True, any, None)
    Password for AXAPI authentication


  client_ssl_template_count (False, any, None)
    Total configurable Client SSL Templates in the System


  real_server_count (False, any, None)
    Total Real Servers in the System


  proxy_template_count (False, any, None)
    Total configurable Proxy Templates in the System


  virtual_port_count (False, any, None)
    Total Virtual Server Ports in the System


  state (True, any, None)
    State of the object to be created.


  fast_tcp_template_count (False, any, None)
    Total configurable Fast TCP Templates in the System


  fix_template_count (False, any, None)
    Total configurable FIX Templates in the System


  fast_udp_template_count (False, any, None)
    Total configurable Fast UDP Templates in the System


  http_template_count (False, any, None)
    Total configurable HTTP Templates in the System


  conn_reuse_template_count (False, any, None)
    Total configurable Connection reuse Templates in the System


  stream_template_count (False, any, None)
    Total configurable Streaming media in the System









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

