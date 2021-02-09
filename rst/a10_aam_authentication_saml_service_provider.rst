.. _a10_aam_authentication_saml_service_provider_module:


a10_aam_authentication_saml_service_provider -- Configures A10 aam.authentication.saml.service-provider
=======================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Authentication service provider






Parameters
----------

  entity_id (False, any, None)
    SAML service provider entity ID


  single_logout_service (False, any, None)
    Field single_logout_service


    SLO_binding (optional, any, None)
      'post'= POST binding of single logout service; 'redirect'= Redirect binding of single logout service; 'soap'= SOAP binding of single logout service;


    SLO_location (optional, any, None)
      The location of name-id management service. (ex. /SAML/POST)



  ansible_username (True, any, None)
    Username for AXAPI authentication


  metadata_export_service (False, any, None)
    Field metadata_export_service


    md_export_location (optional, any, None)
      Specify the URI to export SP metadata (Export URI. Default is /A10SP_Metadata)


    sign_xml (optional, any, None)
      Sign exported SP metadata XML with SP's certificate



  acs_uri_bypass (False, any, None)
    After user authenticated, bypass requests with assertion-consuming-service location URI


  signature_algorithm (False, any, None)
    'SHA1'= use SHA1 as signature algorithm (default); 'SHA256'= use SHA256 as signature algorithm;


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  artifact_resolution_service (False, any, None)
    Field artifact_resolution_service


    artifact_binding (optional, any, None)
      'soap'= SOAP binding of artifact resolution service;


    artifact_index (optional, any, None)
      The index of artifact resolution service


    artifact_location (optional, any, None)
      The location of artifact resolution service. (ex. /SAML/POST)



  ansible_host (True, any, None)
    Host for AXAPI authentication


  name (True, any, None)
    Specify SAML authentication service provider name


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'sp-metadata-export-req'= Metadata Export Request; 'sp-metadata- export-success'= Metadata Export Success; 'login-auth-req'= Login Authentication Request; 'login-auth-resp'= Login Authentication Response; 'acs- req'= SAML Single-Sign-On Request; 'acs-success'= SAML Single-Sign-On Success; 'acs-authz-fail'= SAML Single-Sign-On Authorization Fail; 'acs-error'= SAML Single-Sign-On Error; 'slo-req'= Single Logout Request; 'slo-success'= Single Logout Success; 'slo-error'= Single Logout Error; 'other-error'= Other Error;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    login_auth_req (optional, any, None)
      Login Authentication Request


    acs_error (optional, any, None)
      SAML Single-Sign-On Error


    other_error (optional, any, None)
      Other Error


    acs_success (optional, any, None)
      SAML Single-Sign-On Success


    sp_metadata_export_success (optional, any, None)
      Metadata Export Success


    sp_metadata_export_req (optional, any, None)
      Metadata Export Request


    login_auth_resp (optional, any, None)
      Login Authentication Response


    acs_authz_fail (optional, any, None)
      SAML Single-Sign-On Authorization Fail


    acs_req (optional, any, None)
      SAML Single-Sign-On Request


    slo_success (optional, any, None)
      Single Logout Success


    slo_error (optional, any, None)
      Single Logout Error


    slo_req (optional, any, None)
      Single Logout Request


    name (optional, any, None)
      Specify SAML authentication service provider name



  uuid (False, any, None)
    uuid of the object


  certificate (False, any, None)
    SAML service provider certificate file (PFX format is required.)


  ansible_password (True, any, None)
    Password for AXAPI authentication


  a10_partition (False, any, None)
    Destination/target partition for object/command


  saml_request_signed (False, any, None)
    Field saml_request_signed


    saml_request_signed_disable (optional, any, None)
      Disable signing signature for SAML (Authn/Artifact Resolve) requests



  soap_tls_certificate_validate (False, any, None)
    Field soap_tls_certificate_validate


    soap_tls_certificate_validate_disable (optional, any, None)
      Disable verification for server certificate in TLS session when resolving artificate



  state (True, any, None)
    State of the object to be created.


  require_assertion_signed (False, any, None)
    Field require_assertion_signed


    require_assertion_signed_enable (optional, any, None)
      Enable required signing of SAML assertion



  service_url (False, any, None)
    SAML service provider service URL (ex. https=//www.a10networks.com/saml.sso)


  bad_request_redirect_uri (False, any, None)
    Specify URL to redirect


  assertion_consuming_service (False, any, None)
    Field assertion_consuming_service


    assertion_index (optional, any, None)
      The index of assertion consuming service


    assertion_binding (optional, any, None)
      'artifact'= Artifact binding of assertion consuming service; 'paos'= PAOS binding of assertion consuming service; 'post'= POST binding of assertion consuming service;


    assertion_location (optional, any, None)
      The location of assertion consuming service endpoint. (ex. /SAML/POST)



  adfs_ws_federation (False, any, None)
    Field adfs_ws_federation


    ws_federation_enable (optional, any, None)
      Enable ADFS WS-Federation



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

