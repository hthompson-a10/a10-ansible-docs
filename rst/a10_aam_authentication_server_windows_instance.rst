.. _a10_aam_authentication_server_windows_instance_module:


a10_aam_authentication_server_windows_instance -- Configures A10 aam.authentication.server.windows.instance
===========================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Windows Server, using Kerberos or NTLM for authentication






Parameters
----------

  health_check (False, any, None)
    Check server's health status


  ansible_username (True, any, None)
    Username for AXAPI authentication


  auth_protocol (False, any, None)
    Field auth_protocol


    ntlm_version (optional, any, None)
      Specify NTLM version, default is 2


    ntlm_disable (optional, any, None)
      Disable NTLM authentication protocol


    kport_hm (optional, any, None)
      Check Kerberos port's health status


    ntlm_health_check_disable (optional, any, None)
      Disable configured NTLM port health check configuration


    kerberos_disable (optional, any, None)
      Disable Kerberos authentication protocol


    kerberos_password_change_port (optional, any, None)
      Specify the Kerbros password change port, default is 464


    ntlm_health_check (optional, any, None)
      Check NTLM port's health status


    kerberos_port (optional, any, None)
      Specify the Kerberos port, default is 88


    kport_hm_disable (optional, any, None)
      Disable configured Kerberos port health check configuration



  host (False, any, None)
    Field host


    hostipv6 (optional, any, None)
      Specify the Windows server's IPV6 address


    hostip (optional, any, None)
      Specify the Windows server's hostname(Length 1-31) or IP address



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  stats (False, any, None)
    Field stats


    krb_send_req_success (optional, any, None)
      Kerberos Request


    ntlm_auth_success (optional, any, None)
      NTLM Authentication Success


    ntlm_prepare_req_error (optional, any, None)
      NTLM Prepare Request Error


    ntlm_auth_failure (optional, any, None)
      NTLM Authentication Failure


    krb_timeout_error (optional, any, None)
      Kerberos Timeout


    krb_other_error (optional, any, None)
      Kerberos Other Error


    ntlm_timeout_error (optional, any, None)
      NTLM Timeout


    ntlm_prepare_req_success (optional, any, None)
      NTLM Prepare Request Success


    krb_get_resp_success (optional, any, None)
      Kerberos Response


    ntlm_proto_nego_success (optional, any, None)
      NTLM Protocol Negotiation Success


    name (optional, any, None)
      Specify Windows authentication server name


    ntlm_other_error (optional, any, None)
      NTLM Other Error


    ntlm_proto_nego_failure (optional, any, None)
      NTLM Protocol Negotiation Failure


    krb_pw_change_success (optional, any, None)
      Kerberos password change success


    ntlm_session_setup_success (optional, any, None)
      NTLM Session Setup Success


    krb_pw_expiry (optional, any, None)
      Kerberos password expiry


    ntlm_session_setup_failure (optional, any, None)
      NTLM Session Setup Failure


    krb_pw_change_failure (optional, any, None)
      Kerberos password change failure



  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  health_check_disable (False, any, None)
    Disable configured health check configuration


  uuid (False, any, None)
    uuid of the object


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'krb_send_req_success'= Kerberos Request; 'krb_get_resp_success'= Kerberos Response; 'krb_timeout_error'= Kerberos Timeout; 'krb_other_error'= Kerberos Other Error; 'krb_pw_expiry'= Kerberos password expiry; 'krb_pw_change_success'= Kerberos password change success; 'krb_pw_change_failure'= Kerberos password change failure; 'ntlm_proto_nego_success'= NTLM Protocol Negotiation Success; 'ntlm_proto_nego_failure'= NTLM Protocol Negotiation Failure; 'ntlm_session_setup_success'= NTLM Session Setup Success; 'ntlm_session_setup_failure'= NTLM Session Setup Failure; 'ntlm_prepare_req_success'= NTLM Prepare Request Success; 'ntlm_prepare_req_error'= NTLM Prepare Request Error; 'ntlm_auth_success'= NTLM Authentication Success; 'ntlm_auth_failure'= NTLM Authentication Failure; 'ntlm_timeout_error'= NTLM Timeout; 'ntlm_other_error'= NTLM Other Error;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  realm (False, any, None)
    Specify realm of Windows server


  name (True, any, None)
    Specify Windows authentication server name


  support_apacheds_kdc (False, any, None)
    Enable weak cipher (DES CRC/MD5/MD4) and merge AS-REQ in single packet


  state (True, any, None)
    State of the object to be created.


  timeout (False, any, None)
    Specify connection timeout to server, default is 10 seconds


  ansible_password (True, any, None)
    Password for AXAPI authentication


  health_check_string (False, any, None)
    Health monitor name









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

