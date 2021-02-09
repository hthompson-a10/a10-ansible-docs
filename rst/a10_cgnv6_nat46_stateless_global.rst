.. _a10_cgnv6_nat46_stateless_global_module:


a10_cgnv6_nat46_stateless_global -- Configures A10 cgnv6.nat46.stateless.global
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Stateless NAT46 Statistics






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'outbound_ipv4_received'= Outbound IPv4 packets received; 'outbound_ipv4_drop'= Outbound IPv4 packets dropped; 'outbound_ipv4_fragment_received'= Outbound IPv4 fragment packets received; 'outbound_ipv6_unreachable'= Outbound IPv6 destination unreachable; 'outbound_ipv6_fragmented'= Outbound IPv6 packets fragmented; 'inbound_ipv6_received'= Inbound IPv6 packets received; 'inbound_ipv6_drop'= Inbound IPv6 packets dropped; 'inbound_ipv6_fragment_received'= Inbound IPv6 fragment packets received; 'inbound_ipv4_unreachable'= Inbound IPv4 destination unreachable; 'inbound_ipv4_fragmented'= Inbound IPv4 packets fragmented; 'packet_too_big'= Packet too big; 'fragment_error'= Fragment processing errors; 'icmpv6_to_icmp'= ICMPv6 to ICMP; 'icmpv6_to_icmp_error'= ICMPv6 to ICMP errors; 'icmp_to_icmpv6'= ICMP to ICMPv6; 'icmp_to_icmpv6_error'= ICMP to ICMPv6 errors; 'ha_standby'= HA is standby; 'other_error'= Other errors; 'conn_count'= conn count;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    outbound_ipv4_received (optional, any, None)
      Outbound IPv4 packets received


    outbound_ipv4_drop (optional, any, None)
      Outbound IPv4 packets dropped


    packet_too_big (optional, any, None)
      Packet too big


    icmp_to_icmpv6_error (optional, any, None)
      ICMP to ICMPv6 errors


    fragment_error (optional, any, None)
      Fragment processing errors


    inbound_ipv6_fragment_received (optional, any, None)
      Inbound IPv6 fragment packets received


    outbound_ipv6_unreachable (optional, any, None)
      Outbound IPv6 destination unreachable


    icmpv6_to_icmp (optional, any, None)
      ICMPv6 to ICMP


    inbound_ipv4_unreachable (optional, any, None)
      Inbound IPv4 destination unreachable


    other_error (optional, any, None)
      Other errors


    outbound_ipv6_fragmented (optional, any, None)
      Outbound IPv6 packets fragmented


    ha_standby (optional, any, None)
      HA is standby


    inbound_ipv6_received (optional, any, None)
      Inbound IPv6 packets received


    icmp_to_icmpv6 (optional, any, None)
      ICMP to ICMPv6


    inbound_ipv6_drop (optional, any, None)
      Inbound IPv6 packets dropped


    icmpv6_to_icmp_error (optional, any, None)
      ICMPv6 to ICMP errors


    inbound_ipv4_fragmented (optional, any, None)
      Inbound IPv4 packets fragmented


    outbound_ipv4_fragment_received (optional, any, None)
      Outbound IPv4 fragment packets received


    conn_count (optional, any, None)
      conn count



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

