.. _a10_debug_auth_module:


a10_debug_auth -- Configures A10 debug.auth
===========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Debug authentication






Parameters
----------

  username (False, any, None)
    Show the logs of specific username (User name)


  ansible_port (True, any, None)
    Port for AXAPI authentication


  virtual_server (False, any, None)
    Show the logs of specific virtual-server (Virtual-server name)


  saml_sp (False, any, None)
    Filter SAML logs by SAML service provider name (SAML SP name)


  uuid (False, any, None)
    uuid of the object


  saml (False, any, None)
    Enable debug SAML authentication logs


  ansible_password (True, any, None)
    Password for AXAPI authentication


  client_addr (False, any, None)
    Filter SAML logs by client IP address


  ansible_username (True, any, None)
    Username for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  level (False, any, None)
    '1'= Diagnose Problems; '2'= Detail packet flow;


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

