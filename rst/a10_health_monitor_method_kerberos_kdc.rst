.. _a10_health_monitor_method_kerberos_kdc_module:


a10_health_monitor_method_kerberos_kdc -- Configures A10 health.monitor.method.kerberos-kdc
===========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Kerberos KDC type






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  kerberos_cfg (False, any, None)
    Field kerberos_cfg


    kpasswd_password (optional, any, None)
      Password


    kadmin_realm (optional, any, None)
      Specify the realm


    kinit_kdc (optional, any, None)
      Specify the kdc server, host|ip [=port]


    kadmin_encrypted (optional, any, None)
      Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)


    kpasswd (optional, any, None)
      Kerberos change passwd


    kadmin_kdc (optional, any, None)
      Specify the kdc server, host|ip [=port]


    kinit_encrypted (optional, any, None)
      Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)


    kpasswd_kdc (optional, any, None)
      Specify the kdc server, host|ip [=port]


    kpasswd_pricipal_name (optional, any, None)
      Specify the principal name


    kadmin_server (optional, any, None)
      Specify the admin server, host|ip [=port]


    tcp_only (optional, any, None)
      Specify the kerberos tcp only


    kinit_password (optional, any, None)
      Password


    kadmin_password (optional, any, None)
      Password


    kinit (optional, any, None)
      Kerberos KDC


    kpasswd_server (optional, any, None)
      Specify the Kerberos password server, host|ip [=port]


    kinit_pricipal_name (optional, any, None)
      Specify the principal name


    kadmin (optional, any, None)
      Kerberos admin


    kadmin_pricipal_name (optional, any, None)
      Specify the principal name


    kpasswd_encrypted (optional, any, None)
      Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  monitor_name (optional, any, None)
    Key to identify parent object


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


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

