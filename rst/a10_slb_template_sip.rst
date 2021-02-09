.. _a10_slb_template_sip_module:


a10_slb_template_sip -- Configures A10 slb.template.sip
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

SIP Template






Parameters
----------

  alg_source_nat (False, any, None)
    Translate source IP to NAT IP in SIP message when source NAT is used


  smp_call_id_rtp_session (False, any, None)
    Create the across cpu call-id rtp session


  failed_client_selection_message (False, any, None)
    Send SIP message (includs status code) to server when select client fail(Format= 3 digits(1XX~6XX) space reason)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  acl_id (False, any, None)
    ACL id


  failed_server_selection (False, any, None)
    Define action when select server fail


  alg_dest_nat (False, any, None)
    Translate VIP to real server IP in SIP message when destination NAT is used


  drop_when_client_fail (False, any, None)
    Drop current SIP message when select client fail


  service_group (False, any, None)
    service group name


  client_response_header (False, any, None)
    Field client_response_header


    client_response_header_erase (optional, any, None)
      Erase a SIP header (Header Name)


    client_response_header_insert (optional, any, None)
      Insert a SIP header (Header Content (Format= 'name=value'))


    client_response_erase_all (optional, any, None)
      Erase all headers


    insert_condition_client_response (optional, any, None)
      'insert-if-not-exist'= Only insert the header when it does not exist; 'insert- always'= Always insert the header even when there is a header with the same name;



  uuid (False, any, None)
    uuid of the object


  failed_server_selection_message (False, any, None)
    Send SIP message (includs status code) to client when select server fail(Format= 3 digits(1XX~6XX) space reason)


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  server_keep_alive (False, any, None)
    Send server keep-alive packet for every persist connection when enable conn- reuse


  call_id_persist_disable (False, any, None)
    Disable call-ID persistence


  dialog_aware (False, any, None)
    Permit system processes dialog session


  drop_when_server_fail (False, any, None)
    Drop current SIP message when select server fail


  server_selection_per_request (False, any, None)
    Force server selection on every SIP request


  pstn_gw (False, any, None)
    configure pstn gw host name for tel= uri translate to sip= uri (Hostname String, default is 'pstn')


  client_keep_alive (False, any, None)
    Respond client keep-alive packet directly instead of forwarding to server


  acl_name_value (False, any, None)
    IPv4 Access List Name


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  insert_client_ip (False, any, None)
    Insert Client IP address into SIP header


  name (True, any, None)
    SIP Template Name


  exclude_translation (False, any, None)
    Field exclude_translation


    header_string (optional, any, None)
      SIP header name


    translation_value (optional, any, None)
      'start-line'= SIP request line or status line; 'header'= SIP message headers; 'body'= SIP message body;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  client_request_header (False, any, None)
    Field client_request_header


    insert_condition_client_request (optional, any, None)
      'insert-if-not-exist'= Only insert the header when it does not exist; 'insert- always'= Always insert the header even when there is a header with the same name;


    client_request_header_erase (optional, any, None)
      Erase a SIP header (Header Name)


    client_request_erase_all (optional, any, None)
      Erase all headers


    client_request_header_insert (optional, any, None)
      Insert a SIP header (Header Content (Format= 'name=value'))



  server_response_header (False, any, None)
    Field server_response_header


    server_response_header_erase (optional, any, None)
      Erase a SIP header (Header Name)


    server_response_erase_all (optional, any, None)
      Erase all headers


    server_response_header_insert (optional, any, None)
      Insert a SIP header (Header Content (Format= 'name=value'))


    insert_condition_server_response (optional, any, None)
      'insert-if-not-exist'= Only insert the header when it does not exist; 'insert- always'= Always insert the header even when there is a header with the same name;



  failed_client_selection (False, any, None)
    Define action when select client fail


  ansible_password (True, any, None)
    Password for AXAPI authentication


  interval (False, any, None)
    The interval of keep-alive packet for each persist connection (second)


  keep_server_ip_if_match_acl (False, any, None)
    Use Real Server IP for addresses matching the ACL for a Call-Id


  timeout (False, any, None)
    Time in minutes


  user_tag (False, any, None)
    Customized tag


  server_request_header (False, any, None)
    Field server_request_header


    server_request_erase_all (optional, any, None)
      Erase all headers


    server_request_header_insert (optional, any, None)
      Insert a SIP header (Header Content (Format= 'name=value'))


    insert_condition_server_request (optional, any, None)
      'insert-if-not-exist'= Only insert the header when it does not exist; 'insert- always'= Always insert the header even when there is a header with the same name;


    server_request_header_erase (optional, any, None)
      Erase a SIP header (Header Name)










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

