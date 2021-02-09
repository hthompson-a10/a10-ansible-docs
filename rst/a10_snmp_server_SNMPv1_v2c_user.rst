.. _a10_snmp_server_SNMPv1_v2c_user_module:


a10_snmp_server_SNMPv1_v2c_user -- Configures A10 snmp-server.SNMPv1.v2c.user
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Define configuration for SNMPv1/v2c user






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  oid_list (False, any, None)
    Field oid_list


    remote (optional, any, None)
      Field remote


    oid_val (optional, any, None)
      specific the oid (The oid value, object-key)


    user_tag (optional, any, None)
      Customized tag


    uuid (optional, any, None)
      uuid of the object



  remote (False, any, None)
    Field remote


    ipv6_list (optional, any, None)
      Field ipv6_list


    host_list (optional, any, None)
      Field host_list


    ipv4_list (optional, any, None)
      Field ipv4_list



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  passwd (False, any, None)
    define value of community string


  user_tag (False, any, None)
    Customized tag


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  user (True, any, None)
    SNMPv1/v2c community configuration key


  encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED community string)


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

