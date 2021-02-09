.. _a10_aam_authentication_relay_kerberos_module:


a10_aam_authentication_relay_kerberos -- Configures A10 aam.authentication.relay.kerberos
=========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Kerberos Authentication Relay






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'request-send'= Total Request Send; 'response-get'= Total Response Get; 'timeout-error'= Total Timeout; 'other-error'= Total Other Error; 'request-normal'= Total Normal Request; 'request-dropped'= Total Dropped Request; 'response-success'= Total Success Response; 'response-failure'= Total Failure Response; 'response-error'= Total Error Response; 'response-timeout'= Total Timeout Response; 'response-other'= Total Other Response; 'job-start- error'= Total Job Start Error; 'polling-control-error'= Total Polling Control Error;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    response_timeout (optional, any, None)
      Total Timeout Response


    other_error (optional, any, None)
      Total Other Error


    response_failure (optional, any, None)
      Total Failure Response


    response_success (optional, any, None)
      Total Success Response


    response_get (optional, any, None)
      Total Response Get


    polling_control_error (optional, any, None)
      Total Polling Control Error


    request_normal (optional, any, None)
      Total Normal Request


    instance_list (optional, any, None)
      Field instance_list


    request_dropped (optional, any, None)
      Total Dropped Request


    request_send (optional, any, None)
      Total Request Send


    response_other (optional, any, None)
      Total Other Response


    job_start_error (optional, any, None)
      Total Job Start Error


    timeout_error (optional, any, None)
      Total Timeout


    response_error (optional, any, None)
      Total Error Response



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  instance_list (False, any, None)
    Field instance_list


    sampling_enable (optional, any, None)
      Field sampling_enable


    kerberos_realm (optional, any, None)
      Specify the kerberos realm


    name (optional, any, None)
      Specify Kerberos authentication relay name


    secret_string (optional, any, None)
      The kerberos client password


    encrypted (optional, any, None)
      Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)


    kerberos_account (optional, any, None)
      Specify the kerberos account name


    kerberos_kdc_service_group (optional, any, None)
      Specify an authentication service group as multiple KDCs


    kerberos_kdc (optional, any, None)
      Specify the kerberos kdc ip or host name


    timeout (optional, any, None)
      Specify timeout for kerberos transport, default is 10 seconds (The timeout, default is 10 seconds)


    password (optional, any, None)
      Specify password of Kerberos password


    port (optional, any, None)
      Specify The KDC port, default is 88


    uuid (optional, any, None)
      uuid of the object



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

