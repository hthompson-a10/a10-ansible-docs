.. _a10_enable_management_service_snmp_acl_v4_module:


a10_enable_management_service_snmp_acl_v4 -- Configures A10 enable-management.service.snmp.acl-v4
=================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

IPv4 ACL for SNMP service






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  management (False, any, None)
    Management Interface


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  acl_id (True, any, None)
    ACL id


  state (True, any, None)
    State of the object to be created.


  all_data_intf (False, any, None)
    All Data Interfaces


  ve_cfg (False, any, None)
    Field ve_cfg


    ve_start (optional, any, None)
      VE port (VE Interface number)


    ve_end (optional, any, None)
      VE port



  eth_cfg (False, any, None)
    Field eth_cfg


    ethernet_start (optional, any, None)
      Ethernet port (Ethernet Interface number)


    ethernet_end (optional, any, None)
      Ethernet port



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  tunnel_cfg (False, any, None)
    Field tunnel_cfg


    tunnel_start (optional, any, None)
      tunnel port (tunnel Interface number)


    tunnel_end (optional, any, None)
      tunnel port



  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


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

