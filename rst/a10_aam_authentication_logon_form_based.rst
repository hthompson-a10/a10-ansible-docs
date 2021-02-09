.. _a10_aam_authentication_logon_form_based_module:


a10_aam_authentication_logon_form_based -- Configures A10 aam.authentication.logon.form-based
=============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Form-based Authentication Logon






Parameters
----------

  ansible_username (True, any, None)
    Username for AXAPI authentication


  logon_page_cfg (False, any, None)
    Field logon_page_cfg


    authz_failure_message (optional, any, None)
      Specify authorization failure message shown in logon page (Specify error string, default is 'Authorization failed. Please contact your system administrator.')


    password_variable (optional, any, None)
      Specify password variable name in form submission


    login_failure_message (optional, any, None)
      Specify login failure message shown in logon page (Specify error string, default is 'Invalid username or password. Please try again.')


    username_variable (optional, any, None)
      Specify username variable name in form submission


    disable_change_password_link (optional, any, None)
      Don't display change password link on logon page forcibly even backend authentication server supports it (LDAP or Kerberos)


    action_url (optional, any, None)
      Specify form submission action url


    passcode_variable (optional, any, None)
      Specify passcode variable name in form submission



  new_pin_variable (False, any, None)
    Specify new-pin variable name in form submission


  retry (False, any, None)
    Maximum number of consecutive failed logon attempts (default 3)


  portal (False, any, None)
    Field portal


    new_pin_page (optional, any, None)
      Specify new PIN page name for RSA-RADIUS


    portal_name (optional, any, None)
      Specify portal name


    challenge_page (optional, any, None)
      Specify challenge page name for RSA-RADIUS


    failpage (optional, any, None)
      Specify logon fail page name (portal fail page name)


    default_portal (optional, any, None)
      Use default portal


    notifychangepasswordpage (optional, any, None)
      Specify change password notification page name


    changepasswordpage (optional, any, None)
      Specify change password page name


    next_token_page (optional, any, None)
      Specify next token page name for RSA-RADIUS


    logon (optional, any, None)
      Specify logon page name



  duration (False, any, None)
    The time an account remains locked in seconds (default 1800)


  notify_cp_page_cfg (False, any, None)
    Field notify_cp_page_cfg


    notifychangepassword_continue_url (optional, any, None)
      Specify continue action url for notifychangepassword form


    notifychangepassword_change_url (optional, any, None)
      Specify change password action url for notifychangepassword form



  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  challenge_variable (False, any, None)
    Specify challenge variable name in form submission


  ansible_port (True, any, None)
    Port for AXAPI authentication


  next_token_variable (False, any, None)
    Specify next-token variable name in form submission


  name (True, any, None)
    Specify form-based authentication logon name


  cp_page_cfg (False, any, None)
    Field cp_page_cfg


    cp_user_var (optional, any, None)
      Specify username variable name


    cp_new_pwd_enum (optional, any, None)
      'changepassword-new-password-variable'= Specify new password variable name in form submission;


    changepassword_url (optional, any, None)
      Specify changepassword form submission action url (changepassword action url)


    cp_cfm_pwd_var (optional, any, None)
      Specify password confirm variable name


    cp_new_pwd_var (optional, any, None)
      Specify new password variable name


    cp_cfm_pwd_enum (optional, any, None)
      'changepassword-password-confirm-variable'= Specify password confirm variable name in form submission;


    cp_old_pwd_enum (optional, any, None)
      'changepassword-old-password-variable'= Specify old password variable name in form submission;


    cp_user_enum (optional, any, None)
      'changepassword-username-variable'= Specify username variable name in form submission;


    cp_old_pwd_var (optional, any, None)
      Specify old password variable name



  user_tag (False, any, None)
    Customized tag


  account_lock (False, any, None)
    Lock the account when the failed logon attempts is exceeded


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  ansible_password (True, any, None)
    Password for AXAPI authentication









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

