.. _a10_vcs_device_module:


a10_vcs_device -- Configures A10 vcs.device
===========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

VCS Device






Parameters
----------

  enable (False, any, None)
    Enable


  ansible_username (True, any, None)
    Username for AXAPI authentication


  affinity_vrrp_a_vrid (False, any, None)
    vrid-group


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  ve_cfg (False, any, None)
    Field ve_cfg


    ve (optional, any, None)
      VE interface (VE interface number)



  device (True, any, None)
    Device ID


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  unicast_port (False, any, None)
    Port used in unicast communication (Port number)


  ansible_port (True, any, None)
    Port for AXAPI authentication


  management (False, any, None)
    Management interface


  trunk_cfg (False, any, None)
    Field trunk_cfg


    trunk (optional, any, None)
      Trunk interface (Trunk interface number)



  uuid (False, any, None)
    uuid of the object


  user_tag (False, any, None)
    Customized tag


  state (True, any, None)
    State of the object to be created.


  priority (False, any, None)
    Device priority


  ethernet_cfg (False, any, None)
    Field ethernet_cfg


    ethernet (optional, any, None)
      Ethernet (Ethernet interface number)



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

