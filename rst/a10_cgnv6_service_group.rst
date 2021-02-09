.. _a10_cgnv6_service_group_module:


a10_cgnv6_service_group -- Configures A10 cgnv6.service-group
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Service Group






Parameters
----------

  oper (False, any, None)
    Field oper


    pri_affinity_priority (optional, any, None)
      Field pri_affinity_priority


    name (optional, any, None)
      CGNV6 Service Name


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



  health_check (False, any, None)
    Health Check (Monitor Name)


  protocol (False, any, None)
    'tcp'= TCP LB service; 'udp'= UDP LB service;


  ansible_username (True, any, None)
    Username for AXAPI authentication


  traffic_replication_mirror_ip_repl (False, any, None)
    Replaces IP with server-IP


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  shared_partition (False, any, None)
    Share with a single partition (Partition Name)


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'server_selection_fail_drop'= Service selection fail drop; 'server_selection_fail_reset'= Service selection fail reset; 'service_peak_conn'= Service peak connection;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    server_selection_fail_drop (optional, any, None)
      Service selection fail drop


    server_selection_fail_reset (optional, any, None)
      Service selection fail reset


    service_peak_conn (optional, any, None)
      Service peak connection


    name (optional, any, None)
      CGNV6 Service Name


    member_list (optional, any, None)
      Field member_list



  name (True, any, None)
    CGNV6 Service Name


  user_tag (False, any, None)
    Customized tag


  member_list (False, any, None)
    Field member_list


    sampling_enable (optional, any, None)
      Field sampling_enable


    port (optional, any, None)
      Port number


    user_tag (optional, any, None)
      Customized tag


    uuid (optional, any, None)
      uuid of the object


    name (optional, any, None)
      Member name



  state (True, any, None)
    State of the object to be created.


  shared (False, any, None)
    Share with partition


  ansible_password (True, any, None)
    Password for AXAPI authentication


  shared_group (False, any, None)
    Share with a partition group (Partition Group Name)









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

