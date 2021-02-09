.. _a10_aam_authentication_logon_http_authenticate_instance_module:


a10_aam_authentication_logon_http_authenticate_instance -- Configures A10 aam.authentication.logon.http.authenticate.instance
=============================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

HTTP-authenticate Logon






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'spn_krb_request'= SPN Kerberos Request; 'spn_krb_success'= SPN Kerberos Success; 'spn_krb_faiure'= SPN Kerberos Failure;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  retry (False, any, None)
    Maximum number of consecutive failed logon attempts (default 3)


  stats (False, any, None)
    Field stats


    spn_krb_success (optional, any, None)
      SPN Kerberos Success


    spn_krb_request (optional, any, None)
      SPN Kerberos Request


    name (optional, any, None)
      Specify HTTP-Authenticate logon name


    spn_krb_faiure (optional, any, None)
      SPN Kerberos Failure



  name (True, any, None)
    Specify HTTP-Authenticate logon name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  ansible_host (True, any, None)
    Host for AXAPI authentication


  account_lock (False, any, None)
    Lock the account when the failed logon attempts is exceeded


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  duration (False, any, None)
    The time an account remains locked in seconds (default 1800)


  a10_partition (False, any, None)
    Destination/target partition for object/command


  auth_method (False, any, None)
    Field auth_method


    ntlm (optional, any, None)
      Field ntlm


    negotiate (optional, any, None)
      Field negotiate


    basic (optional, any, None)
      Field basic



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

