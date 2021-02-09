.. _a10_enable_management_service_ping_module:


a10_enable_management_service_ping -- Configures A10 enable.management.service.ping
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Ping service






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  acl_v4_list (False, any, None)
    Field acl_v4_list


    management (optional, any, None)
      Management Interface


    uuid (optional, any, None)
      uuid of the object


    eth_cfg (optional, any, None)
      Field eth_cfg


    acl_id (optional, any, None)
      ACL id


    all_data_intf (optional, any, None)
      All Data Interfaces


    ve_cfg (optional, any, None)
      Field ve_cfg


    tunnel_cfg (optional, any, None)
      Field tunnel_cfg


    user_tag (optional, any, None)
      Customized tag



  acl_v6_list (False, any, None)
    Field acl_v6_list


    management (optional, any, None)
      Management Interface


    uuid (optional, any, None)
      uuid of the object


    acl_name (optional, any, None)
      ACL name


    eth_cfg (optional, any, None)
      Field eth_cfg


    all_data_intf (optional, any, None)
      All Data Interfaces


    ve_cfg (optional, any, None)
      Field ve_cfg


    tunnel_cfg (optional, any, None)
      Field tunnel_cfg


    user_tag (optional, any, None)
      Customized tag



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

