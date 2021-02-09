.. _a10_system_icmp6_module:


a10_system_icmp6 -- Configures A10 system.icmp6
===============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Display ICMPv6 statistics






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'in_msgs'= In messages; 'in_errors'= In Errors; 'in_dest_un_reach'= In Destunation Unreachable; 'in_pkt_too_big'= In Packet too big; 'in_time_exceeds'= In TTL Exceeds; 'in_param_prob'= In Parameter Problem; 'in_echoes'= In Echo requests; 'in_exho_reply'= In Echo replies; 'in_grp_mem_query'= In Group member query; 'in_grp_mem_resp'= In Group member reply; 'in_grp_mem_reduction'= In Group member reduction; 'in_router_sol'= In Router solicitation; 'in_ra'= In Router advertisement; 'in_ns'= In neighbor solicitation; 'in_na'= In neighbor advertisement; 'in_redirect'= In Redirects; 'out_msg'= Out Messages; 'out_dst_un_reach'= Out Destination Unreachable; 'out_pkt_too_big'= Out Packet too big; 'out_time_exceeds'= Out TTL Exceeds; 'out_param_prob'= Out Parameter Problem; 'out_echo_req'= Out Echo requests; 'out_echo_replies'= Out Echo replies; 'out_rs'= Out Router solicitation; 'out_ra'= Out Router advertisement; 'out_ns'= Out neighbor solicitation; 'out_na'= Out neighbor advertisement; 'out_redirects'= Out Redirects; 'out_mem_resp'= Out Group member reply; 'out_mem_reductions'= Out Group member reduction; 'err_rs'= Error Router solicitation; 'err_ra'= Error Router advertisement; 'err_ns'= Error Neighbor solicitation; 'err_na'= Error Neighbor advertisement; 'err_redirects'= Error Redirects; 'err_echoes'= Error Echo requests; 'err_echo_replies'= Error Echo replies;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    out_echo_req (optional, any, None)
      Out Echo requests


    out_param_prob (optional, any, None)
      Out Parameter Problem


    out_pkt_too_big (optional, any, None)
      Out Packet too big


    out_na (optional, any, None)
      Out neighbor advertisement


    out_rs (optional, any, None)
      Out Router solicitation


    err_ns (optional, any, None)
      Error Neighbor solicitation


    in_grp_mem_resp (optional, any, None)
      In Group member reply


    in_echoes (optional, any, None)
      In Echo requests


    out_ns (optional, any, None)
      Out neighbor solicitation


    err_na (optional, any, None)
      Error Neighbor advertisement


    out_ra (optional, any, None)
      Out Router advertisement


    out_mem_reductions (optional, any, None)
      Out Group member reduction


    out_dst_un_reach (optional, any, None)
      Out Destination Unreachable


    in_msgs (optional, any, None)
      In messages


    in_param_prob (optional, any, None)
      In Parameter Problem


    in_pkt_too_big (optional, any, None)
      In Packet too big


    err_ra (optional, any, None)
      Error Router advertisement


    in_redirect (optional, any, None)
      In Redirects


    err_echoes (optional, any, None)
      Error Echo requests


    in_errors (optional, any, None)
      In Errors


    out_echo_replies (optional, any, None)
      Out Echo replies


    in_na (optional, any, None)
      In neighbor advertisement


    in_ra (optional, any, None)
      In Router advertisement


    err_rs (optional, any, None)
      Error Router solicitation


    err_redirects (optional, any, None)
      Error Redirects


    err_echo_replies (optional, any, None)
      Error Echo replies


    in_ns (optional, any, None)
      In neighbor solicitation


    out_msg (optional, any, None)
      Out Messages


    out_mem_resp (optional, any, None)
      Out Group member reply


    out_time_exceeds (optional, any, None)
      Out TTL Exceeds


    in_exho_reply (optional, any, None)
      In Echo replies


    in_router_sol (optional, any, None)
      In Router solicitation


    in_grp_mem_query (optional, any, None)
      In Group member query


    out_redirects (optional, any, None)
      Out Redirects


    in_time_exceeds (optional, any, None)
      In TTL Exceeds


    in_grp_mem_reduction (optional, any, None)
      In Group member reduction


    in_dest_un_reach (optional, any, None)
      In Destunation Unreachable



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

