.. _a10_import_auth_saml_idp_module:


a10_import_auth_saml_idp -- Configures A10 import.auth-saml-idp
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

SAML metadata of identity provider






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  verify_xml_signature (False, any, None)
    Verify metadata's XML signature


  ansible_username (True, any, None)
    Username for AXAPI authentication


  remote_file (False, any, None)
    Profile name for remote url


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  use_mgmt_port (False, any, None)
    Use management port as source port


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  saml_idp_name (False, any, None)
    Metadata name


  password (False, any, None)
    password for the remote site


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  overwrite (False, any, None)
    Overwrite existing file









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

