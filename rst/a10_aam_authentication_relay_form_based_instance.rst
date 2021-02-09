.. _a10_aam_authentication_relay_form_based_instance_module:


a10_aam_authentication_relay_form_based_instance -- Configures A10 aam.authentication.relay.form.based.instance
===============================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Form-based Authentication Relay






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'request'= Request; 'invalid_srv_rsp'= Invalid Server Response; 'post_fail'= POST Failed; 'invalid_cred'= Invalid Credential; 'bad_req'= Bad Request; 'not_fnd'= Not Found; 'error'= Internal Server Error; 'other_error'= Other Error;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    invalid_cred (optional, any, None)
      Invalid Credential


    bad_req (optional, any, None)
      Bad Request


    name (optional, any, None)
      Specify form-based authentication relay name


    other_error (optional, any, None)
      Other Error


    request (optional, any, None)
      Request


    invalid_srv_rsp (optional, any, None)
      Invalid Server Response


    post_fail (optional, any, None)
      POST Failed


    error (optional, any, None)
      Internal Server Error


    not_fnd (optional, any, None)
      Not Found



  name (True, any, None)
    Specify form-based authentication relay name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  request_uri_list (False, any, None)
    Field request_uri_list


    match_type (optional, any, None)
      'equals'= URI exactly matches the string; 'contains'= URI string contains another sub string; 'starts-with'= URI string starts with sub string; 'ends- with'= URI string ends with sub string;


    uuid (optional, any, None)
      uuid of the object


    other_variables (optional, any, None)
      Specify other variables (n1=v1&n2=v2) in form relay


    user_variable (optional, any, None)
      Specify username variable name


    uri (optional, any, None)
      Specify request URI


    password_variable (optional, any, None)
      Specify password variable name


    domain_variable (optional, any, None)
      Specify domain variable name


    action_uri (optional, any, None)
      Specify the action-URI


    cookie (optional, any, None)
      Field cookie


    user_tag (optional, any, None)
      Customized tag


    max_packet_collect_size (optional, any, None)
      Specify the max packet collection size in bytes, default is 1MB



  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uuid (False, any, None)
    uuid of the object









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

