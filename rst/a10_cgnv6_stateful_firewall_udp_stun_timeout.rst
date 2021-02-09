.. _a10_cgnv6_stateful_firewall_udp_stun_timeout_module:


a10_cgnv6_stateful_firewall_udp_stun_timeout -- Configures A10 cgnv6.stateful.firewall.udp.stun-timeout
=======================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Set STUN timeout for endpoint-independent filtering






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  port_end (True, any, None)
    Port Range End


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  stun_timeout_val_port_range (False, any, None)
    STUN timeout (default= 2 minutes)


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  port (True, any, None)
    Single Destination Port or Port Range Start









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

