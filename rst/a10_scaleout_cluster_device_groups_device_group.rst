.. _a10_scaleout_cluster_device_groups_device_group_module:


a10_scaleout_cluster_device_groups_device_group -- Configures A10 scaleout.cluster.device-groups.device.group
=============================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure scaleout device groups






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


  device_id_list (False, any, None)
    Field device_id_list


    device_id_start (optional, any, None)
      Field device_id_start


    device_id_end (optional, any, None)
      Field device_id_end



  ansible_password (True, any, None)
    Password for AXAPI authentication


  device_group (True, any, None)
    scaleout device group


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

