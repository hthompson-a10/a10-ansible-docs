.. _a10_slb_spdy_proxy_module:


a10_slb_spdy_proxy -- Configures A10 slb.spdy-proxy
===================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure SPDY Proxy






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'curr_proxy'= Curr Proxy Conns; 'total_proxy'= Total Proxy Conns; 'curr_http_proxy'= Curr HTTP Proxy Conns; 'total_http_proxy'= Total HTTP Proxy Conns; 'total_v2_proxy'= Version 2 Streams; 'total_v3_proxy'= Version 3 Streams; 'curr_stream'= Curr Streams; 'total_stream'= Total Streams; 'total_stream_succ'= Streams(succ); 'client_rst'= client_rst; 'server_rst'= Server RST sent; 'client_goaway'= client_goaway; 'server_goaway'= Server GOAWAY sent; 'tcp_err'= TCP sock error; 'inflate_ctx'= Inflate context; 'deflate_ctx'= Deflate context; 'ping_sent'= PING sent; 'stream_not_found'= STREAM not found; 'client_fin'= Client FIN; 'server_fin'= Server FIN; 'stream_close'= Stream close; 'stream_err'= Stream err; 'session_err'= Session err; 'control_frame'= Control frame received; 'syn_frame'= SYN stream frame received; 'syn_reply_frame'= SYN reply frame received; 'headers_frame'= Headers frame received; 'settings_frame'= Setting frame received; 'window_frame'= Window update frame received; 'ping_frame'= Ping frame received; 'data_frame'= Data frame received; 'data_no_stream'= Data no stream found; 'data_no_stream_no_goaway'= Data no stream and no goaway; 'data_no_stream_goaway_close'= Data no stream and no goaway and close session; 'est_cb_no_tuple'= Est callback no tuple; 'data_cb_no_tuple'= Data callback no tuple; 'ctx_alloc_fail'= Context alloc fail; 'fin_close_session'= FIN close session; 'server_rst_close_stream'= Server RST close stream; 'stream_found'= Stream found; 'close_stream_session_not_found'= Close stream session not found; 'close_stream_stream_not_found'= Close stream stream not found; 'close_stream_already_closed'= Closing closed stream; 'close_stream_session_close'= Stream close session close; 'close_session_already_closed'= Closing closed session; 'max_concurrent_stream_limit'= Max concurrent stream limit; 'stream_alloc_fail'= Stream alloc fail; 'http_conn_alloc_fail'= HTTP connection allocation fail; 'request_header_alloc_fail'= Request/Header allocation fail; 'name_value_total_len_ex'= Name value total length exceeded; 'name_value_zero_len'= Name value zero name length; 'name_value_invalid_http_ver'= Name value invalid http version; 'name_value_connection'= Name value connection; 'name_value_keepalive'= Name value keep alive; 'name_value_proxy_conn'= Name value proxy-connection; 'name_value_trasnfer_encod'= Name value transfer encoding; 'name_value_no_must_have'= Name value no must have; 'decompress_fail'= Decompress fail; 'syn_after_goaway'= SYN after goaway; 'stream_lt_prev'= Stream id less than previous; 'syn_stream_exist_or_even'= Stream already exists; 'syn_unidir'= Unidirectional SYN; 'syn_reply_alr_rcvd'= SYN reply already received; 'client_rst_nostream'= Close RST stream not found; 'window_no_stream'= Window update no stream found; 'invalid_window_size'= Invalid window size; 'unknown_control_frame'= Unknown control frame; 'data_on_closed_stream'= Data on closed stream; 'invalid_frame_size'= Invalid frame size; 'invalid_version'= Invalid version; 'header_after_session_close'= Header after session close; 'compress_ctx_alloc_fail'= Compression context allocation fail; 'header_compress_fail'= Header compress fail; 'http_data_session_close'= HTTP data session close; 'http_data_stream_not_found'= HTTP data stream not found; 'close_stream_not_http_proxy'= Close Stream not http-proxy; 'session_needs_requeue'= Session needs requeue; 'new_stream_session_del'= New Stream after Session delete; 'fin_stream_closed'= HTTP FIN stream already closed; 'http_close_stream_closed'= HTTP close stream already closed; 'http_err_stream_closed'= HTTP error stream already closed; 'http_hdr_stream_close'= HTTP header stream already closed; 'http_data_stream_close'= HTTP data stream already closed; 'session_close'= Session close;



  oper (False, any, None)
    Field oper


    l4_cpu_list (optional, any, None)
      Field l4_cpu_list


    cpu_count (optional, any, None)
      Field cpu_count



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    name_value_total_len_ex (optional, any, None)
      Name value total length exceeded


    data_cb_no_tuple (optional, any, None)
      Data callback no tuple


    total_proxy (optional, any, None)
      Total Proxy Conns


    curr_http_proxy (optional, any, None)
      Curr HTTP Proxy Conns


    close_stream_stream_not_found (optional, any, None)
      Close stream stream not found


    est_cb_no_tuple (optional, any, None)
      Est callback no tuple


    stream_alloc_fail (optional, any, None)
      Stream alloc fail


    new_stream_session_del (optional, any, None)
      New Stream after Session delete


    client_goaway (optional, any, None)
      Field client_goaway


    compress_ctx_alloc_fail (optional, any, None)
      Compression context allocation fail


    invalid_version (optional, any, None)
      Invalid version


    total_http_proxy (optional, any, None)
      Total HTTP Proxy Conns


    decompress_fail (optional, any, None)
      Decompress fail


    invalid_frame_size (optional, any, None)
      Invalid frame size


    control_frame (optional, any, None)
      Control frame received


    fin_stream_closed (optional, any, None)
      HTTP FIN stream already closed


    stream_close (optional, any, None)
      Stream close


    headers_frame (optional, any, None)
      Headers frame received


    window_no_stream (optional, any, None)
      Window update no stream found


    server_rst_close_stream (optional, any, None)
      Server RST close stream


    data_no_stream (optional, any, None)
      Data no stream found


    data_no_stream_no_goaway (optional, any, None)
      Data no stream and no goaway


    ctx_alloc_fail (optional, any, None)
      Context alloc fail


    syn_stream_exist_or_even (optional, any, None)
      Stream already exists


    server_rst (optional, any, None)
      Server RST sent


    name_value_keepalive (optional, any, None)
      Name value keep alive


    syn_frame (optional, any, None)
      SYN stream frame received


    name_value_proxy_conn (optional, any, None)
      Name value proxy-connection


    request_header_alloc_fail (optional, any, None)
      Request/Header allocation fail


    settings_frame (optional, any, None)
      Setting frame received


    close_stream_already_closed (optional, any, None)
      Closing closed stream


    data_on_closed_stream (optional, any, None)
      Data on closed stream


    name_value_trasnfer_encod (optional, any, None)
      Name value transfer encoding


    fin_close_session (optional, any, None)
      FIN close session


    syn_after_goaway (optional, any, None)
      SYN after goaway


    syn_reply_frame (optional, any, None)
      SYN reply frame received


    name_value_invalid_http_ver (optional, any, None)
      Name value invalid http version


    http_hdr_stream_close (optional, any, None)
      HTTP header stream already closed


    name_value_connection (optional, any, None)
      Name value connection


    client_fin (optional, any, None)
      Client FIN


    data_no_stream_goaway_close (optional, any, None)
      Data no stream and no goaway and close session


    total_stream_succ (optional, any, None)
      Streams(succ)


    stream_lt_prev (optional, any, None)
      Stream id less than previous


    close_stream_not_http_proxy (optional, any, None)
      Close Stream not http-proxy


    session_err (optional, any, None)
      Session err


    server_fin (optional, any, None)
      Server FIN


    total_stream (optional, any, None)
      Total Streams


    total_v2_proxy (optional, any, None)
      Version 2 Streams


    client_rst (optional, any, None)
      Field client_rst


    syn_unidir (optional, any, None)
      Unidirectional SYN


    max_concurrent_stream_limit (optional, any, None)
      Max concurrent stream limit


    deflate_ctx (optional, any, None)
      Deflate context


    inflate_ctx (optional, any, None)
      Inflate context


    server_goaway (optional, any, None)
      Server GOAWAY sent


    http_data_session_close (optional, any, None)
      HTTP data session close


    close_stream_session_close (optional, any, None)
      Stream close session close


    ping_frame (optional, any, None)
      Ping frame received


    ping_sent (optional, any, None)
      PING sent


    http_err_stream_closed (optional, any, None)
      HTTP error stream already closed


    header_after_session_close (optional, any, None)
      Header after session close


    http_data_stream_close (optional, any, None)
      HTTP data stream already closed


    stream_not_found (optional, any, None)
      STREAM not found


    session_needs_requeue (optional, any, None)
      Session needs requeue


    unknown_control_frame (optional, any, None)
      Unknown control frame


    close_stream_session_not_found (optional, any, None)
      Close stream session not found


    stream_found (optional, any, None)
      Stream found


    window_frame (optional, any, None)
      Window update frame received


    close_session_already_closed (optional, any, None)
      Closing closed session


    syn_reply_alr_rcvd (optional, any, None)
      SYN reply already received


    header_compress_fail (optional, any, None)
      Header compress fail


    tcp_err (optional, any, None)
      TCP sock error


    curr_proxy (optional, any, None)
      Curr Proxy Conns


    data_frame (optional, any, None)
      Data frame received


    http_data_stream_not_found (optional, any, None)
      HTTP data stream not found


    http_close_stream_closed (optional, any, None)
      HTTP close stream already closed


    curr_stream (optional, any, None)
      Curr Streams


    name_value_zero_len (optional, any, None)
      Name value zero name length


    name_value_no_must_have (optional, any, None)
      Name value no must have


    client_rst_nostream (optional, any, None)
      Close RST stream not found


    http_conn_alloc_fail (optional, any, None)
      HTTP connection allocation fail


    total_v3_proxy (optional, any, None)
      Version 3 Streams


    invalid_window_size (optional, any, None)
      Invalid window size


    stream_err (optional, any, None)
      Stream err


    session_close (optional, any, None)
      Session close



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

