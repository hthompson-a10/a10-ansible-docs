.. _a10_scaleout_cluster_local_device_module:


a10_scaleout_cluster_local_device -- Configures A10 scaleout.cluster.local-device
=================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Local device configuration






Parameters
----------

  ansible_username (True, any, None)
    Username for AXAPI authentication


  start_delay (False, any, None)
    Field start_delay


  session_sync_interface (False, any, None)
    Field session_sync_interface


    eth_cfg (optional, any, None)
      Field eth_cfg


    ve_cfg (optional, any, None)
      Field ve_cfg


    trunk_cfg (optional, any, None)
      Field trunk_cfg


    uuid (optional, any, None)
      uuid of the object



  cluster_id (optional, any, None)
    Key to identify parent object


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  id (False, any, None)
    Field id


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  l2_redirect (False, any, None)
    Field l2_redirect


    redirect_eth (optional, any, None)
      Ethernet port (Port Value)


    redirect_trunk (optional, any, None)
      L2 Trunk group


    trunk_vlan (optional, any, None)
      VLAN ID


    uuid (optional, any, None)
      uuid of the object


    ethernet_vlan (optional, any, None)
      VLAN ID



  ansible_host (True, any, None)
    Host for AXAPI authentication


  priority (False, any, None)
    Field priority


  state (True, any, None)
    State of the object to be created.


  tracking_template (False, any, None)
    Field tracking_template


    template_list (optional, any, None)
      Field template_list



  action (False, any, None)
    'enable'= enable; 'disable'= disable;


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

