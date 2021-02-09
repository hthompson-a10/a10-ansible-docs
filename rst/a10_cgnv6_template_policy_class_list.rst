.. _a10_cgnv6_template_policy_class_list_module:


a10_cgnv6_template_policy_class_list -- Configures A10 cgnv6.template.policy.class-list
=======================================================================================

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
    Class list name


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


    action_value (optional, any, None)
      'forward'= Forward the traffic even it exceeds limit; 'reset'= Reset the connection when it exceeds limit;


    lidnum (optional, any, None)
      Specify a limit ID


    conn_rate_limit (optional, any, None)
      Specify connection rate limit


    log (optional, any, None)
      Log a message


    over_limit_action (optional, any, None)
      Set action when exceeds limit


    request_per (optional, any, None)
      Per (Specify interval in number of 100ms)


    dns64 (optional, any, None)
      Field dns64


    interval (optional, any, None)
      Specify log interval in minutes, by default system will log every over limit instance


    request_rate_limit (optional, any, None)
      Request rate limit (Specify request rate limit)


    conn_limit (optional, any, None)
      Connection limit


    lockout (optional, any, None)
      Don't accept any new connection for certain time (Lockout duration in minutes)


    request_limit (optional, any, None)
      Request limit (Specify request limit)


    user_tag (optional, any, None)
      Customized tag


    conn_per (optional, any, None)
      Per (Specify interval in number of 100ms)


    uuid (optional, any, None)
      uuid of the object



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

