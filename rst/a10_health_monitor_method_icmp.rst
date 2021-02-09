.. _a10_health_monitor_method_icmp_module:


a10_health_monitor_method_icmp -- Configures A10 health.monitor.method.icmp
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

ICMP type






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ip (False, any, None)
    Specify IPv4 address of destination behind monitored node


  monitor_name (optional, any, None)
    Key to identify parent object


  ansible_password (True, any, None)
    Password for AXAPI authentication


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  ipv6 (False, any, None)
    Specify IPv6 address of destination behind monitored node


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  icmp (False, any, None)
    ICMP type


  a10_partition (False, any, None)
    Destination/target partition for object/command


  transparent (False, any, None)
    Apply transparent mode









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

