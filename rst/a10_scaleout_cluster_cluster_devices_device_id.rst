.. _a10_scaleout_cluster_cluster_devices_device_id_module:


a10_scaleout_cluster_cluster_devices_device_id -- Configures A10 scaleout.cluster.cluster.devices.device-id
===========================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure Scaleout devices






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  ansible_password (True, any, None)
    Password for AXAPI authentication


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  cluster_id (optional, any, None)
    Key to identify parent object


  ip (False, any, None)
    Field ip


  action (False, any, None)
    'enable'= enable; 'disable'= disable;


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  device_id (True, any, None)
    scaleout device id









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

