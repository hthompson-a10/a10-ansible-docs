.. _a10_aam_authentication_saml_metadata_monitor_module:


a10_aam_authentication_saml_metadata_monitor -- Configures A10 aam.authentication.saml.metadata-monitor
=======================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure SAML metadata out-of-sync detection and recovery options






Parameters
----------

  status (False, any, None)
    'enable'= Enable SAML metadata out-of-sync detection; 'disable'= Disable SAML metadata out-of-sync detection;


  ansible_port (True, any, None)
    Port for AXAPI authentication


  acs_missing_period (False, any, None)
    Specify how long no acs request will trigger metadata reload (in seconds (default= 60))


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  acs_continuous_fail_threshold (False, any, None)
    Specify how many ACS continuous fails will trigger metadata reload (ACS continuous fail threshold (default= 10))


  state (True, any, None)
    State of the object to be created.


  acs_missing_threshold (False, any, None)
    Specify how many ACS request missing in the period will trigger metadata reload (ACS request missing threshold (default= 100))


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

