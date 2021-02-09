.. _a10_cgnv6_sixrd_domain_module:


a10_cgnv6_sixrd_domain -- Configures A10 cgnv6.sixrd.domain
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

sixrd Domain






Parameters
----------

  ansible_username (True, any, None)
    Username for AXAPI authentication


  br_ipv4_address (False, any, None)
    6rd BR IPv4 address


  ce_ipv4_network (False, any, None)
    Customer Edge IPv4 network


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'outbound-tcp-packets-received'= Outbound TCP packets received; 'outbound-udp-packets-received'= Outbound UDP packets received; 'outbound-icmp- packets-received'= Outbound ICMP packets received; 'outbound-other-packets- received'= Outbound other packets received; 'outbound-packets-drop'= Outbound packets dropped; 'outbound-ipv6-dest-unreachable'= Outbound IPv6 destination unreachable; 'outbound-fragment-ipv6'= Outbound Fragmented IPv6; 'inbound-tcp- packets-received'= Inbound TCP packets received; 'inbound-udp-packets- received'= Inbound UDP packets received; 'inbound-icmp-packets-received'= Inbound ICMP packets received; 'inbound-other-packets-received'= Inbound other packets received; 'inbound-packets-drop'= Inbound packets dropped; 'inbound- ipv4-dest-unreachable'= Inbound IPv4 destination unreachable; 'inbound- fragment-ipv4'= Inbound Fragmented IPv4; 'inbound-tunnel-fragment-ipv6'= Inbound Fragmented IPv6 in tunnel; 'vport-matched'= Traffic match SLB virtual port; 'unknown-delegated-prefix'= Unknown 6rd delegated prefix; 'packet-too- big'= Packet too big; 'not-local-ip'= Not local IP; 'fragment-error'= Fragment processing errors; 'other-error'= Other errors;



  ce_ipv4_netmask (False, any, None)
    Mask length


  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    outbound_tcp_packets_received (optional, any, None)
      Outbound TCP packets received


    outbound_icmp_packets_received (optional, any, None)
      Outbound ICMP packets received


    outbound_packets_drop (optional, any, None)
      Outbound packets dropped


    packet_too_big (optional, any, None)
      Packet too big


    inbound_other_packets_received (optional, any, None)
      Inbound other packets received


    outbound_udp_packets_received (optional, any, None)
      Outbound UDP packets received


    not_local_ip (optional, any, None)
      Not local IP


    inbound_ipv4_dest_unreachable (optional, any, None)
      Inbound IPv4 destination unreachable


    inbound_tcp_packets_received (optional, any, None)
      Inbound TCP packets received


    unknown_delegated_prefix (optional, any, None)
      Unknown 6rd delegated prefix


    outbound_other_packets_received (optional, any, None)
      Outbound other packets received


    inbound_packets_drop (optional, any, None)
      Inbound packets dropped


    other_error (optional, any, None)
      Other errors


    inbound_tunnel_fragment_ipv6 (optional, any, None)
      Inbound Fragmented IPv6 in tunnel


    outbound_ipv6_dest_unreachable (optional, any, None)
      Outbound IPv6 destination unreachable


    vport_matched (optional, any, None)
      Traffic match SLB virtual port


    fragment_error (optional, any, None)
      Fragment processing errors


    name (optional, any, None)
      6rd Domain name


    inbound_icmp_packets_received (optional, any, None)
      Inbound ICMP packets received


    inbound_udp_packets_received (optional, any, None)
      Inbound UDP packets received


    inbound_fragment_ipv4 (optional, any, None)
      Inbound Fragmented IPv4


    outbound_fragment_ipv6 (optional, any, None)
      Outbound Fragmented IPv6



  name (True, any, None)
    6rd Domain name


  user_tag (False, any, None)
    Customized tag


  mtu (False, any, None)
    Tunnel MTU


  state (True, any, None)
    State of the object to be created.


  ipv6_prefix (False, any, None)
    IPv6 prefix


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

