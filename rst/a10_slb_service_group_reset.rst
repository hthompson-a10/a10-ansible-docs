.. _a10_slb_service_group_reset_module:


a10_slb_service_group_reset -- Configures A10 slb.service.group.reset
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Reset






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  service_group_name (optional, any, None)
    Key to identify parent object


  auto_switch (False, any, None)
    Reset auto stateless state


  ansible_password (True, any, None)
    Password for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


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

