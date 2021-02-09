.. _a10_gslb_dns_module:


a10_gslb_dns -- Configures A10 gslb.dns
=======================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

DNS Global Options






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'total-query'= Total number of DNS queries received; 'total- response'= Total number of DNS replies sent to clients; 'bad-packet-query'= Number of queries with incorrect data length; 'bad-packet-response'= Number of replies with incorrect data length; 'bad-header-query'= Number of queries with incorrect header; 'bad-header-response'= Number of replies with incorrect header; 'bad-format-query'= Number of queries with incorrect format; 'bad- format-response'= Number of replies with incorrect format; 'bad-service-query'= Number of queries with unknown service; 'bad-service-response'= Number of replies with unknown service; 'bad-class-query'= Number of queries with incorrect class; 'bad-class-response'= Number of replies with incorrect class; 'bad-type-query'= Number of queries with incorrect type; 'bad-type-response'= Number of replies with incorrect type; 'no_answer'= Number of replies with unknown server IP; 'metric_health_check'= Metric Health Check Hit; 'metric_weighted_ip'= Metric Weighted IP Hit; 'metric_weighted_site'= Metric Weighted Site Hit; 'metric_capacity'= Metric Capacity Hit; 'metric_active_server'= Metric Active Server Hit; 'metric_easy_rdt'= Metric Easy RDT Hit; 'metric_active_rdt'= Metric Active RDT Hit; 'metric_geographic'= Metric Geographic Hit; 'metric_connection_load'= Metric Connection Load Hit; 'metric_number_of_sessions'= Metric Number of Sessions Hit; 'metric_active_weight'= Metric Active Weight Hit; 'metric_admin_preference'= Metric Admin Preference Hit; 'metric_bandwidth_quality'= Metric Bandwidth Quality Hit; 'metric_bandwidth_cost'= Metric Bandwidth Cost Hit; 'metric_user'= Metric User Hit; 'metric_least_reponse'= Metric Least Reponse Hit; 'metric_admin_ip'= Metric Admin IP Hit; 'metric_round_robin'= Metric Round Robin Hit;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  logging (False, any, None)
    'none'= No logging (default); 'query'= DNS Query; 'response'= DNS Response; 'both'= Both DNS Query and Response;


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  template (False, any, None)
    Logging template (Logging Template Name)


  action (False, any, None)
    'none'= No action (default); 'drop'= Drop query; 'reject'= Send refuse response; 'ignore'= Send empty response;


  stats (False, any, None)
    Field stats


    metric_capacity (optional, any, None)
      Metric Capacity Hit


    metric_admin_ip (optional, any, None)
      Metric Admin IP Hit


    bad_packet_query (optional, any, None)
      Number of queries with incorrect data length


    no_answer (optional, any, None)
      Number of replies with unknown server IP


    metric_active_server (optional, any, None)
      Metric Active Server Hit


    total_query (optional, any, None)
      Total number of DNS queries received


    bad_format_response (optional, any, None)
      Number of replies with incorrect format


    bad_format_query (optional, any, None)
      Number of queries with incorrect format


    bad_packet_response (optional, any, None)
      Number of replies with incorrect data length


    metric_active_rdt (optional, any, None)
      Metric Active RDT Hit


    total_response (optional, any, None)
      Total number of DNS replies sent to clients


    bad_service_query (optional, any, None)
      Number of queries with unknown service


    metric_connection_load (optional, any, None)
      Metric Connection Load Hit


    bad_type_response (optional, any, None)
      Number of replies with incorrect type


    metric_bandwidth_cost (optional, any, None)
      Metric Bandwidth Cost Hit


    metric_bandwidth_quality (optional, any, None)
      Metric Bandwidth Quality Hit


    metric_user (optional, any, None)
      Metric User Hit


    metric_least_reponse (optional, any, None)
      Metric Least Reponse Hit


    metric_weighted_site (optional, any, None)
      Metric Weighted Site Hit


    metric_health_check (optional, any, None)
      Metric Health Check Hit


    bad_header_response (optional, any, None)
      Number of replies with incorrect header


    metric_round_robin (optional, any, None)
      Metric Round Robin Hit


    metric_easy_rdt (optional, any, None)
      Metric Easy RDT Hit


    metric_geographic (optional, any, None)
      Metric Geographic Hit


    metric_weighted_ip (optional, any, None)
      Metric Weighted IP Hit


    bad_class_response (optional, any, None)
      Number of replies with incorrect class


    bad_service_response (optional, any, None)
      Number of replies with unknown service


    bad_class_query (optional, any, None)
      Number of queries with incorrect class


    metric_active_weight (optional, any, None)
      Metric Active Weight Hit


    metric_admin_preference (optional, any, None)
      Metric Admin Preference Hit


    bad_header_query (optional, any, None)
      Number of queries with incorrect header


    metric_number_of_sessions (optional, any, None)
      Metric Number of Sessions Hit


    bad_type_query (optional, any, None)
      Number of queries with incorrect type



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

