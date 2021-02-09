.. _a10_system_template_bind_monitor_module:


a10_system_template_bind_monitor -- Configures A10 system.template.bind.monitor
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Apply monitor template to the whole system






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  template_monitor (True, any, None)
    Monitor template ID Number


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

