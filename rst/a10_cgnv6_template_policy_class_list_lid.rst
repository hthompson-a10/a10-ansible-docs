.. _a10_cgnv6_template_policy_class_list_lid_module:


a10_cgnv6_template_policy_class_list_lid -- Configures A10 cgnv6.template.policy.class-list.lid
===============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Limit ID






Parameters
----------

  ansible_username (True, any, None)
    Username for AXAPI authentication


  dns64 (False, any, None)
    Field dns64


    prefix (optional, any, None)
      IPv6 prefix


    disable (optional, any, None)
      Disable


    exclusive_answer (optional, any, None)
      Exclusive Answer in DNS Response



  lidnum (True, any, None)
    Specify a limit ID


  request_rate_limit (False, any, None)
    Request rate limit (Specify request rate limit)


  policy_name (optional, any, None)
    Key to identify parent object


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


  uuid (False, any, None)
    uuid of the object


  action_value (False, any, None)
    'forward'= Forward the traffic even it exceeds limit; 'reset'= Reset the connection when it exceeds limit;


  ansible_port (True, any, None)
    Port for AXAPI authentication


  conn_rate_limit (False, any, None)
    Specify connection rate limit


  log (False, any, None)
    Log a message


  over_limit_action (False, any, None)
    Set action when exceeds limit


  request_per (False, any, None)
    Per (Specify interval in number of 100ms)


  ansible_password (True, any, None)
    Password for AXAPI authentication


  interval (False, any, None)
    Specify log interval in minutes, by default system will log every over limit instance


  state (True, any, None)
    State of the object to be created.


  lockout (False, any, None)
    Don't accept any new connection for certain time (Lockout duration in minutes)


  user_tag (False, any, None)
    Customized tag


  conn_per (False, any, None)
    Per (Specify interval in number of 100ms)









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

