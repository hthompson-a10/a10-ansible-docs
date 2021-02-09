.. _a10_health_monitor_method_udp_module:


a10_health_monitor_method_udp -- Configures A10 health.monitor.method.udp
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

UDP type






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  monitor_name (optional, any, None)
    Key to identify parent object


  udp (False, any, None)
    UDP type


  udp_port (False, any, None)
    Specify UDP port (Specify port number)


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  force_up_with_single_healthcheck (False, any, None)
    Force Up with no response at the first time









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

