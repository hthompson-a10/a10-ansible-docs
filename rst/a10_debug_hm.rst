.. _a10_debug_hm_module:


a10_debug_hm -- Configures A10 debug.hm
=======================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Debug health monitor






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  method_type (False, any, None)
    'icmp'= ICMP type; 'tcp'= TCP type; 'udp'= UDP type; 'ftp'= FTP type; 'http'= HTTP type; 'snmp'= SNMP type; 'smtp'= SMTP type; 'dns'= DNS type; 'dns-tcp'= DNS TCP type; 'pop3'= POP3 type; 'imap'= IMAP type; 'sip'= SIP type; 'sip-tcp'= SIP TCP type; 'radius'= RADIUS type; 'ldap'= LDAP type; 'rtsp'= RTSP type; 'kerberos-kdc'= Kerberos KDC type; 'database'= DATABASE type; 'external'= EXTERNAL type; 'https'= HTTPS type; 'ntp'= NTP type; 'compound'= Compound type;


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  level (False, any, None)
    Debug level (Level 1-3)


  pin_uid (False, any, None)
    Debug Pin Unique Id


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


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

