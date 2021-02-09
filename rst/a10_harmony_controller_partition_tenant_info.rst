.. _a10_harmony_controller_partition_tenant_info_module:


a10_harmony_controller_partition_tenant_info -- Configures A10 harmony.controller.partition-tenant-info
=======================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Harmony controller profile






Parameters
----------

  oper (False, any, None)
    Field oper


    cluster_name (optional, any, None)
      Field cluster_name


    cluster_id (optional, any, None)
      Field cluster_id


    log_rate_per_sec (optional, any, None)
      Field log_rate_per_sec


    tenant_id (optional, any, None)
      Field tenant_id


    tenant_name (optional, any, None)
      Field tenant_name


    partition_name (optional, any, None)
      Field partition_name



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

