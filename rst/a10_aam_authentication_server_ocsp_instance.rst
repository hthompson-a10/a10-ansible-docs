.. _a10_aam_authentication_server_ocsp_instance_module:


a10_aam_authentication_server_ocsp_instance -- Configures A10 aam.authentication.server.ocsp.instance
=====================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Specify OCSP authentication server name






Parameters
----------

  health_check (False, any, None)
    Check server's health status


  ansible_username (True, any, None)
    Username for AXAPI authentication


  port_health_check (False, any, None)
    Check port's health status


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  health_check_disable (False, any, None)
    Disable configured health check configuration


  uuid (False, any, None)
    uuid of the object


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'request'= Request; 'certificate-good'= Good Certificate Response; 'certificate-revoked'= Revoked Certificate Response; 'certificate-unknown'= Unknown Certificate Response; 'timeout'= Timeout; 'fail'= Handle OCSP response failed; 'stapling-request'= OCSP Stapling Request Send; 'stapling-certificate- good'= OCSP Stapling Good Certificate Response; 'stapling-certificate-revoked'= OCSP Stapling Revoked Certificate Response; 'stapling-certificate-unknown'= OCSP Stapling Unknown Certificate Response; 'stapling-timeout'= OCSP Stapling Timeout; 'stapling-fail'= Handle OCSP response failed;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    stapling_certificate_unknown (optional, any, None)
      OCSP Stapling Unknown Certificate Response


    stapling_request (optional, any, None)
      OCSP Stapling Request Send


    request (optional, any, None)
      Request


    stapling_fail (optional, any, None)
      Handle OCSP response failed


    certificate_good (optional, any, None)
      Good Certificate Response


    certificate_unknown (optional, any, None)
      Unknown Certificate Response


    timeout (optional, any, None)
      Timeout


    stapling_certificate_good (optional, any, None)
      OCSP Stapling Good Certificate Response


    fail (optional, any, None)
      Handle OCSP response failed


    certificate_revoked (optional, any, None)
      Revoked Certificate Response


    stapling_certificate_revoked (optional, any, None)
      OCSP Stapling Revoked Certificate Response


    stapling_timeout (optional, any, None)
      OCSP Stapling Timeout


    name (optional, any, None)
      Specify OCSP authentication server name



  name (True, any, None)
    Specify OCSP authentication server name


  version_type (False, any, None)
    '1.1'= HTTP version 1.1;


  url (False, any, None)
    Specify the OCSP server's address (Format= http=//host[=port]/) (The OCSP server's address(Format= http=//host[=port]/))


  http_version (False, any, None)
    Set HTTP version (default 1.0)


  responder_cert (False, any, None)
    Specify the trusted OCSP responder's cert filename


  state (True, any, None)
    State of the object to be created.


  responder_ca (False, any, None)
    Specify the trusted OCSP responder's CA cert filename


  ansible_password (True, any, None)
    Password for AXAPI authentication


  health_check_string (False, any, None)
    Health monitor name


  port_health_check_disable (False, any, None)
    Disable configured port health check configuration









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

