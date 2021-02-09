.. _a10_system_probe_network_devices_module:


a10_system_probe_network_devices -- Configures A10 system.probe-network-devices
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Scan platform for network devices






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  ansible_password (True, any, None)
    Password for AXAPI authentication


  a10_partition (False, any, None)
    Destination/target partition for object/command


  state (True, any, None)
    State of the object to be created.


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

