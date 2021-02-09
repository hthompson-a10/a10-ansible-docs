.. _a10_slb_template_persist_cookie_module:


a10_slb_template_persist_cookie -- Configures A10 slb.template.persist.cookie
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Cookie persistence






Parameters
----------

  domain (False, any, None)
    Set cookie domain


  match_type (False, any, None)
    Persist for server, default is port


  secure (False, any, None)
    Enable secure attribute


  name (True, any, None)
    Cookie persistence (Cookie persistence template name)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)


  cookie_name (False, any, None)
    Set cookie name


  prefix (False, any, None)
    'host'= the cookie will have been set with a Secure attribute, a Path attribute with a value of /, and no Domain attribute; 'secure'= the cookie will have been set with a Secure attribute; 'check'= check server prefix and enforce prefix format;


  expire (False, any, None)
    Set cookie expiration time (Expiration in seconds)


  dont_honor_conn_rules (False, any, None)
    Do not observe connection rate rules


  pass_phrase (False, any, None)
    Set passphrase for encryption


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  path (False, any, None)
    Set cookie path


  server (False, any, None)
    Persist to the same server, default is port


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  service_group (False, any, None)
    Persist within the same service group


  ansible_port (True, any, None)
    Port for AXAPI authentication


  insert_always (False, any, None)
    Insert persist cookie to every reponse


  server_service_group (False, any, None)
    Persist to the same server and within the same service group


  pass_thru (False, any, None)
    Pass thru mode - Server sends the persist cookie


  ansible_password (True, any, None)
    Password for AXAPI authentication


  scan_all_members (False, any, None)
    Persist within the same server SCAN


  state (True, any, None)
    State of the object to be created.


  samesite (False, any, None)
    'none'= none; 'lax'= lax; 'strict'= strict;


  user_tag (False, any, None)
    Customized tag


  encrypt_level (False, any, None)
    Encryption level for cookie name / value


  httponly (False, any, None)
    Enable HttpOnly attribute









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

