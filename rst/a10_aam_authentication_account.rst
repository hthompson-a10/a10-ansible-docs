.. _a10_aam_authentication_account_module:


a10_aam_authentication_account -- Configures A10 aam.authentication.account
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Authentication account configuration






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'request-normal'= Total Normal Request; 'request-dropped'= Total Dropped Request; 'response-success'= Total Success Response; 'response- failure'= Total Failure Response; 'response-error'= Total Error Response; 'response-timeout'= Total Timeout Response; 'response-other'= Total Other Response;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    response_timeout (optional, any, None)
      Total Timeout Response


    request_dropped (optional, any, None)
      Total Dropped Request


    response_failure (optional, any, None)
      Total Failure Response


    response_success (optional, any, None)
      Total Success Response


    response_other (optional, any, None)
      Total Other Response


    response_error (optional, any, None)
      Total Error Response


    request_normal (optional, any, None)
      Total Normal Request



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  kerberos_spn_list (False, any, None)
    Field kerberos_spn_list


    secret_string (optional, any, None)
      Password of AD account


    account (optional, any, None)
      Specify domain account for SPN


    realm (optional, any, None)
      Specify Kerberos realm


    name (optional, any, None)
      Specify AD account name


    encrypted (optional, any, None)
      Do NOT use this option manually. (This is an A10 reserved keyword.)


    service_principal_name (optional, any, None)
      Specify service principal name


    password (optional, any, None)
      Specify password of domain account


    user_tag (optional, any, None)
      Customized tag


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

