.. _a10_cgnv6_nat_icmp_module:


a10_cgnv6_nat_icmp -- Configures A10 cgnv6.nat.icmp
===================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure NAT ICMP settings






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


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  always_source_nat_errors (False, any, None)
    Source NAT intermediate routers' IPs for ICMP errors (default= disabled)


  respond_to_ping (False, any, None)
    Respond to ICMP echo requests to NAT pool IPs (default= disabled)


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

