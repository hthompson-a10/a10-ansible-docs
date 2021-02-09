.. _a10_slb_http2_module:


a10_slb_http2 -- Configures A10 slb.http2
=========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure http2






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'curr_proxy'= Curr Proxy Conns; 'total_proxy'= Total Proxy Conns; 'connection_preface_rcvd'= Connection preface rcvd; 'control_frame'= Control Frame Rcvd; 'headers_frame'= HEADERS Frame Rcvd; 'continuation_frame'= CONTINUATION Frame Rcvd; 'rst_frame_rcvd'= RST_STREAM Frame Rcvd; 'settings_frame'= SETTINGS Frame Rcvd; 'window_update_frame'= WINDOW_UPDATE Frame Rcvd; 'ping_frame'= PING Frame Rcvd; 'goaway_frame'= GOAWAY Frame Rcvd; 'priority_frame'= PRIORITY Frame Rcvd; 'data_frame'= DATA Frame Recvd; 'unknown_frame'= Unknown Frame Recvd; 'connection_preface_sent'= Connection preface sent; 'settings_frame_sent'= SETTINGS Frame Sent; 'settings_ack_sent'= SETTINGS ACK Frame Sent; 'empty_settings_sent'= Empty SETTINGS Frame Sent; 'ping_frame_sent'= PING Frame Sent; 'window_update_frame_sent'= WINDOW_UPDATE Frame Sent; 'rst_frame_sent'= RST_STREAM Frame Sent; 'goaway_frame_sent'= GOAWAY Frame Sent; 'header_to_app'= HEADER Frame to HTTP; 'data_to_app'= DATA Frame to HTTP; 'protocol_error'= Protocol Error; 'internal_error'= Internal Error; 'proxy_alloc_error'= HTTP2 Proxy alloc Error; 'split_buff_fail'= Splitting Buffer Failed; 'invalid_frame_size'= Invalid Frame Size Rcvd; 'error_max_invalid_stream'= Max Invalid Stream Rcvd; 'data_no_stream'= DATA Frame Rcvd on non-existent stream; 'flow_control_error'= Flow Control Error; 'settings_timeout'= Settings Timeout; 'frame_size_error'= Frame Size Error; 'refused_stream'= Refused Stream; 'cancel'= cancel; 'compression_error'= compression error; 'connect_error'= connect error; 'enhance_your_calm'= enhance your calm error; 'inadequate_security'= inadequate security; 'http_1_1_required'= HTTP1.1 Required; 'deflate_alloc_fail'= deflate alloc fail; 'inflate_alloc_fail'= inflate alloc fail; 'inflate_header_fail'= Inflate Header Fail; 'bad_connection_preface'= Bad Connection Preface; 'cant_allocate_control_frame'= Cant allocate control frame; 'cant_allocate_settings_frame'= Cant allocate SETTINGS frame; 'bad_frame_type_for_stream_state'= Bad frame type for stream state; 'wrong_stream_state'= Wrong Stream State; 'data_queue_alloc_error'= Data Queue Alloc Error; 'buff_alloc_error'= Buff alloc error; 'cant_allocate_rst_frame'= Cant allocate RST_STREAM frame; 'cant_allocate_goaway_frame'= Cant allocate GOAWAY frame; 'cant_allocate_ping_frame'= Cant allocate PING frame; 'cant_allocate_stream'= Cant allocate stream; 'cant_allocate_window_frame'= Cant allocate WINDOW_UPDATE frame; 'header_no_stream'= header no stream; 'header_padlen_gt_frame_payload'= Header padlen greater than frame payload size; 'streams_gt_max_concur_streams'= Streams greater than max allowed concurrent streams; 'idle_state_unexpected_frame'= Unxpected frame received in idle state; 'reserved_local_state_unexpected_frame'= Unexpected frame received in reserved local state; 'reserved_remote_state_unexpected_frame'= Unexpected frame received in reserved remote state; 'half_closed_remote_state_unexpected_frame'= Unexpected frame received in half closed remote state; 'closed_state_unexpected_frame'= Unexpected frame received in closed state; 'zero_window_size_on_stream'= Window Update with zero increment rcvd; 'exceeds_max_window_size_stream'= Window Update with increment that results in exceeding max window; 'stream_closed'= stream closed; 'continuation_before_headers'= CONTINUATION frame with no headers frame; 'invalid_frame_during_headers'= frame before headers were complete; 'headers_after_continuation'= headers frame before CONTINUATION was complete; 'invalid_push_promise'= unexpected PUSH_PROMISE frame; 'invalid_stream_id'= received invalid stream ID; 'headers_interleaved'= headers interleaved on streams; 'trailers_no_end_stream'= trailers not marked as end-of-stream; 'invalid_setting_value'= invalid setting-frame value; 'invalid_window_update'= window-update value out of range; 'frame_header_bytes_received'= frame header bytes received; 'frame_header_bytes_sent'= frame header bytes sent; 'control_bytes_received'= HTTP/2 control frame bytes received; 'control_bytes_sent'= HTTP/2 control frame bytes sent; 'header_bytes_received'= HTTP/2 header bytes received; 'header_bytes_sent'= HTTP/2 header bytes sent; 'data_bytes_received'= HTTP/2 data bytes received; 'data_bytes_sent'= HTTP/2 data bytes sent; 'total_bytes_received'= HTTP/2 total bytes received; 'total_bytes_sent'= HTTP/2 total bytes sent; 'peak_proxy'= Peak Proxy Conns; 'control_frame_sent'= Control Frame Sent; 'continuation_frame_sent'= CONTINUATION Frame Sent; 'data_frame_sent'= DATA Frame Sent; 'headers_frame_sent'= HEADERS Frame Sent; 'priority_frame_sent'= PRIORITY Frame Sent; 'settings_ack_rcvd'= SETTINGS ACK Frame Rcvd; 'empty_settings_rcvd'= Empty SETTINGS Frame Rcvd; 'alloc_fail_total'= Alloc Fail - Total; 'err_rcvd_total'= Error Rcvd - Total; 'err_sent_total'= Error Rent - Total; 'err_sent_proto_err'= Error Sent - PROTOCOL_ERROR; 'err_sent_internal_err'= Error Sent - INTERNAL_ERROR; 'err_sent_flow_control'= Error Sent - FLOW_CONTROL_ERROR; 'err_sent_setting_timeout'= Error Sent - SETTINGS_TIMEOUT; 'err_sent_stream_closed'= Error Sent - STREAM_CLOSED; 'err_sent_frame_size_err'= Error Sent - FRAME_SIZE_ERROR; 'err_sent_refused_stream'= Error Sent - REFUSED_STREAM; 'err_sent_cancel'= Error Sent - CANCEL; 'err_sent_compression_err'= Error Sent - COMPRESSION_ERROR; 'err_sent_connect_err'= Error Sent - CONNECT_ERROR; 'err_sent_your_calm'= Error Sent - ENHANCE_YOUR_CALM; 'err_sent_inadequate_security'= Error Sent - INADEQUATE_SECURITY; 'err_sent_http11_required'= Error Sent - HTTP_1_1_REQUIRED;



  oper (False, any, None)
    Field oper


    cpu_count (optional, any, None)
      Field cpu_count


    http2_cpu_list (optional, any, None)
      Field http2_cpu_list



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    window_update_frame (optional, any, None)
      WINDOW_UPDATE Frame Rcvd


    err_sent_flow_control (optional, any, None)
      Error Sent - FLOW_CONTROL_ERROR


    inadequate_security (optional, any, None)
      inadequate security


    zero_window_size_on_stream (optional, any, None)
      Window Update with zero increment rcvd


    total_proxy (optional, any, None)
      Total Proxy Conns


    headers_frame (optional, any, None)
      HEADERS Frame Rcvd


    cant_allocate_ping_frame (optional, any, None)
      Cant allocate PING frame


    err_sent_inadequate_security (optional, any, None)
      Error Sent - INADEQUATE_SECURITY


    err_sent_frame_size_err (optional, any, None)
      Error Sent - FRAME_SIZE_ERROR


    control_frame_sent (optional, any, None)
      Control Frame Sent


    headers_after_continuation (optional, any, None)
      headers frame before CONTINUATION was complete


    invalid_window_update (optional, any, None)
      window-update value out of range


    goaway_frame (optional, any, None)
      GOAWAY Frame Rcvd


    window_update_frame_sent (optional, any, None)
      WINDOW_UPDATE Frame Sent


    rst_frame_sent (optional, any, None)
      RST_STREAM Frame Sent


    refused_stream (optional, any, None)
      Refused Stream


    invalid_frame_size (optional, any, None)
      Invalid Frame Size Rcvd


    header_no_stream (optional, any, None)
      header no stream


    control_frame (optional, any, None)
      Control Frame Rcvd


    settings_ack_rcvd (optional, any, None)
      SETTINGS ACK Frame Rcvd


    control_bytes_received (optional, any, None)
      HTTP/2 control frame bytes received


    err_sent_compression_err (optional, any, None)
      Error Sent - COMPRESSION_ERROR


    internal_error (optional, any, None)
      Internal Error


    data_no_stream (optional, any, None)
      DATA Frame Rcvd on non-existent stream


    rst_frame_rcvd (optional, any, None)
      RST_STREAM Frame Rcvd


    half_closed_remote_state_unexpected_frame (optional, any, None)
      Unexpected frame received in half closed remote state


    enhance_your_calm (optional, any, None)
      enhance your calm error


    reserved_local_state_unexpected_frame (optional, any, None)
      Unexpected frame received in reserved local state


    http_1_1_required (optional, any, None)
      HTTP1.1 Required


    data_queue_alloc_error (optional, any, None)
      Data Queue Alloc Error


    continuation_frame (optional, any, None)
      CONTINUATION Frame Rcvd


    cant_allocate_settings_frame (optional, any, None)
      Cant allocate SETTINGS frame


    continuation_frame_sent (optional, any, None)
      CONTINUATION Frame Sent


    empty_settings_sent (optional, any, None)
      Empty SETTINGS Frame Sent


    err_sent_cancel (optional, any, None)
      Error Sent - CANCEL


    connection_preface_sent (optional, any, None)
      Connection preface sent


    settings_frame (optional, any, None)
      SETTINGS Frame Rcvd


    err_rcvd_total (optional, any, None)
      Error Rcvd - Total


    inflate_header_fail (optional, any, None)
      Inflate Header Fail


    cant_allocate_window_frame (optional, any, None)
      Cant allocate WINDOW_UPDATE frame


    frame_header_bytes_sent (optional, any, None)
      frame header bytes sent


    streams_gt_max_concur_streams (optional, any, None)
      Streams greater than max allowed concurrent streams


    priority_frame (optional, any, None)
      PRIORITY Frame Rcvd


    bad_connection_preface (optional, any, None)
      Bad Connection Preface


    error_max_invalid_stream (optional, any, None)
      Max Invalid Stream Rcvd


    stream_closed (optional, any, None)
      stream closed


    header_padlen_gt_frame_payload (optional, any, None)
      Header padlen greater than frame payload size


    protocol_error (optional, any, None)
      Protocol Error


    data_to_app (optional, any, None)
      DATA Frame to HTTP


    split_buff_fail (optional, any, None)
      Splitting Buffer Failed


    invalid_stream_id (optional, any, None)
      received invalid stream ID


    cant_allocate_rst_frame (optional, any, None)
      Cant allocate RST_STREAM frame


    inflate_alloc_fail (optional, any, None)
      inflate alloc fail


    cancel (optional, any, None)
      cancel


    err_sent_connect_err (optional, any, None)
      Error Sent - CONNECT_ERROR


    err_sent_http11_required (optional, any, None)
      Error Sent - HTTP_1_1_REQUIRED


    cant_allocate_control_frame (optional, any, None)
      Cant allocate control frame


    err_sent_your_calm (optional, any, None)
      Error Sent - ENHANCE_YOUR_CALM


    flow_control_error (optional, any, None)
      Flow Control Error


    trailers_no_end_stream (optional, any, None)
      trailers not marked as end-of-stream


    wrong_stream_state (optional, any, None)
      Wrong Stream State


    invalid_push_promise (optional, any, None)
      unexpected PUSH_PROMISE frame


    idle_state_unexpected_frame (optional, any, None)
      Unxpected frame received in idle state


    frame_header_bytes_received (optional, any, None)
      frame header bytes received


    unknown_frame (optional, any, None)
      Unknown Frame Recvd


    ping_frame (optional, any, None)
      PING Frame Rcvd


    settings_ack_sent (optional, any, None)
      SETTINGS ACK Frame Sent


    data_bytes_sent (optional, any, None)
      HTTP/2 data bytes sent


    invalid_setting_value (optional, any, None)
      invalid setting-frame value


    header_to_app (optional, any, None)
      HEADER Frame to HTTP


    total_bytes_sent (optional, any, None)
      HTTP/2 total bytes sent


    control_bytes_sent (optional, any, None)
      HTTP/2 control frame bytes sent


    peak_proxy (optional, any, None)
      Peak Proxy Conns


    total_bytes_received (optional, any, None)
      HTTP/2 total bytes received


    header_bytes_received (optional, any, None)
      HTTP/2 header bytes received


    err_sent_setting_timeout (optional, any, None)
      Error Sent - SETTINGS_TIMEOUT


    ping_frame_sent (optional, any, None)
      PING Frame Sent


    data_bytes_received (optional, any, None)
      HTTP/2 data bytes received


    invalid_frame_during_headers (optional, any, None)
      frame before headers were complete


    reserved_remote_state_unexpected_frame (optional, any, None)
      Unexpected frame received in reserved remote state


    deflate_alloc_fail (optional, any, None)
      deflate alloc fail


    curr_proxy (optional, any, None)
      Curr Proxy Conns


    priority_frame_sent (optional, any, None)
      PRIORITY Frame Sent


    goaway_frame_sent (optional, any, None)
      GOAWAY Frame Sent


    header_bytes_sent (optional, any, None)
      HTTP/2 header bytes sent


    settings_frame_sent (optional, any, None)
      SETTINGS Frame Sent


    closed_state_unexpected_frame (optional, any, None)
      Unexpected frame received in closed state


    compression_error (optional, any, None)
      compression error


    exceeds_max_window_size_stream (optional, any, None)
      Window Update with increment that results in exceeding max window


    cant_allocate_stream (optional, any, None)
      Cant allocate stream


    data_frame (optional, any, None)
      DATA Frame Recvd


    settings_timeout (optional, any, None)
      Settings Timeout


    empty_settings_rcvd (optional, any, None)
      Empty SETTINGS Frame Rcvd


    err_sent_total (optional, any, None)
      Error Rent - Total


    continuation_before_headers (optional, any, None)
      CONTINUATION frame with no headers frame


    err_sent_stream_closed (optional, any, None)
      Error Sent - STREAM_CLOSED


    headers_frame_sent (optional, any, None)
      HEADERS Frame Sent


    bad_frame_type_for_stream_state (optional, any, None)
      Bad frame type for stream state


    err_sent_refused_stream (optional, any, None)
      Error Sent - REFUSED_STREAM


    frame_size_error (optional, any, None)
      Frame Size Error


    err_sent_internal_err (optional, any, None)
      Error Sent - INTERNAL_ERROR


    connect_error (optional, any, None)
      connect error


    data_frame_sent (optional, any, None)
      DATA Frame Sent


    alloc_fail_total (optional, any, None)
      Alloc Fail - Total


    connection_preface_rcvd (optional, any, None)
      Connection preface rcvd


    err_sent_proto_err (optional, any, None)
      Error Sent - PROTOCOL_ERROR


    proxy_alloc_error (optional, any, None)
      HTTP2 Proxy alloc Error


    cant_allocate_goaway_frame (optional, any, None)
      Cant allocate GOAWAY frame


    headers_interleaved (optional, any, None)
      headers interleaved on streams


    buff_alloc_error (optional, any, None)
      Buff alloc error



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

