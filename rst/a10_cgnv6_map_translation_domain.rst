.. _a10_cgnv6_map_translation_domain_module:


a10_cgnv6_map_translation_domain -- Configures A10 cgnv6.map.translation.domain
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

MAP Translation domain






Parameters
----------

  description (False, any, None)
    MAP-T domain description


  ansible_username (True, any, None)
    Username for AXAPI authentication


  tcp (False, any, None)
    Field tcp


    mss_clamp (optional, any, None)
      Field mss_clamp



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
      'all'= all; 'inbound_packet_received'= Inbound IPv4 Packets Received; 'inbound_frag_packet_received'= Inbound IPv4 Fragment Packets Received; 'inbound_addr_port_validation_failed'= Inbound IPv4 Destination Address Port Validation Failed; 'inbound_rev_lookup_failed'= Inbound IPv4 Reverse Route Lookup Failed; 'inbound_dest_unreachable'= Inbound IPv6 Destination Address Unreachable; 'outbound_packet_received'= Outbound IPv6 Packets Received; 'outbound_frag_packet_received'= Outbound IPv6 Fragment Packets Received; 'outbound_addr_validation_failed'= Outbound IPv6 Source Address Validation Failed; 'outbound_rev_lookup_failed'= Outbound IPv6 Reverse Route Lookup Failed; 'outbound_dest_unreachable'= Outbound IPv4 Destination Address Unreachable; 'packet_mtu_exceeded'= Packet Exceeded MTU; 'frag_icmp_sent'= ICMP Packet Too Big Sent; 'interface_not_configured'= Interfaces not Configured Dropped; 'bmr_prefixrules_configured'= BMR prefix rules configured; 'helper_count'= Helper Count; 'active_dhcpv6_leases'= Active DHCPv6 leases;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    interface_not_configured (optional, any, None)
      Interfaces not Configured Dropped


    inbound_packet_received (optional, any, None)
      Inbound IPv4 Packets Received


    name (optional, any, None)
      MAP-T domain name


    outbound_dest_unreachable (optional, any, None)
      Outbound IPv4 Destination Address Unreachable


    frag_icmp_sent (optional, any, None)
      ICMP Packet Too Big Sent


    inbound_dest_unreachable (optional, any, None)
      Inbound IPv6 Destination Address Unreachable


    inbound_rev_lookup_failed (optional, any, None)
      Inbound IPv4 Reverse Route Lookup Failed


    bmr_prefixrules_configured (optional, any, None)
      BMR prefix rules configured


    outbound_frag_packet_received (optional, any, None)
      Outbound IPv6 Fragment Packets Received


    outbound_addr_validation_failed (optional, any, None)
      Outbound IPv6 Source Address Validation Failed


    packet_mtu_exceeded (optional, any, None)
      Packet Exceeded MTU


    inbound_addr_port_validation_failed (optional, any, None)
      Inbound IPv4 Destination Address Port Validation Failed


    outbound_packet_received (optional, any, None)
      Outbound IPv6 Packets Received


    inbound_frag_packet_received (optional, any, None)
      Inbound IPv4 Fragment Packets Received


    outbound_rev_lookup_failed (optional, any, None)
      Outbound IPv6 Reverse Route Lookup Failed



  name (True, any, None)
    MAP-T domain name


  ansible_password (True, any, None)
    Password for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  mtu (False, any, None)
    Domain MTU


  state (True, any, None)
    State of the object to be created.


  default_mapping_rule (False, any, None)
    Field default_mapping_rule


    rule_ipv6_prefix (optional, any, None)
      Rule IPv6 prefix


    uuid (optional, any, None)
      uuid of the object



  basic_mapping_rule (False, any, None)
    Field basic_mapping_rule


    prefix_rule_list (optional, any, None)
      Field prefix_rule_list


    uuid (optional, any, None)
      uuid of the object


    share_ratio (optional, any, None)
      Port sharing ratio for each NAT IP. Must be Power of 2 value


    rule_ipv4_address_port_settings (optional, any, None)
      'prefix-addr'= Each CE is assigned an IPv4 prefix; 'single-addr'= Each CE is assigned an IPv4 address; 'shared-addr'= Each CE is assigned a shared IPv4 address;


    port_start (optional, any, None)
      Starting Port, Must be Power of 2 value


    ea_length (optional, any, None)
      Length of Embedded Address (EA) bits



  health_check_gateway (False, any, None)
    Field health_check_gateway


    withdraw_route (optional, any, None)
      'all-link-failure'= Withdraw routes on health-check failure of all IPv4 gateways or all IPv6 gateways; 'any-link-failure'= Withdraw routes on health- check failure of any gateway (default);


    ipv6_address_list (optional, any, None)
      Field ipv6_address_list


    uuid (optional, any, None)
      uuid of the object


    address_list (optional, any, None)
      Field address_list










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

