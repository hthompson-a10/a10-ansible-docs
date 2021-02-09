.. _a10_scaleout_cluster_cluster_devices_module:


a10_scaleout_cluster_cluster_devices -- Configures A10 scaleout.cluster.cluster-devices
=======================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure devices in the cluster






Parameters
----------

  cluster_discovery_timeout (False, any, None)
    Field cluster_discovery_timeout


    timer_val (optional, any, None)
      Cluster node discovery timeout value (secs (Default= 120))


    uuid (optional, any, None)
      uuid of the object



  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  device_id_list (False, any, None)
    Field device_id_list


    action (optional, any, None)
      'enable'= enable; 'disable'= disable;


    ip (optional, any, None)
      Field ip


    user_tag (optional, any, None)
      Customized tag


    uuid (optional, any, None)
      uuid of the object


    device_id (optional, any, None)
      scaleout device id



  minimum_nodes (False, any, None)
    Field minimum_nodes


    minimum_nodes_num (optional, any, None)
      Specify the minimum number of the node required to start service


    uuid (optional, any, None)
      uuid of the object



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

