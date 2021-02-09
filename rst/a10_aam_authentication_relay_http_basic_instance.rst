.. _a10_aam_authentication_relay_http_basic_instance_module:


a10_aam_authentication_relay_http_basic_instance -- Configures A10 aam.authentication.relay.http.basic.instance
===============================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

HTTP Basic Authentication Relay instance






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'success'= Success; 'no-creds'= No Credential; 'bad-req'= Bad Request; 'unauth'= Unauthorized; 'forbidden'= Forbidden; 'not-found'= Not Found; 'server-error'= Internal Server Error; 'unavailable'= Service Unavailable;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    server_error (optional, any, None)
      Internal Server Error


    bad_req (optional, any, None)
      Bad Request


    unavailable (optional, any, None)
      Service Unavailable


    success (optional, any, None)
      Success


    forbidden (optional, any, None)
      Forbidden


    no_creds (optional, any, None)
      No Credential


    unauth (optional, any, None)
      Unauthorized


    not_found (optional, any, None)
      Not Found


    name (optional, any, None)
      Specify HTTP basic authentication relay name



  name (True, any, None)
    Specify HTTP basic authentication relay name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  domain (False, any, None)
    Specify user domain, default is null


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  domain_format (False, any, None)
    'user-principal-name'= Append domain with User Principal Name format. (e.g. user@domain); 'down-level-logon-name'= Append domain with Down-Level Logon Name format. (e.g. domain\user);


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


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

