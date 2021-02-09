.. _a10_health_external_edit_module:


a10_health_external_edit -- Configures A10 health.external.edit
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Edit external health monitor script






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  description (False, any, None)
    Describe health external monitor script briefly


  ansible_username (True, any, None)
    Username for AXAPI authentication


  file_name (False, any, None)
    External health monitor script file name


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

