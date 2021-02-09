.. _a10_system_resource_accounting_template_module:


a10_system_resource_accounting_template -- Configures A10 system.resource.accounting.template
=============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create resource accounting template






Parameters
----------

  system_resources (False, any, None)
    Field system_resources


    natcps_limit_cfg (optional, any, None)
      Field natcps_limit_cfg


    l7cps_limit_cfg (optional, any, None)
      Field l7cps_limit_cfg


    ssl_throughput_limit_cfg (optional, any, None)
      Field ssl_throughput_limit_cfg


    concurrent_session_limit_cfg (optional, any, None)
      Field concurrent_session_limit_cfg


    l4_session_limit_cfg (optional, any, None)
      Field l4_session_limit_cfg


    fwcps_limit_cfg (optional, any, None)
      Field fwcps_limit_cfg


    sslcps_limit_cfg (optional, any, None)
      Field sslcps_limit_cfg


    l4cps_limit_cfg (optional, any, None)
      Field l4cps_limit_cfg


    threshold (optional, any, None)
      Enter the threshold as a percentage (Threshold in percentage(default is 100%))


    bw_limit_cfg (optional, any, None)
      Field bw_limit_cfg


    uuid (optional, any, None)
      uuid of the object



  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    Enter template name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  network_resources (False, any, None)
    Field network_resources


    static_mac_cfg (optional, any, None)
      Field static_mac_cfg


    uuid (optional, any, None)
      uuid of the object


    object_group_cfg (optional, any, None)
      Field object_group_cfg


    static_neighbor_cfg (optional, any, None)
      Field static_neighbor_cfg


    static_ipv4_route_cfg (optional, any, None)
      Field static_ipv4_route_cfg


    static_arp_cfg (optional, any, None)
      Field static_arp_cfg


    ipv4_acl_line_cfg (optional, any, None)
      Field ipv4_acl_line_cfg


    ipv6_acl_line_cfg (optional, any, None)
      Field ipv6_acl_line_cfg


    object_group_clause_cfg (optional, any, None)
      Field object_group_clause_cfg


    threshold (optional, any, None)
      Enter the threshold as a percentage (Threshold in percentage(default is 100%))


    static_ipv6_route_cfg (optional, any, None)
      Field static_ipv6_route_cfg



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  app_resources (False, any, None)
    Field app_resources


    gslb_device_cfg (optional, any, None)
      Field gslb_device_cfg


    service_group_cfg (optional, any, None)
      Field service_group_cfg


    gslb_service_ip_cfg (optional, any, None)
      Field gslb_service_ip_cfg


    gslb_svc_group_cfg (optional, any, None)
      Field gslb_svc_group_cfg


    gslb_ip_list_cfg (optional, any, None)
      Field gslb_ip_list_cfg


    gslb_policy_cfg (optional, any, None)
      Field gslb_policy_cfg


    gslb_template_cfg (optional, any, None)
      Field gslb_template_cfg


    threshold (optional, any, None)
      Enter the threshold as a percentage (Threshold in percentage(default is 100%))


    gslb_zone_cfg (optional, any, None)
      Field gslb_zone_cfg


    uuid (optional, any, None)
      uuid of the object


    gslb_geo_location_cfg (optional, any, None)
      Field gslb_geo_location_cfg


    gslb_service_cfg (optional, any, None)
      Field gslb_service_cfg


    gslb_site_cfg (optional, any, None)
      Field gslb_site_cfg


    real_port_cfg (optional, any, None)
      Field real_port_cfg


    virtual_server_cfg (optional, any, None)
      Field virtual_server_cfg


    health_monitor_cfg (optional, any, None)
      Field health_monitor_cfg


    gslb_service_port_cfg (optional, any, None)
      Field gslb_service_port_cfg


    real_server_cfg (optional, any, None)
      Field real_server_cfg



  uuid (False, any, None)
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

