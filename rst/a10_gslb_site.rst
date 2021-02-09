.. _a10_gslb_site_module:


a10_gslb_site -- Configures A10 gslb.site
=========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Specify a GSLB site






Parameters
----------

  oper (False, any, None)
    Field oper


    state (optional, any, None)
      Field state


    gslb_site (optional, any, None)
      Field gslb_site


    site_name (optional, any, None)
      Specify GSLB site name


    ip_server_list (optional, any, None)
      Field ip_server_list


    slb_dev_list (optional, any, None)
      Field slb_dev_list


    type_last (optional, any, None)
      Field type_last


    client_ldns_list (optional, any, None)
      Field client_ldns_list



  site_name (True, any, None)
    Specify GSLB site name


  weight (False, any, None)
    Specify a weight for the GSLB site (Weight, default is 1)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  controller (False, any, None)
    Specify the local controller for the GSLB site (Specify the hostname of the local controller)


  disable (False, any, None)
    Disable all servers in the GSLB site


  slb_dev_list (False, any, None)
    Field slb_dev_list


    client_ip (optional, any, None)
      Specify client IP address


    proto_aging_time (optional, any, None)
      Specify GSLB Protocol aging time, default is 60


    max_client (optional, any, None)
      Specify maximum number of clients, default is 32768


    msg_format_acos_2x (optional, any, None)
      Run GSLB Protocol in compatible mode with a ACOS 2.x GSLB peer


    admin_preference (optional, any, None)
      Specify administrative preference (Specify admin-preference value,default is 100)


    auto_detect (optional, any, None)
      'ip'= Service IP only; 'port'= Service Port only; 'ip-and-port'= Both service IP and service port; 'disabled'= disable auto-detect;


    gateway_ip_addr (optional, any, None)
      IP address


    ip_address (optional, any, None)
      IP address


    uuid (optional, any, None)
      uuid of the object


    health_check_action (optional, any, None)
      'health-check'= Enable health Check; 'health-check-disable'= Disable health check;


    device_name (optional, any, None)
      Specify SLB device name


    rdt_value (optional, any, None)
      Specify Round-delay-time


    auto_map (optional, any, None)
      Enable DNS Auto Mapping


    proto_aging_fast (optional, any, None)
      Fast GSLB Protocol aging


    proto_compatible (optional, any, None)
      Run GSLB Protocol in compatible mode


    vip_server (optional, any, None)
      Field vip_server


    user_tag (optional, any, None)
      Customized tag



  threshold (False, any, None)
    Specify the threshold for limit


  bw_cost (False, any, None)
    Specify cost of band-width


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'hits'= Number of times the site was selected;



  easy_rdt (False, any, None)
    Field easy_rdt


    uuid (optional, any, None)
      uuid of the object


    ignore_count (optional, any, None)
      Ignore count if RDT is out of range, default is 5


    mask (optional, any, None)
      Client IP subnet mask, default is 32


    overlap (optional, any, None)
      Enable overlap for geo-location to do longest match


    bind_geoloc (optional, any, None)
      Bind RDT to geo-location


    smooth_factor (optional, any, None)
      Factor of Smooth RDT, default is 10


    limit (optional, any, None)
      Limit of valid RDT, default is 16383 (Limit, unit= millisecond)


    aging_time (optional, any, None)
      Aging Time, Unit= min, default is 10


    range_factor (optional, any, None)
      Factor of RDT Range, default is 25 (Range Factor of Smooth RDT)



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    ip_server_list (optional, any, None)
      Field ip_server_list


    site_name (optional, any, None)
      Specify GSLB site name


    hits (optional, any, None)
      Number of times the site was selected


    slb_dev_list (optional, any, None)
      Field slb_dev_list



  uuid (False, any, None)
    uuid of the object


  ansible_password (True, any, None)
    Password for AXAPI authentication


  active_rdt (False, any, None)
    Field active_rdt


    uuid (optional, any, None)
      uuid of the object


    ignore_count (optional, any, None)
      Ignore count if RDT is out of range, default is 5


    mask (optional, any, None)
      Client IP subnet mask, default is 32


    overlap (optional, any, None)
      Enable overlap for geo-location to do longest match


    bind_geoloc (optional, any, None)
      Bind RDT to geo-location


    smooth_factor (optional, any, None)
      Factor of Smooth RDT, default is 10


    limit (optional, any, None)
      Limit of valid RDT, default is 16383 (Limit, unit= millisecond)


    aging_time (optional, any, None)
      Aging Time, Unit= min, default is 10


    range_factor (optional, any, None)
      Factor of RDT Range, default is 25 (Range Factor of Smooth RDT)



  auto_map (False, any, None)
    Enable DNS Auto Mapping


  multiple_geo_locations (False, any, None)
    Field multiple_geo_locations


    geo_location (optional, any, None)
      Specify the geographic location of the GSLB site (Specify geo-location for this site)



  state (True, any, None)
    State of the object to be created.


  limit (False, any, None)
    Specify the limit for bandwidth, default is unlimited


  template (False, any, None)
    Specify template to collect site information (Specify GSLB SNMP template name)


  ip_server_list (False, any, None)
    Field ip_server_list


    sampling_enable (optional, any, None)
      Field sampling_enable


    ip_server_name (optional, any, None)
      Specify the real server name


    uuid (optional, any, None)
      uuid of the object



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

