.. _a10_aam_authentication_server_ldap_module:


a10_aam_authentication_server_ldap -- Configures A10 aam.authentication.server.ldap
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

LDAP Authentication Server






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'admin-bind-success'= Total Admin Bind Success; 'admin-bind- failure'= Total Admin Bind Failure; 'bind-success'= Total User Bind Success; 'bind-failure'= Total User Bind Failure; 'search-success'= Total Search Success; 'search-failure'= Total Search Failure; 'authorize-success'= Total Authorization Success; 'authorize-failure'= Total Authorization Failure; 'timeout-error'= Total Timeout; 'other-error'= Total Other Error; 'request'= Total Request; 'request-normal'= Total Normal Request; 'request-dropped'= Total Dropped Request; 'response-success'= Total Success Response; 'response- failure'= Total Failure Response; 'response-error'= Total Error Response; 'response-timeout'= Total Timeout Response; 'response-other'= Total Other Response; 'job-start-error'= Total Job Start Error; 'polling-control-error'= Total Polling Control Error; 'ssl-session-created'= TLS/SSL Session Created; 'ssl-session-failure'= TLS/SSL Session Failure; 'ldaps-idle-conn-num'= LDAPS Idle Connection Number; 'ldaps-inuse-conn-num'= LDAPS In-use Connection Number; 'pw-expiry'= Total Password expiry; 'pw-change-success'= Total password change success; 'pw-change-failure'= Total password change failure;



  oper (False, any, None)
    Field oper


    ldaps_server_list (optional, any, None)
      Field ldaps_server_list



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    response_timeout (optional, any, None)
      Total Timeout Response


    bind_success (optional, any, None)
      Total User Bind Success


    other_error (optional, any, None)
      Total Other Error


    pw_change_failure (optional, any, None)
      Total password change failure


    request_normal (optional, any, None)
      Total Normal Request


    pw_expiry (optional, any, None)
      Total Password expiry


    response_success (optional, any, None)
      Total Success Response


    bind_failure (optional, any, None)
      Total User Bind Failure


    authorize_failure (optional, any, None)
      Total Authorization Failure


    response_other (optional, any, None)
      Total Other Response


    timeout_error (optional, any, None)
      Total Timeout


    response_error (optional, any, None)
      Total Error Response


    admin_bind_success (optional, any, None)
      Total Admin Bind Success


    instance_list (optional, any, None)
      Field instance_list


    response_failure (optional, any, None)
      Total Failure Response


    pw_change_success (optional, any, None)
      Total password change success


    polling_control_error (optional, any, None)
      Total Polling Control Error


    ldaps_idle_conn_num (optional, any, None)
      LDAPS Idle Connection Number


    ldaps_inuse_conn_num (optional, any, None)
      LDAPS In-use Connection Number


    request (optional, any, None)
      Total Request


    ssl_session_failure (optional, any, None)
      TLS/SSL Session Failure


    search_failure (optional, any, None)
      Total Search Failure


    request_dropped (optional, any, None)
      Total Dropped Request


    admin_bind_failure (optional, any, None)
      Total Admin Bind Failure


    job_start_error (optional, any, None)
      Total Job Start Error


    search_success (optional, any, None)
      Total Search Success


    authorize_success (optional, any, None)
      Total Authorization Success


    ssl_session_created (optional, any, None)
      TLS/SSL Session Created



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  instance_list (False, any, None)
    Field instance_list


    auth_type (optional, any, None)
      'ad'= Active Directory. Default; 'open-ldap'= OpenLDAP;


    secret_string (optional, any, None)
      secret password


    health_check (optional, any, None)
      Check server's health status


    protocol (optional, any, None)
      'ldap'= Use LDAP (default); 'ldaps'= Use LDAP over SSL; 'starttls'= Use LDAP StartTLS;


    health_check_string (optional, any, None)
      Health monitor name


    ca_cert (optional, any, None)
      Specify the LDAPS CA cert filename (Trusted LDAPS CA cert filename)


    encrypted (optional, any, None)
      Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)


    default_domain (optional, any, None)
      Specify default domain for LDAP


    host (optional, any, None)
      Field host


    base (optional, any, None)
      Specify the LDAP server's search base


    derive_bind_dn (optional, any, None)
      Field derive_bind_dn


    port_hm (optional, any, None)
      Check port's health status


    port (optional, any, None)
      Specify the LDAP server's authentication port, default is 389


    ldaps_conn_reuse_idle_timeout (optional, any, None)
      Specify LDAPS connection reuse idle timeout value (in seconds) (Specify idle timeout value (in seconds), default is 0 (not reuse LDAPS connection))


    name (optional, any, None)
      Specify LDAP authentication server name


    sampling_enable (optional, any, None)
      Field sampling_enable


    admin_dn (optional, any, None)
      The LDAP server's admin DN


    uuid (optional, any, None)
      uuid of the object


    dn_attribute (optional, any, None)
      Specify Distinguished Name attribute, default is CN


    port_hm_disable (optional, any, None)
      Disable configured port health check configuration


    admin_secret (optional, any, None)
      Specify the LDAP server's admin secret password


    health_check_disable (optional, any, None)
      Disable configured health check configuration


    timeout (optional, any, None)
      Specify timout for LDAP, default is 10 seconds (The timeout, default is 10 seconds)


    pwdmaxage (optional, any, None)
      Specify the LDAP server's default password expiration time (in seconds) (The LDAP server's default password expiration time (in seconds), default is 0 (no expiration))


    bind_with_dn (optional, any, None)
      Enforce using DN for LDAP binding(All user input name will be used to create DN)


    prompt_pw_change_before_exp (optional, any, None)
      Prompt user to change password before expiration in N days. This option only takes effect when server type is AD (Prompt user to change password before expiration in N days, default is not to prompt the user)



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

