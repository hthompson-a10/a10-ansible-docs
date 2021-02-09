.. _a10_interface_ve_module:


a10_interface_ve -- Configures A10 interface.ve
===============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Virtual ethernet interface






Parameters
----------

  oper (False, any, None)
    Field oper


    user_trunk_id (optional, any, None)
      Field user_trunk_id


    line_protocol (optional, any, None)
      Field line_protocol


    ipv4_address (optional, any, None)
      IP address


    ipv4_addr_count (optional, any, None)
      Field ipv4_addr_count


    ipv6_addr_count (optional, any, None)
      Field ipv6_addr_count


    ipv4_netmask (optional, any, None)
      IP subnet mask


    ipv4_list (optional, any, None)
      Field ipv4_list


    igmp_query_sent (optional, any, None)
      Field igmp_query_sent


    icmp6_rate_limit_current (optional, any, None)
      Field icmp6_rate_limit_current


    ipv6_list (optional, any, None)
      Field ipv6_list


    ipv6_link_local (optional, any, None)
      Field ipv6_link_local


    ipv6_link_local_scope (optional, any, None)
      Field ipv6_link_local_scope


    icmp_rate_limit_current (optional, any, None)
      Field icmp_rate_limit_current


    ipv6_link_local_prefix (optional, any, None)
      Field ipv6_link_local_prefix


    mac (optional, any, None)
      Field mac


    icmp_rate_over_limit_drop (optional, any, None)
      Field icmp_rate_over_limit_drop


    ipv6_link_local_type (optional, any, None)
      Field ipv6_link_local_type


    icmp6_rate_over_limit_drop (optional, any, None)
      Field icmp6_rate_over_limit_drop


    state (optional, any, None)
      Field state


    ifnum (optional, any, None)
      Virtual ethernet interface number


    link_type (optional, any, None)
      Field link_type



  map (False, any, None)
    Field map


    uuid (optional, any, None)
      uuid of the object


    inside (optional, any, None)
      Configure MAP inside interface (connected to MAP domains)


    map_t_inside (optional, any, None)
      Configure MAP inside interface (connected to MAP domains)


    map_t_outside (optional, any, None)
      Configure MAP outside interface


    outside (optional, any, None)
      Configure MAP outside interface



  mtu (False, any, None)
    Interface mtu (Interface MTU, default 1 (min MTU is 1280 for IPv6))


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ip (False, any, None)
    Field ip


    max_resp_time (optional, any, None)
      Maximum Response Time (Max Response Time (Default is 100))


    rip (optional, any, None)
      Field rip


    dhcp (optional, any, None)
      Use DHCP to configure IP address


    stateful_firewall (optional, any, None)
      Field stateful_firewall


    uuid (optional, any, None)
      uuid of the object


    slb_partition_redirect (optional, any, None)
      Redirect SLB traffic across partition


    inside (optional, any, None)
      Configure interface as inside


    allow_promiscuous_vip (optional, any, None)
      Allow traffic to be associated with promiscuous VIP


    server (optional, any, None)
      Server facing interface for IPv4/v6 traffic


    outside (optional, any, None)
      Configure interface as outside


    client (optional, any, None)
      Client facing interface for IPv4/v6 traffic


    ttl_ignore (optional, any, None)
      Ignore TTL decrement for a received packet


    generate_membership_query (optional, any, None)
      Enable Membership Query


    router (optional, any, None)
      Field router


    query_interval (optional, any, None)
      1 - 255 (Default is 125)


    helper_address_list (optional, any, None)
      Field helper_address_list


    ospf (optional, any, None)
      Field ospf


    address_list (optional, any, None)
      Field address_list



  ansible_password (True, any, None)
    Password for AXAPI authentication


  ddos (False, any, None)
    Field ddos


    outside (optional, any, None)
      DDoS inside (trusted) or outside (untrusted) interface


    inside (optional, any, None)
      DDoS inside (trusted) or outside (untrusted) interface


    uuid (optional, any, None)
      uuid of the object



  l3_vlan_fwd_disable (False, any, None)
    Disable L3 forwarding between VLANs for incoming packets on this interface


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  isis (False, any, None)
    Field isis


    mesh_group (optional, any, None)
      Field mesh_group


    bfd_cfg (optional, any, None)
      Field bfd_cfg


    password_list (optional, any, None)
      Field password_list


    lsp_interval (optional, any, None)
      Set LSP transmission interval (LSP transmission interval (milliseconds))


    padding (optional, any, None)
      Add padding to IS-IS hello packets


    csnp_interval_list (optional, any, None)
      Field csnp_interval_list


    hello_multiplier_list (optional, any, None)
      Field hello_multiplier_list


    priority_list (optional, any, None)
      Field priority_list


    wide_metric_list (optional, any, None)
      Field wide_metric_list


    uuid (optional, any, None)
      uuid of the object


    retransmit_interval (optional, any, None)
      Set per-LSP retransmission interval (Interval between retransmissions of the same LSP (seconds))


    metric_list (optional, any, None)
      Field metric_list


    network (optional, any, None)
      'broadcast'= Specify IS-IS broadcast multi-access network; 'point-to-point'= Specify IS-IS point-to-point network;


    circuit_type (optional, any, None)
      'level-1'= Level-1 only adjacencies are formed; 'level-1-2'= Level-1-2 adjacencies are formed; 'level-2-only'= Level-2 only adjacencies are formed;


    hello_interval_list (optional, any, None)
      Field hello_interval_list


    authentication (optional, any, None)
      Field authentication


    hello_interval_minimal_list (optional, any, None)
      Field hello_interval_minimal_list



  nptv6 (False, any, None)
    Field nptv6


    domain_list (optional, any, None)
      Field domain_list



  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  icmp_rate_limit (False, any, None)
    Field icmp_rate_limit


    lockup (optional, any, None)
      Enter lockup state when ICMP rate exceeds lockup rate limit (Maximum rate limit. If exceeds this limit, drop all ICMP packet for a time period)


    normal (optional, any, None)
      Normal rate limit. If exceeds this limit, drop the ICMP packet that goes over the limit


    lockup_period (optional, any, None)
      Lockup period (second)



  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'num_pkts'= Input packets; 'num_total_bytes'= Input bytes; 'num_unicast_pkts'= Received unicasts; 'num_broadcast_pkts'= Received broadcasts; 'num_multicast_pkts'= Received multicasts; 'num_tx_pkts'= Transmitted packets; 'num_total_tx_bytes'= Transmitted bytes; 'num_unicast_tx_pkts'= Transmitted unicasts; 'num_broadcast_tx_pkts'= Transmitted broadcasts; 'num_multicast_tx_pkts'= Transmitted multicasts; 'rate_pkt_sent'= Packet sent rate packets/sec; 'rate_byte_sent'= Byte sent rate bits/sec; 'rate_pkt_rcvd'= Packet received rate packets/sec; 'rate_byte_rcvd'= Byte received rate bits/sec; 'load_interval'= Load Interval;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    rate_pkt_rcvd (optional, any, None)
      Packet received rate packets/sec


    num_multicast_pkts (optional, any, None)
      Received multicasts


    num_broadcast_pkts (optional, any, None)
      Received broadcasts


    rate_byte_sent (optional, any, None)
      Byte sent rate bits/sec


    rate_byte_rcvd (optional, any, None)
      Byte received rate bits/sec


    num_total_bytes (optional, any, None)
      Input bytes


    load_interval (optional, any, None)
      Load Interval


    num_pkts (optional, any, None)
      Input packets


    num_tx_pkts (optional, any, None)
      Transmitted packets


    num_total_tx_bytes (optional, any, None)
      Transmitted bytes


    num_unicast_pkts (optional, any, None)
      Received unicasts


    num_broadcast_tx_pkts (optional, any, None)
      Transmitted broadcasts


    num_multicast_tx_pkts (optional, any, None)
      Transmitted multicasts


    ifnum (optional, any, None)
      Virtual ethernet interface number


    num_unicast_tx_pkts (optional, any, None)
      Transmitted unicasts


    rate_pkt_sent (optional, any, None)
      Packet sent rate packets/sec



  uuid (False, any, None)
    uuid of the object


  lw_4o6 (False, any, None)
    Field lw_4o6


    outside (optional, any, None)
      Configure LW-4over6 inside interface


    inside (optional, any, None)
      Configure LW-4over6 outside interface


    uuid (optional, any, None)
      uuid of the object



  icmpv6_rate_limit (False, any, None)
    Field icmpv6_rate_limit


    normal_v6 (optional, any, None)
      Normal rate limit. If exceeds this limit, drop the ICMP packet that goes over the limit


    lockup_v6 (optional, any, None)
      Enter lockup state when ICMP rate exceeds lockup rate limit (Maximum rate limit. If exceeds this limit, drop all ICMP packet for a time period)


    lockup_period_v6 (optional, any, None)
      Lockup period (second)



  bfd (False, any, None)
    Field bfd


    authentication (optional, any, None)
      Field authentication


    echo (optional, any, None)
      Enable BFD Echo


    interval_cfg (optional, any, None)
      Field interval_cfg


    uuid (optional, any, None)
      uuid of the object


    demand (optional, any, None)
      Demand mode



  ifnum (True, any, None)
    Virtual ethernet interface number


  access_list (False, any, None)
    Field access_list


    acl_id (optional, any, None)
      ACL id


    acl_name (optional, any, None)
      Named Access List



  name (False, any, None)
    Name for the interface


  state (True, any, None)
    State of the object to be created.


  ipv6 (False, any, None)
    Field ipv6


    router_adver (optional, any, None)
      Field router_adver


    v6_acl_name (optional, any, None)
      Apply ACL rules to incoming packets on this interface (Named Access List)


    uuid (optional, any, None)
      uuid of the object


    inbound (optional, any, None)
      ACL applied on incoming packets to this interface


    inside (optional, any, None)
      Configure interface as NAT inside


    rip (optional, any, None)
      Field rip


    ipv6_enable (optional, any, None)
      Enable IPv6 processing


    outside (optional, any, None)
      Configure interface as NAT outside


    ttl_ignore (optional, any, None)
      Ignore TTL decrement for a received packet


    router (optional, any, None)
      Field router


    stateful_firewall (optional, any, None)
      Field stateful_firewall


    ospf (optional, any, None)
      Field ospf


    address_list (optional, any, None)
      Field address_list



  action (False, any, None)
    'enable'= Enable; 'disable'= Disable;


  trap_source (False, any, None)
    The trap source


  user_tag (False, any, None)
    Customized tag









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

