.. _a10_cgnv6_service_group_member_module:


a10_cgnv6_service_group_member -- Configures A10 cgnv6.service.group.member
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Service Group Member






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'curr_conn'= Current connections; 'total_fwd_bytes'= Total forward bytes; 'total_fwd_pkts'= Total forward packets; 'total_rev_bytes'= Total reverse bytes; 'total_rev_pkts'= Total reverse packets; 'total_conn'= Total connections; 'total_rev_pkts_inspected'= Total reverse packets inspected; 'total_rev_pkts_inspected_status_code_2xx'= Total reverse packets inspected status code 2xx; 'total_rev_pkts_inspected_status_code_non_5xx'= Total reverse packets inspected status code non 5xx; 'curr_req'= Current requests; 'total_req'= Total requests; 'total_req_succ'= Total requests success; 'peak_conn'= Peak connections; 'response_time'= Response time; 'fastest_rsp_time'= Fastest response time; 'slowest_rsp_time'= Slowest response time; 'curr_ssl_conn'= Current SSL connections; 'total_ssl_conn'= Total SSL connections;



  oper (False, any, None)
    Field oper


    state (optional, any, None)
      Field state


    hm_key (optional, any, None)
      Field hm_key


    hm_index (optional, any, None)
      Field hm_index


    name (optional, any, None)
      Member name


    port (optional, any, None)
      Port number



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    curr_req (optional, any, None)
      Current requests


    peak_conn (optional, any, None)
      Peak connections


    total_req (optional, any, None)
      Total requests


    total_rev_pkts (optional, any, None)
      Total reverse packets


    curr_ssl_conn (optional, any, None)
      Current SSL connections


    curr_conn (optional, any, None)
      Current connections


    total_rev_pkts_inspected_status_code_non_5xx (optional, any, None)
      Total reverse packets inspected status code non 5xx


    total_fwd_bytes (optional, any, None)
      Total forward bytes


    port (optional, any, None)
      Port number


    response_time (optional, any, None)
      Response time


    total_rev_bytes (optional, any, None)
      Total reverse bytes


    name (optional, any, None)
      Member name


    total_rev_pkts_inspected_status_code_2xx (optional, any, None)
      Total reverse packets inspected status code 2xx


    total_ssl_conn (optional, any, None)
      Total SSL connections


    total_conn (optional, any, None)
      Total connections


    fastest_rsp_time (optional, any, None)
      Fastest response time


    total_fwd_pkts (optional, any, None)
      Total forward packets


    total_req_succ (optional, any, None)
      Total requests success


    total_rev_pkts_inspected (optional, any, None)
      Total reverse packets inspected


    slowest_rsp_time (optional, any, None)
      Slowest response time



  name (True, any, None)
    Member name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  service_group_name (optional, any, None)
    Key to identify parent object


  ansible_password (True, any, None)
    Password for AXAPI authentication


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  port (True, any, None)
    Port number


  uuid (False, any, None)
    uuid of the object









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

