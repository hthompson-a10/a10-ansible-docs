.. _a10_overlay_tunnel_vtep_module:


a10_overlay_tunnel_vtep -- Configures A10 overlay-tunnel.vtep
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Virtual Tunnel end point Configuration






Parameters
----------

  ansible_username (True, any, None)
    Username for AXAPI authentication


  host_list (False, any, None)
    Field host_list


    overlay_mac_addr (optional, any, None)
      MAC Address of the overlay host


    ip_addr (optional, any, None)
      IPv4 address of the overlay host


    vni (optional, any, None)
       Configure the segment id ( VNI of the remote host)


    destination_vtep (optional, any, None)
      Configure the VTEP IP address (IPv4 address of the VTEP for the remote host)


    uuid (optional, any, None)
      uuid of the object



  source_ip_address (False, any, None)
    Field source_ip_address


    vni_list (optional, any, None)
      Field vni_list


    ip_address (optional, any, None)
      Source Tunnel End Point IPv4 address


    uuid (optional, any, None)
      uuid of the object



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  id (True, any, None)
    VTEP Identifier


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'cfg_err_count'= Config errors; 'flooded_pkt_count'= Flooded packet count; 'encap_unresolved_count'= Encap unresolved failures; 'unknown_encap_rx_pkt'= Encap miss rx pkts; 'unknown_encap_tx_pkt'= Encap miss tx pkts; 'arp_req_sent'= Arp request sent; 'vtep_host_learned'= Hosts learned; 'vtep_host_learn_error'= Host learn error; 'invalid_lif_rx'= Invalid Lif pkts in; 'invalid_lif_tx'= Invalid Lif pkts out; 'unknown_vtep_tx'= Vtep unknown tx; 'unknown_vtep_rx'= Vtep Unkown rx; 'unhandled_pkt_rx'= Unhandled packets in; 'unhandled_pkt_tx'= Unhandled packets out; 'total_pkts_rx'= Total packets out; 'total_bytes_rx'= Total packet bytes in; 'unicast_pkt_rx'= Total unicast packets in; 'bcast_pkt_rx'= Total broadcast packets in; 'mcast_pkt_rx'= Total multicast packets in; 'dropped_pkt_rx'= Dropped received packets; 'encap_miss_pkts_rx'= Encap missed in received packets; 'bad_chksum_pks_rx'= Bad checksum in received packets; 'requeue_pkts_in'= Requeued packets in; 'pkts_out'= Packets out; 'total_bytes_tx'= Packet bytes out; 'unicast_pkt_tx'= Unicast packets out; 'bcast_pkt_tx'= Broadcast packets out; 'mcast_pkt_tx'= Multicast packets out; 'dropped_pkts_tx'= Dropped packets out; 'large_pkts_rx'= Too large packets in; 'dot1q_pkts_rx'= Dot1q packets in; 'frag_pkts_tx'= Frag packets out; 'reassembled_pkts_rx'= Reassembled packets in; 'bad_inner_ipv4_len_rx'= bad inner ipv4 packet len; 'bad_inner_ipv6_len_rx'= Bad inner ipv6 packet len; 'lif_un_init_rx'= Lif uninitialized packets in;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  destination_ip_address_list (False, any, None)
    Field destination_ip_address_list


    vni_list (optional, any, None)
      Field vni_list


    ip_address (optional, any, None)
      IP Address of the remote VTEP


    user_tag (optional, any, None)
      Customized tag


    uuid (optional, any, None)
      uuid of the object


    encap (optional, any, None)
      'nvgre'= Tunnel Encapsulation Type is NVGRE; 'vxlan'= Tunnel Encapsulation Type is VXLAN;



  stats (False, any, None)
    Field stats


    total_bytes_rx (optional, any, None)
      Total packet bytes in


    dropped_pkt_rx (optional, any, None)
      Dropped received packets


    mcast_pkt_tx (optional, any, None)
      Multicast packets out


    unhandled_pkt_rx (optional, any, None)
      Unhandled packets in


    unknown_encap_tx_pkt (optional, any, None)
      Encap miss tx pkts


    reassembled_pkts_rx (optional, any, None)
      Reassembled packets in


    id (optional, any, None)
      VTEP Identifier


    frag_pkts_tx (optional, any, None)
      Frag packets out


    dropped_pkts_tx (optional, any, None)
      Dropped packets out


    total_bytes_tx (optional, any, None)
      Packet bytes out


    large_pkts_rx (optional, any, None)
      Too large packets in


    unicast_pkt_rx (optional, any, None)
      Total unicast packets in


    invalid_lif_rx (optional, any, None)
      Invalid Lif pkts in


    invalid_lif_tx (optional, any, None)
      Invalid Lif pkts out


    dot1q_pkts_rx (optional, any, None)
      Dot1q packets in


    vtep_host_learned (optional, any, None)
      Hosts learned


    unhandled_pkt_tx (optional, any, None)
      Unhandled packets out


    unknown_vtep_rx (optional, any, None)
      Vtep Unkown rx


    encap_miss_pkts_rx (optional, any, None)
      Encap missed in received packets


    unknown_encap_rx_pkt (optional, any, None)
      Encap miss rx pkts


    bad_chksum_pks_rx (optional, any, None)
      Bad checksum in received packets


    encap_unresolved_count (optional, any, None)
      Encap unresolved failures


    bad_inner_ipv6_len_rx (optional, any, None)
      Bad inner ipv6 packet len


    cfg_err_count (optional, any, None)
      Config errors


    unknown_vtep_tx (optional, any, None)
      Vtep unknown tx


    flooded_pkt_count (optional, any, None)
      Flooded packet count


    total_pkts_rx (optional, any, None)
      Total packets out


    vtep_host_learn_error (optional, any, None)
      Host learn error


    requeue_pkts_in (optional, any, None)
      Requeued packets in


    lif_un_init_rx (optional, any, None)
      Lif uninitialized packets in


    mcast_pkt_rx (optional, any, None)
      Total multicast packets in


    bcast_pkt_tx (optional, any, None)
      Broadcast packets out


    bcast_pkt_rx (optional, any, None)
      Total broadcast packets in


    unicast_pkt_tx (optional, any, None)
      Unicast packets out


    pkts_out (optional, any, None)
      Packets out


    bad_inner_ipv4_len_rx (optional, any, None)
      bad inner ipv4 packet len


    arp_req_sent (optional, any, None)
      Arp request sent



  uuid (False, any, None)
    uuid of the object


  ansible_password (True, any, None)
    Password for AXAPI authentication


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  encap (False, any, None)
    'nvgre'= Tunnel Encapsulation Type is NVGRE; 'vxlan'= Tunnel Encapsulation Type is VXLAN;


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

