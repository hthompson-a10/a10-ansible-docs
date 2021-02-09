.. _a10_scaleout_cluster_service_config_template_module:


a10_scaleout_cluster_service_config_template -- Configures A10 scaleout.cluster.service.config.template
=======================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Scaleout template






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    Scaleout template Name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  bucket_count (False, any, None)
    Number of traffic buckets


  ansible_password (True, any, None)
    Password for AXAPI authentication


  device_group (False, any, None)
    Device group id


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


  uuid (False, any, None)
    uuid of the object









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

