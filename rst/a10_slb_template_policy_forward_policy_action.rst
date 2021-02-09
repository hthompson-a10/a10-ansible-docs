.. _a10_slb_template_policy_forward_policy_action_module:


a10_slb_template_policy_forward_policy_action -- Configures A10 slb.template.policy.forward.policy.action
=========================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

action list






Parameters
----------

  ansible_username (True, any, None)
    Username for AXAPI authentication


  drop_redirect_url (False, any, None)
    Specify URL to which client request is redirected upon being dropped


  drop_message (False, any, None)
    drop-message sent to the client as webpage(html tags are included and quotation marks are required for white spaces)


  action1 (False, any, None)
    'forward-to-internet'= Forward request to Internet; 'forward-to-service-group'= Forward request to service group; 'forward-to-proxy'= Forward request to HTTP proxy server; 'drop'= Drop request;


  forward_snat (False, any, None)
    Source NAT pool or pool group


  policy_name (optional, any, None)
    Key to identify parent object


  fall_back_snat (False, any, None)
    Source NAT pool or pool group for fallback server


  fall_back (False, any, None)
    Fallback service group for Internet


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  http_status_code (False, any, None)
    '301'= Moved permanently; '302'= Found;


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  log (False, any, None)
    enable logging


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'hits'= Number of requests matching this destination rule;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  fake_sg (False, any, None)
    service group to forward the packets to Internet


  stats (False, any, None)
    Field stats


    hits (optional, any, None)
      Number of requests matching this destination rule


    name (optional, any, None)
      Action policy name



  uuid (False, any, None)
    uuid of the object


  user_tag (False, any, None)
    Customized tag


  drop_response_code (False, any, None)
    Specify response code for drop action


  name (True, any, None)
    Action policy name


  state (True, any, None)
    State of the object to be created.


  ansible_password (True, any, None)
    Password for AXAPI authentication


  real_sg (False, any, None)
    service group to forward the packets









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

