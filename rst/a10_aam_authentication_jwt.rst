.. _a10_aam_authentication_jwt_module:


a10_aam_authentication_jwt -- Configures A10 aam.authentication.jwt
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

JWT issuance configuration






Parameters
----------

  token_lifetime (False, any, None)
    Specify JWT token lifetime (Specify lifetime (in seconds), default is 300.)


  secret_string (False, any, None)
    The JWT signature secret


  encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    Specify JWT issuer template name


  user_tag (False, any, None)
    Customized tag


  ansible_username (True, any, None)
    Username for AXAPI authentication


  signature_secret (False, any, None)
    Specify the JWT signature secret


  state (True, any, None)
    State of the object to be created.


  action (False, any, None)
    'redirect'= redirect JWT to specific URI; 'relay'= relay JWT to back-end;


  issuer (False, any, None)
    Specify JWT issuer claim value


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

