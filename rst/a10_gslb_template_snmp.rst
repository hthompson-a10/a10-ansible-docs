.. _a10_gslb_template_snmp_module:


a10_gslb_template_snmp -- Configures A10 gslb.template.snmp
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Specify SNMP template






Parameters
----------

  username (False, any, None)
    Specify username (User name)


  priv_key (False, any, None)
    Specify privacy key (Specify key)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  priv_proto (False, any, None)
    'aes'= AES; 'des'= DES;


  oid (False, any, None)
    Specify OID


  community (False, any, None)
    Specify community for version 2c (Community name)


  interface (False, any, None)
    Specify Interface ID


  host (False, any, None)
    Specify host (Host name or ip address)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  context_name (False, any, None)
    Specify context name


  context_engine_id (False, any, None)
    Specify context engine ID


  a10_partition (False, any, None)
    Destination/target partition for object/command


  port (False, any, None)
    Specify port, default is 161 (Port Number, default is 161)


  auth_proto (False, any, None)
    'sha'= SHA; 'md5'= MD5;


  ansible_port (True, any, None)
    Port for AXAPI authentication


  security_engine_id (False, any, None)
    Specify security engine ID


  uuid (False, any, None)
    uuid of the object


  auth_key (False, any, None)
    Specify authentication key (Specify key)


  ansible_password (True, any, None)
    Password for AXAPI authentication


  interval (False, any, None)
    Specify interval, default is 3 (Interval, unit= second, default is 3)


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  version (False, any, None)
    'v1'= Version 1; 'v2c'= Version 2c; 'v3'= Version 3;


  snmp_name (True, any, None)
    Specify name of snmp template


  security_level (False, any, None)
    'no-auth'= No authentication; 'auth-no-priv'= Authentication, but no privacy; 'auth-priv'= Authentication and privacy;


  user_tag (False, any, None)
    Customized tag









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

