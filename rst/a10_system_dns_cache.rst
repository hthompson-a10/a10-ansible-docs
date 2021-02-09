.. _a10_system_dns_cache_module:


a10_system_dns_cache -- Configures A10 system.dns-cache
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

DNS Cache Statistics






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'total_q'= Total query; 'total_r'= Total server response; 'hit'= Total cache hit; 'bad_q'= Query not passed; 'encode_q'= Query encoded; 'multiple_q'= Query with multiple questions; 'oversize_q'= Query exceed cache size; 'bad_r'= Response not passed; 'oversize_r'= Response exceed cache size; 'encode_r'= Response encoded; 'multiple_r'= Response with multiple questions; 'answer_r'= Response with multiple answers; 'ttl_r'= Response with short TTL; 'ageout'= Total aged out; 'bad_answer'= Bad Answer; 'ageout_weight'= Total aged for lower weight; 'total_log'= Total stats log sent; 'total_alloc'= Total allocated; 'total_freed'= Total freed; 'current_allocate'= Current allocate; 'current_data_allocate'= Current data allocate;



  oper (False, any, None)
    Field oper


    cache_entry (optional, any, None)
      Field cache_entry


    entry (optional, any, None)
      Field entry


    total (optional, any, None)
      Field total


    cache_client (optional, any, None)
      Field cache_client


    client (optional, any, None)
      Field client



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    hit (optional, any, None)
      Total cache hit


    multiple_r (optional, any, None)
      Response with multiple questions


    multiple_q (optional, any, None)
      Query with multiple questions


    current_allocate (optional, any, None)
      Current allocate


    bad_q (optional, any, None)
      Query not passed


    bad_r (optional, any, None)
      Response not passed


    answer_r (optional, any, None)
      Response with multiple answers


    encode_q (optional, any, None)
      Query encoded


    oversize_r (optional, any, None)
      Response exceed cache size


    current_data_allocate (optional, any, None)
      Current data allocate


    ttl_r (optional, any, None)
      Response with short TTL


    oversize_q (optional, any, None)
      Query exceed cache size


    ageout_weight (optional, any, None)
      Total aged for lower weight


    bad_answer (optional, any, None)
      Bad Answer


    ageout (optional, any, None)
      Total aged out


    total_freed (optional, any, None)
      Total freed


    total_alloc (optional, any, None)
      Total allocated


    total_q (optional, any, None)
      Total query


    total_r (optional, any, None)
      Total server response


    total_log (optional, any, None)
      Total stats log sent


    encode_r (optional, any, None)
      Response encoded



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


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

