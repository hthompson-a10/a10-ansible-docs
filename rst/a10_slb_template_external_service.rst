.. _a10_slb_template_external_service_module:


a10_slb_template_external_service -- Configures A10 slb.template.external-service
=================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

External service template






Parameters
----------

  failure_action (False, any, None)
    'continue'= Continue; 'drop'= Drop; 'reset'= Reset;


  shared_partition_tcp_proxy_template (False, any, None)
    Reference a TCP Proxy template from shared partition


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ntype (False, any, None)
    'skyfire-icap'= Skyfire ICAP service; 'url-filter'= URL filtering service;


  ansible_password (True, any, None)
    Password for AXAPI authentication


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  template_persist_source_ip_shared (False, any, None)
    Source IP Persistence Template Name


  template_tcp_proxy_shared (False, any, None)
    TCP Proxy Template name


  ansible_host (True, any, None)
    Host for AXAPI authentication


  name (True, any, None)
    External Service Template Name


  service_group (False, any, None)
    Bind a Service Group to the template (Service Group Name)


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  a10_partition (False, any, None)
    Destination/target partition for object/command


  bypass_ip_cfg (False, any, None)
    Field bypass_ip_cfg


    mask (optional, any, None)
      IP prefix mask


    bypass_ip (optional, any, None)
      ip address to bypass external service



  source_ip (False, any, None)
    Source IP persistence template (Source IP persistence template name)


  user_tag (False, any, None)
    Customized tag


  request_header_forward_list (False, any, None)
    Field request_header_forward_list


    request_header_forward (optional, any, None)
      Request header to be forwarded to external service (Header Name)



  state (True, any, None)
    State of the object to be created.


  shared_partition_persist_source_ip_template (False, any, None)
    Reference a persist source ip template from shared partition


  timeout (False, any, None)
    Timeout value 1 - 200 in units of 200ms, default is 5 (default is 1000ms) (1 - 200 in units of 200ms, default is 5 (1000ms))


  action (False, any, None)
    'continue'= Continue; 'drop'= Drop; 'reset'= Reset;


  tcp_proxy (False, any, None)
    TCP Proxy Template Name









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

