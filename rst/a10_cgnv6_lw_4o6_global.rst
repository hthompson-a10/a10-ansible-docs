.. _a10_cgnv6_lw_4o6_global_module:


a10_cgnv6_lw_4o6_global -- Configures A10 cgnv6.lw.4o6.global
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure LW-4over6 parameters






Parameters
----------

  no_reverse_match (False, any, None)
    Field no_reverse_match


    send_icmp (optional, any, None)
      Send ICMP Type 3 Code 1



  ansible_username (True, any, None)
    Username for AXAPI authentication


  hairpinning (False, any, None)
    'filter-all'= Disable all Hairpinning; 'filter-none'= Allow all Hairpinning (default); 'filter-self-ip'= Block Hairpinning to same IP; 'filter-self-ip- port'= Block hairpinning to same IP and Port combination;


  use_binding_table (False, any, None)
    Bind LW-4over6 binding table for use (LW-4over6 Binding Table Name)


  no_forward_match (False, any, None)
    Field no_forward_match


    send_icmpv6 (optional, any, None)
      Send ICMPv6 Type 1 Code 5



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
      'all'= all; 'entry_count'= Total Entries Configured; 'self_hairpinning_drop'= Self-Hairpinning Drops; 'all_hairpinning_drop'= All Hairpinning Drops; 'no_match_icmpv6_sent'= No-Forward-Match ICMPv6 Sent; 'no_match_icmp_sent'= No- Reverse-Match ICMP Sent; 'icmp_inbound_drop'= Inbound ICMP Drops; 'fwd_lookup_failed'= Forward Route Lookup Failed; 'rev_lookup_failed'= Reverse Route Lookup Failed; 'interface_not_configured'= LW-4over6 Interfaces not Configured Drops; 'no_binding_table_matches_fwd'= No Forward Binding Table Entry Match Drops; 'no_binding_table_matches_rev'= No Reverse Binding Table Entry Match Drops; 'session_count'= LW-4over6 Session Count; 'system_address_drop'= LW-4over6 System Address Drops;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    interface_not_configured (optional, any, None)
      LW-4over6 Interfaces not Configured Drops


    no_match_icmp_sent (optional, any, None)
      No-Reverse-Match ICMP Sent


    no_binding_table_matches_rev (optional, any, None)
      No Reverse Binding Table Entry Match Drops


    rev_lookup_failed (optional, any, None)
      Reverse Route Lookup Failed


    self_hairpinning_drop (optional, any, None)
      Self-Hairpinning Drops


    entry_count (optional, any, None)
      Total Entries Configured


    all_hairpinning_drop (optional, any, None)
      All Hairpinning Drops


    icmp_inbound_drop (optional, any, None)
      Inbound ICMP Drops


    fwd_lookup_failed (optional, any, None)
      Forward Route Lookup Failed


    no_binding_table_matches_fwd (optional, any, None)
      No Forward Binding Table Entry Match Drops


    no_match_icmpv6_sent (optional, any, None)
      No-Forward-Match ICMPv6 Sent



  inside_src_access_list (False, any, None)
    Access List for inside IPv4 addresses (ACL ID)


  icmp_inbound (False, any, None)
    'drop'= Drop Inbound ICMP packets; 'handle'= Handle Inbound ICMP packets(default);


  state (True, any, None)
    State of the object to be created.


  nat_prefix_list (False, any, None)
    Configure LW-4over6 NAT Prefix List (LW-4over6 NAT Prefix Class-list)


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

