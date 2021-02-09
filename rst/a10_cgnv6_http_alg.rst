.. _a10_cgnv6_http_alg_module:


a10_cgnv6_http_alg -- Configures A10 cgnv6.http-alg
===================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

HTTP-ALG Statistics






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'request-processed'= HTTP Request Processed; 'request-insert- msisdn-performed'= HTTP MSISDN Insertion Performed; 'request-insert-client-ip- performed'= HTTP Client IP Insertion Performed; 'request-insert-msisdn- unavailable'= Inserted MSISDN is 0000 (MSISDN Unavailable); 'queued-session- too-many'= Queued Session Exceed Drop; 'radius-query-succeed'= MSISDN Query Succeed; 'radius-query-failed'= MSISDN Query Failed; 'radius-requst-sent'= Query Request Sent; 'radius-requst-dropped'= Query Request Dropped; 'radius- response-received'= Query Response Received; 'radius-response-dropped'= Query Response Dropped; 'out-of-memory-dropped'= Out-of-Memory Dropped; 'queue-len- exceed-dropped'= Queue Length Exceed Dropped; 'out-of-order-dropped'= Packet Out-of-Order Dropped; 'buff-resent'= Packet Resent from Queue; 'buff-spilt- failed'= Buff Split Failed; 'header-insertion-failed'= Buff Insertion Failed; 'header-removal-failed'= Buff Removal Failed; 'no-queue'= No Queue;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    request_insert_msisdn_performed (optional, any, None)
      HTTP MSISDN Insertion Performed


    radius_response_dropped (optional, any, None)
      Query Response Dropped


    request_processed (optional, any, None)
      HTTP Request Processed


    radius_requst_sent (optional, any, None)
      Query Request Sent


    radius_requst_dropped (optional, any, None)
      Query Request Dropped


    queued_session_too_many (optional, any, None)
      Queued Session Exceed Drop


    radius_query_failed (optional, any, None)
      MSISDN Query Failed


    request_insert_msisdn_unavailable (optional, any, None)
      Inserted MSISDN is 0000 (MSISDN Unavailable)


    radius_query_succeed (optional, any, None)
      MSISDN Query Succeed


    request_insert_client_ip_performed (optional, any, None)
      HTTP Client IP Insertion Performed


    radius_response_received (optional, any, None)
      Query Response Received



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

