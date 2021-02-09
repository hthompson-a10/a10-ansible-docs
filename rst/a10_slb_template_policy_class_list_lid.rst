.. _a10_slb_template_policy_class_list_lid_module:


a10_slb_template_policy_class_list_lid -- Configures A10 slb.template.policy.class-list.lid
===========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Limit ID






Parameters
----------

  direct_fail (False, any, None)
    Only log unsuccessful connections


  ansible_username (True, any, None)
    Username for AXAPI authentication


  direct_pbslb_logging (False, any, None)
    Configure PBSLB logging


  policy_name (optional, any, None)
    Key to identify parent object


  conn_rate_limit (False, any, None)
    Specify connection rate limit


  direct_action (False, any, None)
    Set action when match the lid


  request_per (False, any, None)
    Per (Specify interval in number of 100ms)


  direct_action_value (False, any, None)
    'drop'= drop the packet; 'reset'= Send reset back;


  state (True, any, None)
    State of the object to be created.


  bw_per (False, any, None)
    Per (Specify interval in number of 100ms)


  direct_logging_drp_rst (False, any, None)
    Configure PBSLB logging


  lidnum (True, any, None)
    Specify a limit ID


  dns64 (False, any, None)
    Field dns64


    prefix (optional, any, None)
      IPv6 prefix


    disable (optional, any, None)
      Disable


    exclusive_answer (optional, any, None)
      Exclusive Answer in DNS Response



  direct_service_group (False, any, None)
    Specify a service group (Specify the service group name)


  request_rate_limit (False, any, None)
    Request rate limit (Specify request rate limit)


  bw_rate_limit (False, any, None)
    Specify bandwidth rate limit (Bandwidth rate limit in bytes)


  conn_limit (False, any, None)
    Connection limit


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  request_limit (False, any, None)
    Request limit (Specify request limit)


  log (False, any, None)
    Log a message


  action_value (False, any, None)
    'forward'= Forward the traffic even it exceeds limit; 'reset'= Reset the connection when it exceeds limit;


  ansible_port (True, any, None)
    Port for AXAPI authentication


  over_limit_action (False, any, None)
    Set action when exceeds limit


  ansible_password (True, any, None)
    Password for AXAPI authentication


  interval (False, any, None)
    Specify log interval in minutes, by default system will log every over limit instance


  uuid (False, any, None)
    uuid of the object


  response_code_rate_limit (False, any, None)
    Field response_code_rate_limit


    code_range_start (optional, any, None)
      server response code range start


    threshold (optional, any, None)
      the times of getting the response code


    code_range_end (optional, any, None)
      server response code range end


    period (optional, any, None)
      seconds



  lockout (False, any, None)
    Don't accept any new connection for certain time (Lockout duration in minutes)


  conn_per (False, any, None)
    Per (Specify interval in number of 100ms)


  direct_pbslb_interval (False, any, None)
    Specify logging interval in minutes(default is 3)


  user_tag (False, any, None)
    Customized tag


  direct_action_interval (False, any, None)
    Specify logging interval in minute (default is 3)









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

