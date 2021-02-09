.. _a10_aam_authentication_relay_ws_federation_module:


a10_aam_authentication_relay_ws_federation -- Configures A10 aam.authentication.relay.ws-federation
===================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

WS-Federation Authentication Relay






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'request'= Request; 'success'= Success; 'failure'= Failure;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    failure (optional, any, None)
      Failure


    request (optional, any, None)
      Request


    name (optional, any, None)
      Specify WS-Federation authentication relay name


    success (optional, any, None)
      Success



  name (True, any, None)
    Specify WS-Federation authentication relay name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  authentication_uri (False, any, None)
    Specify WS-Federation relay URI, default is /_trust/


  application_server (False, any, None)
    'sharepoint'= Microsoft SharePoint; 'exchange-owa'= Microsoft Exchange OWA;


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


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

