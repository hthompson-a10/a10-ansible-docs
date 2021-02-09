.. _a10_health_monitor_method_rtsp_module:


a10_health_monitor_method_rtsp -- Configures A10 health.monitor.method.rtsp
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

RTSP type






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  rtspurl (False, any, None)
    Specify URL string (Specify the path on the server)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  monitor_name (optional, any, None)
    Key to identify parent object


  rtsp (False, any, None)
    RTSP type


  state (True, any, None)
    State of the object to be created.


  rtsp_port (False, any, None)
    Specify RTSP port, default is 554 (Port Number (default 554))


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

