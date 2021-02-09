.. _a10_cgnv6_template_dns_module:


a10_cgnv6_template_dns -- Configures A10 cgnv6.template.dns
===========================================================

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


  dns64 (False, any, None)
    Field dns64


    trans_ptr (optional, any, None)
      Translate DNS PTR Records


    enable (optional, any, None)
      Enable DNS64 (Need to config this option before config any other dns64 options)


    answer_only_disable (optional, any, None)
      Disable Only translate the Answer Section


    deep_check_rr_disable (optional, any, None)
      Disable Check DNS Response Records


    ignore_rcode3_disable (optional, any, None)
      Disable Ignore DNS error Response with rcode 3


    ttl (optional, any, None)
      Specify Max TTL in DNS Response, unit= second


    change_query (optional, any, None)
      Always change incoming AAAA DNS Query to A


    passive_query_disable (optional, any, None)
      Disable Generate A query upon empty or error Response


    retry (optional, any, None)
      Retry count, default is 3 (Retry Number)


    single_response_disable (optional, any, None)
      Disable Single Response which is used to avoid ambiguity


    uuid (optional, any, None)
      uuid of the object


    max_qr_length (optional, any, None)
      Max Question Record Length, default is 128


    trans_ptr_query (optional, any, None)
      Translate DNS PTR Query


    cache (optional, any, None)
      Use a cached A-query response to provide AAAA query responses for the same hostname


    compress_disable (optional, any, None)
      Disable Always try DNS Compression


    auth_data (optional, any, None)
      Set AA flag in DNS Response


    parallel_query (optional, any, None)
      Forward AAAA Query & generate A Query in parallel


    timeout (optional, any, None)
      Timeout to send additional Queries, unit= second, default is 1


    drop_cname_disable (optional, any, None)
      Disable Drop DNS CNAME Response



  max_cache_size (False, any, None)
    Define maximum cache size (Maximum cache entry per VIP)


  disable_dns_template (False, any, None)
    Disable DNS template


  default_policy (False, any, None)
    'nocache'= Cache disable; 'cache'= Cache enable;


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    DNS Template Name


  user_tag (False, any, None)
    Customized tag


  drop (False, any, None)
    Drop the malformed query


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


  ansible_password (True, any, None)
    Password for AXAPI authentication









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

