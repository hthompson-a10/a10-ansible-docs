.. _a10_slb_ssl_forward_proxy_module:


a10_slb_ssl_forward_proxy -- Configures A10 slb.ssl-forward-proxy
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

SSL forward proxy stats info






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'cert_create'= Certificates created; 'cert_expr'= Certificates expired; 'cert_hit'= Certificate cache hits; 'cert_miss'= Certificate cache miss; 'conn_bypass'= Connections bypassed; 'conn_inspect'= Connections inspected; 'bypass-failsafe-ssl-sessions'= Bypass Failsafe SSL sessions; 'bypass-sni-sessions'= Bypass SNI sessions; 'bypass-client-auth-sessions'= Bypass Client Auth sessions; 'failed-in-ssl-handshakes'= Failed in SSL handshakes; 'failed-in-crypto-operations'= Failed in crypto operations; 'failed-in-tcp'= Failed in TCP; 'failed-in-certificate-verification'= Failed in Certificate verification; 'failed-in-certificate-signing'= Failed in Certificate signing; 'invalid-ocsp-stapling-response'= Invalid OCSP Stapling Response; 'revoked-ocsp-response'= Revoked OCSP Response; 'unsupported-ssl- version'= Unsupported SSL version; 'certificates-in-cache'= Certificates in cache; 'connections-failed'= Connections failed; 'aflex-bypass'= Bypass triggered by aFleX; 'bypass-cert-subject-sessions'= Bypass Cert Subject sessions; 'bypass-cert-issuer-sessions'= Bypass Cert issuer sessions; 'bypass- cert-san-sessions'= Bypass Cert SAN sessions; 'bypass-no-sni-sessions'= Bypass NO SNI sessions; 'reset-no-sni-sessions'= Reset No SNI sessions; 'bypass- username-sessions'= Bypass Username sessions; 'bypass-ad-group-sessions'= Bypass AD-group sessions; 'cert_in_cache'= Certificates in cache; 'tot_conn_in_buff'= Total buffered async connections; 'curr_conn_in_buff'= Current buffered async connections;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    unsupported_ssl_version (optional, any, None)
      Unsupported SSL version


    certificates_in_cache (optional, any, None)
      Certificates in cache


    revoked_ocsp_response (optional, any, None)
      Revoked OCSP Response


    bypass_ad_group_sessions (optional, any, None)
      Bypass AD-group sessions


    failed_in_certificate_verification (optional, any, None)
      Failed in Certificate verification


    connections_failed (optional, any, None)
      Connections failed


    failed_in_certificate_signing (optional, any, None)
      Failed in Certificate signing


    bypass_failsafe_ssl_sessions (optional, any, None)
      Bypass Failsafe SSL sessions


    bypass_cert_san_sessions (optional, any, None)
      Bypass Cert SAN sessions


    invalid_ocsp_stapling_response (optional, any, None)
      Invalid OCSP Stapling Response


    failed_in_crypto_operations (optional, any, None)
      Failed in crypto operations


    bypass_no_sni_sessions (optional, any, None)
      Bypass NO SNI sessions


    bypass_sni_sessions (optional, any, None)
      Bypass SNI sessions


    bypass_client_auth_sessions (optional, any, None)
      Bypass Client Auth sessions


    cert_create (optional, any, None)
      Certificates created


    cert_hit (optional, any, None)
      Certificate cache hits


    failed_in_ssl_handshakes (optional, any, None)
      Failed in SSL handshakes


    reset_no_sni_sessions (optional, any, None)
      Reset No SNI sessions


    cert_miss (optional, any, None)
      Certificate cache miss


    bypass_cert_subject_sessions (optional, any, None)
      Bypass Cert Subject sessions


    conn_bypass (optional, any, None)
      Connections bypassed


    aflex_bypass (optional, any, None)
      Bypass triggered by aFleX


    curr_conn_in_buff (optional, any, None)
      Current buffered async connections


    conn_inspect (optional, any, None)
      Connections inspected


    tot_conn_in_buff (optional, any, None)
      Total buffered async connections


    cert_expr (optional, any, None)
      Certificates expired


    failed_in_tcp (optional, any, None)
      Failed in TCP


    cert_in_cache (optional, any, None)
      Certificates in cache


    bypass_cert_issuer_sessions (optional, any, None)
      Bypass Cert issuer sessions


    bypass_username_sessions (optional, any, None)
      Bypass Username sessions



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

