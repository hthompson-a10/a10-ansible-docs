.. _a10_interface_lif_module:


a10_interface_lif -- Configures A10 interface.lif
=================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Logical interface






Parameters
----------

  oper (False, any, None)
    Field oper


    igmp_query_sent (optional, any, None)
      Field igmp_query_sent


    icmp6_rate_limit_current (optional, any, None)
      Field icmp6_rate_limit_current


    ipv6_list (optional, any, None)
      Field ipv6_list


    icmp_rate_limit_current (optional, any, None)
      Field icmp_rate_limit_current


    mac (optional, any, None)
      Field mac


    icmp_rate_over_limit_drop (optional, any, None)
      Field icmp_rate_over_limit_drop


    ipv4_list (optional, any, None)
      Field ipv4_list


    icmp6_rate_over_limit_drop (optional, any, None)
      Field icmp6_rate_over_limit_drop


    ipv4_addr_count (optional, any, None)
      Field ipv4_addr_count


    state (optional, any, None)
      Field state


    ipv6_addr_count (optional, any, None)
      Field ipv6_addr_count


    ifnum (optional, any, None)
      Lif interface number



  ansible_username (True, any, None)
    Username for AXAPI authentication


  ip (False, any, None)
    Field ip


    uuid (optional, any, None)
      uuid of the object


    outside (optional, any, None)
      Configure interface as outside


    inside (optional, any, None)
      Configure interface as inside


    max_resp_time (optional, any, None)
      Maximum Response Time (Max Response Time (Default is 100))


    cache_spoofing_port (optional, any, None)
      This interface connects to spoofing cache


    rip (optional, any, None)
      Field rip


    allow_promiscuous_vip (optional, any, None)
      Allow traffic to be associated with promiscuous VIP


    dhcp (optional, any, None)
      Use DHCP to configure IP address


    generate_membership_query (optional, any, None)
      Enable Membership Query


    router (optional, any, None)
      Field router


    query_interval (optional, any, None)
      1 - 255 (Default is 125)


    ospf (optional, any, None)
      Field ospf


    address_list (optional, any, None)
      Field address_list



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  stats (False, any, None)
    Field stats


    num_tx_pkts (optional, any, None)
      Field num_tx_pkts


    dropped_dis_tx_pkts (optional, any, None)
      Field dropped_dis_tx_pkts


    num_total_tx_bytes (optional, any, None)
      Field num_total_tx_bytes


    num_multicast_pkts (optional, any, None)
      Field num_multicast_pkts


    num_unicast_pkts (optional, any, None)
      Field num_unicast_pkts


    num_broadcast_tx_pkts (optional, any, None)
      Field num_broadcast_tx_pkts


    num_broadcast_pkts (optional, any, None)
      Field num_broadcast_pkts


    num_multicast_tx_pkts (optional, any, None)
      Field num_multicast_tx_pkts


    ifnum (optional, any, None)
      Lif interface number


    num_unicast_tx_pkts (optional, any, None)
      Field num_unicast_tx_pkts


    dropped_rx_pkts (optional, any, None)
      Field dropped_rx_pkts


    num_total_bytes (optional, any, None)
      Field num_total_bytes


    num_pkts (optional, any, None)
      Field num_pkts


    dropped_dis_rx_pkts (optional, any, None)
      Field dropped_dis_rx_pkts


    dropped_tx_pkts (optional, any, None)
      Field dropped_tx_pkts



  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'num_pkts'= num_pkts; 'num_total_bytes'= num_total_bytes; 'num_unicast_pkts'= num_unicast_pkts; 'num_broadcast_pkts'= num_broadcast_pkts; 'num_multicast_pkts'= num_multicast_pkts; 'num_tx_pkts'= num_tx_pkts; 'num_total_tx_bytes'= num_total_tx_bytes; 'num_unicast_tx_pkts'= num_unicast_tx_pkts; 'num_broadcast_tx_pkts'= num_broadcast_tx_pkts; 'num_multicast_tx_pkts'= num_multicast_tx_pkts; 'dropped_dis_rx_pkts'= dropped_dis_rx_pkts; 'dropped_rx_pkts'= dropped_rx_pkts; 'dropped_dis_tx_pkts'= dropped_dis_tx_pkts; 'dropped_tx_pkts'= dropped_tx_pkts;



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



  uuid (False, any, None)
    uuid of the object


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



  user_tag (False, any, None)
    Customized tag


  state (True, any, None)
    State of the object to be created.


  access_list (False, any, None)
    Field access_list


    acl_id (optional, any, None)
      ACL id


    acl_name (optional, any, None)
      Apply an access list (Named Access List)



  mtu (False, any, None)
    Interface mtu (Interface MTU, default 1 (min MTU is 1280 for IPv6))


  ifnum (True, any, None)
    Lif interface number


  action (False, any, None)
    'enable'= Enable; 'disable'= Disable;


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

