.. _a10_aam_authentication_server_ldap_instance_module:


a10_aam_authentication_server_ldap_instance -- Configures A10 aam.authentication.server.ldap.instance
=====================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

LDAP Authentication Server






Parameters
----------

  auth_type (False, any, None)
    'ad'= Active Directory. Default; 'open-ldap'= OpenLDAP;


  secret_string (False, any, None)
    secret password


  protocol (False, any, None)
    'ldap'= Use LDAP (default); 'ldaps'= Use LDAP over SSL; 'starttls'= Use LDAP StartTLS;


  ansible_username (True, any, None)
    Username for AXAPI authentication


  encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)


  derive_bind_dn (False, any, None)
    Field derive_bind_dn


    username_attr (optional, any, None)
      Specify attribute name of username



  port (False, any, None)
    Specify the LDAP server's authentication port, default is 389


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'admin-bind-success'= Admin Bind Success; 'admin-bind-failure'= Admin Bind Failure; 'bind-success'= User Bind Success; 'bind-failure'= User Bind Failure; 'search-success'= Search Success; 'search-failure'= Search Failure; 'authorize-success'= Authorization Success; 'authorize-failure'= Authorization Failure; 'timeout-error'= Timeout; 'other-error'= Other Error; 'request'= Request; 'ssl-session-created'= TLS/SSL Session Created; 'ssl- session-failure'= TLS/SSL Session Failure; 'pw_expiry'= Password expiry; 'pw_change_success'= Password change success; 'pw_change_failure'= Password change failure;



  admin_dn (False, any, None)
    The LDAP server's admin DN


  stats (False, any, None)
    Field stats


    bind_success (optional, any, None)
      User Bind Success


    other_error (optional, any, None)
      Other Error


    pw_change_failure (optional, any, None)
      Password change failure


    pw_expiry (optional, any, None)
      Password expiry


    bind_failure (optional, any, None)
      User Bind Failure


    authorize_failure (optional, any, None)
      Authorization Failure


    timeout_error (optional, any, None)
      Timeout


    admin_bind_success (optional, any, None)
      Admin Bind Success


    name (optional, any, None)
      Specify LDAP authentication server name


    pw_change_success (optional, any, None)
      Password change success


    request (optional, any, None)
      Request


    ssl_session_failure (optional, any, None)
      TLS/SSL Session Failure


    search_failure (optional, any, None)
      Search Failure


    admin_bind_failure (optional, any, None)
      Admin Bind Failure


    search_success (optional, any, None)
      Search Success


    authorize_success (optional, any, None)
      Authorization Success


    ssl_session_created (optional, any, None)
      TLS/SSL Session Created



  uuid (False, any, None)
    uuid of the object


  dn_attribute (False, any, None)
    Specify Distinguished Name attribute, default is CN


  state (True, any, None)
    State of the object to be created.


  health_check_disable (False, any, None)
    Disable configured health check configuration


  pwdmaxage (False, any, None)
    Specify the LDAP server's default password expiration time (in seconds) (The LDAP server's default password expiration time (in seconds), default is 0 (no expiration))


  bind_with_dn (False, any, None)
    Enforce using DN for LDAP binding(All user input name will be used to create DN)


  prompt_pw_change_before_exp (False, any, None)
    Prompt user to change password before expiration in N days. This option only takes effect when server type is AD (Prompt user to change password before expiration in N days, default is not to prompt the user)


  admin_secret (False, any, None)
    Specify the LDAP server's admin secret password


  health_check (False, any, None)
    Check server's health status


  ca_cert (False, any, None)
    Specify the LDAPS CA cert filename (Trusted LDAPS CA cert filename)


  default_domain (False, any, None)
    Specify default domain for LDAP


  host (False, any, None)
    Field host


    hostipv6 (optional, any, None)
      Server's IPV6 address


    hostip (optional, any, None)
      Server's hostname(Length 1-31) or IP address



  base (False, any, None)
    Specify the LDAP server's search base


  port_hm (False, any, None)
    Check port's health status


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ldaps_conn_reuse_idle_timeout (False, any, None)
    Specify LDAPS connection reuse idle timeout value (in seconds) (Specify idle timeout value (in seconds), default is 0 (not reuse LDAPS connection))


  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    Specify LDAP authentication server name


  port_hm_disable (False, any, None)
    Disable configured port health check configuration


  timeout (False, any, None)
    Specify timout for LDAP, default is 10 seconds (The timeout, default is 10 seconds)


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

