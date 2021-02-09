.. _a10_slb_template_reqmod_icap_module:


a10_slb_template_reqmod_icap -- Configures A10 slb.template.reqmod-icap
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

REQMOD ICAP template






Parameters
----------

  tcp_proxy (False, any, None)
    TCP Proxy Template Name


  disable_http_server_reset (False, any, None)
    Don't reset http server


  shared_partition_tcp_proxy_template (False, any, None)
    Reference a TCP Proxy template from shared partition


  name (True, any, None)
    Reqmod ICAP Template Name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  source_ip (False, any, None)
    Source IP persistence template (Source IP persistence template name)


  ansible_password (True, any, None)
    Password for AXAPI authentication


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  x_auth_url (False, any, None)
    Use URL format for authentication


  template_persist_source_ip_shared (False, any, None)
    Source IP Persistence Template Name


  template_tcp_proxy_shared (False, any, None)
    TCP Proxy Template name


  ansible_host (True, any, None)
    Host for AXAPI authentication


  include_protocol_in_uri (False, any, None)
    Include protocol and port in HTTP URI


  service_group (False, any, None)
    Bind a Service Group to the template (Service Group Name)


  log_only_allowed_method (False, any, None)
    Only log allowed HTTP method


  ansible_port (True, any, None)
    Port for AXAPI authentication


  logging (False, any, None)
    logging template (Logging template name)


  uuid (False, any, None)
    uuid of the object


  a10_partition (False, any, None)
    Destination/target partition for object/command


  bypass_ip_cfg (False, any, None)
    Field bypass_ip_cfg


    mask (optional, any, None)
      IP prefix mask


    bypass_ip (optional, any, None)
      ip address to bypass reqmod-icap service



  server_ssl (False, any, None)
    Server SSL template (Server SSL template name)


  state (True, any, None)
    State of the object to be created.


  fail_close (False, any, None)
    When template sg is down mark vport down


  cylance (False, any, None)
    cylance external server


  service_url (False, any, None)
    URL to send to ICAP server (Service URL Name)


  shared_partition_persist_source_ip_template (False, any, None)
    Reference a persist source ip template from shared partition


  action (False, any, None)
    'continue'= Continue; 'drop'= Drop; 'reset'= Reset;


  min_payload_size (False, any, None)
    min-payload-size value 0 - 65535, default is 0


  preview (False, any, None)
    Preview value 1 - 32768, default is 32768


  allowed_http_methods (False, any, None)
    List of allowed HTTP methods. Default is 'Allow All'. (List of HTTP methods allowed (default 'Allow All'))


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

