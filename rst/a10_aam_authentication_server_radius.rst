.. _a10_aam_authentication_server_radius_module:


a10_aam_authentication_server_radius -- Configures A10 aam.authentication.server.radius
=======================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

RADIUS Authentication Server






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'authen_success'= Total Authentication Success; 'authen_failure'= Total Authentication Failure; 'authorize_success'= Total Authorization Success; 'authorize_failure'= Total Authorization Failure; 'access_challenge'= Total Access-Challenge Message Receive; 'timeout_error'= Total Timeout; 'other_error'= Total Other Error; 'request'= Total Request; 'request-normal'= Total Normal Request; 'request-dropped'= Total Dropped Request; 'response- success'= Total Success Response; 'response-failure'= Total Failure Response; 'response-error'= Total Error Response; 'response-timeout'= Total Timeout Response; 'response-other'= Total Other Response; 'job-start-error'= Total Job Start Error; 'polling-control-error'= Total Polling Control Error; 'accounting- request-sent'= Accounting-Request Sent; 'accounting-success'= Accounting Success; 'accounting-failure'= Accounting Failure;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    response_timeout (optional, any, None)
      Total Timeout Response


    access_challenge (optional, any, None)
      Total Access-Challenge Message Receive


    other_error (optional, any, None)
      Total Other Error


    request_normal (optional, any, None)
      Total Normal Request


    accounting_request_sent (optional, any, None)
      Accounting-Request Sent


    response_success (optional, any, None)
      Total Success Response


    accounting_success (optional, any, None)
      Accounting Success


    response_other (optional, any, None)
      Total Other Response


    authen_failure (optional, any, None)
      Total Authentication Failure


    timeout_error (optional, any, None)
      Total Timeout


    response_error (optional, any, None)
      Total Error Response


    authorize_failure (optional, any, None)
      Total Authorization Failure


    response_failure (optional, any, None)
      Total Failure Response


    polling_control_error (optional, any, None)
      Total Polling Control Error


    request (optional, any, None)
      Total Request


    instance_list (optional, any, None)
      Field instance_list


    accounting_failure (optional, any, None)
      Accounting Failure


    request_dropped (optional, any, None)
      Total Dropped Request


    job_start_error (optional, any, None)
      Total Job Start Error


    authen_success (optional, any, None)
      Total Authentication Success


    authorize_success (optional, any, None)
      Total Authorization Success



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  instance_list (False, any, None)
    Field instance_list


    auth_type (optional, any, None)
      'pap'= PAP authentication. Default; 'mschapv2'= MS-CHAPv2 authentication; 'mschapv2-pap'= Use MS-CHAPv2 first. If server doesn't support it, try PAP;


    secret_string (optional, any, None)
      The RADIUS server's secret


    acct_port_hm (optional, any, None)
      Specify accounting port health check method


    health_check (optional, any, None)
      Check server's health status


    encrypted (optional, any, None)
      Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)


    host (optional, any, None)
      Field host


    port_hm (optional, any, None)
      Check port's health status


    acct_port_hm_disable (optional, any, None)
      Disable configured accounting port health check configuration


    port (optional, any, None)
      Specify the RADIUS server's authentication port, default is 1812


    health_check_disable (optional, any, None)
      Disable configured health check configuration


    name (optional, any, None)
      Specify RADIUS authentication server name


    accounting_port (optional, any, None)
      Specify the RADIUS server's accounting port, default is 1813


    retry (optional, any, None)
      Specify the retry number for resend the request, default is 5 (The retry number, default is 5)


    uuid (optional, any, None)
      uuid of the object


    interval (optional, any, None)
      Specify the interval time for resend the request (second), default is 3 seconds (The interval time(second), default is 3 seconds)


    port_hm_disable (optional, any, None)
      Disable configured port health check configuration


    secret (optional, any, None)
      Specify the RADIUS server's secret


    health_check_string (optional, any, None)
      Health monitor name


    sampling_enable (optional, any, None)
      Field sampling_enable



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

