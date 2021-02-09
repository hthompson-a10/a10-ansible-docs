.. _a10_slb_generic_proxy_module:


a10_slb_generic_proxy -- Configures A10 slb.generic-proxy
=========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure Generic Proxy






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'num'= Number; 'curr'= Current; 'total'= Total; 'svrsel_fail'= Number of server selection failed; 'no_route'= Number of no routes; 'snat_fail'= Number of snat failures; 'client_fail'= Number of client failures; 'server_fail'= Number of server failures; 'no_sess'= Number of no sessions; 'user_session'= Number of user sessions; 'acr_out'= Number of ACRs out; 'acr_in'= Number of ACRs in; 'aca_out'= Number of ACAs out; 'aca_in'= Number of ACAs in; 'cea_out'= Number of CEAs out; 'cea_in'= Number of CEAs in; 'cer_out'= Number of CERs out; 'cer_in'= Number of CERs in; 'dwr_out'= Number of DWRs out; 'dwr_in'= Number of DWRs in; 'dwa_out'= Number of DWAs out; 'dwa_in'= Number of DWAs in; 'str_out'= Number of STRs out; 'str_in'= Number of STRs in; 'sta_out'= Number of STAs out; 'sta_in'= Number of STAs in; 'asr_out'= Number of ASRs out; 'asr_in'= Number of ASRs in; 'asa_out'= Number of ASAs out; 'asa_in'= Number of ASAs in; 'other_out'= Number of other messages out; 'other_in'= Number of other messages in; 'total_http_req_enter_gen'= Total number of HTTP requests enter generic proxy; 'mismatch_fwd_id'= Diameter mismatch fwd session id; 'mismatch_rev_id'= Diameter mismatch rev session id; 'unkwn_cmd_code'= Diameter unkown cmd code; 'no_session_id'= Diameter no session id avp; 'no_fwd_tuple'= Diameter no fwd tuple matched; 'no_rev_tuple'= Diameter no rev tuple matched; 'dcmsg_fwd_in'= Diameter cross cpu fwd in; 'dcmsg_fwd_out'= Diameter cross cpu fwd out; 'dcmsg_rev_in'= Diameter cross cpu rev in; 'dcmsg_rev_out'= Diameter cross cpu rev out; 'dcmsg_error'= Diameter cross cpu error; 'retry_client_request'= Diameter retry client request; 'retry_client_request_fail'= Diameter retry client request fail; 'reply_unknown_session_id'= Reply with unknown session ID error info; 'ccr_out'= Number of CCRs out; 'ccr_in'= Number of CCRs in; 'cca_out'= Number of CCAs out; 'cca_in'= Number of CCAs in; 'ccr_i'= Number of CCRs initial; 'ccr_u'= Number of CCRs update; 'ccr_t'= Number of CCRs terminate; 'cca_t'= Number of CCAs terminate; 'terminate_on_cca_t'= Diameter terminate on cca_t; 'forward_unknown_session_id'= Forward server side message with unknown session id; 'update_latest_server'= Update to the latest server that used a session id; 'client_select_fail'= Fail to select client; 'close_conn_when_vport_down'= Close client conn when virtual port is down; 'invalid_avp'= AVP value contains illegal chars; 'reselect_fwd_tuple'= Original client tuple does not exist so reselect another one; 'reselect_fwd_tuple_other_cpu'= Original client tuple does not exist so reselect another one on other CPUs; 'reselect_rev_tuple'= Original server tuple does not exist so reselect another one; 'conn_closed_by_client'= Client initiates TCP close/reset; 'conn_closed_by_server'= Server initiates TCP close/reset; 'reply_invalid_avp_value'= Reply with invalid AVP error info; 'reply_unable_to_deliver'= Reply with unable to deliver error info; 'reply_error_info_fail'= Fail to reply error info to peer; 'dpr_out'= Number of DPRs out; 'dpr_in'= Number of DPRs in; 'dpa_out'= Number of DPAs out; 'dpa_in'= Number of DPAs in;



  oper (False, any, None)
    Field oper


    l4_cpu_list (optional, any, None)
      Field l4_cpu_list


    cpu_count (optional, any, None)
      Field cpu_count



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    no_route (optional, any, None)
      Number of no routes


    server_fail (optional, any, None)
      Number of server failures


    user_session (optional, any, None)
      Number of user sessions


    dcmsg_fwd_in (optional, any, None)
      Diameter cross cpu fwd in


    str_out (optional, any, None)
      Number of STRs out


    dwa_in (optional, any, None)
      Number of DWAs in


    client_select_fail (optional, any, None)
      Fail to select client


    asa_in (optional, any, None)
      Number of ASAs in


    dcmsg_fwd_out (optional, any, None)
      Diameter cross cpu fwd out


    reselect_fwd_tuple (optional, any, None)
      Original client tuple does not exist so reselect another one


    reply_unable_to_deliver (optional, any, None)
      Reply with unable to deliver error info


    retry_client_request_fail (optional, any, None)
      Diameter retry client request fail


    aca_in (optional, any, None)
      Number of ACAs in


    terminate_on_cca_t (optional, any, None)
      Diameter terminate on cca_t


    unkwn_cmd_code (optional, any, None)
      Diameter unkown cmd code


    invalid_avp (optional, any, None)
      AVP value contains illegal chars


    asr_out (optional, any, None)
      Number of ASRs out


    sta_out (optional, any, None)
      Number of STAs out


    snat_fail (optional, any, None)
      Number of snat failures


    cca_t (optional, any, None)
      Number of CCAs terminate


    no_session_id (optional, any, None)
      Diameter no session id avp


    update_latest_server (optional, any, None)
      Update to the latest server that used a session id


    dcmsg_rev_in (optional, any, None)
      Diameter cross cpu rev in


    cea_in (optional, any, None)
      Number of CEAs in


    dwr_out (optional, any, None)
      Number of DWRs out


    asa_out (optional, any, None)
      Number of ASAs out


    dcmsg_rev_out (optional, any, None)
      Diameter cross cpu rev out


    reply_unknown_session_id (optional, any, None)
      Reply with unknown session ID error info


    ccr_in (optional, any, None)
      Number of CCRs in


    forward_unknown_session_id (optional, any, None)
      Forward server side message with unknown session id


    svrsel_fail (optional, any, None)
      Number of server selection failed


    curr (optional, any, None)
      Current


    acr_out (optional, any, None)
      Number of ACRs out


    dwr_in (optional, any, None)
      Number of DWRs in


    num (optional, any, None)
      Number


    conn_closed_by_client (optional, any, None)
      Client initiates TCP close/reset


    reply_invalid_avp_value (optional, any, None)
      Reply with invalid AVP error info


    ccr_out (optional, any, None)
      Number of CCRs out


    aca_out (optional, any, None)
      Number of ACAs out


    sta_in (optional, any, None)
      Number of STAs in


    total (optional, any, None)
      Total


    total_http_req_enter_gen (optional, any, None)
      Total number of HTTP requests enter generic proxy


    dwa_out (optional, any, None)
      Number of DWAs out


    retry_client_request (optional, any, None)
      Diameter retry client request


    reselect_rev_tuple (optional, any, None)
      Original server tuple does not exist so reselect another one


    no_fwd_tuple (optional, any, None)
      Diameter no fwd tuple matched


    cca_out (optional, any, None)
      Number of CCAs out


    cca_in (optional, any, None)
      Number of CCAs in


    other_out (optional, any, None)
      Number of other messages out


    cea_out (optional, any, None)
      Number of CEAs out


    dpr_in (optional, any, None)
      Number of DPRs in


    asr_in (optional, any, None)
      Number of ASRs in


    reply_error_info_fail (optional, any, None)
      Fail to reply error info to peer


    cer_in (optional, any, None)
      Number of CERs in


    str_in (optional, any, None)
      Number of STRs in


    client_fail (optional, any, None)
      Number of client failures


    cer_out (optional, any, None)
      Number of CERs out


    dpa_out (optional, any, None)
      Number of DPAs out


    dcmsg_error (optional, any, None)
      Diameter cross cpu error


    ccr_t (optional, any, None)
      Number of CCRs terminate


    ccr_u (optional, any, None)
      Number of CCRs update


    mismatch_fwd_id (optional, any, None)
      Diameter mismatch fwd session id


    close_conn_when_vport_down (optional, any, None)
      Close client conn when virtual port is down


    other_in (optional, any, None)
      Number of other messages in


    mismatch_rev_id (optional, any, None)
      Diameter mismatch rev session id


    reselect_fwd_tuple_other_cpu (optional, any, None)
      Original client tuple does not exist so reselect another one on other CPUs


    no_sess (optional, any, None)
      Number of no sessions


    dpa_in (optional, any, None)
      Number of DPAs in


    acr_in (optional, any, None)
      Number of ACRs in


    conn_closed_by_server (optional, any, None)
      Server initiates TCP close/reset


    dpr_out (optional, any, None)
      Number of DPRs out


    no_rev_tuple (optional, any, None)
      Diameter no rev tuple matched


    ccr_i (optional, any, None)
      Number of CCRs initial



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication









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

