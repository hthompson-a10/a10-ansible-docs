.. _a10_interface_tunnel_module:


a10_interface_tunnel -- Configures A10 interface.tunnel
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Tunnel interface






Parameters
----------

  oper (False, any, None)
    Field oper


    line_protocol (optional, any, None)
      Field line_protocol


    state (optional, any, None)
      Field state


    ipv6_link_local_scope (optional, any, None)
      Field ipv6_link_local_scope


    ipv4_address (optional, any, None)
      IPv4 address


    ipv4_addr_count (optional, any, None)
      Field ipv4_addr_count


    ipv6_addr_count (optional, any, None)
      Field ipv6_addr_count


    ipv4_netmask (optional, any, None)
      IPv4 subnet mask


    ipv4_list (optional, any, None)
      Field ipv4_list


    ipv6_list (optional, any, None)
      Field ipv6_list


    ipv6_link_local (optional, any, None)
      Field ipv6_link_local


    config_speed (optional, any, None)
      Field config_speed


    ipv6_link_local_prefix (optional, any, None)
      Field ipv6_link_local_prefix


    mac (optional, any, None)
      Field mac


    ifnum (optional, any, None)
      Tunnel interface number


    ipv6_link_local_type (optional, any, None)
      Field ipv6_link_local_type


    link_type (optional, any, None)
      Field link_type



  ansible_username (True, any, None)
    Username for AXAPI authentication


  ip (False, any, None)
    Field ip


    generate_membership_query_val (optional, any, None)
      1 - 255 (Default is 125)


    uuid (optional, any, None)
      uuid of the object


    address (optional, any, None)
      Field address


    generate_membership_query (optional, any, None)
      Enable Membership Query


    ospf (optional, any, None)
      Field ospf


    max_resp_time (optional, any, None)
      Max Response Time (Default is 100)


    rip (optional, any, None)
      Field rip



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
      'all'= all; 'num-rx-pkts'= received packets; 'num-total-rx-bytes'= received bytes; 'num-tx-pkts'= sent packets; 'num-total-tx-bytes'= sent bytes; 'num-rx- err-pkts'= received error packets; 'num-tx-err-pkts'= sent error packets; 'rate_pkt_sent'= Packet sent rate packets/sec; 'rate_byte_sent'= Byte sent rate bits/sec; 'rate_pkt_rcvd'= Packet received rate packets/sec; 'rate_byte_rcvd'= Byte received rate bits/sec;



  load_interval (False, any, None)
    Configure Load Interval (Seconds (5-300, Multiple of 5), default 300)


  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    num_tx_pkts (optional, any, None)
      sent packets


    num_total_tx_bytes (optional, any, None)
      sent bytes


    num_rx_pkts (optional, any, None)
      received packets


    num_tx_err_pkts (optional, any, None)
      sent error packets


    num_total_rx_bytes (optional, any, None)
      received bytes


    rate_pkt_rcvd (optional, any, None)
      Packet received rate packets/sec


    rate_byte_sent (optional, any, None)
      Byte sent rate bits/sec


    ifnum (optional, any, None)
      Tunnel interface number


    rate_byte_rcvd (optional, any, None)
      Byte received rate bits/sec


    num_rx_err_pkts (optional, any, None)
      received error packets


    rate_pkt_sent (optional, any, None)
      Packet sent rate packets/sec



  name (False, any, None)
    Name for the interface


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  mtu (False, any, None)
    Interface mtu (Interface MTU, default 1 (min MTU is 1280 for IPv6))


  ifnum (True, any, None)
    Tunnel interface number


  ipv6 (False, any, None)
    Field ipv6


    address_cfg (optional, any, None)
      Field address_cfg


    ipv6_enable (optional, any, None)
      Enable IPv6 processing


    ospf (optional, any, None)
      Field ospf


    uuid (optional, any, None)
      uuid of the object


    router (optional, any, None)
      Field router



  action (False, any, None)
    'enable'= Enable; 'disable'= Disable;


  user_tag (False, any, None)
    Customized tag


  speed (False, any, None)
    Speed in Gbit/Sec (Default 10 Gbps)









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

