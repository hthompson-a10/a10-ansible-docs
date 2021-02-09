.. _a10_slb_ssl_cert_revoke_module:


a10_slb_ssl_cert_revoke -- Configures A10 slb.ssl-cert-revoke
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure ssl-cert-revoke-stats






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'ocsp_stapling_response_good'= OCSP stapling response good; 'ocsp_chain_status_good'= Certificate chain status good; 'ocsp_chain_status_revoked'= Certificate chain status revoked; 'ocsp_chain_status_unknown'= Certificate chain status unknown; 'ocsp_request'= OCSP requests; 'ocsp_response'= OCSP responses; 'ocsp_connection_error'= OCSP connection error; 'ocsp_uri_not_found'= OCSP URI not found; 'ocsp_uri_https'= Log OCSP URI https; 'ocsp_uri_unsupported'= OCSP URI unsupported; 'ocsp_response_status_good'= OCSP response status good; 'ocsp_response_status_revoked'= OCSP response status revoked; 'ocsp_response_status_unknown'= OCSP response status unknown; 'ocsp_cache_status_good'= OCSP cache status good; 'ocsp_cache_status_revoked'= OCSP cache status revoked; 'ocsp_cache_miss'= OCSP cache miss; 'ocsp_cache_expired'= OCSP cache expired; 'ocsp_other_error'= Log OCSP other errors; 'ocsp_response_no_nonce'= Log OCSP other errors; 'ocsp_response_nonce_error'= Log OCSP other errors; 'crl_request'= CRL requests; 'crl_response'= CRL responses; 'crl_connection_error'= CRL connection errors; 'crl_uri_not_found'= CRL URI not found; 'crl_uri_https'= CRL URI https; 'crl_uri_unsupported'= CRL URI unsupported; 'crl_response_status_good'= CRL response status good; 'crl_response_status_revoked'= CRL response status revoked; 'crl_response_status_unknown'= CRL response status unknown; 'crl_cache_status_good'= CRL cache status good; 'crl_cache_status_revoked'= CRL cache status revoked; 'crl_other_error'= CRL other errors;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    ocsp_request (optional, any, None)
      OCSP requests


    ocsp_cache_status_revoked (optional, any, None)
      OCSP cache status revoked


    crl_uri_not_found (optional, any, None)
      CRL URI not found


    crl_uri_https (optional, any, None)
      CRL URI https


    ocsp_response_status_revoked (optional, any, None)
      OCSP response status revoked


    ocsp_chain_status_good (optional, any, None)
      Certificate chain status good


    ocsp_response_no_nonce (optional, any, None)
      Log OCSP other errors


    crl_response (optional, any, None)
      CRL responses


    crl_cache_status_good (optional, any, None)
      CRL cache status good


    ocsp_cache_expired (optional, any, None)
      OCSP cache expired


    ocsp_response_nonce_error (optional, any, None)
      Log OCSP other errors


    ocsp_uri_unsupported (optional, any, None)
      OCSP URI unsupported


    crl_other_error (optional, any, None)
      CRL other errors


    ocsp_cache_miss (optional, any, None)
      OCSP cache miss


    ocsp_stapling_response_good (optional, any, None)
      OCSP stapling response good


    ocsp_uri_https (optional, any, None)
      Log OCSP URI https


    crl_connection_error (optional, any, None)
      CRL connection errors


    ocsp_chain_status_revoked (optional, any, None)
      Certificate chain status revoked


    ocsp_chain_status_unknown (optional, any, None)
      Certificate chain status unknown


    ocsp_uri_not_found (optional, any, None)
      OCSP URI not found


    crl_response_status_revoked (optional, any, None)
      CRL response status revoked


    ocsp_response_status_good (optional, any, None)
      OCSP response status good


    ocsp_response (optional, any, None)
      OCSP responses


    crl_response_status_unknown (optional, any, None)
      CRL response status unknown


    crl_uri_unsupported (optional, any, None)
      CRL URI unsupported


    ocsp_cache_status_good (optional, any, None)
      OCSP cache status good


    crl_request (optional, any, None)
      CRL requests


    ocsp_other_error (optional, any, None)
      Log OCSP other errors


    crl_response_status_good (optional, any, None)
      CRL response status good


    ocsp_connection_error (optional, any, None)
      OCSP connection error


    crl_cache_status_revoked (optional, any, None)
      CRL cache status revoked


    ocsp_response_status_unknown (optional, any, None)
      OCSP response status unknown



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

