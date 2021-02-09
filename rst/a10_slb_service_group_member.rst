.. _a10_slb_service_group_member_module:


a10_slb_service_group_member -- Configures A10 slb.service.group.member
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Service Group Member






Parameters
----------

  oper (False, any, None)
    Field oper


    state (optional, any, None)
      Field state


    hm_key (optional, any, None)
      Field hm_key


    drs_list (optional, any, None)
      Field drs_list


    name (optional, any, None)
      Member name


    alt_list (optional, any, None)
      Field alt_list


    hm_index (optional, any, None)
      Field hm_index


    port (optional, any, None)
      Port number



  ansible_username (True, any, None)
    Username for AXAPI authentication


  member_priority (False, any, None)
    Priority of Port in the Group (Priority of Port in the Group, default is 1)


  service_group_name (optional, any, None)
    Key to identify parent object


  resolve_as (False, any, None)
    'resolve-to-ipv4'= Use A Query only to resolve FQDN; 'resolve-to-ipv6'= Use AAAA Query only to resolve FQDN; 'resolve-to-ipv4-and-ipv6'= Use A as well as AAAA Query to resolve FQDN;


  host (False, any, None)
    IP Address - Not applicable if real server is already defined


  member_template (False, any, None)
    Real server port template (Real server port template name)


  stats (False, any, None)
    Field stats


    curr_req (optional, any, None)
      Current requests


    peak_conn (optional, any, None)
      Peak connections


    total_rev_pkts_inspected_status_code_non_5xx (optional, any, None)
      Total reverse packets inspected status code non 5xx


    total_fwd_pkts (optional, any, None)
      Packets processed in forward direction


    curr_ssl_conn (optional, any, None)
      Current SSL connections


    curr_conn (optional, any, None)
      Current established connections


    total_req (optional, any, None)
      Total requests


    total_fwd_bytes (optional, any, None)
      Bytes processed in forward direction


    port (optional, any, None)
      Port number


    response_time (optional, any, None)
      Response time


    total_rev_bytes (optional, any, None)
      Bytes processed in reverse direction


    name (optional, any, None)
      Member name


    total_rev_pkts_inspected_status_code_2xx (optional, any, None)
      Total reverse packets inspected status code 2xx


    total_ssl_conn (optional, any, None)
      Total SSL connections


    total_conn (optional, any, None)
      Total established connections


    fastest_rsp_time (optional, any, None)
      Fastest response time


    state_flaps (optional, any, None)
      State flaps count


    total_rev_pkts (optional, any, None)
      Packets processed in reverse direction


    total_req_succ (optional, any, None)
      Total requests successful


    total_rev_pkts_inspected (optional, any, None)
      Total reverse packets inspected


    curr_conn_overflow (optional, any, None)
      Current connection counter overflow count


    slowest_rsp_time (optional, any, None)
      Slowest response time



  a10_partition (False, any, None)
    Destination/target partition for object/command


  port (True, any, None)
    Port number


  name (True, any, None)
    Member name


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'total_fwd_bytes'= Bytes processed in forward direction; 'total_fwd_pkts'= Packets processed in forward direction; 'total_rev_bytes'= Bytes processed in reverse direction; 'total_rev_pkts'= Packets processed in reverse direction; 'total_conn'= Total established connections; 'total_rev_pkts_inspected'= Total reverse packets inspected; 'total_rev_pkts_inspected_status_code_2xx'= Total reverse packets inspected status code 2xx; 'total_rev_pkts_inspected_status_code_non_5xx'= Total reverse packets inspected status code non 5xx; 'curr_req'= Current requests; 'total_req'= Total requests; 'total_req_succ'= Total requests successful; 'peak_conn'= Peak connections; 'response_time'= Response time; 'fastest_rsp_time'= Fastest response time; 'slowest_rsp_time'= Slowest response time; 'curr_ssl_conn'= Current SSL connections; 'total_ssl_conn'= Total SSL connections; 'curr_conn_overflow'= Current connection counter overflow count; 'state_flaps'= State flaps count;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  fqdn_name (False, any, None)
    Server hostname - Not applicable if real server is already defined


  uuid (False, any, None)
    uuid of the object


  ansible_password (True, any, None)
    Password for AXAPI authentication


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  member_stats_data_disable (False, any, None)
    Disable statistical data collection


  member_state (False, any, None)
    'enable'= Enable member service port; 'disable'= Disable member service port; 'disable-with-health-check'= disable member service port, but health check work;


  user_tag (False, any, None)
    Customized tag


  server_ipv6_addr (False, any, None)
    IPV6 Address - Not applicable if real server is already defined









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

