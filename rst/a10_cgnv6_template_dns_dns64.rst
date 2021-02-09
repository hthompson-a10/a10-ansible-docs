.. _a10_cgnv6_template_dns_dns64_module:


a10_cgnv6_template_dns_dns64 -- Configures A10 cgnv6.template.dns.dns64
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Enable DNS64






Parameters
----------

  trans_ptr (False, any, None)
    Translate DNS PTR Records


  enable (False, any, None)
    Enable DNS64 (Need to config this option before config any other dns64 options)


  answer_only_disable (False, any, None)
    Disable Only translate the Answer Section


  deep_check_rr_disable (False, any, None)
    Disable Check DNS Response Records


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ignore_rcode3_disable (False, any, None)
    Disable Ignore DNS error Response with rcode 3


  change_query (False, any, None)
    Always change incoming AAAA DNS Query to A


  timeout (False, any, None)
    Timeout to send additional Queries, unit= second, default is 1


  ttl (False, any, None)
    Specify Max TTL in DNS Response, unit= second


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ansible_port (True, any, None)
    Port for AXAPI authentication


  retry (False, any, None)
    Retry count, default is 3 (Retry Number)


  single_response_disable (False, any, None)
    Disable Single Response which is used to avoid ambiguity


  uuid (False, any, None)
    uuid of the object


  max_qr_length (False, any, None)
    Max Question Record Length, default is 128


  trans_ptr_query (False, any, None)
    Translate DNS PTR Query


  dns_name (optional, any, None)
    Key to identify parent object


  cache (False, any, None)
    Use a cached A-query response to provide AAAA query responses for the same hostname


  compress_disable (False, any, None)
    Disable Always try DNS Compression


  auth_data (False, any, None)
    Set AA flag in DNS Response


  parallel_query (False, any, None)
    Forward AAAA Query & generate A Query in parallel


  state (True, any, None)
    State of the object to be created.


  passive_query_disable (False, any, None)
    Disable Generate A query upon empty or error Response


  ansible_password (True, any, None)
    Password for AXAPI authentication


  drop_cname_disable (False, any, None)
    Disable Drop DNS CNAME Response









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

