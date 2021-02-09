.. _a10_slb_template_tcp_proxy_module:


a10_slb_template_tcp_proxy -- Configures A10 slb.template.tcp-proxy
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

TCP Proxy






Parameters
----------

  init_cwnd (False, any, None)
    The initial congestion control window size (packets), default is 10 (init-cwnd in packets, default 10)


  reassembly_limit (False, any, None)
    The reassembly queuing limit, default is 25 segments (number)


  qos (False, any, None)
    QOS level (number)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  reno (False, any, None)
    Enable Reno Congestion Control Algorithm


  down (False, any, None)
    send reset to client when server is down


  dynamic_buffer_allocation (False, any, None)
    Optimally adjust the transmit and receive buffer sizes of TCP proxy while keeping their sum constant


  reset_fwd (False, any, None)
    send reset to server if error happens


  del_session_on_server_down (False, any, None)
    Delete session if the server/port goes down (either disabled/hm down)


  timewait (False, any, None)
    Timewait Threshold (sec), default 5 (number)


  disable_window_scale (False, any, None)
    disable TCP Window-Scale Option


  transmit_buffer (False, any, None)
    TCP Transmit Buffer (default 200k) (number default 200000 bytes)


  keepalive_probes (False, any, None)
    Number of keepalive probes sent, default is off


  uuid (False, any, None)
    uuid of the object


  syn_retries (False, any, None)
    SYN Retry Numbers, default is 5


  server_down_action (False, any, None)
    'FIN'= FIN Connection; 'RST'= Reset Connection;


  a10_partition (False, any, None)
    Destination/target partition for object/command


  mss (False, any, None)
    Responding MSS to use if client MSS is large, default is off (number)


  disable_sack (False, any, None)
    disable Selective Ack Option


  alive_if_active (False, any, None)
    keep connection alive if active traffic


  half_close_idle_timeout (False, any, None)
    TCP Half Close Idle Timeout (sec), default is off (cmd is deprecated, use fin- timeout instead) (number)


  state (True, any, None)
    State of the object to be created.


  proxy_header (False, any, None)
    Field proxy_header


    version (optional, any, None)
      'v1'= version 1; 'v2'= version 2;


    proxy_header_action (optional, any, None)
      'insert'= Insert proxy header;



  min_rto (False, any, None)
    The minmum retransmission timeout, default is 200ms (number)


  nagle (False, any, None)
    Enable Nagle Algorithm


  ack_aggressiveness (False, any, None)
    'low'= Delayed ACK; 'medium'= Delayed ACK, with ACK on each packet with PUSH flag; 'high'= ACK on each packet;


  backend_wscale (False, any, None)
    The TCP window scale used for the server side, default is off (number)


  psh_flag_optimization (False, any, None)
    Enable Optimized PSH Flag Use


  disable_abc (False, any, None)
    Appropriate Byte Counting RFC 3465 Disabled, default is enabled (Appropriate Byte Counting (ABC) is enabled by default)


  limited_slowstart (False, any, None)
    RFC 3742 Limited Slow-Start for TCP with Large Congestion Windows (number)


  ansible_port (True, any, None)
    Port for AXAPI authentication


  fin_timeout (False, any, None)
    FIN timeout (sec), default is disabled (number)


  idle_timeout (False, any, None)
    Idle Timeout (Interval of 60 seconds), default is 600 (idle timeout in second, default 600)


  disable (False, any, None)
    send reset to client when server is disabled


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  ansible_host (True, any, None)
    Host for AXAPI authentication


  half_open_idle_timeout (False, any, None)
    TCP Half Open Idle Timeout (sec), default is off (number)


  maxburst (False, any, None)
    The max packet count sent per transmission event (number)


  insert_client_ip (False, any, None)
    Insert client ip into TCP option


  keepalive_interval (False, any, None)
    Interval between keepalive probes (sec), default is off (number (seconds))


  initial_window_size (False, any, None)
    Set the initial window size, default is off (number)


  name (True, any, None)
    TCP Proxy Template Name


  ansible_password (True, any, None)
    Password for AXAPI authentication


  retransmit_retries (False, any, None)
    Number of Retries for Retransmit, default is 5


  disable_tcp_timestamps (False, any, None)
    disable TCP Timestamps Option


  force_delete_timeout (False, any, None)
    The maximum time that a session can stay in the system before being deleted, default is off (number (second))


  reset_rev (False, any, None)
    send reset to client if error happens


  force_delete_timeout_100ms (False, any, None)
    The maximum time that a session can stay in the system before being deleted, default is off (number in 100ms)


  invalid_rate_limit (False, any, None)
    Invalid Packet Response Rate Limit (ms), default is 500 (number default 500 challenges)


  user_tag (False, any, None)
    Customized tag


  reassembly_timeout (False, any, None)
    The reassembly timeout, default is 30sec (number)


  receive_buffer (False, any, None)
    TCP Receive Buffer (default 200k) (number default 200000 bytes)


  early_retransmit (False, any, None)
    Configure the Early-Retransmit Algorithm (RFC 5827) (Early-Retransmit is disabled by default)









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

