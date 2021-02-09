.. _a10_interface_management_lldp_module:


a10_interface_management_lldp -- Configures A10 interface.management.lldp
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Interface lldp configuration






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


  notification_cfg (False, any, None)
    Field notification_cfg


    notification (optional, any, None)
      Interface lldp notification configuration


    notif_enable (optional, any, None)
      Interface lldp notification enable



  tx_tlvs_cfg (False, any, None)
    Field tx_tlvs_cfg


    system_name (optional, any, None)
      Interface lldp system name


    tx_tlvs (optional, any, None)
      Interface lldp tx TLVs configuration


    port_description (optional, any, None)
      Interface lldp port description


    management_address (optional, any, None)
      Interface lldp management address


    system_description (optional, any, None)
      Interface lldp system description


    exclude (optional, any, None)
      Configure which TLVs excluded. All basic TLVs will be included by default


    system_capabilities (optional, any, None)
      Interface lldp system capabilities



  enable_cfg (False, any, None)
    Field enable_cfg


    rx (optional, any, None)
      Enable lldp rx


    rt_enable (optional, any, None)
      Interface lldp enable/disable


    tx (optional, any, None)
      Enable lldp tx



  tx_dot1_cfg (False, any, None)
    Field tx_dot1_cfg


    vlan (optional, any, None)
      Interface vlan information


    tx_dot1_tlvs (optional, any, None)
      Interface lldp tx IEEE 802.1 Organizationally specific TLVs configuration


    link_aggregation (optional, any, None)
      Interface link aggregation information



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

