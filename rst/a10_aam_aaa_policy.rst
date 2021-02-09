.. _a10_aam_aaa_policy_module:


a10_aam_aaa_policy -- Configures A10 aam.aaa-policy
===================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

AAM AAA policy configuration






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'req'= Request; 'req-reject'= Request Rejected; 'req-auth'= Request Matching Authentication Template; 'req-bypass'= Request Bypassed; 'req-skip'= Request Skipped; 'error'= Error; 'failure-bypass'= Auth Failure Bypass;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    req_bypass (optional, any, None)
      Request Bypassed


    req (optional, any, None)
      Request


    req_auth (optional, any, None)
      Request Matching Authentication Template


    failure_bypass (optional, any, None)
      Auth Failure Bypass


    aaa_rule_list (optional, any, None)
      Field aaa_rule_list


    error (optional, any, None)
      Error


    req_reject (optional, any, None)
      Request Rejected


    req_skip (optional, any, None)
      Request Skipped


    name (optional, any, None)
      Specify AAA policy name



  name (True, any, None)
    Specify AAA policy name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  aaa_rule_list (False, any, None)
    Field aaa_rule_list


    sampling_enable (optional, any, None)
      Field sampling_enable


    index (optional, any, None)
      Specify AAA rule index


    authorize_policy (optional, any, None)
      Specify authorization policy to bind to the AAA rule


    uuid (optional, any, None)
      uuid of the object


    authentication_template (optional, any, None)
      Specify authentication template name to bind to the AAA rule


    uri (optional, any, None)
      Field uri


    access_list (optional, any, None)
      Field access_list


    domain_name (optional, any, None)
      Specify domain name to bind to the AAA rule (ex= a10networks.com, www.a10networks.com)


    host (optional, any, None)
      Field host


    user_agent (optional, any, None)
      Field user_agent


    action (optional, any, None)
      'allow'= Allow traffic that matches this rule; 'deny'= Deny traffic that matches this rule;


    match_encoded_uri (optional, any, None)
      Enable URL decoding for URI matching


    auth_failure_bypass (optional, any, None)
      Forward client’s request even though authentication has failed


    user_tag (optional, any, None)
      Customized tag


    port (optional, any, None)
      Specify port number for aaa-rule, default is 0 for all port numbers



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

