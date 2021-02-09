.. _a10_health_monitor_method_ldap_module:


a10_health_monitor_method_ldap -- Configures A10 health.monitor.method.ldap
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

LDAP type






Parameters
----------

  AcceptResRef (False, any, None)
    Mark server up on receiving a search result reference response


  ldap_port (False, any, None)
    Specify the LDAP port (Speciry port number, default is 389, or 636 if LDAP over SSL)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ldap_binddn (False, any, None)
    Specify the distinguished name for bindRequest (LDAP DN distinguished name)


  ldap_password_string (False, any, None)
    Configure password, '' means empty password


  ldap_query (False, any, None)
    LDAP query to be excuted


  ldap_run_search (False, any, None)
    Specify a query to be executed


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  ldap_security (False, any, None)
    'overssl'= Set LDAP over SSL; 'StartTLS'= LDAP switch to TLS;


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  AcceptNotFound (False, any, None)
    Mark server up on receiving a not-found response


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ldap_password (False, any, None)
    Specify the user password


  monitor_name (optional, any, None)
    Key to identify parent object


  BaseDN (False, any, None)
    Specify LDAP DN distinguished name


  ldap_encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)


  state (True, any, None)
    State of the object to be created.


  ldap (False, any, None)
    LDAP type


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

