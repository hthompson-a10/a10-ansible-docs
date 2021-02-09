.. _a10_system_resource_accounting_template_app_resources_module:


a10_system_resource_accounting_template_app_resources -- Configures A10 system.resource.accounting.template.app-resources
=========================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Enter the application resource limits






Parameters
----------

  gslb_device_cfg (False, any, None)
    Field gslb_device_cfg


    gslb_device_max (optional, any, None)
      Enter the number of gslb-device allowed (gslb-device count (default is max- value))


    gslb_device_min_guarantee (optional, any, None)
      Minimum guaranteed value ( Minimum guaranteed value)



  service_group_cfg (False, any, None)
    Field service_group_cfg


    service_group_max (optional, any, None)
      Enter the number of service groups allowed (service-group count (default is max-value))


    service_group_min_guarantee (optional, any, None)
      Minimum guaranteed value ( Minimum guaranteed value)



  ansible_username (True, any, None)
    Username for AXAPI authentication


  gslb_service_ip_cfg (False, any, None)
    Field gslb_service_ip_cfg


    gslb_service_ip_max (optional, any, None)
      Enter the number of gslb-service-ip allowed (gslb-service-ip count (default is max-value))


    gslb_service_ip_min_guarantee (optional, any, None)
      Minimum guaranteed value ( Minimum guaranteed value)



  template_name (optional, any, None)
    Key to identify parent object


  real_server_cfg (False, any, None)
    Field real_server_cfg


    real_server_min_guarantee (optional, any, None)
      Minimum guaranteed value ( Minimum guaranteed value)


    real_server_max (optional, any, None)
      Enter the number of real-servers allowed (real-server count (default is max- value))



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  health_monitor_cfg (False, any, None)
    Field health_monitor_cfg


    health_monitor_max (optional, any, None)
      Enter the number of health monitors allowed (health-monitor count (default is max-value))


    health_monitor_min_guarantee (optional, any, None)
      Minimum guaranteed value ( Minimum guaranteed value)



  gslb_policy_cfg (False, any, None)
    Field gslb_policy_cfg


    gslb_policy_max (optional, any, None)
      Enter the number of gslb-policy allowed (gslb-policy count (default is max- value))


    gslb_policy_min_guarantee (optional, any, None)
      Minimum guaranteed value ( Minimum guaranteed value)



  gslb_template_cfg (False, any, None)
    Field gslb_template_cfg


    gslb_template_min_guarantee (optional, any, None)
      Minimum guaranteed value ( Minimum guaranteed value)


    gslb_template_max (optional, any, None)
      Enter the number of gslb-template allowed (gslb-template count (default is max- value))



  threshold (False, any, None)
    Enter the threshold as a percentage (Threshold in percentage(default is 100%))


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  gslb_zone_cfg (False, any, None)
    Field gslb_zone_cfg


    gslb_zone_min_guarantee (optional, any, None)
      Minimum guaranteed value ( Minimum guaranteed value)


    gslb_zone_max (optional, any, None)
      Enter the number of gslb-zone allowed (gslb-zone count (default is max-value))



  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  gslb_geo_location_cfg (False, any, None)
    Field gslb_geo_location_cfg


    gslb_geo_location_min_guarantee (optional, any, None)
      Minimum guaranteed value ( Minimum guaranteed value)


    gslb_geo_location_max (optional, any, None)
      Enter the number of gslb-geo-location allowed (gslb-geo-location count (default is max-value))



  gslb_service_cfg (False, any, None)
    Field gslb_service_cfg


    gslb_service_min_guarantee (optional, any, None)
      Minimum guaranteed value ( Minimum guaranteed value)


    gslb_service_max (optional, any, None)
      Enter the number of gslb-service allowed (gslb-service count (default is max- value)



  gslb_site_cfg (False, any, None)
    Field gslb_site_cfg


    gslb_site_max (optional, any, None)
      Enter the number of gslb-site allowed (gslb-site count (default is max-value))


    gslb_site_min_guarantee (optional, any, None)
      Minimum guaranteed value ( Minimum guaranteed value)



  gslb_service_port_cfg (False, any, None)
    Field gslb_service_port_cfg


    gslb_service_port_max (optional, any, None)
      Enter the number of gslb-service-port allowed ( gslb-service-port count (default is max-value))


    gslb_service_port_min_guarantee (optional, any, None)
      Minimum guaranteed value ( Minimum guaranteed value)



  real_port_cfg (False, any, None)
    Field real_port_cfg


    real_port_max (optional, any, None)
      Enter the number of real-ports allowed (real-port count (default is max-value))


    real_port_min_guarantee (optional, any, None)
      Minimum guaranteed value ( Minimum guaranteed value)



  state (True, any, None)
    State of the object to be created.


  virtual_server_cfg (False, any, None)
    Field virtual_server_cfg


    virtual_server_max (optional, any, None)
      Enter the number of virtual-servers allowed (virtual-server count (default is max-value))


    virtual_server_min_guarantee (optional, any, None)
      Minimum guaranteed value ( Minimum guaranteed value)



  gslb_ip_list_cfg (False, any, None)
    Field gslb_ip_list_cfg


    gslb_ip_list_max (optional, any, None)
      Enter the number of gslb-ip-list allowed (gslb-ip-list count (default is max- value))


    gslb_ip_list_min_guarantee (optional, any, None)
      Minimum guaranteed value ( Minimum guaranteed value)



  ansible_password (True, any, None)
    Password for AXAPI authentication


  gslb_svc_group_cfg (False, any, None)
    Field gslb_svc_group_cfg


    gslb_svc_group_min_guarantee (optional, any, None)
      Minimum guaranteed value ( Minimum guaranteed value)


    gslb_svc_group_max (optional, any, None)
      Enter the number of gslb-svc-group allowed (gslb-svc-group count (default is max-value))










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

