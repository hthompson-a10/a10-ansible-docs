.. _a10_interface_ethernet_module:


a10_interface_ethernet -- Configures A10 interface.ethernet
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Ethernet interface






Parameters
----------

  oper (False, any, None)
    Field oper


    line_protocol (optional, any, None)
      Field line_protocol


    outgoing_pkts_mirrored (optional, any, None)
      Field outgoing_pkts_mirrored


    rate_byte_sent (optional, any, None)
      Field rate_byte_sent


    actual_speed (optional, any, None)
      Field actual_speed


    is_tagged (optional, any, None)
      Field is_tagged


    outgoing_pkts_monitored (optional, any, None)
      Field outgoing_pkts_monitored


    ipv4_list (optional, any, None)
      Field ipv4_list


    vlan_id (optional, any, None)
      Field vlan_id


    ipv6_link_local (optional, any, None)
      Field ipv6_link_local


    config_speed (optional, any, None)
      Field config_speed


    icmp6_rate_over_limit_drop (optional, any, None)
      Field icmp6_rate_over_limit_drop


    output_utilization (optional, any, None)
      Field output_utilization


    incoming_pkts_mirrored (optional, any, None)
      Field incoming_pkts_mirrored


    icmp_rate_limit_current (optional, any, None)
      Field icmp_rate_limit_current


    state (optional, any, None)
      Field state


    is_device_transparent (optional, any, None)
      Field is_device_transparent


    media_type (optional, any, None)
      Field media_type


    ipv6_link_local_type (optional, any, None)
      Field ipv6_link_local_type


    link_type (optional, any, None)
      Field link_type


    rate_pkt_rcvd (optional, any, None)
      Field rate_pkt_rcvd


    current_vnp_id (optional, any, None)
      Field current_vnp_id


    ipv4_address (optional, any, None)
      IP address


    ipv4_addr_count (optional, any, None)
      Field ipv4_addr_count


    port_vnp_id (optional, any, None)
      Field port_vnp_id


    ipv6_addr_count (optional, any, None)
      Field ipv6_addr_count


    actual_duplexity (optional, any, None)
      Field actual_duplexity


    incoming_pkts_monitored (optional, any, None)
      Field incoming_pkts_monitored


    igmp_query_sent (optional, any, None)
      Field igmp_query_sent


    icmp6_rate_limit_current (optional, any, None)
      Field icmp6_rate_limit_current


    ipv6_list (optional, any, None)
      Field ipv6_list


    ipv6_link_local_scope (optional, any, None)
      Field ipv6_link_local_scope


    is_pristine (optional, any, None)
      Field is_pristine


    ipv6_link_local_prefix (optional, any, None)
      Field ipv6_link_local_prefix


    mac (optional, any, None)
      Field mac


    icmp_rate_over_limit_drop (optional, any, None)
      Field icmp_rate_over_limit_drop


    input_utilization (optional, any, None)
      Field input_utilization


    is_lead_member (optional, any, None)
      Field is_lead_member


    ifnum (optional, any, None)
      Ethernet interface number


    rate_byte_rcvd (optional, any, None)
      Field rate_byte_rcvd


    rate_pkt_sent (optional, any, None)
      Field rate_pkt_sent


    tagged_vlan_list (optional, any, None)
      Field tagged_vlan_list


    config_duplexity (optional, any, None)
      Field config_duplexity


    ipv4_netmask (optional, any, None)
      IP subnet mask



  fec_forced_on (False, any, None)
    turn on the FEC


  ansible_username (True, any, None)
    Username for AXAPI authentication


  speed_forced_40g (False, any, None)
    force the speed to be 40G on 100G link


  media_type_copper (False, any, None)
    Set the media type to copper


  ddos (False, any, None)
    Field ddos


    outside (optional, any, None)
      DDoS outside (untrusted) interface


    inside (optional, any, None)
      DDoS inside (trusted) interface


    uuid (optional, any, None)
      uuid of the object



  speed (False, any, None)
    '10'= 10; '100'= 100; '1000'= 1000; 'auto'= auto;


  cpu_process (False, any, None)
    All Packets to this port are processed by CPU


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'packets_input'= Input packets; 'bytes_input'= Input bytes; 'received_broadcasts'= Received broadcasts; 'received_multicasts'= Received multicasts; 'received_unicasts'= Received unicasts; 'input_errors'= Input errors; 'crc'= CRC; 'frame'= Frames; 'runts'= Runts; 'giants'= Giants; 'packets_output'= Output packets; 'bytes_output'= Output bytes; 'transmitted_broadcasts'= Transmitted broadcasts; 'transmitted_multicasts'= Transmitted multicasts; 'transmitted_unicasts'= Transmitted unicasts; 'output_errors'= Output errors; 'collisions'= Collisions; 'giants_output'= Output Giants; 'rate_pkt_sent'= Packet sent rate packets/sec; 'rate_byte_sent'= Byte sent rate bits/sec; 'rate_pkt_rcvd'= Packet received rate packets/sec; 'rate_byte_rcvd'= Byte received rate bits/sec; 'load_interval'= Load Interval;



  load_interval (False, any, None)
    Configure Load Interval (Seconds (5-300, Multiple of 5), default 300)


  fec_forced_off (False, any, None)
    turn off the FEC


  stats (False, any, None)
    Field stats


    giants (optional, any, None)
      Giants


    packets_output (optional, any, None)
      Output packets


    crc (optional, any, None)
      CRC


    frame (optional, any, None)
      Frames


    giants_output (optional, any, None)
      Output Giants


    rate_byte_sent (optional, any, None)
      Byte sent rate bits/sec


    rate_byte_rcvd (optional, any, None)
      Byte received rate bits/sec


    runts (optional, any, None)
      Runts


    bytes_output (optional, any, None)
      Output bytes


    input_errors (optional, any, None)
      Input errors


    bytes_input (optional, any, None)
      Input bytes


    transmitted_broadcasts (optional, any, None)
      Transmitted broadcasts


    rate_pkt_rcvd (optional, any, None)
      Packet received rate packets/sec


    load_interval (optional, any, None)
      Load Interval


    transmitted_multicasts (optional, any, None)
      Transmitted multicasts


    packets_input (optional, any, None)
      Input packets


    received_multicasts (optional, any, None)
      Received multicasts


    received_broadcasts (optional, any, None)
      Received broadcasts


    transmitted_unicasts (optional, any, None)
      Transmitted unicasts


    collisions (optional, any, None)
      Collisions


    ifnum (optional, any, None)
      Ethernet interface number


    received_unicasts (optional, any, None)
      Received unicasts


    output_errors (optional, any, None)
      Output errors


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



  l3_vlan_fwd_disable (False, any, None)
    Field l3_vlan_fwd_disable


  access_list (False, any, None)
    Field access_list


    acl_id (optional, any, None)
      ACL id


    acl_name (optional, any, None)
      Apply an access list (Named Access List)



  state (True, any, None)
    State of the object to be created.


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


    cache_spoofing_port (optional, any, None)
      This interface connects to spoofing cache


    server (optional, any, None)
      Server facing interface for IPv4/v6 traffic


    outside (optional, any, None)
      Configure interface as outside


    allow_promiscuous_vip (optional, any, None)
      Allow traffic to be associated with promiscuous VIP


    client (optional, any, None)
      Client facing interface for IPv4/v6 traffic


    ttl_ignore (optional, any, None)
      Ignore TTL decrement for a received packet before sending out


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



  remove_vlan_tag (False, any, None)
    Remove the vlan tag for egressing packets


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



  auto_neg_enable (False, any, None)
    enable auto-negotiation


  ipv6 (False, any, None)
    Field ipv6


    router_adver (optional, any, None)
      Field router_adver


    uuid (optional, any, None)
      uuid of the object


    inside (optional, any, None)
      Configure interface as inside


    rip (optional, any, None)
      Field rip


    ipv6_enable (optional, any, None)
      Enable IPv6 processing


    outside (optional, any, None)
      Configure interface as outside


    access_list_cfg (optional, any, None)
      Field access_list_cfg


    ttl_ignore (optional, any, None)
      Ignore TTL decrement for a received packet before sending out


    router (optional, any, None)
      Field router


    stateful_firewall (optional, any, None)
      Field stateful_firewall


    ospf (optional, any, None)
      Field ospf


    address_list (optional, any, None)
      Field address_list



  trunk_group_list (False, any, None)
    Field trunk_group_list


    trunk_number (optional, any, None)
      Trunk Number


    uuid (optional, any, None)
      uuid of the object


    ntype (optional, any, None)
      'static'= Static (default); 'lacp'= lacp; 'lacp-udld'= lacp-udld;


    port_priority (optional, any, None)
      Set LACP priority for a port (LACP port priority)


    admin_key (optional, any, None)
      LACP admin key (Admin key value)


    mode (optional, any, None)
      'active'= enable initiation of LACP negotiation on a port(default); 'passive'= disable initiation of LACP negotiation on a port;


    timeout (optional, any, None)
      'long'= Set LACP long timeout (default); 'short'= Set LACP short timeout;


    udld_timeout_cfg (optional, any, None)
      Field udld_timeout_cfg


    user_tag (optional, any, None)
      Customized tag



  cpu_process_dir (False, any, None)
    'primary'= Primary board; 'blade'= blade board; 'hash-dip'= Hash based on the Destination IP; 'hash-sip'= Hash based on the Source IP; 'hash-dmac'= Hash based on the Destination MAC; 'hash-smac'= Hash based on the Source MAC;


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


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



  trap_source (False, any, None)
    The trap source


  ansible_port (True, any, None)
    Port for AXAPI authentication


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



  name (False, any, None)
    Name for the interface


  duplexity (False, any, None)
    'Full'= Full; 'Half'= Half; 'auto'= auto;


  ansible_password (True, any, None)
    Password for AXAPI authentication


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



  monitor_list (False, any, None)
    Field monitor_list


    monitor_vlan (optional, any, None)
      VLAN number


    mirror_index (optional, any, None)
      Mirror index


    monitor (optional, any, None)
      'input'= Incoming packets; 'output'= Outgoing packets; 'both'= Both incoming and outgoing packets;



  mtu (False, any, None)
    Interface mtu (Interface MTU, default 1 (min MTU is 1280 for IPv6))


  ifnum (True, any, None)
    Ethernet interface number


  flow_control (False, any, None)
    Enable 802.3x flow control on full duplex port


  icmpv6_rate_limit (False, any, None)
    Field icmpv6_rate_limit


    normal_v6 (optional, any, None)
      Normal rate limit. If exceeds this limit, drop the ICMP packet that goes over the limit


    lockup_v6 (optional, any, None)
      Enter lockup state when ICMP rate exceeds lockup rate limit (Maximum rate limit. If exceeds this limit, drop all ICMP packet for a time period)


    lockup_period_v6 (optional, any, None)
      Lockup period (second)



  action (False, any, None)
    'enable'= Enable; 'disable'= Disable;


  traffic_distribution_mode (False, any, None)
    'sip'= sip; 'dip'= dip; 'primary'= primary; 'blade'= blade; 'l4-src-port'= l4-src-port; 'l4-dst-port'= l4-dst-port;


  user_tag (False, any, None)
    Customized tag


  lldp (False, any, None)
    Field lldp


    enable_cfg (optional, any, None)
      Field enable_cfg


    tx_dot1_cfg (optional, any, None)
      Field tx_dot1_cfg


    notification_cfg (optional, any, None)
      Field notification_cfg


    tx_tlvs_cfg (optional, any, None)
      Field tx_tlvs_cfg


    uuid (optional, any, None)
      uuid of the object










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

