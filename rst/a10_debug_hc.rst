.. _a10_debug_hc_module:


a10_debug_hc -- Configures A10 debug.hc
=======================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Debug Harmony Controller






Parameters
----------

  object_uuid (False, any, None)
    UUID of the object to filter


  ansible_username (True, any, None)
    Username for AXAPI authentication


  app_svc_id (False, any, None)
    Application service id (virtual-server_port_protocol)


  metrics (False, any, None)
    Debug logs for harmony controller (metrics)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  registration (False, any, None)
    Debug logs for harmony controller (registration)


  per_request (False, any, None)
    Debug logs for harmony controller (per-request)


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  per_connection (False, any, None)
    Debug logs for harmony controller (per-connection)


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_password (True, any, None)
    Password for AXAPI authentication


  uri (False, any, None)
    URI of the object to filter


  state (True, any, None)
    State of the object to be created.


  error (False, any, None)
    Debug logs for harmony controller (error)


  anomaly (False, any, None)
    Dump per-request in anomaly cases only









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

