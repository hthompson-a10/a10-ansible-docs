.. _a10_aam_authentication_global_module:


a10_aam_authentication_global -- Configures A10 aam.authentication.global
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Global AAM authentication statistics






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'requests'= Total Authentication Request; 'responses'= Total Authentication Response; 'misses'= Total Authentication Request Missed; 'ocsp- stapling-requests-to-a10authd'= Total OCSP Stapling Request; 'ocsp-stapling- responses-from-a10authd'= Total OCSP Stapling Response; 'opened-socket'= Total AAM Socket Opened; 'open-socket-failed'= Total AAM Open Socket Failed; 'connect'= Total AAM Connection; 'connect-failed'= Total AAM Connect Failed; 'created-timer'= Total AAM Timer Created; 'create-timer-failed'= Total AAM Timer Creation Failed; 'total-request'= Total Request Received by A10 Auth Service; 'get-socket-option-failed'= Total AAM Get Socket Option Failed; 'aflex-authz-succ'= Total Authorization success number in aFleX; 'aflex-authz- fail'= Total Authorization failure number in aFleX; 'authn-success'= Total Authentication success number; 'authn-failure'= Total Authentication failure number; 'authz-success'= Total Authorization success number; 'authz-failure'= Total Authorization failure number; 'active-session'= Total Active Auth- Sessions; 'active-user'= Total Active Users; 'dns-resolve-failed'= Total AAM DNS resolve failed;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    created_timer (optional, any, None)
      Total AAM Timer Created


    ocsp_stapling_requests_to_a10authd (optional, any, None)
      Total OCSP Stapling Request


    authn_success (optional, any, None)
      Total Authentication success number


    open_socket_failed (optional, any, None)
      Total AAM Open Socket Failed


    total_request (optional, any, None)
      Total Request Received by A10 Auth Service


    authn_failure (optional, any, None)
      Total Authentication failure number


    opened_socket (optional, any, None)
      Total AAM Socket Opened


    connect (optional, any, None)
      Total AAM Connection


    authz_success (optional, any, None)
      Total Authorization success number


    aflex_authz_fail (optional, any, None)
      Total Authorization failure number in aFleX


    aflex_authz_succ (optional, any, None)
      Total Authorization success number in aFleX


    active_session (optional, any, None)
      Total Active Auth-Sessions


    responses (optional, any, None)
      Total Authentication Response


    get_socket_option_failed (optional, any, None)
      Total AAM Get Socket Option Failed


    dns_resolve_failed (optional, any, None)
      Total AAM DNS resolve failed


    connect_failed (optional, any, None)
      Total AAM Connect Failed


    authz_failure (optional, any, None)
      Total Authorization failure number


    ocsp_stapling_responses_from_a10authd (optional, any, None)
      Total OCSP Stapling Response


    active_user (optional, any, None)
      Total Active Users


    misses (optional, any, None)
      Total Authentication Request Missed


    create_timer_failed (optional, any, None)
      Total AAM Timer Creation Failed


    requests (optional, any, None)
      Total Authentication Request



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


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

