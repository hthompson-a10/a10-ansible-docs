.. _a10_slb_l7session_module:


a10_slb_l7session -- Configures A10 slb.l7session
=================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure l7session






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'start_server_conn_succ'= Start Server Conn Success; 'conn_not_exist'= Conn does not exist; 'data_event'= Data event from TCP; 'client_fin'= FIN from client; 'server_fin'= FIN from server; 'wbuf_event'= Wbuf event from TCP; 'wbuf_cb_failed'= Wbuf event callback failed; 'err_event'= Err event from TCP; 'err_cb_failed'= Err event callback failed; 'server_conn_failed'= Server connection failed; 'client_rst'= RST from client; 'server_rst'= RST from server; 'client_rst_req'= RST from client - request; 'client_rst_connecting'= RST from client - connecting; 'client_rst_connected'= RST from client - connected; 'client_rst_rsp'= RST from client - response; 'server_rst_req'= RST from server - request; 'server_rst_connecting'= RST from server - connecting; 'server_rst_connected'= RST from server - connected; 'server_rst_rsp'= RST from server - response; 'proxy_v1_connection'= counter for Proxy v1 connection; 'proxy_v2_connection'= counter for Proxy v2 connection; 'curr_proxy'= Curr proxy conn; 'curr_proxy_client'= Curr proxy conn - client; 'curr_proxy_server'= Curr proxy conn - server; 'curr_proxy_es'= Curr proxy conn - ES; 'total_proxy'= Total proxy conn; 'total_proxy_client'= Total proxy conn - client; 'total_proxy_server'= Total proxy conn - server; 'total_proxy_es'= Total proxy conn - ES; 'server_select_fail'= Server selection fail; 'est_event'= Est event from TCP; 'est_cb_failed'= Est event callback fail; 'data_cb_failed'= Data event callback fail; 'hps_fwdreq_fail'= Fwd req fail; 'hps_fwdreq_fail_buff'= Fwd req fail - buff; 'hps_fwdreq_fail_rport'= Fwd req fail - rport; 'hps_fwdreq_fail_route'= Fwd req fail - route; 'hps_fwdreq_fail_persist'= Fwd req fail - persist; 'hps_fwdreq_fail_server'= Fwd req fail - server; 'hps_fwdreq_fail_tuple'= Fwd req fail - tuple;



  oper (False, any, None)
    Field oper


    cpu_count (optional, any, None)
      Field cpu_count


    l7_cpu_list (optional, any, None)
      Field l7_cpu_list



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    server_fin (optional, any, None)
      FIN from server


    server_rst (optional, any, None)
      RST from server


    server_select_fail (optional, any, None)
      Server selection fail


    total_proxy (optional, any, None)
      Total proxy conn


    curr_proxy (optional, any, None)
      Curr proxy conn


    client_rst (optional, any, None)
      RST from client


    hps_fwdreq_fail (optional, any, None)
      Fwd req fail


    err_event (optional, any, None)
      Err event from TCP


    start_server_conn_succ (optional, any, None)
      Start Server Conn Success


    wbuf_event (optional, any, None)
      Wbuf event from TCP


    data_event (optional, any, None)
      Data event from TCP


    wbuf_cb_failed (optional, any, None)
      Wbuf event callback failed


    err_cb_failed (optional, any, None)
      Err event callback failed


    client_fin (optional, any, None)
      FIN from client


    server_conn_failed (optional, any, None)
      Server connection failed


    data_cb_failed (optional, any, None)
      Data event callback fail


    conn_not_exist (optional, any, None)
      Conn does not exist



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

