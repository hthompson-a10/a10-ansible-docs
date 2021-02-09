.. _a10_slb_smtp_module:


a10_slb_smtp -- Configures A10 slb.smtp
=======================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure SMTP






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'curr_proxy'= Current proxy conns; 'total_proxy'= Total proxy conns; 'request'= SMTP requests; 'request_success'= SMTP requests (success); 'no_proxy'= No proxy error; 'client_reset'= Client reset; 'server_reset'= Server reset; 'no_tuple'= No tuple error; 'parse_req_fail'= Parse request failure; 'server_select_fail'= Server selection failure; 'forward_req_fail'= Forward request failure; 'forward_req_data_fail'= Forward REQ data failure; 'req_retran'= Request retransmit; 'req_ofo'= Request pkt out-of-order; 'server_reselect'= Server reselection; 'server_prem_close'= Server premature close; 'new_server_conn'= Server connection made; 'snat_fail'= Source NAT failure; 'tcp_out_reset'= TCP out reset; 'recv_client_command_EHLO'= Recv client EHLO; 'recv_client_command_HELO'= Recv client HELO; 'recv_client_command_MAIL'= Recv client MAIL; 'recv_client_command_RCPT'= Recv client RCPT; 'recv_client_command_DATA'= Recv client DATA; 'recv_client_command_RSET'= Recv client RSET; 'recv_client_command_VRFY'= Recv client VRFY; 'recv_client_command_EXPN'= Recv client EXPN; 'recv_client_command_HELP'= Recv client HELP; 'recv_client_command_NOOP'= Recv client NOOP; 'recv_client_command_QUIT'= Recv client QUIT; 'recv_client_command_STARTTLS'= Recv client STARTTLS; 'recv_client_command_others'= Recv client other cmds; 'recv_server_service_not_ready'= Recv server serv-not-rdy; 'recv_server_unknow_reply_code'= Recv server unknown-code; 'send_client_service_ready'= Sent client serv-rdy; 'send_client_service_not_ready'= Sent client serv-not-rdy; 'send_client_close_connection'= Sent client close-conn; 'send_client_go_ahead'= Sent client go-ahead; 'send_client_start_TLS_first'= Sent client STARTTLS-1st; 'send_client_TLS_not_available'= Sent client TLS-not-aval; 'send_client_no_command'= Sent client no-such-cmd; 'send_server_cmd_reset'= Sent server RSET; 'TLS_established'= SSL session established; 'L4_switch'= L4 switching; 'Aflex_switch'= aFleX switching; 'Aflex_switch_ok'= aFleX switching (succ); 'client_domain_switch'= Client domain switching; 'client_domain_switch_ok'= Client domain sw (succ); 'LB_switch'= LB switching; 'LB_switch_ok'= LB switching (succ); 'read_request_line_fail'= Read request line fail; 'get_all_headers_fail'= Get all headers fail; 'too_many_headers'= Too many headers; 'line_too_long'= Line too long; 'line_across_packet'= Line across packets; 'line_extend'= Line extend; 'line_extend_fail'= Line extend fail; 'line_table_extend'= Table extend; 'line_table_extend_fail'= Table extend fail; 'parse_request_line_fail'= Parse request line fail; 'insert_resonse_line_fail'= Ins response line fail; 'remove_resonse_line_fail'= Del response line fail; 'parse_resonse_line_fail'= Parse response line fail; 'Aflex_lb_reselect'= aFleX lb reselect; 'Aflex_lb_reselect_ok'= aFleX lb reselect (succ); 'server_STARTTLS_init'= Init server side STARTTLS; 'server_STARTTLS_fail'= Server side STARTTLS fail; 'rserver_STARTTLS_disable'= real server not support STARTTLS; 'recv_client_command_TURN'= Recv client TURN; 'recv_client_command_ETRN'= Recv client ETRN;



  oper (False, any, None)
    Field oper


    cpu_count (optional, any, None)
      Field cpu_count


    smtp_cpu_list (optional, any, None)
      Field smtp_cpu_list



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    recv_client_command_RCPT (optional, any, None)
      Recv client RCPT


    recv_client_command_DATA (optional, any, None)
      Recv client DATA


    total_proxy (optional, any, None)
      Total proxy conns


    L4_switch (optional, any, None)
      L4 switching


    too_many_headers (optional, any, None)
      Too many headers


    recv_client_command_QUIT (optional, any, None)
      Recv client QUIT


    recv_client_command_NOOP (optional, any, None)
      Recv client NOOP


    new_server_conn (optional, any, None)
      Server connection made


    recv_client_command_MAIL (optional, any, None)
      Recv client MAIL


    line_extend_fail (optional, any, None)
      Line extend fail


    forward_req_data_fail (optional, any, None)
      Forward REQ data failure


    recv_client_command_HELO (optional, any, None)
      Recv client HELO


    line_across_packet (optional, any, None)
      Line across packets


    client_domain_switch_ok (optional, any, None)
      Client domain sw (succ)


    recv_client_command_STARTTLS (optional, any, None)
      Recv client STARTTLS


    recv_client_command_others (optional, any, None)
      Recv client other cmds


    recv_client_command_EXPN (optional, any, None)
      Recv client EXPN


    LB_switch (optional, any, None)
      LB switching


    get_all_headers_fail (optional, any, None)
      Get all headers fail


    send_client_no_command (optional, any, None)
      Sent client no-such-cmd


    Aflex_switch_ok (optional, any, None)
      aFleX switching (succ)


    server_select_fail (optional, any, None)
      Server selection failure


    server_reselect (optional, any, None)
      Server reselection


    send_client_go_ahead (optional, any, None)
      Sent client go-ahead


    req_ofo (optional, any, None)
      Request pkt out-of-order


    client_domain_switch (optional, any, None)
      Client domain switching


    snat_fail (optional, any, None)
      Source NAT failure


    send_client_service_not_ready (optional, any, None)
      Sent client serv-not-rdy


    parse_req_fail (optional, any, None)
      Parse request failure


    read_request_line_fail (optional, any, None)
      Read request line fail


    server_STARTTLS_fail (optional, any, None)
      Server side STARTTLS fail


    recv_client_command_EHLO (optional, any, None)
      Recv client EHLO


    send_client_TLS_not_available (optional, any, None)
      Sent client TLS-not-aval


    recv_client_command_TURN (optional, any, None)
      Recv client TURN


    request_success (optional, any, None)
      SMTP requests (success)


    recv_client_command_ETRN (optional, any, None)
      Recv client ETRN


    forward_req_fail (optional, any, None)
      Forward request failure


    tcp_out_reset (optional, any, None)
      TCP out reset


    req_retran (optional, any, None)
      Request retransmit


    recv_client_command_VRFY (optional, any, None)
      Recv client VRFY


    server_prem_close (optional, any, None)
      Server premature close


    parse_resonse_line_fail (optional, any, None)
      Parse response line fail


    send_client_close_connection (optional, any, None)
      Sent client close-conn


    insert_resonse_line_fail (optional, any, None)
      Ins response line fail


    no_proxy (optional, any, None)
      No proxy error


    client_reset (optional, any, None)
      Client reset


    server_STARTTLS_init (optional, any, None)
      Init server side STARTTLS


    recv_client_command_HELP (optional, any, None)
      Recv client HELP


    send_client_start_TLS_first (optional, any, None)
      Sent client STARTTLS-1st


    recv_client_command_RSET (optional, any, None)
      Recv client RSET


    Aflex_switch (optional, any, None)
      aFleX switching


    no_tuple (optional, any, None)
      No tuple error


    rserver_STARTTLS_disable (optional, any, None)
      real server not support STARTTLS


    recv_server_unknow_reply_code (optional, any, None)
      Recv server unknown-code


    line_table_extend (optional, any, None)
      Table extend


    send_server_cmd_reset (optional, any, None)
      Sent server RSET


    Aflex_lb_reselect (optional, any, None)
      aFleX lb reselect


    curr_proxy (optional, any, None)
      Current proxy conns


    send_client_service_ready (optional, any, None)
      Sent client serv-rdy


    server_reset (optional, any, None)
      Server reset


    recv_server_service_not_ready (optional, any, None)
      Recv server serv-not-rdy


    parse_request_line_fail (optional, any, None)
      Parse request line fail


    remove_resonse_line_fail (optional, any, None)
      Del response line fail


    line_table_extend_fail (optional, any, None)
      Table extend fail


    LB_switch_ok (optional, any, None)
      LB switching (succ)


    line_too_long (optional, any, None)
      Line too long


    request (optional, any, None)
      SMTP requests


    line_extend (optional, any, None)
      Line extend


    Aflex_lb_reselect_ok (optional, any, None)
      aFleX lb reselect (succ)


    TLS_established (optional, any, None)
      SSL session established



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

