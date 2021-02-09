.. _a10_gslb_site_slb_dev_module:


a10_gslb_site_slb_dev -- Configures A10 gslb.site.slb-dev
=========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Specify a SLB device for the GSLB site






Parameters
----------

  oper (False, any, None)
    Field oper


    dev_gw_state (optional, any, None)
      Field dev_gw_state


    dev_name (optional, any, None)
      Field dev_name


    dev_ip_cnt (optional, any, None)
      Field dev_ip_cnt


    client_ldns_list (optional, any, None)
      Field client_ldns_list


    device_name (optional, any, None)
      Specify SLB device name


    dev_attr (optional, any, None)
      Field dev_attr


    dev_ip (optional, any, None)
      Field dev_ip


    dev_state (optional, any, None)
      Field dev_state


    vip_server (optional, any, None)
      Field vip_server


    dev_session_num (optional, any, None)
      Field dev_session_num


    dev_admin_preference (optional, any, None)
      Field dev_admin_preference


    dev_session_util (optional, any, None)
      Field dev_session_util



  client_ip (False, any, None)
    Specify client IP address


  site_name (optional, any, None)
    Key to identify parent object


  proto_aging_time (False, any, None)
    Specify GSLB Protocol aging time, default is 60


  max_client (False, any, None)
    Specify maximum number of clients, default is 32768


  msg_format_acos_2x (False, any, None)
    Run GSLB Protocol in compatible mode with a ACOS 2.x GSLB peer


  health_check_action (False, any, None)
    'health-check'= Enable health Check; 'health-check-disable'= Disable health check;


  admin_preference (False, any, None)
    Specify administrative preference (Specify admin-preference value,default is 100)


  ansible_port (True, any, None)
    Port for AXAPI authentication


  auto_detect (False, any, None)
    'ip'= Service IP only; 'port'= Service Port only; 'ip-and-port'= Both service IP and service port; 'disabled'= disable auto-detect;


  proto_compatible (False, any, None)
    Run GSLB Protocol in compatible mode


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  ip_address (False, any, None)
    IP address


  ansible_host (True, any, None)
    Host for AXAPI authentication


  gateway_ip_addr (False, any, None)
    IP address


  uuid (False, any, None)
    uuid of the object


  ansible_password (True, any, None)
    Password for AXAPI authentication


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_username (True, any, None)
    Username for AXAPI authentication


  auto_map (False, any, None)
    Enable DNS Auto Mapping


  device_name (True, any, None)
    Specify SLB device name


  rdt_value (False, any, None)
    Specify Round-delay-time


  state (True, any, None)
    State of the object to be created.


  proto_aging_fast (False, any, None)
    Fast GSLB Protocol aging


  vip_server (False, any, None)
    Field vip_server


    vip_server_name_list (optional, any, None)
      Field vip_server_name_list


    vip_server_v6_list (optional, any, None)
      Field vip_server_v6_list


    vip_server_v4_list (optional, any, None)
      Field vip_server_v4_list



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

