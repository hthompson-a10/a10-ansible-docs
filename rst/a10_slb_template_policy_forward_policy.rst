.. _a10_slb_template_policy_forward_policy_module:


a10_slb_template_policy_forward_policy -- Configures A10 slb.template.policy.forward-policy
===========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Forward Policy commands






Parameters
----------

  filtering (False, any, None)
    Field filtering


    ssli_url_filtering (optional, any, None)
      'bypassed-sni-disable'= Disable SNI filtering for bypassed URL's(enabled by default); 'intercepted-sni-enable'= Enable SNI filtering for intercepted URL's(disabled by default); 'intercepted-http-disable'= Disable HTTP(host/URL) filtering for intercepted URL's(enabled by default); 'no-sni-allow'= Allow connection if SNI filtering is enabled and SNI header is not present(Drop by default);



  source_list (False, any, None)
    Field source_list


    sampling_enable (optional, any, None)
      Field sampling_enable


    uuid (optional, any, None)
      uuid of the object


    match_authorize_policy (optional, any, None)
      Authorize-policy for user and group based policy


    destination (optional, any, None)
      Field destination


    match_class_list (optional, any, None)
      Class List Name


    priority (optional, any, None)
      Priority of the source(higher the number higher the priority, default 0)


    user_tag (optional, any, None)
      Customized tag


    match_any (optional, any, None)
      Match any source


    name (optional, any, None)
      source destination match rule name



  action_list (False, any, None)
    Field action_list


    sampling_enable (optional, any, None)
      Field sampling_enable


    fake_sg (optional, any, None)
      service group to forward the packets to Internet


    name (optional, any, None)
      Action policy name


    drop_response_code (optional, any, None)
      Specify response code for drop action


    drop_redirect_url (optional, any, None)
      Specify URL to which client request is redirected upon being dropped


    drop_message (optional, any, None)
      drop-message sent to the client as webpage(html tags are included and quotation marks are required for white spaces)


    action1 (optional, any, None)
      'forward-to-internet'= Forward request to Internet; 'forward-to-service-group'= Forward request to service group; 'forward-to-proxy'= Forward request to HTTP proxy server; 'drop'= Drop request;


    forward_snat (optional, any, None)
      Source NAT pool or pool group


    http_status_code (optional, any, None)
      '301'= Moved permanently; '302'= Found;


    fall_back_snat (optional, any, None)
      Source NAT pool or pool group for fallback server


    fall_back (optional, any, None)
      Fallback service group for Internet


    log (optional, any, None)
      enable logging


    user_tag (optional, any, None)
      Customized tag


    real_sg (optional, any, None)
      service group to forward the packets


    uuid (optional, any, None)
      uuid of the object



  ansible_username (True, any, None)
    Username for AXAPI authentication


  local_logging (False, any, None)
    Enable local logging


  policy_name (optional, any, None)
    Key to identify parent object


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  acos_event_log (False, any, None)
    Enable acos event logging


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  state (True, any, None)
    State of the object to be created.


  no_client_conn_reuse (False, any, None)
    Inspects only first request of a connection


  san_filtering (False, any, None)
    Field san_filtering


    ssli_url_filtering_san (optional, any, None)
      'enable-san'= Enable SAN filtering(disabled by default); 'bypassed-san- disable'= Disable SAN filtering for bypassed URL's(enabled by default); 'intercepted-san-enable'= Enable SAN filtering for intercepted URL's(disabled by default); 'no-san-allow'= Allow connection if SAN filtering is enabled and SAN field is not present(Drop by default);



  require_web_category (False, any, None)
    Wait for web category to be resolved before taking proxy decision


  ansible_password (True, any, None)
    Password for AXAPI authentication









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

