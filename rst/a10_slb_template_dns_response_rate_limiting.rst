.. _a10_slb_template_dns_response_rate_limiting_module:


a10_slb_template_dns_response_rate_limiting -- Configures A10 slb.template.dns.response-rate-limiting
=====================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

DNS Response Rate Limiting






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  enable_log (False, any, None)
    Enable logging


  slip_rate (False, any, None)
    Every n'th response that would be rate-limited will be let through instead


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  window (False, any, None)
    Rate-Limiting Interval in Seconds (default is one)


  filter_response_rate (False, any, None)
    Maximum allowed request rate for the filter. This should match average traffic. (default 20 per two seconds)


  dns_name (optional, any, None)
    Key to identify parent object


  action (False, any, None)
    'log-only'= Only log rate-limiting, do not actually rate limit. Requires enable-log configuration; 'rate-limit'= Rate-Limit based on configuration (Default); 'whitelist'= Whitelist, disable rate-limiting;


  response_rate (False, any, None)
    Responses exceeding this rate within the window will be dropped (default 5 per second)


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication









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

