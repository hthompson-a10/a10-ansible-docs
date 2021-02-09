.. _a10_aam_authentication_saml_global_module:


a10_aam_authentication_saml_global -- Configures A10 aam.authentication.saml.global
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Global SAML statistics






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'requests-to-a10saml'= Total Request to A10 SAML Service; 'responses-from-a10saml'= Total Response from A10 SAML Service; 'sp-metadata- export-req'= Total Metadata Export Request; 'sp-metadata-export-success'= Toal Metadata Export Success; 'login-auth-req'= Total Login Authentication Request; 'login-auth-resp'= Total Login Authentication Response; 'acs-req'= Total SAML Single-Sign-On Request; 'acs-success'= Total SAML Single-Sign-On Success; 'acs- authz-fail'= Total SAML Single-Sign-On Authorization Fail; 'acs-error'= Total SAML Single-Sign-On Error; 'slo-req'= Total Single Logout Request; 'slo- success'= Total Single Logout Success; 'slo-error'= Total Single Logout Error; 'other-error'= Total Other Error;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    requests_to_a10saml (optional, any, None)
      Total Request to A10 SAML Service


    login_auth_req (optional, any, None)
      Total Login Authentication Request


    acs_error (optional, any, None)
      Total SAML Single-Sign-On Error


    other_error (optional, any, None)
      Total Other Error


    acs_success (optional, any, None)
      Total SAML Single-Sign-On Success


    sp_metadata_export_success (optional, any, None)
      Toal Metadata Export Success


    sp_metadata_export_req (optional, any, None)
      Total Metadata Export Request


    login_auth_resp (optional, any, None)
      Total Login Authentication Response


    acs_authz_fail (optional, any, None)
      Total SAML Single-Sign-On Authorization Fail


    acs_req (optional, any, None)
      Total SAML Single-Sign-On Request


    slo_success (optional, any, None)
      Total Single Logout Success


    slo_error (optional, any, None)
      Total Single Logout Error


    responses_from_a10saml (optional, any, None)
      Total Response from A10 SAML Service


    slo_req (optional, any, None)
      Total Single Logout Request



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

