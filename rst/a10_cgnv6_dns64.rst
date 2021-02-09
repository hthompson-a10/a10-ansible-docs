.. _a10_cgnv6_dns64_module:


a10_cgnv6_dns64 -- Configures A10 cgnv6.dns64
=============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

DNS64 Statistics






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'query'= Query; 'query-bad-pkt'= Query Bad Packet; 'query-chg'= Query Changed; 'query-parallel'= Query Parallel; 'query-passive'= Query Passive; 'resp'= Response; 'resp-bad-pkt'= Response Bad Packet; 'resp-bad-qr'= Response Bad Query; 'resp-chg'= Response Changed; 'resp-err'= Response Error; 'resp-empty'= Response Empty; 'resp-local'= Response Local; 'adjust'= Translated; 'cache'= Cache; 'drop'= Dropped;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    resp_local (optional, any, None)
      Response Local


    cache (optional, any, None)
      Cache


    query_chg (optional, any, None)
      Query Changed


    resp (optional, any, None)
      Response


    query_passive (optional, any, None)
      Query Passive


    resp_err (optional, any, None)
      Response Error


    query_bad_pkt (optional, any, None)
      Query Bad Packet


    resp_bad_pkt (optional, any, None)
      Response Bad Packet


    adjust (optional, any, None)
      Translated


    resp_empty (optional, any, None)
      Response Empty


    query (optional, any, None)
      Query


    drop (optional, any, None)
      Dropped


    resp_chg (optional, any, None)
      Response Changed


    resp_bad_qr (optional, any, None)
      Response Bad Query


    query_parallel (optional, any, None)
      Query Parallel



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

