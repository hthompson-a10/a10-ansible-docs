.. _a10_visibility_monitor_netflow_module:


a10_visibility_monitor_netflow -- Configures A10 visibility.monitor.netflow
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure Netflow parameters for flow based monitoring






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  listening_port (False, any, None)
    Netflow port to receive packets (Netflow port number(default 9996))


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  template_active_timeout (False, any, None)
    Configure active timeout of the netflow templates received in mins (Template active timeout(mins)(default 30mins))


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

