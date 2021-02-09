.. _a10_ntp_auth_key_module:


a10_ntp_auth_key -- Configures A10 ntp.auth-key
===============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

authentication key






Parameters
----------

  alg_type (False, any, None)
    'M'= encryption using MD5; 'SHA'= encryption using SHA; 'SHA1'= encryption using SHA1;


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  hex_key (False, any, None)
    Field hex_key


  encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)


  ansible_password (True, any, None)
    Password for AXAPI authentication


  key_type (False, any, None)
    'ascii'= key string in ASCII form; 'hex'= key string in hex form;


  state (True, any, None)
    State of the object to be created.


  asc_key (False, any, None)
    Field asc_key


  key (True, any, None)
    authentication key


  hex_encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)


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

