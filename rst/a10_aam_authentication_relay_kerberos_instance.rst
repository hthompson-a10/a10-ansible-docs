.. _a10_aam_authentication_relay_kerberos_instance_module:


a10_aam_authentication_relay_kerberos_instance -- Configures A10 aam.authentication.relay.kerberos.instance
===========================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Kerberos Authentication Relay






Parameters
----------

  oper (False, any, None)
    Field oper


    default_principal (optional, any, None)
      Field default_principal


    ticket_cache (optional, any, None)
      Field ticket_cache


    name (optional, any, None)
      Specify Kerberos authentication relay name


    item_list (optional, any, None)
      Field item_list



  secret_string (False, any, None)
    The kerberos client password


  ansible_username (True, any, None)
    Username for AXAPI authentication


  encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  password (False, any, None)
    Specify password of Kerberos password


  a10_partition (False, any, None)
    Destination/target partition for object/command


  port (False, any, None)
    Specify The KDC port, default is 88


  uuid (False, any, None)
    uuid of the object


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'request-send'= Request Send; 'response-receive'= Response Receive; 'current-requests-of-user'= Current Pending Requests of User; 'tickets'= Tickets;



  kerberos_realm (False, any, None)
    Specify the kerberos realm


  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    tickets (optional, any, None)
      Tickets


    request_send (optional, any, None)
      Request Send


    name (optional, any, None)
      Specify Kerberos authentication relay name


    current_requests_of_user (optional, any, None)
      Current Pending Requests of User


    response_receive (optional, any, None)
      Response Receive



  name (True, any, None)
    Specify Kerberos authentication relay name


  state (True, any, None)
    State of the object to be created.


  kerberos_account (False, any, None)
    Specify the kerberos account name


  kerberos_kdc_service_group (False, any, None)
    Specify an authentication service group as multiple KDCs


  kerberos_kdc (False, any, None)
    Specify the kerberos kdc ip or host name


  timeout (False, any, None)
    Specify timeout for kerberos transport, default is 10 seconds (The timeout, default is 10 seconds)


  ansible_host (True, any, None)
    Host for AXAPI authentication


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

