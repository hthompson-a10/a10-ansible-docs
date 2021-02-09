.. _a10_scaleout_cluster_cluster_devices_cluster_discovery_timeout_module:


a10_scaleout_cluster_cluster_devices_cluster_discovery_timeout -- Configures A10 scaleout.cluster.cluster.devices.cluster-discovery-timeout
===========================================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure cluster discovery timeout






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


  timer_val (False, any, None)
    Cluster node discovery timeout value (secs (Default= 120))


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

