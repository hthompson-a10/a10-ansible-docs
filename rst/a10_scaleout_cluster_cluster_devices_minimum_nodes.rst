.. _a10_scaleout_cluster_cluster_devices_minimum_nodes_module:


a10_scaleout_cluster_cluster_devices_minimum_nodes -- Configures A10 scaleout.cluster.cluster.devices.minimum-nodes
===================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Minimum number of nodes to start scaleout






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


  state (True, any, None)
    State of the object to be created.


  minimum_nodes_num (False, any, None)
    Specify the minimum number of the node required to start service


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

