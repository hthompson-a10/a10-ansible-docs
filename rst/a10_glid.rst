.. _a10_glid_module:


a10_glid -- Configures A10 glid
===============================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure global limit ID






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



  conn_rate_limit_interval (False, any, None)
    Field conn_rate_limit_interval


  request_rate_limit (False, any, None)
    Request rate limit


  conn_limit (False, any, None)
    Connection Limit for the GLID


  num (True, any, None)
    Global Limit ID


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  request_limit (False, any, None)
    Request limit


  uuid (False, any, None)
    uuid of the object


  action_value (False, any, None)
    'drop'= Silently Drop the new connection / new packet when it exceeds limit; 'dns-cache-disable'= Disable dns cache when it exceeds limit; 'dns-cache- enable'= Enable dns cache when it exceeds limit; 'forward'= Forward the traffic even it exceeds limit; 'reset'= Reset the connection when it exceeds limit;


  ansible_port (True, any, None)
    Port for AXAPI authentication


  conn_rate_limit (False, any, None)
    Connection rate Limit for the GLID


  log (False, any, None)
    Log a message


  over_limit_action (False, any, None)
    Action when exceeds limit


  ansible_password (True, any, None)
    Password for AXAPI authentication


  use_nat_pool (False, any, None)
    Use NAT pool specified to do reverse NAT for class list members bound to the lid


  log_interval (False, any, None)
    Log interval (minute, by default system will log every over limit instance)


  request_rate_limit_interval (False, any, None)
    Number of 100ms


  state (True, any, None)
    State of the object to be created.


  lockout (False, any, None)
    Don't accept any new connection for certain time (Lockout duration in minutes)


  dns (False, any, None)
    Field dns


    action (optional, any, None)
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

