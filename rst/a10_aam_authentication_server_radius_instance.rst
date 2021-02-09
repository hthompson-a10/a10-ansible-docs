.. _a10_aam_authentication_server_radius_instance_module:


a10_aam_authentication_server_radius_instance -- Configures A10 aam.authentication.server.radius.instance
=========================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

RADIUS Authentication Server instance






Parameters
----------

  auth_type (False, any, None)
    'pap'= PAP authentication. Default; 'mschapv2'= MS-CHAPv2 authentication; 'mschapv2-pap'= Use MS-CHAPv2 first. If server doesn't support it, try PAP;


  secret_string (False, any, None)
    The RADIUS server's secret


  health_check (False, any, None)
    Check server's health status


  name (True, any, None)
    Specify RADIUS authentication server name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)


  host (False, any, None)
    Field host


    hostipv6 (optional, any, None)
      Server's IPV6 address


    hostip (optional, any, None)
      Server's hostname(Length 1-31) or IP address



  port_hm (False, any, None)
    Check port's health status


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  port_hm_disable (False, any, None)
    Disable configured port health check configuration


  acct_port_hm_disable (False, any, None)
    Disable configured accounting port health check configuration


  port (False, any, None)
    Specify the RADIUS server's authentication port, default is 1812


  health_check_disable (False, any, None)
    Disable configured health check configuration


  acct_port_hm (False, any, None)
    Specify accounting port health check method


  accounting_port (False, any, None)
    Specify the RADIUS server's accounting port, default is 1813


  ansible_port (True, any, None)
    Port for AXAPI authentication


  retry (False, any, None)
    Specify the retry number for resend the request, default is 5 (The retry number, default is 5)


  stats (False, any, None)
    Field stats


    authorize_failure (optional, any, None)
      Authorization Failure


    name (optional, any, None)
      Specify RADIUS authentication server name


    other_error (optional, any, None)
      Other Error


    request (optional, any, None)
      Request


    accounting_request_sent (optional, any, None)
      Accounting-Request Sent


    accounting_failure (optional, any, None)
      Accounting Failure


    authen_success (optional, any, None)
      Authentication Success


    access_challenge (optional, any, None)
      Access-Challenge Message Receive


    authen_failure (optional, any, None)
      Authentication Failure


    timeout_error (optional, any, None)
      Timeout


    authorize_success (optional, any, None)
      Authorization Success


    accounting_success (optional, any, None)
      Accounting Success



  uuid (False, any, None)
    uuid of the object


  a10_partition (False, any, None)
    Destination/target partition for object/command


  interval (False, any, None)
    Specify the interval time for resend the request (second), default is 3 seconds (The interval time(second), default is 3 seconds)


  secret (False, any, None)
    Specify the RADIUS server's secret


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  ansible_password (True, any, None)
    Password for AXAPI authentication


  health_check_string (False, any, None)
    Health monitor name


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'authen_success'= Authentication Success; 'authen_failure'= Authentication Failure; 'authorize_success'= Authorization Success; 'authorize_failure'= Authorization Failure; 'access_challenge'= Access- Challenge Message Receive; 'timeout_error'= Timeout; 'other_error'= Other Error; 'request'= Request; 'accounting-request-sent'= Accounting-Request Sent; 'accounting-success'= Accounting Success; 'accounting-failure'= Accounting Failure;










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

