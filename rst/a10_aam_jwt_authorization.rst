.. _a10_aam_jwt_authorization_module:


a10_aam_jwt_authorization -- Configures A10 aam.jwt-authorization
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

AAM JWT authorization related configuration






Parameters
----------

  verification_secret (False, any, None)
    Specify secret for verify JWT token signature


  ansible_username (True, any, None)
    Username for AXAPI authentication


  encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)


  jwt_exp_default (False, any, None)
    Specify the default token expiration if exp claim is not available (default 1800)


  verification_cert (False, any, None)
    Specify the certificate to verify JWT token signature


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  exp_claim_requried (False, any, None)
    Specify the exp claim is required for JWT authorization


  stats (False, any, None)
    Field stats


    jwt_request (optional, any, None)
      JWT Request


    name (optional, any, None)
      Specify JWT authorization template name


    jwt_missing_claim (optional, any, None)
      JWT Missing Claim


    jwt_missing_token (optional, any, None)
      JWT Missing Token


    jwt_authorize_success (optional, any, None)
      JWT Authorize Success


    jwt_authorize_failure (optional, any, None)
      JWT Authorize Failure


    jwt_token_expired (optional, any, None)
      JWT Token Expired


    jwt_other_error (optional, any, None)
      JWT Other Error


    jwt_signature_failure (optional, any, None)
      JWT Signature Failure



  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  jwt_cache_enable (False, any, None)
    Enable caching authorized JWT token and skip verification and authorization for cached tokens


  uuid (False, any, None)
    uuid of the object


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'jwt-request'= JWT Request; 'jwt-authorize-success'= JWT Authorize Success; 'jwt-authorize-failure'= JWT Authorize Failure; 'jwt-missing-token'= JWT Missing Token; 'jwt-missing-claim'= JWT Missing Claim; 'jwt-token-expired'= JWT Token Expired; 'jwt-signature-failure'= JWT Signature Failure; 'jwt-other- error'= JWT Other Error;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  log_level (False, any, None)
    '0'= log disable; '1'= only log authorzation fail (default); '2'= only log authorization success; '3'= log all;


  name (True, any, None)
    Specify JWT authorization template name


  jwt_forwarding (False, any, None)
    Specify JWT token will not be stripped while forwarding client request


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  verification_jwks (False, any, None)
    Specify the jwks file to verify JWT token signature


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

