.. _a10_cgnv6_lw_4o6_health_check_gateway_module:


a10_cgnv6_lw_4o6_health_check_gateway -- Configures A10 cgnv6.lw.4o6.health-check-gateway
=========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure LW-4over6 health-check gateway






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


  ipv6_addr (True, any, None)
    LW-4over6 IPv6 Gateway


  state (True, any, None)
    State of the object to be created.


  ipv4_addr (True, any, None)
    LW-4over6 IPv4 Gateway


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

