.. _a10_aam_authentication_service_group_module:


a10_aam_authentication_service_group -- Configures A10 aam.authentication.service-group
=======================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Authentication service group






Parameters
----------

  oper (False, any, None)
    Field oper


    pri_affinity_priority (optional, any, None)
      Field pri_affinity_priority


    name (optional, any, None)
      Specify AAM service group name


    sgm_list (optional, any, None)
      Field sgm_list


    stateless_current_rate (optional, any, None)
      Field stateless_current_rate


    servers_down (optional, any, None)
      Field servers_down


    stateless_state (optional, any, None)
      Field stateless_state


    servers_disable (optional, any, None)
      Field servers_disable


    filter (optional, any, None)
      Field filter


    stateless_type (optional, any, None)
      Field stateless_type


    servers_total (optional, any, None)
      Field servers_total


    state (optional, any, None)
      Field state


    member_list (optional, any, None)
      Field member_list


    servers_up (optional, any, None)
      Field servers_up


    stateless_current_usage (optional, any, None)
      Field stateless_current_usage


    hm_dsr_enable_all_vip (optional, any, None)
      Field hm_dsr_enable_all_vip



  lb_method (False, any, None)
    'round-robin'= Round robin on server level;


  protocol (False, any, None)
    'tcp'= TCP AAM service; 'udp'= UDP AAM service;


  ansible_username (True, any, None)
    Username for AXAPI authentication


  health_check (False, any, None)
    Health Check (Monitor Name)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  health_check_disable (False, any, None)
    Disable health check


  uuid (False, any, None)
    uuid of the object


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'server_selection_fail_drop'= Drops due to Service selection failure; 'server_selection_fail_reset'= Resets sent out for Service selection failure; 'service_peak_conn'= Peak connection count for the Service Group; 'service_healthy_host'= Service Group healthy host count; 'service_unhealthy_host'= Service Group unhealthy host count; 'service_req_count'= Service Group request count; 'service_resp_count'= Service Group response count; 'service_resp_2xx'= Service Group response 2xx count; 'service_resp_3xx'= Service Group response 3xx count; 'service_resp_4xx'= Service Group response 4xx count; 'service_resp_5xx'= Service Group response 5xx count; 'service_curr_conn_overflow'= Current connection counter overflow count;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    service_resp_2xx (optional, any, None)
      Service Group response 2xx count


    service_unhealthy_host (optional, any, None)
      Service Group unhealthy host count


    service_curr_conn_overflow (optional, any, None)
      Current connection counter overflow count


    name (optional, any, None)
      Specify AAM service group name


    server_selection_fail_drop (optional, any, None)
      Drops due to Service selection failure


    service_healthy_host (optional, any, None)
      Service Group healthy host count


    service_resp_count (optional, any, None)
      Service Group response count


    member_list (optional, any, None)
      Field member_list


    service_req_count (optional, any, None)
      Service Group request count


    service_resp_4xx (optional, any, None)
      Service Group response 4xx count


    service_peak_conn (optional, any, None)
      Peak connection count for the Service Group


    server_selection_fail_reset (optional, any, None)
      Resets sent out for Service selection failure


    service_resp_3xx (optional, any, None)
      Service Group response 3xx count


    service_resp_5xx (optional, any, None)
      Service Group response 5xx count



  name (True, any, None)
    Specify AAM service group name


  ansible_password (True, any, None)
    Password for AXAPI authentication


  member_list (False, any, None)
    Field member_list


    sampling_enable (optional, any, None)
      Field sampling_enable


    member_state (optional, any, None)
      'enable'= Enable member service port; 'disable'= Disable member service port;


    uuid (optional, any, None)
      uuid of the object


    member_priority (optional, any, None)
      Priority of Port in the Group


    user_tag (optional, any, None)
      Customized tag


    port (optional, any, None)
      Port number


    name (optional, any, None)
      Member name



  state (True, any, None)
    State of the object to be created.


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

