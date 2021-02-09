.. _a10_health_monitor_method_ntp_module:


a10_health_monitor_method_ntp -- Configures A10 health.monitor.method.ntp
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

NTP type






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  monitor_name (optional, any, None)
    Key to identify parent object


  ntp_port (False, any, None)
    Specify the NTP port, default is 123 (Port Number (default 123))


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  ntp (False, any, None)
    NTP type


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

