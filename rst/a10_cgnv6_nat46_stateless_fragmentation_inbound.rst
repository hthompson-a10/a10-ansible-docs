.. _a10_cgnv6_nat46_stateless_fragmentation_inbound_module:


a10_cgnv6_nat46_stateless_fragmentation_inbound -- Configures A10 cgnv6.nat46.stateless.fragmentation.inbound
=============================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Stateless NAT46 fragmentation rules for inbound oversize packets






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


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  action (False, any, None)
    'drop'= Drop Silently; 'ipv4'= Use IPv4 fragmentation for oversize packets (default); 'send-icmpv6'= Send ICMP Type 2 Code 0 (Packet Too Big);


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

