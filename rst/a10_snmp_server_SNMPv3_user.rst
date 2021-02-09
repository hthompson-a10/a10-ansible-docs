.. _a10_snmp_server_SNMPv3_user_module:


a10_snmp_server_SNMPv3_user -- Configures A10 snmp-server.SNMPv3.user
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Define a user who can access the SNMP engine






Parameters
----------

  username (True, any, None)
    Name of the user


  ansible_username (True, any, None)
    Username for AXAPI authentication


  passwd (False, any, None)
    Password of this user


  pw_encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED passphrase string)


  v3 (False, any, None)
    'auth'= Using the authNoPriv Security Level; 'noauth'= Using the noAuthNoPriv Security Level;


  priv_pw_encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED passphrase string)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  auth_val (False, any, None)
    'md5'= Use HMAC MD5 algorithm for authentication; 'sha'= Use HMAC SHA algorithm for authentication;


  priv (False, any, None)
    'des'= DES encryption alogrithm; 'aes'= AES encryption alogrithm;  (Encryption type)


  ansible_port (True, any, None)
    Port for AXAPI authentication


  group (False, any, None)
    Group to which the user belongs


  uuid (False, any, None)
    uuid of the object


  encpasswd (False, any, None)
    Passphrase for encryption


  state (True, any, None)
    State of the object to be created.


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

