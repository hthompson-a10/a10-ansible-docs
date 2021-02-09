.. _a10_visibility_reporting_template_notification_template_name_authentication_module:


a10_visibility_reporting_template_notification_template_name_authentication -- Configures A10 visibility.reporting.template.notification.template.name.authentication
=====================================================================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure authentication information






Parameters
----------

  auth_password_string (False, any, None)
    Configure the authentication user password (Authentication password)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)


  relative_logoff_uri (False, any, None)
    Configure the authentication logoff uri


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  api_key_string (False, any, None)
    Configure api-key as a mode of authentication


  auth_password (False, any, None)
    Configure the authentication user password (Authentication password)


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  auth_username (False, any, None)
    Configure the authentication user name


  state (True, any, None)
    State of the object to be created.


  template_name_name (optional, any, None)
    Key to identify parent object


  relative_login_uri (False, any, None)
    Configure the authentication login uri


  api_key_encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)


  api_key (False, any, None)
    Configure api-key as a mode of authentication


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

