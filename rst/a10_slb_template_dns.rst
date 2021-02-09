.. _a10_slb_template_dns_module:


a10_slb_template_dns -- Configures A10 slb.template.dns
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

DNS template






Parameters
----------

  ansible_username (True, any, None)
    Username for AXAPI authentication


  max_cache_size (False, any, None)
    Define maximum cache size (Maximum cache entry per VIP)


  disable_dns_template (False, any, None)
    Disable DNS template


  max_cache_entry_size (False, any, None)
    Define maximum cache entry size (Maximum cache entry size per VIP)


  default_policy (False, any, None)
    'nocache'= Cache disable; 'cache'= Cache enable;


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  enable_cache_sharing (False, any, None)
    Enable DNS cache sharing


  ansible_port (True, any, None)
    Port for AXAPI authentication


  dnssec_service_group (False, any, None)
    Use different service group if DNSSEC DO bit set (Service Group Name)


  uuid (False, any, None)
    uuid of the object


  ansible_password (True, any, None)
    Password for AXAPI authentication


  max_query_length (False, any, None)
    Define Maximum DNS Query Length, default is unlimited (Specify Maximum Length)


  drop (False, any, None)
    Drop the malformed query


  response_rate_limiting (False, any, None)
    Field response_rate_limiting


    slip_rate (optional, any, None)
      Every n'th response that would be rate-limited will be let through instead


    uuid (optional, any, None)
      uuid of the object


    action (optional, any, None)
      'log-only'= Only log rate-limiting, do not actually rate limit. Requires enable-log configuration; 'rate-limit'= Rate-Limit based on configuration (Default); 'whitelist'= Whitelist, disable rate-limiting;


    response_rate (optional, any, None)
      Responses exceeding this rate within the window will be dropped (default 5 per second)


    enable_log (optional, any, None)
      Enable logging


    window (optional, any, None)
      Rate-Limiting Interval in Seconds (default is one)


    filter_response_rate (optional, any, None)
      Maximum allowed request rate for the filter. This should match average traffic. (default 20 per two seconds)



  name (True, any, None)
    DNS Template Name


  query_id_switch (False, any, None)
    Use DNS query ID to create sesion


  class_list (False, any, None)
    Field class_list


    lid_list (optional, any, None)
      Field lid_list


    name (optional, any, None)
      Specify a class list name


    uuid (optional, any, None)
      uuid of the object



  state (True, any, None)
    State of the object to be created.


  period (False, any, None)
    Period in minutes


  forward (False, any, None)
    Forward to service group (Service group name)


  redirect_to_tcp_port (False, any, None)
    Direct the client to retry with TCP for DNS UDP request


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

