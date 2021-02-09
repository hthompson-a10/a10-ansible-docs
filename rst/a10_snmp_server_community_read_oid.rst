.. _a10_snmp_server_community_read_oid_module:


a10_snmp_server_community_read_oid -- Configures A10 snmp-server.community.read.oid
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Define a remote entity to which user belongs






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


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


  user_tag (False, any, None)
    Customized tag


  ansible_password (True, any, None)
    Password for AXAPI authentication


  read_user (optional, any, None)
    Key to identify parent object


  state (True, any, None)
    State of the object to be created.


  oid_val (True, any, None)
    specific the oid (The oid value, object-key)


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

