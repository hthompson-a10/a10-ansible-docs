.. _a10_slb_template_http_module:


a10_slb_template_http -- Configures A10 slb.template.http
=========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

HTTP






Parameters
----------

  term_11client_hdr_conn_close (False, any, None)
    Terminate HTTP 1.1 client when req has Connection= close


  log_retry (False, any, None)
    log when HTTP request retry


  http_100_cont_wait_for_req_complete (False, any, None)
    When REQ has Expect 100 and response is not 100, then wait for whole request to be sent


  strict_transaction_switch (False, any, None)
    Force server selection on every HTTP request


  response_content_replace_list (False, any, None)
    Field response_content_replace_list


    response_new_string (optional, any, None)
      String will be in the http content


    response_content_replace (optional, any, None)
      replace the data from HTTP response content (String in the http content need to be replaced)



  failover_url (False, any, None)
    Failover to this URL (Failover URL Name)


  prefix (False, any, None)
    'host'= the cookie will have been set with a Secure attribute, a Path attribute with a value of /, and no Domain attribute; 'secure'= the cookie will have been set with a Secure attribute; 'check'= check server prefix and enforce prefix format;


  url_switching (False, any, None)
    Field url_switching


    url_switching_type (optional, any, None)
      'contains'= Select service group if URL string contains another string; 'ends- with'= Select service group if URL string ends with another string; 'equals'= Select service group if URL string equals another string; 'starts-with'= Select service group if URL string starts with another string; 'regex-match'= Select service group if URL string matches with regular expression; 'url-case- insensitive'= Case insensitive URL switching; 'url-hits-enable'= Enables URL Hits;


    url_service_group (optional, any, None)
      Create a Service Group comprising Servers (Service Group Name)


    url_match_string (optional, any, None)
      URL String



  compression_enable (False, any, None)
    Enable Compression


  redirect (False, any, None)
    Automatically send a redirect response


  url_hash_first (False, any, None)
    Use the begining part of URL to calculate hash value (URL string length to calculate hash value)


  host_switching (False, any, None)
    Field host_switching


    host_service_group (optional, any, None)
      Create a Service Group comprising Servers (Service Group Name)


    host_match_string (optional, any, None)
      Hostname String


    host_switching_type (optional, any, None)
      'contains'= Select service group if hostname contains another string; 'ends- with'= Select service group if hostname ends with another string; 'equals'= Select service group if hostname equals another string; 'starts-with'= Select service group if hostname starts with another string; 'regex-match'= Select service group if URL string matches with regular expression; 'host-hits- enable'= Enables Host Hits counters;



  persist_on_401 (False, any, None)
    Persist to the same server if the response code is 401


  rd_simple_loc (False, any, None)
    Redirect location tag absolute URI string


  client_port_hdr_replace (False, any, None)
    Replace the existing header


  response_header_erase_list (False, any, None)
    Field response_header_erase_list


    response_header_erase (optional, any, None)
      Erase a header from HTTP response (Header Name)



  insert_client_ip (False, any, None)
    Insert Client IP address into HTTP header


  rd_secure (False, any, None)
    Use HTTPS


  compression_keep_accept_encoding (False, any, None)
    Keep accept encoding


  req_hdr_wait_time (False, any, None)
    HTTP request header wait time before abort connection


  keep_client_alive (False, any, None)
    Keep client alive


  compression_minimum_content_length (False, any, None)
    Minimum Content Length (Minimum content length for compression in bytes. Default is 120.)


  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    HTTP Template Name


  request_header_insert_list (False, any, None)
    Field request_header_insert_list


    request_header_insert_type (optional, any, None)
      'insert-if-not-exist'= Only insert the header when it does not exist; 'insert- always'= Always insert the header even when there is a header with the same name;


    request_header_insert (optional, any, None)
      Insert a header into HTTP request (Header Content (Format= '[name]=[value]'))



  request_line_case_insensitive (False, any, None)
    Parse http request line as case insensitive


  redirect_rewrite (False, any, None)
    Field redirect_rewrite


    match_list (optional, any, None)
      Field match_list


    redirect_secure_port (optional, any, None)
      Port (Port Number)


    redirect_secure (optional, any, None)
      Use HTTPS



  url_hash_last (False, any, None)
    Use the end part of URL to calculate hash value (URL string length to calculate hash value)


  frame_limit (False, any, None)
    Limit the number of CONTINUATION, PING, PRIORITY, RESET, SETTINGS and empty frames in one HTTP2 connection, default 10000


  ansible_username (True, any, None)
    Username for AXAPI authentication


  req_hdr_wait_time_val (False, any, None)
    Number of seconds wait for client request header (default is 7)


  retry_on_5xx_per_req_val (False, any, None)
    Number of times to retry (default is 3)


  response_header_insert_list (False, any, None)
    Field response_header_insert_list


    response_header_insert (optional, any, None)
      Insert a header into HTTP response (Header Content (Format= '[name]=[value]'))


    response_header_insert_type (optional, any, None)
      'insert-if-not-exist'= Only insert the header when it does not exist; 'insert- always'= Always insert the header even when there is a header with the same name;



  compression_keep_accept_encoding_enable (False, any, None)
    Enable Server Accept Encoding


  retry_on_5xx_val (False, any, None)
    Number of times to retry (default is 3)


  retry_on_5xx_per_req (False, any, None)
    Retry http request on HTTP 5xx code for each request


  compression_content_type (False, any, None)
    Field compression_content_type


    content_type (optional, any, None)
      Compression content-type



  retry_on_5xx (False, any, None)
    Retry http request on HTTP 5xx code and request timeout


  use_server_status (False, any, None)
    Use Server-Status header to do URL hashing


  rd_resp_code (False, any, None)
    '301'= Moved Permanently; '302'= Found; '303'= See Other; '307'= Temporary Redirect;


  state (True, any, None)
    State of the object to be created.


  template (False, any, None)
    Field template


    logging (optional, any, None)
      Logging template (Logging Config name)



  client_ip_hdr_replace (False, any, None)
    Replace the existing header


  compression_level (False, any, None)
    compression level, default 1 (compression level value, default is 1)


  non_http_bypass (False, any, None)
    Bypass non-http traffic instead of dropping


  compression_exclude_content_type (False, any, None)
    Field compression_exclude_content_type


    exclude_content_type (optional, any, None)
      Compression exclude content-type (Compression exclude content type)



  request_timeout (False, any, None)
    Request timeout if response not received (timeout in seconds)


  url_hash_persist (False, any, None)
    Use URL's hash value to select server


  compression_auto_disable_on_high_cpu (False, any, None)
    Auto-disable software compression on high cpu usage (Disable compression if cpu usage is above threshold. Default is off.)


  insert_client_port (False, any, None)
    Insert Client Port address into HTTP header


  insert_client_ip_header_name (False, any, None)
    HTTP Header Name for inserting Client IP


  compression_exclude_uri (False, any, None)
    Field compression_exclude_uri


    exclude_uri (optional, any, None)
      Compression exclude uri



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  rd_port (False, any, None)
    Port (Port Number)


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  cookie_format (False, any, None)
    'rfc6265'= Follow rfc6265;


  ansible_password (True, any, None)
    Password for AXAPI authentication


  url_hash_offset (False, any, None)
    Skip part of URL to calculate hash value (Offset of the URL string)


  request_header_erase_list (False, any, None)
    Field request_header_erase_list


    request_header_erase (optional, any, None)
      Erase a header from HTTP request (Header Name)



  bypass_sg (False, any, None)
    Select service group for non-http traffic (Service Group Name)


  cookie_samesite (False, any, None)
    'none'= none; 'lax'= lax; 'strict'= strict;


  max_concurrent_streams (False, any, None)
    (http2 only) Max concurrent streams, default 100


  insert_client_port_header_name (False, any, None)
    HTTP Header Name for inserting Client Port


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

