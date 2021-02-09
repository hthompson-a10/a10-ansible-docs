.. _a10_aam_authentication_server_ocsp_module:


a10_aam_authentication_server_ocsp -- Configures A10 aam.authentication.server.ocsp
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

OCSP Authentication Server






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'stapling-certificate-good'= Total OCSP Stapling Good Certificate Response; 'stapling-certificate-revoked'= Total OCSP Stapling Revoked Certificate Response; 'stapling-certificate-unknown'= Total OCSP Stapling Unknown Certificate Response; 'stapling-request-normal'= Total OSCP Stapling Normal Request; 'stapling-request-dropped'= Total OCSP Stapling Dropped Request; 'stapling-response-success'= Total OCSP Stapling Success Response; 'stapling-response-failure'= Total OCSP Stapling Failure Response; 'stapling- response-error'= Total OCSP Stapling Error Response; 'stapling-response- timeout'= Total OCSP Stapling Timeout Response; 'stapling-response-other'= Total OCSP Stapling Other Response; 'request-normal'= Total OSCP Normal Request; 'request-dropped'= Total OCSP Dropped Request; 'response-success'= Total OCSP Success Response; 'response-failure'= Total OCSP Failure Response; 'response-error'= Total OCSP Error Response; 'response-timeout'= Total OCSP Timeout Response; 'response-other'= Total OCSP Other Response; 'job-start- error'= Total OCSP Job Start Error; 'polling-control-error'= Total OCSP Polling Control Error;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    stapling_response_error (optional, any, None)
      Total OCSP Stapling Error Response


    response_timeout (optional, any, None)
      Total OCSP Timeout Response


    stapling_response_success (optional, any, None)
      Total OCSP Stapling Success Response


    request_normal (optional, any, None)
      Total OSCP Normal Request


    response_success (optional, any, None)
      Total OCSP Success Response


    response_other (optional, any, None)
      Total OCSP Other Response


    response_error (optional, any, None)
      Total OCSP Error Response


    stapling_response_failure (optional, any, None)
      Total OCSP Stapling Failure Response


    stapling_certificate_unknown (optional, any, None)
      Total OCSP Stapling Unknown Certificate Response


    response_failure (optional, any, None)
      Total OCSP Failure Response


    stapling_request_normal (optional, any, None)
      Total OSCP Stapling Normal Request


    polling_control_error (optional, any, None)
      Total OCSP Polling Control Error


    stapling_request_dropped (optional, any, None)
      Total OCSP Stapling Dropped Request


    instance_list (optional, any, None)
      Field instance_list


    request_dropped (optional, any, None)
      Total OCSP Dropped Request


    job_start_error (optional, any, None)
      Total OCSP Job Start Error


    stapling_certificate_good (optional, any, None)
      Total OCSP Stapling Good Certificate Response


    stapling_certificate_revoked (optional, any, None)
      Total OCSP Stapling Revoked Certificate Response


    stapling_response_other (optional, any, None)
      Total OCSP Stapling Other Response


    stapling_response_timeout (optional, any, None)
      Total OCSP Stapling Timeout Response



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


    responder_ca (optional, any, None)
      Specify the trusted OCSP responder's CA cert filename


    health_check (optional, any, None)
      Check server's health status


    name (optional, any, None)
      Specify OCSP authentication server name


    version_type (optional, any, None)
      '1.1'= HTTP version 1.1;


    url (optional, any, None)
      Specify the OCSP server's address (Format= http=//host[=port]/) (The OCSP server's address(Format= http=//host[=port]/))


    http_version (optional, any, None)
      Set HTTP version (default 1.0)


    port_health_check (optional, any, None)
      Check port's health status


    health_check_string (optional, any, None)
      Health monitor name


    responder_cert (optional, any, None)
      Specify the trusted OCSP responder's cert filename


    port_health_check_disable (optional, any, None)
      Disable configured port health check configuration


    health_check_disable (optional, any, None)
      Disable configured health check configuration


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

