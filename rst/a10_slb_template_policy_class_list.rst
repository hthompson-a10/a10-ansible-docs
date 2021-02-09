.. _a10_slb_template_policy_class_list_module:


a10_slb_template_policy_class_list -- Configures A10 slb.template.policy.class-list
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure classification list






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  client_ip_l7_header (False, any, None)
    Use extract client IP address from L7 header


  name (True, any, None)
    Class list name or geo-location-class-list name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  policy_name (optional, any, None)
    Key to identify parent object


  client_ip_l3_dest (False, any, None)
    Use destination IP as client IP address


  lid_list (False, any, None)
    Field lid_list


    direct_service_group (optional, any, None)
      Specify a service group (Specify the service group name)


    direct_fail (optional, any, None)
      Only log unsuccessful connections


    dns64 (optional, any, None)
      Field dns64


    direct_pbslb_logging (optional, any, None)
      Configure PBSLB logging


    request_rate_limit (optional, any, None)
      Request rate limit (Specify request rate limit)


    bw_rate_limit (optional, any, None)
      Specify bandwidth rate limit (Bandwidth rate limit in bytes)


    conn_limit (optional, any, None)
      Connection limit


    lidnum (optional, any, None)
      Specify a limit ID


    log (optional, any, None)
      Log a message


    request_limit (optional, any, None)
      Request limit (Specify request limit)


    bw_per (optional, any, None)
      Per (Specify interval in number of 100ms)


    action_value (optional, any, None)
      'forward'= Forward the traffic even it exceeds limit; 'reset'= Reset the connection when it exceeds limit;


    uuid (optional, any, None)
      uuid of the object


    conn_rate_limit (optional, any, None)
      Specify connection rate limit


    direct_action (optional, any, None)
      Set action when match the lid


    over_limit_action (optional, any, None)
      Set action when exceeds limit


    request_per (optional, any, None)
      Per (Specify interval in number of 100ms)


    interval (optional, any, None)
      Specify log interval in minutes, by default system will log every over limit instance


    direct_action_value (optional, any, None)
      'drop'= drop the packet; 'reset'= Send reset back;


    response_code_rate_limit (optional, any, None)
      Field response_code_rate_limit


    lockout (optional, any, None)
      Don't accept any new connection for certain time (Lockout duration in minutes)


    direct_action_interval (optional, any, None)
      Specify logging interval in minute (default is 3)


    direct_pbslb_interval (optional, any, None)
      Specify logging interval in minutes(default is 3)


    user_tag (optional, any, None)
      Customized tag


    conn_per (optional, any, None)
      Per (Specify interval in number of 100ms)


    direct_logging_drp_rst (optional, any, None)
      Configure PBSLB logging



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  header_name (False, any, None)
    Specify L7 header name


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


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

