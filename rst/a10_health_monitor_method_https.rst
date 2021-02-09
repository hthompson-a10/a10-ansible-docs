.. _a10_health_monitor_method_https_module:


a10_health_monitor_method_https -- Configures A10 health.monitor.method.https
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

HTTPS type






Parameters
----------

  https_expect (False, any, None)
    Specify what you expect from the response message


  https_kerberos_auth (False, any, None)
    Https Kerberos Auth


  ansible_username (True, any, None)
    Username for AXAPI authentication


  https_postfile (False, any, None)
    Specify the HTTP post data (Input post data file name here)


  https_text (False, any, None)
    Specify text expected


  https_username (False, any, None)
    Specify the username


  cert_key_shared (False, any, None)
    Select shared partition


  post_type (False, any, None)
    'postdata'= Specify the HTTP post data; 'postfile'= Specify the HTTP post data;


  https_kerberos_kdc (False, any, None)
    Field https_kerberos_kdc


    https_kerberos_hostip (optional, any, None)
      Kdc's hostname(length=1-31) or IP address


    https_kerberos_portv6 (optional, any, None)
      Specify the kdc port


    https_kerberos_hostipv6 (optional, any, None)
      Server's IPV6 address


    https_kerberos_port (optional, any, None)
      Specify the kdc port



  monitor_name (optional, any, None)
    Key to identify parent object


  url_path (False, any, None)
    Specify URL path, default is '/'


  uuid (False, any, None)
    uuid of the object


  https_maintenance_code (False, any, None)
    Specify response code for maintenance (Format is xx,xx-xx (xx between [100, 899])


  a10_partition (False, any, None)
    Destination/target partition for object/command


  https_password (False, any, None)
    Specify the user password


  cert (False, any, None)
    Specify client certificate (Certificate name)


  https_url (False, any, None)
    Specify URL string, default is GET /


  https_encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)


  state (True, any, None)
    State of the object to be created.


  https (False, any, None)
    HTTPS type


  text_regex (False, any, None)
    Specify text expected  with Regex


  ansible_port (True, any, None)
    Port for AXAPI authentication


  post_path (False, any, None)
    Specify URL path, default is '/'


  https_password_string (False, any, None)
    Configure password, '' means empty password


  https_key_encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)


  key (False, any, None)
    Specify client private key (Key name)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  https_kerberos_realm (False, any, None)
    Specify realm of Kerberos server


  disable_sslv2hello (False, any, None)
    Disable SSLv2Hello for HTTPs


  url_type (False, any, None)
    'GET'= HTTP GET method; 'POST'= HTTP POST method; 'HEAD'= HTTP HEAD method;


  ansible_host (True, any, None)
    Host for AXAPI authentication


  https_response_code (False, any, None)
    Specify response code range (e.g. 200,400-430) (Format is xx,xx-xx (xx between [100, 899])


  web_port (False, any, None)
    Specify HTTPS port (Port Number (default 443))


  https_postdata (False, any, None)
    Specify the HTTP post data (Input post data here)


  https_host (False, any, None)
    Specify 'Host=' header used in request (enclose IPv6 address in [])


  response_code_regex (False, any, None)
    Specify response code range with Regex (code with Regex, such as [2-5][0-9][0-9])


  key_pass_phrase (False, any, None)
    Client private key password phrase


  key_phrase (False, any, None)
    Password Phrase


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

