.. _a10_aam_authentication_server_windows_module:


a10_aam_authentication_server_windows -- Configures A10 aam.authentication.server.windows
=========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Windows Server, using Kerberos or NTLM for authentication






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'kerberos-request-send'= Total Kerberos Request; 'kerberos- response-get'= Total Kerberos Response; 'kerberos-timeout-error'= Total Kerberos Timeout; 'kerberos-other-error'= Total Kerberos Other Error; 'ntlm- authentication-success'= Total NTLM Authentication Success; 'ntlm- authentication-failure'= Total NTLM Authentication Failure; 'ntlm-proto- negotiation-success'= Total NTLM Protocol Negotiation Success; 'ntlm-proto- negotiation-failure'= Total NTLM Protocol Negotiation Failure; 'ntlm-session- setup-success'= Total NTLM Session Setup Success; 'ntlm-session-setup-failed'= Total NTLM Session Setup Failure; 'kerberos-request-normal'= Total Kerberos Normal Request; 'kerberos-request-dropped'= Total Kerberos Dropped Request; 'kerberos-response-success'= Total Kerberos Success Response; 'kerberos- response-failure'= Total Kerberos Failure Response; 'kerberos-response-error'= Total Kerberos Error Response; 'kerberos-response-timeout'= Total Kerberos Timeout Response; 'kerberos-response-other'= Total Kerberos Other Response; 'kerberos-job-start-error'= Total Kerberos Job Start Error; 'kerberos-polling- control-error'= Total Kerberos Polling Control Error; 'ntlm-prepare-req- success'= Total NTLM Prepare Request Success; 'ntlm-prepare-req-failed'= Total NTLM Prepare Request Failed; 'ntlm-timeout-error'= Total NTLM Timeout; 'ntlm- other-error'= Total NTLM Other Error; 'ntlm-request-normal'= Total NTLM Normal Request; 'ntlm-request-dropped'= Total NTLM Dropped Request; 'ntlm-response- success'= Total NTLM Success Response; 'ntlm-response-failure'= Total NTLM Failure Response; 'ntlm-response-error'= Total NTLM Error Response; 'ntlm- response-timeout'= Total NTLM Timeout Response; 'ntlm-response-other'= Total NTLM Other Response; 'ntlm-job-start-error'= Total NTLM Job Start Error; 'ntlm- polling-control-error'= Total NTLM Polling Control Error; 'kerberos-pw-expiry'= Total Kerberos password expiry; 'kerberos-pw-change-success'= Total Kerberos password change success; 'kerberos-pw-change-failure'= Total Kerberos password change failure;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    kerberos_response_get (optional, any, None)
      Total Kerberos Response


    kerberos_response_success (optional, any, None)
      Total Kerberos Success Response


    kerberos_polling_control_error (optional, any, None)
      Total Kerberos Polling Control Error


    kerberos_response_other (optional, any, None)
      Total Kerberos Other Response


    ntlm_timeout_error (optional, any, None)
      Total NTLM Timeout


    ntlm_prepare_req_success (optional, any, None)
      Total NTLM Prepare Request Success


    kerberos_response_timeout (optional, any, None)
      Total Kerberos Timeout Response


    ntlm_prepare_req_failed (optional, any, None)
      Total NTLM Prepare Request Failed


    kerberos_pw_change_success (optional, any, None)
      Total Kerberos password change success


    kerberos_job_start_error (optional, any, None)
      Total Kerberos Job Start Error


    ntlm_polling_control_error (optional, any, None)
      Total NTLM Polling Control Error


    instance_list (optional, any, None)
      Field instance_list


    ntlm_response_success (optional, any, None)
      Total NTLM Success Response


    ntlm_response_other (optional, any, None)
      Total NTLM Other Response


    ntlm_proto_negotiation_success (optional, any, None)
      Total NTLM Protocol Negotiation Success


    ntlm_request_normal (optional, any, None)
      Total NTLM Normal Request


    kerberos_response_error (optional, any, None)
      Total Kerberos Error Response


    ntlm_proto_negotiation_failure (optional, any, None)
      Total NTLM Protocol Negotiation Failure


    ntlm_response_timeout (optional, any, None)
      Total NTLM Timeout Response


    ntlm_authentication_failure (optional, any, None)
      Total NTLM Authentication Failure


    kerberos_request_send (optional, any, None)
      Total Kerberos Request


    ntlm_response_failure (optional, any, None)
      Total NTLM Failure Response


    ntlm_request_dropped (optional, any, None)
      Total NTLM Dropped Request


    ntlm_authentication_success (optional, any, None)
      Total NTLM Authentication Success


    kerberos_timeout_error (optional, any, None)
      Total Kerberos Timeout


    kerberos_pw_expiry (optional, any, None)
      Total Kerberos password expiry


    kerberos_request_normal (optional, any, None)
      Total Kerberos Normal Request


    ntlm_other_error (optional, any, None)
      Total NTLM Other Error


    kerberos_other_error (optional, any, None)
      Total Kerberos Other Error


    ntlm_session_setup_failed (optional, any, None)
      Total NTLM Session Setup Failure


    ntlm_job_start_error (optional, any, None)
      Total NTLM Job Start Error


    ntlm_session_setup_success (optional, any, None)
      Total NTLM Session Setup Success


    kerberos_response_failure (optional, any, None)
      Total Kerberos Failure Response


    kerberos_request_dropped (optional, any, None)
      Total Kerberos Dropped Request


    ntlm_response_error (optional, any, None)
      Total NTLM Error Response


    kerberos_pw_change_failure (optional, any, None)
      Total Kerberos password change failure



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  instance_list (False, any, None)
    Field instance_list


    sampling_enable (optional, any, None)
      Field sampling_enable


    health_check (optional, any, None)
      Check server's health status


    realm (optional, any, None)
      Specify realm of Windows server


    name (optional, any, None)
      Specify Windows authentication server name


    support_apacheds_kdc (optional, any, None)
      Enable weak cipher (DES CRC/MD5/MD4) and merge AS-REQ in single packet


    auth_protocol (optional, any, None)
      Field auth_protocol


    host (optional, any, None)
      Field host


    health_check_string (optional, any, None)
      Health monitor name


    timeout (optional, any, None)
      Specify connection timeout to server, default is 10 seconds


    health_check_disable (optional, any, None)
      Disable configured health check configuration


    uuid (optional, any, None)
      uuid of the object



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

