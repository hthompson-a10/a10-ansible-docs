.. _a10_visibility_reporting_template_notification_template_name_module:


a10_visibility_reporting_template_notification_template_name -- Configures A10 visibility.reporting.template.notification.template-name
=======================================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Notification template configuration






Parameters
----------

  ipv6_address (False, any, None)
    Configure the host IPv6 address


  relative_uri (False, any, None)
    Configure the relative uri(e.g /example , default /)


  protocol (False, any, None)
    'http'= Use http protocol; 'https'= Use https protocol(default);  (http protocol)


  https_port (False, any, None)
    Configure the https port to use(default 443) (http port(default 443))


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ipv4_address (False, any, None)
    Configure the host IPv4 address


  test_connectivity (False, any, None)
    Test connectivity to notification receiver


  use_mgmt_port (False, any, None)
    Use management port for notifications


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  name (True, any, None)
    Notification template name


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'sent_successful'= Sent successful; 'send_fail'= Send failures; 'response_fail'= Response failures;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  http_port (False, any, None)
    Configure the http port to use(default 80) (http port(default 80))


  stats (False, any, None)
    Field stats


    sent_successful (optional, any, None)
      Sent successful


    send_fail (optional, any, None)
      Send failures


    name (optional, any, None)
      Notification template name


    response_fail (optional, any, None)
      Response failures



  uuid (False, any, None)
    uuid of the object


  authentication (False, any, None)
    Field authentication


    auth_password_string (optional, any, None)
      Configure the authentication user password (Authentication password)


    auth_password (optional, any, None)
      Configure the authentication user password (Authentication password)


    uuid (optional, any, None)
      uuid of the object


    encrypted (optional, any, None)
      Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)


    relative_logoff_uri (optional, any, None)
      Configure the authentication logoff uri


    api_key_encrypted (optional, any, None)
      Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)


    relative_login_uri (optional, any, None)
      Configure the authentication login uri


    api_key_string (optional, any, None)
      Configure api-key as a mode of authentication


    api_key (optional, any, None)
      Configure api-key as a mode of authentication


    auth_username (optional, any, None)
      Configure the authentication user name



  state (True, any, None)
    State of the object to be created.


  debug_mode (False, any, None)
    Enable debug mode


  host_name (False, any, None)
    Configure the host name(e.g www.a10networks.com)


  action (False, any, None)
    'enable'= Enable; 'disable'= Disable;


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

