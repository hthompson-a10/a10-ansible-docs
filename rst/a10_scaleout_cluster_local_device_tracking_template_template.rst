.. _a10_scaleout_cluster_local_device_tracking_template_template_module:


a10_scaleout_cluster_local_device_tracking_template_template -- Configures A10 scaleout.cluster.local.device.tracking.template.template
=======================================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure tracking template to be used by scaleout






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


  state (True, any, None)
    State of the object to be created.


  threshold_cfg (False, any, None)
    Field threshold_cfg


    threshold (optional, any, None)
      action triggering threshold


    action (optional, any, None)
      'down'= node stops processing user traffic; 'exit-cluster'= node exits scaleout cluster;



  cluster_id (optional, any, None)
    Key to identify parent object


  template (True, any, None)
    bind tracking template name


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

