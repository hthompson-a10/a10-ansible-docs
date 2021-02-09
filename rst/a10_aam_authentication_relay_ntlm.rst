.. _a10_aam_authentication_relay_ntlm_module:


a10_aam_authentication_relay_ntlm -- Configures A10 aam.authentication.relay.ntlm
=================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

NTLM Authentication Relay






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'success'= Success; 'failure'= Failure; 'request'= Request; 'response'= Response; 'http-code-200'= HTTP 200 OK; 'http-code-400'= HTTP 400 Bad Request; 'http-code-401'= HTTP 401 Unauthorized; 'http-code-403'= HTTP 403 Forbidden; 'http-code-404'= HTTP 404 Not Found; 'http-code-500'= HTTP 500 Internal Server Error; 'http-code-503'= HTTP 503 Service Unavailable; 'http- code-other'= Other HTTP Response; 'buffer-alloc-fail'= Buffer Allocation Failure; 'encoding-fail'= Encoding Failure; 'insert-header-fail'= Insert Header Failure; 'parse-header-fail'= Parse Header Failure; 'internal-error'= Internal Error; 'ntlm-auth-skipped'= Requests for which NTLM relay is skipped; 'large- request-processing'= Requests invoking large request processing; 'large- request-flushed'= Large requests sent to server; 'head-negotiate-request-sent'= HEAD requests sent with NEGOTIATE header; 'head-auth-request-sent'= HEAD requests sent with AUTH header;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    request (optional, any, None)
      Request


    insert_header_fail (optional, any, None)
      Insert Header Failure


    encoding_fail (optional, any, None)
      Encoding Failure


    ntlm_auth_skipped (optional, any, None)
      Requests for which NTLM relay is skipped


    failure (optional, any, None)
      Failure


    http_code_other (optional, any, None)
      Other HTTP Response


    response (optional, any, None)
      Response


    name (optional, any, None)
      Specify NTLM authentication relay name


    large_request_processing (optional, any, None)
      Requests invoking large request processing


    head_auth_request_sent (optional, any, None)
      HEAD requests sent with AUTH header


    head_negotiate_request_sent (optional, any, None)
      HEAD requests sent with NEGOTIATE header


    success (optional, any, None)
      Success


    http_code_400 (optional, any, None)
      HTTP 400 Bad Request


    http_code_401 (optional, any, None)
      HTTP 401 Unauthorized


    large_request_flushed (optional, any, None)
      Large requests sent to server


    http_code_403 (optional, any, None)
      HTTP 403 Forbidden


    http_code_404 (optional, any, None)
      HTTP 404 Not Found


    buffer_alloc_fail (optional, any, None)
      Buffer Allocation Failure


    http_code_500 (optional, any, None)
      HTTP 500 Internal Server Error


    http_code_503 (optional, any, None)
      HTTP 503 Service Unavailable


    internal_error (optional, any, None)
      Internal Error


    parse_header_fail (optional, any, None)
      Parse Header Failure


    http_code_200 (optional, any, None)
      HTTP 200 OK



  name (True, any, None)
    Specify NTLM authentication relay name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  domain (False, any, None)
    Specify NTLM domain, default is null


  state (True, any, None)
    State of the object to be created.


  version (False, any, None)
    Specify NTLM version, default is NTLM 2


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


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

