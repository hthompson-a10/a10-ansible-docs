.. _a10_aam_aaa_policy_aaa_rule_module:


a10_aam_aaa_policy_aaa_rule -- Configures A10 aam.aaa.policy.aaa-rule
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Rules of AAA policy






Parameters
----------

  authorize_policy (False, any, None)
    Specify authorization policy to bind to the AAA rule


  ansible_username (True, any, None)
    Username for AXAPI authentication


  authentication_template (False, any, None)
    Specify authentication template name to bind to the AAA rule


  uri (False, any, None)
    Field uri


    match_type (optional, any, None)
      'contains'= Match URI if request URI contains specified URI; 'ends-with'= Match URI if request URI ends with specified URI; 'equals'= Match URI if request URI equals specified URI; 'starts-with'= Match URI if request URI starts with specified URI;


    uri_str (optional, any, None)
      Specify URI string



  host (False, any, None)
    Field host


    host_match_type (optional, any, None)
      'contains'= Match HOST if request HTTP HOST header contains specified hostname; 'ends-with'= Match HOST if request HTTP HOST header ends with specified hostname; 'equals'= Match HOST if request HTTP HOST header equals specified hostname; 'starts-with'= Match HOST if request HTTP HOST header starts with specified hostname;


    host_str (optional, any, None)
      Specify URI string



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  match_encoded_uri (False, any, None)
    Enable URL decoding for URI matching


  a10_partition (False, any, None)
    Destination/target partition for object/command


  port (False, any, None)
    Specify port number for aaa-rule, default is 0 for all port numbers


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'total_count'= total_count; 'hit_deny'= hit_deny; 'hit_auth'= hit_auth; 'hit_bypass'= hit_bypass; 'failure_bypass'= failure_bypass;



  index (True, any, None)
    Specify AAA rule index


  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    index (optional, any, None)
      Specify AAA rule index


    hit_auth (optional, any, None)
      Field hit_auth


    hit_bypass (optional, any, None)
      Field hit_bypass


    total_count (optional, any, None)
      Field total_count


    hit_deny (optional, any, None)
      Field hit_deny


    failure_bypass (optional, any, None)
      Field failure_bypass



  uuid (False, any, None)
    uuid of the object


  ansible_password (True, any, None)
    Password for AXAPI authentication


  domain_name (False, any, None)
    Specify domain name to bind to the AAA rule (ex= a10networks.com, www.a10networks.com)


  access_list (False, any, None)
    Field access_list


    acl_id (optional, any, None)
      ACL id


    name (optional, any, None)
      Specify Named Access List


    acl_name (optional, any, None)
      'ip-name'= Apply an IP named access list; 'ipv6-name'= Apply an IPv6 named access list;



  auth_failure_bypass (False, any, None)
    Forward client’s request even though authentication has failed


  state (True, any, None)
    State of the object to be created.


  user_agent (False, any, None)
    Field user_agent


    user_agent_match_type (optional, any, None)
      'contains'= Match request User-Agent header if it contains specified string; 'ends-with'= Match request User-Agent header if it ends with specified string; 'equals'= Match request User-Agent header if it equals specified string; 'starts-with'= Match request User-Agent header if it starts with specified string;


    user_agent_str (optional, any, None)
      Specify request User-Agent string



  action (False, any, None)
    'allow'= Allow traffic that matches this rule; 'deny'= Deny traffic that matches this rule;


  ansible_host (True, any, None)
    Host for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  aaa_policy_name (optional, any, None)
    Key to identify parent object









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

