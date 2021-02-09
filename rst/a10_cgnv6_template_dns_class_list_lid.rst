.. _a10_cgnv6_template_dns_class_list_lid_module:


a10_cgnv6_template_dns_class_list_lid -- Configures A10 cgnv6.template.dns.class-list.lid
=========================================================================================

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


  lidnum (True, any, None)
    Specify a limit ID


  ansible_password (True, any, None)
    Password for AXAPI authentication


  log_interval (False, any, None)
    Log interval (minute, by default system will log every over limit instance)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  action_value (False, any, None)
    'dns-cache-disable'= Disable DNS cache when it exceeds limit; 'dns-cache- enable'= Enable DNS cache when it exceeds limit; 'forward'= Forward the traffic even it exceeds limit;


  ansible_port (True, any, None)
    Port for AXAPI authentication


  conn_rate_limit (False, any, None)
    Connection rate limit


  log (False, any, None)
    Log a message


  over_limit_action (False, any, None)
    Action when exceeds limit


  dns_name (optional, any, None)
    Key to identify parent object


  per (False, any, None)
    Per (Number of 100ms)


  state (True, any, None)
    State of the object to be created.


  lockout (False, any, None)
    Don't accept any new connection for certain time (Lockout duration in minutes)


  dns (False, any, None)
    Field dns


    cache_action (optional, any, None)
      'cache-disable'= Disable dns cache; 'cache-enable'= Enable dns cache;


    weight (optional, any, None)
      Weight for cache entry


    ttl (optional, any, None)
      TTL for cache entry (TTL in seconds)



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

