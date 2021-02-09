.. _a10_slb_template_policy_module:


a10_slb_template_policy -- Configures A10 slb.template.policy
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Policy config






Parameters
----------

  over_limit_logging (False, any, None)
    Log a message


  ansible_username (True, any, None)
    Username for AXAPI authentication


  over_limit_reset (False, any, None)
    Reset the connection when it exceeds limit


  share (False, any, None)
    Share counters between virtual ports and virtual servers


  ansible_password (True, any, None)
    Password for AXAPI authentication


  bw_list_id (False, any, None)
    Field bw_list_id


    service_group (optional, any, None)
      Specify a service group (Specify the service group name)


    pbslb_logging (optional, any, None)
      Configure PBSLB logging


    action_interval (optional, any, None)
      Specify logging interval in minute (default is 3)


    logging_drp_rst (optional, any, None)
      Configure PBSLB logging


    bw_list_action (optional, any, None)
      'drop'= drop the packet; 'reset'= Send reset back;


    fail (optional, any, None)
      Only log unsuccessful connections


    pbslb_interval (optional, any, None)
      Specify logging interval in minutes


    id (optional, any, None)
      Specify id that maps to service group (The id number)



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  stats (False, any, None)
    Field stats


    exp_client_hello_not_found (optional, any, None)
      Expected Client HELLO requests not found


    name (optional, any, None)
      Policy template name


    forward_policy (optional, any, None)
      Field forward_policy


    fwd_policy_dns_outstanding (optional, any, None)
      Forward-policy current DNS outstanding requests


    fwd_policy_forward_to_proxy (optional, any, None)
      Number of forward-policy requests forwarded to proxy


    fwd_policy_source_match_not_found (optional, any, None)
      Forward-policy requests without matching source rule


    fwd_policy_forward_to_service_group (optional, any, None)
      Number of forward-policy requests forwarded to service group


    fwd_policy_forward_to_internet (optional, any, None)
      Number of forward-policy requests forwarded to internet


    fwd_policy_hits (optional, any, None)
      Number of forward-policy requests for this policy template


    fwd_policy_snat_fail (optional, any, None)
      Forward-policy source-nat translation failure


    fwd_policy_dns_unresolved (optional, any, None)
      Forward-policy unresolved DNS queries


    fwd_policy_policy_drop (optional, any, None)
      Number of forward-policy requests dropped



  bw_list_name (False, any, None)
    Specify a blacklist/whitelist name


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  name (True, any, None)
    Policy template name


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'fwd-policy-dns-unresolved'= Forward-policy unresolved DNS queries; 'fwd-policy-dns-outstanding'= Forward-policy current DNS outstanding requests; 'fwd-policy-snat-fail'= Forward-policy source-nat translation failure; 'fwd- policy-hits'= Number of forward-policy requests for this policy template; 'fwd- policy-forward-to-internet'= Number of forward-policy requests forwarded to internet; 'fwd-policy-forward-to-service-group'= Number of forward-policy requests forwarded to service group; 'fwd-policy-forward-to-proxy'= Number of forward-policy requests forwarded to proxy; 'fwd-policy-policy-drop'= Number of forward-policy requests dropped; 'fwd-policy-source-match-not-found'= Forward- policy requests without matching source rule; 'exp-client-hello-not-found'= Expected Client HELLO requests not found;



  over_limit_lockup (False, any, None)
    Don't accept any new connection for certain time (Lockup duration (minute))


  ansible_port (True, any, None)
    Port for AXAPI authentication


  over_limit (False, any, None)
    Specify operation in case over limit


  uuid (False, any, None)
    uuid of the object


  forward_policy (False, any, None)
    Field forward_policy


    local_logging (optional, any, None)
      Enable local logging


    filtering (optional, any, None)
      Field filtering


    uuid (optional, any, None)
      uuid of the object


    action_list (optional, any, None)
      Field action_list


    no_client_conn_reuse (optional, any, None)
      Inspects only first request of a connection


    san_filtering (optional, any, None)
      Field san_filtering


    require_web_category (optional, any, None)
      Wait for web category to be resolved before taking proxy decision


    acos_event_log (optional, any, None)
      Enable acos event logging


    source_list (optional, any, None)
      Field source_list



  full_domain_tree (False, any, None)
    Share counters between geo-location and sub regions


  use_destination_ip (False, any, None)
    Use destination IP to match the policy


  interval (False, any, None)
    Log interval (minute)


  overlap (False, any, None)
    Use overlap mode for geo-location to do longest match


  class_list (False, any, None)
    Field class_list


    client_ip_l3_dest (optional, any, None)
      Use destination IP as client IP address


    lid_list (optional, any, None)
      Field lid_list


    client_ip_l7_header (optional, any, None)
      Use extract client IP address from L7 header


    uuid (optional, any, None)
      uuid of the object


    header_name (optional, any, None)
      Specify L7 header name


    name (optional, any, None)
      Class list name or geo-location-class-list name



  state (True, any, None)
    State of the object to be created.


  timeout (False, any, None)
    Define timeout value of PBSLB dynamic entry (Timeout value (minute, default is 5))


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

