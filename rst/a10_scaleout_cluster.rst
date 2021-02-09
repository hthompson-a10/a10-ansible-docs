.. _a10_scaleout_cluster_module:


a10_scaleout_cluster -- Configures A10 scaleout.cluster
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure scaleout cluster






Parameters
----------

  db_config (False, any, None)
    Field db_config


    uuid (optional, any, None)
      uuid of the object



  ansible_username (True, any, None)
    Username for AXAPI authentication


  cluster_id (True, any, None)
    Scaleout cluster-id


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  follow_vcs (False, any, None)
    Field follow_vcs


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  service_config (False, any, None)
    Field service_config


    template_list (optional, any, None)
      Field template_list


    uuid (optional, any, None)
      uuid of the object



  local_device (False, any, None)
    Field local_device


    uuid (optional, any, None)
      uuid of the object


    l2_redirect (optional, any, None)
      Field l2_redirect


    start_delay (optional, any, None)
      Field start_delay


    priority (optional, any, None)
      Field priority


    action (optional, any, None)
      'enable'= enable; 'disable'= disable;


    tracking_template (optional, any, None)
      Field tracking_template


    session_sync_interface (optional, any, None)
      Field session_sync_interface


    id (optional, any, None)
      Field id



  cluster_devices (False, any, None)
    Field cluster_devices


    cluster_discovery_timeout (optional, any, None)
      Field cluster_discovery_timeout


    device_id_list (optional, any, None)
      Field device_id_list


    uuid (optional, any, None)
      uuid of the object


    minimum_nodes (optional, any, None)
      Field minimum_nodes



  state (True, any, None)
    State of the object to be created.


  tracking_template (False, any, None)
    Field tracking_template


    template_list (optional, any, None)
      Field template_list



  device_groups (False, any, None)
    Field device_groups


    device_group_list (optional, any, None)
      Field device_group_list


    uuid (optional, any, None)
      uuid of the object



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

