.. _a10_health_monitor_method_http_module:


a10_health_monitor_method_http -- Configures A10 health.monitor.method.http
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

HTTP type






Parameters
----------

  http_username (False, any, None)
    Specify the username


  ansible_username (True, any, None)
    Username for AXAPI authentication


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  post_type (False, any, None)
    'postdata'= Specify the HTTP post data; 'postfile'= Specify the HTTP post data;


  http_text (False, any, None)
    Specify text expected


  monitor_name (optional, any, None)
    Key to identify parent object


  http_password (False, any, None)
    Specify the user password


  http_port (False, any, None)
    Specify HTTP Port (Specify port number (default 80))


  uuid (False, any, None)
    uuid of the object


  http_encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)


  state (True, any, None)
    State of the object to be created.


  http_kerberos_realm (False, any, None)
    Specify realm of Kerberos server


  text_regex (False, any, None)
    Specify text expected  with Regex


  http_maintenance_code (False, any, None)
    Specify response code for maintenance (Format is xx,xx-xx (xx between [100, 899]))


  http_url (False, any, None)
    Specify URL string, default is GET /


  http_postdata (False, any, None)
    Specify the HTTP post data (Input post data here)


  post_path (False, any, None)
    Specify URL path, default is '/'


  http (False, any, None)
    HTTP type


  http_host (False, any, None)
    Specify 'Host=' header used in request (enclose IPv6 address in [])


  url_type (False, any, None)
    'GET'= HTTP GET method; 'POST'= HTTP POST method; 'HEAD'= HTTP HEAD method;


  http_kerberos_kdc (False, any, None)
    Field http_kerberos_kdc


    http_kerberos_hostipv6 (optional, any, None)
      Server's IPV6 address


    http_kerberos_port (optional, any, None)
      Specify the kdc port


    http_kerberos_portv6 (optional, any, None)
      Specify the kdc port


    http_kerberos_hostip (optional, any, None)
      Kdc's hostname(length=1-31) or IP address



  url_path (False, any, None)
    Specify URL path, default is '/'


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ansible_port (True, any, None)
    Port for AXAPI authentication


  http_response_code (False, any, None)
    Specify response code range (e.g. 200,400-430) (Format is xx,xx-xx (xx between [100, 899]))


  http_kerberos_auth (False, any, None)
    Http Kerberos Auth


  response_code_regex (False, any, None)
    Specify response code range with Regex (code with Regex, such as [2-5][0-9][0-9])


  http_expect (False, any, None)
    Specify what you expect from the response message


  http_postfile (False, any, None)
    Specify the HTTP post data (Input post data file name here)


  http_password_string (False, any, None)
    Specify password, '' means empty password


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

