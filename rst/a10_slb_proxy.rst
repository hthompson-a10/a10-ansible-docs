.. _a10_slb_proxy_module:


a10_slb_proxy -- Configures A10 slb.proxy
=========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure Proxy Global






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'num'= Num; 'tcp_event'= TCP stack event; 'est_event'= Connection established; 'data_event'= Data received; 'client_fin'= Client FIN; 'server_fin'= Server FIN; 'wbuf_event'= Ready to send data; 'err_event'= Error occured; 'no_mem'= No memory; 'client_rst'= Client RST; 'server_rst'= Server RST; 'queue_depth_over_limit'= Queue depth over limit; 'event_failed'= Event failed; 'conn_not_exist'= Conn not exist; 'service_alloc_cb'= Service alloc callback; 'service_alloc_cb_failed'= Service alloc callback failed; 'service_free_cb'= Service free callback; 'service_free_cb_failed'= Service free callback failed; 'est_cb_failed'= App EST callback failed; 'data_cb_failed'= App DATA callback failed; 'wbuf_cb_failed'= App WBUF callback failed; 'err_cb_failed'= App ERR callback failed; 'start_server_conn'= Start server conn; 'start_server_conn_succ'= Success; 'start_server_conn_no_route'= No route to server; 'start_server_conn_fail_mem'= No memory; 'start_server_conn_fail_snat'= Failed Source NAT; 'start_server_conn_fail_persist'= Fail Persistence; 'start_server_conn_fail_server'= Fail Server issue; 'start_server_conn_fail_tuple'= Fail Tuple Issue; 'line_too_long'= Line too long;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    service_alloc_cb (optional, any, None)
      Service alloc callback


    queue_depth_over_limit (optional, any, None)
      Queue depth over limit


    server_fin (optional, any, None)
      Server FIN


    start_server_conn_fail_tuple (optional, any, None)
      Fail Tuple Issue


    start_server_conn_fail_snat (optional, any, None)
      Failed Source NAT


    start_server_conn_no_route (optional, any, None)
      No route to server


    start_server_conn_succ (optional, any, None)
      Success


    client_rst (optional, any, None)
      Client RST


    err_cb_failed (optional, any, None)
      App ERR callback failed


    start_server_conn (optional, any, None)
      Start server conn


    start_server_conn_fail_server (optional, any, None)
      Fail Server issue


    server_rst (optional, any, None)
      Server RST


    service_free_cb_failed (optional, any, None)
      Service free callback failed


    err_event (optional, any, None)
      Error occured


    est_event (optional, any, None)
      Connection established


    line_too_long (optional, any, None)
      Line too long


    service_free_cb (optional, any, None)
      Service free callback


    start_server_conn_fail_mem (optional, any, None)
      No memory


    wbuf_event (optional, any, None)
      Ready to send data


    no_mem (optional, any, None)
      No memory


    data_event (optional, any, None)
      Data received


    wbuf_cb_failed (optional, any, None)
      App WBUF callback failed


    start_server_conn_fail_persist (optional, any, None)
      Fail Persistence


    service_alloc_cb_failed (optional, any, None)
      Service alloc callback failed


    client_fin (optional, any, None)
      Client FIN


    est_cb_failed (optional, any, None)
      App EST callback failed


    tcp_event (optional, any, None)
      TCP stack event


    event_failed (optional, any, None)
      Event failed


    data_cb_failed (optional, any, None)
      App DATA callback failed


    conn_not_exist (optional, any, None)
      Conn not exist



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

