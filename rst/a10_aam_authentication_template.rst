.. _a10_aam_authentication_template_module:


a10_aam_authentication_template -- Configures A10 aam.authentication.template
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Authentication template






Parameters
----------

  cookie_domain_group (False, any, None)
    Field cookie_domain_group


    cookie_dmngrp (optional, any, None)
      Specify group id to join in the cookie-domain



  saml_sp (False, any, None)
    Specify SAML service provider


  ansible_username (True, any, None)
    Username for AXAPI authentication


  forward_logout_disable (False, any, None)
    Disable forward logout request to backend application server. The config-field logout-url must be configured first


  service_group (False, any, None)
    Bind an authentication service group to this template (Specify authentication service group name)


  local_logging (False, any, None)
    Enable local logging


  log (False, any, None)
    'use-partition-level-config'= Use configuration of authentication-log enable command; 'enable'= Enable authentication logs for this template; 'disable'= Disable authentication logs for this template;


  cookie_httponly_enable (False, any, None)
    Enable httponly attribute for AAM cookies


  cookie_secure_enable (False, any, None)
    Enable secure attribute for AAM cookies


  logout_url (False, any, None)
    Specify logout url (Specify logout url string)


  state (True, any, None)
    State of the object to be created.


  accounting_server (False, any, None)
    Specify a RADIUS accounting server


  saml_idp (False, any, None)
    Specify SAML identity provider


  logout_idle_timeout (False, any, None)
    Specify idle logout time (Specify idle timeout in seconds, default is 300)


  max_session_time (False, any, None)
    Specify default SAML token lifetime (Specify lifetime (in seconds) of SAML token when it not provided by token attributes, default is 28800. (0 for indefinite))


  relay (False, any, None)
    Specify authentication relay (Specify authentication relay template name)


  ntype (False, any, None)
    'saml'= SAML authentication template; 'standard'= Standard authentication template;


  ansible_port (True, any, None)
    Port for AXAPI authentication


  redirect_hostname (False, any, None)
    Hostname(Length 1-31) for transparent-proxy authentication


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  logon (False, any, None)
    Specify authentication logon (Specify authentication logon template name)


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  accounting_service_group (False, any, None)
    Specify an authentication service group for RADIUS accounting


  account (False, any, None)
    Specify AD domain account


  name (True, any, None)
    Authentication template name


  cookie_domain (False, any, None)
    Field cookie_domain


    cookie_dmn (optional, any, None)
      Specify domain scope for the authentication (ex= .a10networks.com)



  ansible_password (True, any, None)
    Password for AXAPI authentication


  jwt (False, any, None)
    Specify authentication jwt template


  uuid (False, any, None)
    uuid of the object


  server (False, any, None)
    Specify authentication server (Specify authentication server template name)


  modify_content_security_policy (False, any, None)
    Put redirect-uri or service-principal-name into CSP header to avoid CPS break authentication process


  cookie_max_age (False, any, None)
    Configure Max-Age for authentication session cookie (Configure Max-Age in seconds. System will not set Max-Age/Expires for value 0 and default is 604800 (1 week).)


  cookie_samesite (False, any, None)
    'strict'= Specify SameSite attribute as Strict for AAM cookie; 'lax'= Specify SameSite attribute as Lax for AAM cookie; 'none'= Specify SameSite attribute as None for AAM cookie;


  auth_sess_mode (False, any, None)
    'cookie-based'= Track auth-session by cookie (default); 'ip-based'= Track auth- session by client IP;


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

