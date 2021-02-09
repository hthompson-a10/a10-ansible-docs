.. _a10_aam_authentication_portal_module:


a10_aam_authentication_portal -- Configures A10 aam.authentication.portal
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Authentication portal configuration






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    'default-portal'= Default portal configuration;


  ansible_username (True, any, None)
    Username for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  logo_cfg (False, any, None)
    Field logo_cfg


    logo (optional, any, None)
      Specify logo image filename


    width (optional, any, None)
      Specify logo image width (Default= 134)


    height (optional, any, None)
      Specify logo image height (Default= 71)



  ansible_password (True, any, None)
    Password for AXAPI authentication


  ansible_host (True, any, None)
    Host for AXAPI authentication


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  change_password (False, any, None)
    Field change_password


    submit_text (optional, any, None)
      Specify submit button text in default change password page (Default= Submit)


    cfm_pwd_cfg (optional, any, None)
      Field cfm_pwd_cfg


    background (optional, any, None)
      Field background


    username_var (optional, any, None)
      Specify username variable name in default change password page (Default= cp_usr)


    username_cfg (optional, any, None)
      Field username_cfg


    new_pwd_cfg (optional, any, None)
      Field new_pwd_cfg


    old_password_var (optional, any, None)
      Specify old password variable name in default change password page (Default= cp_old_pwd)


    action_url (optional, any, None)
      Specify form action URL in default change password page (Default= /change.fo)


    old_pwd_cfg (optional, any, None)
      Field old_pwd_cfg


    title_cfg (optional, any, None)
      Field title_cfg


    confirm_password_var (optional, any, None)
      Specify confirm password variable name in default change password page (Default= cp_cfm_pwd)


    reset_text (optional, any, None)
      Specify reset button text in default change password page (Default= Reset)


    new_password_var (optional, any, None)
      Specify new password variable name in default change password page (Default= cp_new_pwd)


    uuid (optional, any, None)
      uuid of the object



  notify_change_password (False, any, None)
    Field notify_change_password


    change_url (optional, any, None)
      Specify change password action URL in default change password notification page (Default= /notify_change.fo)


    cfm_pwd_cfg (optional, any, None)
      Field cfm_pwd_cfg


    background (optional, any, None)
      Field background


    username_var (optional, any, None)
      Specify username variable name in default change password notification page (Default= cp_usr)


    username_cfg (optional, any, None)
      Field username_cfg


    new_pwd_cfg (optional, any, None)
      Field new_pwd_cfg


    old_password_var (optional, any, None)
      Specify old password variable name in default change password notification page (Default= cp_old_pwd)


    continue_url (optional, any, None)
      Specify continue action URL in default change password notification page (Default= /continue.fo)


    change_text (optional, any, None)
      Specify change button text in default change password notification page (Default= Change)


    old_pwd_cfg (optional, any, None)
      Field old_pwd_cfg


    new_password_var (optional, any, None)
      Specify new password variable name in default change password notification page (Default= cp_new_pwd)


    confirm_password_var (optional, any, None)
      Specify confirm password variable name in default change password notification page (Default= cp_cfm_pwd)


    continue_text (optional, any, None)
      Specify continue button text in default change password notification page (Default= Continue)


    uuid (optional, any, None)
      uuid of the object



  logon (False, any, None)
    Field logon


    submit_text (optional, any, None)
      Specify submit button text in default logon page (Default= Log In)


    uuid (optional, any, None)
      uuid of the object


    username_var (optional, any, None)
      Specify username variable name in default logon page (Default= user)


    username_cfg (optional, any, None)
      Field username_cfg


    passcode_var (optional, any, None)
      Specify passcode variable name in default logon page (Default= passcode)


    enable_passcode (optional, any, None)
      Enable passcode field in default logon page


    fail_msg_cfg (optional, any, None)
      Field fail_msg_cfg


    action_url (optional, any, None)
      Specify form action URL in default logon page (Default= /logon.fo)


    password_cfg (optional, any, None)
      Field password_cfg


    background (optional, any, None)
      Field background


    password_var (optional, any, None)
      Specify password variable name in default logon page (Default= pwd)


    passcode_cfg (optional, any, None)
      Field passcode_cfg



  a10_partition (False, any, None)
    Destination/target partition for object/command


  logon_fail (False, any, None)
    Field logon_fail


    fail_msg_cfg (optional, any, None)
      Field fail_msg_cfg


    title_cfg (optional, any, None)
      Field title_cfg


    uuid (optional, any, None)
      uuid of the object


    background (optional, any, None)
      Field background



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

