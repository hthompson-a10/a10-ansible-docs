.. _a10_netflow_monitor_destination_module:


a10_netflow_monitor_destination -- Configures A10 netflow.monitor.destination
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure destination where netflow records will be sent






Parameters
----------

  service_group (False, any, None)
    Service-group for load balancing between multiple collector servers


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ip_cfg (False, any, None)
    Field ip_cfg


    ip (optional, any, None)
      IP address of netflow collector


    port4 (optional, any, None)
      Port number, default is 9996



  ansible_username (True, any, None)
    Username for AXAPI authentication


  monitor_name (optional, any, None)
    Key to identify parent object


  ansible_password (True, any, None)
    Password for AXAPI authentication


  ipv6_cfg (False, any, None)
    Field ipv6_cfg


    port6 (optional, any, None)
      Port number, default is 9996


    ipv6 (optional, any, None)
      IPv6 address of netflow collector



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

