.. _a10_ldap_server_host_ipv4_module:


a10_ldap_server_host_ipv4 -- Configures A10 ldap-server.host.ipv4
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Specify the hostname of ldap server






Parameters
----------

  domain (False, any, None)
    Configure AD domain name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  dn_value (False, any, None)
    LDAP distinguished name (dn)


  base (False, any, None)
    Configure the group DN which user belongs to


  ipv4_addr (True, any, None)
    IPV4 address of ldap server


  domain_cfg (False, any, None)
    Field domain_cfg


    ssl (optional, any, None)
      Use SSL


    port (optional, any, None)
      Specify the LDAP server's port (default 389 without ssl or 636 with ssl)


    timeout (optional, any, None)
      Specify the LDAP server's timeout (default 3)



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  port_cfg (False, any, None)
    Field port_cfg


    ssl (optional, any, None)
      Use SSL


    port (optional, any, None)
      Specify the LDAP server's port (default 389 without ssl or 636 with ssl)


    timeout (optional, any, None)
      Specify the LDAP server's timeout (default 3)



  ansible_port (True, any, None)
    Port for AXAPI authentication


  group (False, any, None)
    Configure the group DN which user belongs to


  uuid (False, any, None)
    uuid of the object


  cn_value (False, any, None)
    LDAP common name identifier (i.e.= cn, uid)


  ipv4_addr_cfg (False, any, None)
    Field ipv4_addr_cfg


    ssl (optional, any, None)
      Use SSL


    port (optional, any, None)
      Specify the LDAP server's port (default 3268 without ssl or 3269 with ssl)


    timeout (optional, any, None)
      Specify the LDAP server's timeout (default 3)



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

