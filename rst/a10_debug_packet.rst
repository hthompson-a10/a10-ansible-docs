.. _a10_debug_packet_module:


a10_debug_packet -- Configures A10 debug.packet
===============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Debug packet






Parameters
----------

  arp (False, any, None)
    ARP


  all (False, any, None)
    All


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ip (False, any, None)
    IP


  ipv6ad (False, any, None)
    IPV6 Address


  udp (False, any, None)
    Field udp


  tcp (False, any, None)
    Field tcp


  interface (False, any, None)
    Interface to debug


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  l3_protocol (False, any, None)
    Layer 3 protocol


  icmp (False, any, None)
    Field icmp


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  count (False, any, None)
    Maximum packets to capture. Default is 3000 (Specify maximum packet number. For umlimited, specify 0)


  ansible_port (True, any, None)
    Port for AXAPI authentication


  l4_protocol (False, any, None)
    Layer 4 protocol


  uuid (False, any, None)
    uuid of the object


  icmpv6 (False, any, None)
    Field icmpv6


  detail (False, any, None)
    Print packet content


  port_range (False, any, None)
    Port Number


  state (True, any, None)
    State of the object to be created.


  ipv4ad (False, any, None)
    IP Address


  neighbor (False, any, None)
    IPv6 Neighbor/Router


  ipv6 (False, any, None)
    IPV6


  ethernet (False, any, None)
    Ethernet interface number


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

