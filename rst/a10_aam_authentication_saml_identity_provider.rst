.. _a10_aam_authentication_saml_identity_provider_module:


a10_aam_authentication_saml_identity_provider -- Configures A10 aam.authentication.saml.identity-provider
=========================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Authentication identity provider






Parameters
----------

  oper (False, any, None)
    Field oper


    md (optional, any, None)
      Field md


    entity_id (optional, any, None)
      Field entity_id


    name (optional, any, None)
      SAML authentication identity provider name


    ars_list (optional, any, None)
      Field ars_list


    aqs_list (optional, any, None)
      Field aqs_list


    cert (optional, any, None)
      Field cert


    slo_list (optional, any, None)
      Field slo_list


    sso_list (optional, any, None)
      Field sso_list



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    md_update (optional, any, None)
      Metadata Update Success Count


    md_fail (optional, any, None)
      Metadata Update Fail Count


    acs_state (optional, any, None)
      ACS State


    name (optional, any, None)
      SAML authentication identity provider name


    acs_pass (optional, any, None)
      ACS Pass Count


    md_state (optional, any, None)
      Metadata State


    valid_status (optional, any, None)
      Valid IdP status or not


    acs_req (optional, any, None)
      ACS Request Total Count


    acs_fail (optional, any, None)
      ACS Fail Count



  name (True, any, None)
    SAML authentication identity provider name


  reload_metadata (False, any, None)
    Reload IdP's metadata immediately


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  reload_interval (False, any, None)
    Specify URI metadata reload period (Specify URI metadata reload period in seconds, default is 28800)


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  metadata (False, any, None)
    URL of SAML identity provider's metadata file


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


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

