.. _a10_scaleout_cluster_local_device_session_sync_interface_module:


a10_scaleout_cluster_local_device_session_sync_interface -- Configures A10 scaleout.cluster.local.device.session-sync-interface
===============================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Interface for scaleout session sync






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  trunk_cfg (False, any, None)
    Field trunk_cfg


    trunk (optional, any, None)
      Trunk Interface (Trunk interface number)



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  eth_cfg (False, any, None)
    Field eth_cfg


    ethernet (optional, any, None)
      Ethernet Interface (Ethernet interface number)



  ve_cfg (False, any, None)
    Field ve_cfg


    ve (optional, any, None)
      Virtual ethernet Interface (Virtual ethernet interface number)



  cluster_id (optional, any, None)
    Key to identify parent object


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

