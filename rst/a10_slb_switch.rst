.. _a10_slb_switch_module:


a10_slb_switch -- Configures A10 slb.switch
===========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure slb switch






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'fwlb'= FWLB; 'licexpire_drop'= License Expire Drop; 'bwl_drop'= BW Limit Drop; 'rx_kernel'= Received kernel; 'rx_arp_req'= ARP REQ Rcvd; 'rx_arp_resp'= ARP RESP Rcvd; 'vlan_flood'= VLAN Flood; 'l2_def_vlan_drop'= L2 Default Vlan FWD Drop; 'ipv4_noroute_drop'= IPv4 No Route Drop; 'ipv6_noroute_drop'= IPv6 No Route Drop; 'prot_down_drop'= Prot Down Drop; 'l2_forward'= L2 Forward; 'l3_forward_ip'= L3 IP Forward; 'l3_forward_ipv6'= L3 IPv6 Forward; 'l4_process'= L4 Process; 'unknown_prot_drop'= Unknown Prot Drop; 'ttl_exceeded_drop'= TTL Exceeded Drop; 'linkdown_drop'= Link Down Drop; 'sport_drop'= SPORT Drop; 'incorrect_len_drop'= Incorrect Length Drop; 'ip_defrag'= IP Defrag; 'acl_deny'= ACL Denys; 'ipfrag_tcp'= IP(TCP) Fragment Rcvd; 'ipfrag_overlap'= IP Fragment Overlap; 'ipfrag_timeout'= IP Fragment Timeout; 'ipfrag_overload'= IP Frag Overload Drops; 'ipfrag_reasmoks'= IP Fragment Reasm OKs; 'ipfrag_reasmfails'= IP Fragment Reasm Fails; 'land_drop'= Anomaly Land Attack Drop; 'ipoptions_drop'= Anomaly IP OPT Drops; 'badpkt_drop'= Bad Pkt Drop; 'pingofdeath_drop'= Anomaly PingDeath Drop; 'allfrag_drop'= Anomaly All Frag Drop; 'tcpnoflag_drop'= Anomaly TCP noFlag Drop; 'tcpsynfrag_drop'= Anomaly SYN Frag Drop; 'tcpsynfin_drop'= Anomaly TCP SYNFIN Drop; 'ipsec_drop'= IPSec Drop; 'bpdu_rcvd'= BPDUs Received; 'bpdu_sent'= BPDUs Sent; 'ctrl_syn_rate_drop'= SYN rate exceeded Drop; 'ip_defrag_invalid_len'= IP Invalid Length Frag; 'ipv4_frag_6rd_ok'= IPv4 Frag 6RD OK; 'ipv4_frag_6rd_drop'= IPv4 Frag 6RD Dropped; 'no_ip_drop'= No IP Drop; 'ipv6frag_udp'= IPv6 Frag UDP; 'ipv6frag_udp_dropped'= IPv6 Frag UDP Dropped; 'ipv6frag_tcp_dropped'= IPv6 Frag TCP Dropped; 'ipv6frag_ipip_ok'= IPv6 Frag IPIP OKs; 'ipv6frag_ipip_dropped'= IPv6 Frag IPIP Drop; 'ip_frag_oversize'= IP Fragment oversize; 'ip_frag_too_many'= IP Fragment too many; 'ipv4_novlanfwd_drop'= IPv4 No L3 VLAN FWD Drop; 'ipv6_novlanfwd_drop'= IPv6 No L3 VLAN FWD Drop; 'fpga_error_pkt1'= FPGA Error PKT1; 'fpga_error_pkt2'= FPGA Error PKT2; 'max_arp_drop'= Max ARP Drop; 'ipv6frag_tcp'= IPv6 Frag TCP; 'ipv6frag_icmp'= IPv6 Frag ICMP; 'ipv6frag_ospf'= IPv6 Frag OSPF; 'ipv6frag_esp'= IPv6 Frag ESP; 'l4_in_ctrl_cpu'= L4 In Ctrl CPU; 'mgmt_svc_drop'= Management Service Drop; 'jumbo_frag_drop'= Jumbo Frag Drop; 'ipv6_jumbo_frag_drop'= IPv6 Jumbo Frag Drop; 'ipipv6_jumbo_frag_drop'= IPIPv6 Jumbo Frag Drop; 'ipv6_ndisc_dad_solicits'= IPv6 DAD on Solicits; 'ipv6_ndisc_dad_adverts'= IPv6 DAD on Adverts; 'ipv6_ndisc_mac_changes'= IPv6 DAD MAC Changed; 'ipv6_ndisc_out_of_memory'= IPv6 DAD Out-of-memory; 'sp_non_ctrl_pkt_drop'= Shared IP mode non ctrl packet to linux drop; 'urpf_pkt_drop'= URPF check packet drop; 'fw_smp_zone_mismatch'= FW SMP Zone Mismatch; 'ipfrag_udp'= IP(UDP) Fragment Rcvd; 'ipfrag_icmp'= IP(ICMP) Fragment Rcvd; 'ipfrag_ospf'= IP(OSPF) Fragment Rcvd; 'ipfrag_esp'= IP(ESP) Fragment Rcvd; 'ipfrag_tcp_dropped'= IP Frag TCP Dropped; 'ipfrag_udp_dropped'= IP Frag UDP Dropped; 'ipfrag_ipip_dropped'= IP Frag IPIP Drop; 'redirect_fwd_fail'= Redirect failed in the fwd direction; 'redirect_fwd_sent'= Redirect succeeded in the fwd direction; 'redirect_rev_fail'= Redirect failed in the rev direction; 'redirect_rev_sent'= Redirect succeeded in the rev direction; 'redirect_setup_fail'= Redirect connection setup failed; 'ip_frag_sent'= IP frag sent; 'invalid_rx_arp_pkt'= Invalid ARP PKT Rcvd; 'invalid_sender_mac_arp_drop'= ARP PKT dropped due to invalid sender MAC; 'dev_based_arp_drop'= ARP PKT dropped due to interface state checks; 'scaleout_arp_drop'= ARP PKT dropped due to scaleout checks; 'virtual_ip_not_found_arp_drop'= ARP PKT dropped due to virtual IP not found; 'inactive_static_nat_pool_arp_drop'= ARP PKT dropped due to inactive static nat pool; 'inactive_nat_pool_arp_drop'= ARP PKT dropped due to inactive nat pool; 'scaleout_hairpin_arp_drop'= ARP PKT dropped due to scaleout hairpin checks; 'self_grat_arp_drop'= Self generated grat ARP PKT dropped; 'self_grat_nat_ip_arp_drop'= Self generated grat ARP PKT dropped for NAT IP; 'ip_not_found_arp_drop'= ARP PKT dropped due to IP not found; 'dev_link_down_arp_drop'= ARP PKT dropped due to interface is down; 'lacp_tx_intf_err_drop'= LACP interface error corrected;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    bwl_drop (optional, any, None)
      BW Limit Drop


    jumbo_frag_drop (optional, any, None)
      Jumbo Frag Drop


    ipv6_ndisc_mac_changes (optional, any, None)
      IPv6 DAD MAC Changed


    lacp_tx_intf_err_drop (optional, any, None)
      LACP interface error corrected


    fwlb (optional, any, None)
      FWLB


    ipfrag_tcp (optional, any, None)
      IP(TCP) Fragment Rcvd


    ipipv6_jumbo_frag_drop (optional, any, None)
      IPIPv6 Jumbo Frag Drop


    redirect_fwd_fail (optional, any, None)
      Redirect failed in the fwd direction


    ipv6frag_ipip_ok (optional, any, None)
      IPv6 Frag IPIP OKs


    urpf_pkt_drop (optional, any, None)
      URPF check packet drop


    ipfrag_esp (optional, any, None)
      IP(ESP) Fragment Rcvd


    ipfrag_ospf (optional, any, None)
      IP(OSPF) Fragment Rcvd


    rx_kernel (optional, any, None)
      Received kernel


    fw_smp_zone_mismatch (optional, any, None)
      FW SMP Zone Mismatch


    dev_based_arp_drop (optional, any, None)
      ARP PKT dropped due to interface state checks


    ctrl_syn_rate_drop (optional, any, None)
      SYN rate exceeded Drop


    self_grat_nat_ip_arp_drop (optional, any, None)
      Self generated grat ARP PKT dropped for NAT IP


    ipv6frag_udp_dropped (optional, any, None)
      IPv6 Frag UDP Dropped


    rx_arp_resp (optional, any, None)
      ARP RESP Rcvd


    l4_process (optional, any, None)
      L4 Process


    ip_frag_too_many (optional, any, None)
      IP Fragment too many


    ipfrag_tcp_dropped (optional, any, None)
      IP Frag TCP Dropped


    ipv6frag_tcp (optional, any, None)
      IPv6 Frag TCP


    redirect_fwd_sent (optional, any, None)
      Redirect succeeded in the fwd direction


    ipv4_frag_6rd_drop (optional, any, None)
      IPv4 Frag 6RD Dropped


    ipv6_jumbo_frag_drop (optional, any, None)
      IPv6 Jumbo Frag Drop


    invalid_sender_mac_arp_drop (optional, any, None)
      ARP PKT dropped due to invalid sender MAC


    inactive_static_nat_pool_arp_drop (optional, any, None)
      ARP PKT dropped due to inactive static nat pool


    linkdown_drop (optional, any, None)
      Link Down Drop


    redirect_setup_fail (optional, any, None)
      Redirect connection setup failed


    sport_drop (optional, any, None)
      SPORT Drop


    ipfrag_overlap (optional, any, None)
      IP Fragment Overlap


    self_grat_arp_drop (optional, any, None)
      Self generated grat ARP PKT dropped


    max_arp_drop (optional, any, None)
      Max ARP Drop


    redirect_rev_sent (optional, any, None)
      Redirect succeeded in the rev direction


    bpdu_sent (optional, any, None)
      BPDUs Sent


    invalid_rx_arp_pkt (optional, any, None)
      Invalid ARP PKT Rcvd


    ipfrag_ipip_dropped (optional, any, None)
      IP Frag IPIP Drop


    ipv6_ndisc_dad_adverts (optional, any, None)
      IPv6 DAD on Adverts


    inactive_nat_pool_arp_drop (optional, any, None)
      ARP PKT dropped due to inactive nat pool


    scaleout_hairpin_arp_drop (optional, any, None)
      ARP PKT dropped due to scaleout hairpin checks


    ip_frag_sent (optional, any, None)
      IP frag sent


    ipfrag_reasmoks (optional, any, None)
      IP Fragment Reasm OKs


    ipv6_novlanfwd_drop (optional, any, None)
      IPv6 No L3 VLAN FWD Drop


    unknown_prot_drop (optional, any, None)
      Unknown Prot Drop


    badpkt_drop (optional, any, None)
      Bad Pkt Drop


    ipfrag_icmp (optional, any, None)
      IP(ICMP) Fragment Rcvd


    l2_forward (optional, any, None)
      L2 Forward


    rx_arp_req (optional, any, None)
      ARP REQ Rcvd


    ipv4_frag_6rd_ok (optional, any, None)
      IPv4 Frag 6RD OK


    no_ip_drop (optional, any, None)
      No IP Drop


    ipfrag_timeout (optional, any, None)
      IP Fragment Timeout


    l2_def_vlan_drop (optional, any, None)
      L2 Default Vlan FWD Drop


    vlan_flood (optional, any, None)
      VLAN Flood


    ipv6frag_tcp_dropped (optional, any, None)
      IPv6 Frag TCP Dropped


    bpdu_rcvd (optional, any, None)
      BPDUs Received


    ttl_exceeded_drop (optional, any, None)
      TTL Exceeded Drop


    acl_deny (optional, any, None)
      ACL Denys


    redirect_rev_fail (optional, any, None)
      Redirect failed in the rev direction


    ip_defrag (optional, any, None)
      IP Defrag


    incorrect_len_drop (optional, any, None)
      Incorrect Length Drop


    licexpire_drop (optional, any, None)
      License Expire Drop


    prot_down_drop (optional, any, None)
      Prot Down Drop


    ip_defrag_invalid_len (optional, any, None)
      IP Invalid Length Frag


    ipv6_ndisc_out_of_memory (optional, any, None)
      IPv6 DAD Out-of-memory


    scaleout_arp_drop (optional, any, None)
      ARP PKT dropped due to scaleout checks


    sp_non_ctrl_pkt_drop (optional, any, None)
      Shared IP mode non ctrl packet to linux drop


    l4_in_ctrl_cpu (optional, any, None)
      L4 In Ctrl CPU


    fpga_error_pkt1 (optional, any, None)
      FPGA Error PKT1


    fpga_error_pkt2 (optional, any, None)
      FPGA Error PKT2


    ipfrag_udp (optional, any, None)
      IP(UDP) Fragment Rcvd


    virtual_ip_not_found_arp_drop (optional, any, None)
      ARP PKT dropped due to virtual IP not found


    ipv6frag_ipip_dropped (optional, any, None)
      IPv6 Frag IPIP Drop


    mgmt_svc_drop (optional, any, None)
      Management Service Drop


    ipv6_ndisc_dad_solicits (optional, any, None)
      IPv6 DAD on Solicits


    ipfrag_reasmfails (optional, any, None)
      IP Fragment Reasm Fails


    ipv6_noroute_drop (optional, any, None)
      IPv6 No Route Drop


    ipv6frag_icmp (optional, any, None)
      IPv6 Frag ICMP


    ipv4_noroute_drop (optional, any, None)
      IPv4 No Route Drop


    ipsec_drop (optional, any, None)
      IPSec Drop


    ip_not_found_arp_drop (optional, any, None)
      ARP PKT dropped due to IP not found


    l3_forward_ip (optional, any, None)
      L3 IP Forward


    ipv6frag_esp (optional, any, None)
      IPv6 Frag ESP


    ipv6frag_ospf (optional, any, None)
      IPv6 Frag OSPF


    l3_forward_ipv6 (optional, any, None)
      L3 IPv6 Forward


    dev_link_down_arp_drop (optional, any, None)
      ARP PKT dropped due to interface is down


    ipfrag_overload (optional, any, None)
      IP Frag Overload Drops


    ip_frag_oversize (optional, any, None)
      IP Fragment oversize


    ipv4_novlanfwd_drop (optional, any, None)
      IPv4 No L3 VLAN FWD Drop


    ipfrag_udp_dropped (optional, any, None)
      IP Frag UDP Dropped


    ipv6frag_udp (optional, any, None)
      IPv6 Frag UDP



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

