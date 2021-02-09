.. _a10_network_icmp_rate_limit_module:


a10_network_icmp_rate_limit -- Configures A10 network.icmp-rate-limit
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Limit the rate of ICMP packet






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  icmp_lockup (False, any, None)
    Enter lockup state when ICMP rate exceeds lockup rate limit (Maximum rate limit. If exceeds this limit, drop all ICMP packet for a time period)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  icmp_lockup_period (False, any, None)
    Lockup period (second)


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  icmp_normal_rate_limit (False, any, None)
    Normal rate limit. If exceeds this limit, drop the ICMP packet that goes over the limit









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

