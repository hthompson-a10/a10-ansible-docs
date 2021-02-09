.. _a10_rename_module:


a10_rename -- Configures A10 rename
===================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Rename Object Name






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  object (False, any, None)
    Lineage of object being renamed e.g= slb.server, slb.service-group, slb.virtual-server


  instance_name (False, any, None)
    Old Instance Name


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  new_instance_name (False, any, None)
    New Instance Name


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

