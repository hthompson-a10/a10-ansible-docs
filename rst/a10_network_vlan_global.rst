.. _a10_network_vlan_global_module:


a10_network_vlan_global -- Configures A10 network.vlan-global
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure global options for vlan






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'xparent_vlan_list_err'= Transparent Mode VLAN List Errors;



  oper (False, any, None)
    Field oper


    vlan_trans_list (optional, any, None)
      Field vlan_trans_list



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    xparent_vlan_list_err (optional, any, None)
      Transparent Mode VLAN List Errors



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  l3_vlan_fwd_disable (False, any, None)
    Disable L3 forwarding between VLANs


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  enable_def_vlan_l2_forwarding (False, any, None)
    Enable layer 2 forwarding on default vlan


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

