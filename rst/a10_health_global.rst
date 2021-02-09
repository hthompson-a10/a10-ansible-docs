.. _a10_health_global_module:


a10_health_global -- Configures A10 health.global
=================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Define the Health Monitor global default






Parameters
----------

  interval (False, any, None)
    Specify the Healthcheck Interval (Interval Value, in seconds (default 5))


  ansible_username (True, any, None)
    Username for AXAPI authentication


  up_retry (False, any, None)
    Specify the Healthcheck Retries before declaring target up (Up-retry count (default 1))


  external_rate (False, any, None)
    Define the External Health Check Rate (Number of External Script Programs (default 2))


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  check_rate (False, any, None)
    Health Check Rate per 500ms (default 1000)


  ansible_port (True, any, None)
    Port for AXAPI authentication


  retry (False, any, None)
    Specify the Healthcheck Retries (Retry Count (default 3))


  uuid (False, any, None)
    uuid of the object


  disable_auto_adjust (False, any, None)
    Disable the Health Check Rate Auto Adjustment


  multi_process (False, any, None)
    Start Health Monitoring in Multi-Process Mode (Specify the number of multiple processes (default 1))


  per (False, any, None)
    Specify the Unit Time for the rate (Specify the Unit Time, multiple of 100ms)


  state (True, any, None)
    State of the object to be created.


  timeout (False, any, None)
    Specify the Healthcheck Timeout (Timeout Value, in seconds (default 5), Timeout should be less than or equal to interval)


  ansible_password (True, any, None)
    Password for AXAPI authentication









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

