.. _a10_delete_service_partition_module:


a10_delete_service_partition -- Configures A10 delete.service-partition
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Hard delete a service partition






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  id (False, any, None)
    Specify unique service partition id


  partition_name (False, any, None)
    Object service partition name









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

