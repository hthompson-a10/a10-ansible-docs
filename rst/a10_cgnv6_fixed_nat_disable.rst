.. _a10_cgnv6_fixed_nat_disable_module:


a10_cgnv6_fixed_nat_disable -- Configures A10 cgnv6.fixed.nat.disable
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Disable fixed-nat configuration (Operation)






Parameters
----------

  ansible_username (True, any, None)
    Username for AXAPI authentication


  clear_session (False, any, None)
    Clear all sessions


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  inside_end_v4address (False, any, None)
    IPv4 Inside User End Address


  inside_start_v4address (False, any, None)
    IPv4 Inside User Start Address


  ansible_host (True, any, None)
    Host for AXAPI authentication


  v6_netmask (False, any, None)
    Inside User IPv6 Netmask


  inside_end_v6address (False, any, None)
    IPv6 Inside User End Address


  ansible_port (True, any, None)
    Port for AXAPI authentication


  ip_list (False, any, None)
    Name of IP List used to specify Inside Users


  inside_start_v6address (False, any, None)
    IPv6 Inside User Start Address


  a10_partition (False, any, None)
    Destination/target partition for object/command


  partition (False, any, None)
    Inside User Partition (Partition Name)


  state (True, any, None)
    State of the object to be created.


  v4_netmask (False, any, None)
    IPv4 Netmask


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

