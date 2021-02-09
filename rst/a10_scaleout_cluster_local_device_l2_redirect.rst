.. _a10_scaleout_cluster_local_device_l2_redirect_module:


a10_scaleout_cluster_local_device_l2_redirect -- Configures A10 scaleout.cluster.local.device.l2-redirect
=========================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure interface for redirection






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  trunk_vlan (False, any, None)
    VLAN ID


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  redirect_eth (False, any, None)
    Ethernet port (Port Value)


  ansible_password (True, any, None)
    Password for AXAPI authentication


  ethernet_vlan (False, any, None)
    VLAN ID


  redirect_trunk (False, any, None)
    L2 Trunk group


  state (True, any, None)
    State of the object to be created.


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

