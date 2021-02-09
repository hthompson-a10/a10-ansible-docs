.. _a10_cgnv6_ddos_protection_module:


a10_cgnv6_ddos_protection -- Configures A10 cgnv6.ddos-protection
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure CGNV6 DDoS Protection






Parameters
----------

  max_hw_entries (False, any, None)
    Configure maximum HW entries


  ansible_username (True, any, None)
    Username for AXAPI authentication


  toggle (False, any, None)
    'enable'= Enable CGNV6 NAT pool DDoS protection (default); 'disable'= Disable CGNV6 NAT pool DDoS protection;


  l4_entries (False, any, None)
    Field l4_entries


    uuid (optional, any, None)
      uuid of the object



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  stats (False, any, None)
    Field stats


    ip_other_block_alloc (optional, any, None)
      Other block alloc


    l4_entry_list_alloc (optional, any, None)
      L4 Entry list alloc


    entry_added_shadow (optional, any, None)
      Entry added shadow


    l4_entry_list_free (optional, any, None)
      L4 Entry list free


    l4_entry_added (optional, any, None)
      L4 Entry added


    l4_hw_out_of_entries (optional, any, None)
      HW out of L4 entries


    ip_node_free (optional, any, None)
      Node free


    l4_entry_added_to_hw (optional, any, None)
      L4 Entry added to HW


    ip_node_alloc (optional, any, None)
      Node alloc


    l3_entry_match_drop_hw (optional, any, None)
      L3 HW entry match drop


    l4_entry_deleted (optional, any, None)
      L4 Entry deleted


    l3_entry_remove_from_bgp_failure (optional, any, None)
      L3 entry BGP remove failures


    l3_entry_removed_from_hw (optional, any, None)
      L3 Entry removed from HW


    l3_entry_deleted (optional, any, None)
      L3 Entry Deleted


    l3_entry_added_to_hw (optional, any, None)
      L3 Entry added to HW


    l3_entry_too_many (optional, any, None)
      L3 Too many entries


    l3_entry_match_drop (optional, any, None)
      L3 Entry match drop


    l3_entry_drop_max_hw_exceeded (optional, any, None)
      L3 Entry Drop due to HW Limit Exceeded


    l4_entry_match_drop (optional, any, None)
      L4 Entry match drop


    ip_port_block_free (optional, any, None)
      Port block free


    entry_invalidated (optional, any, None)
      Entry invalidated


    l4_entry_drop_max_hw_exceeded (optional, any, None)
      L4 Entry Drop due to HW Limit Exceeded


    l3_entry_add_to_hw_failure (optional, any, None)
      L3 entry HW add failure


    ip_other_block_alloc_failure (optional, any, None)
      Other block alloc failure


    ip_port_block_alloc (optional, any, None)
      Port block alloc


    l3_entry_removed_from_bgp (optional, any, None)
      Entry removed from BGP


    l4_entry_list_alloc_failure (optional, any, None)
      L4 Entry list alloc failures


    ip_other_block_free (optional, any, None)
      Other block free


    l4_entry_match_drop_hw (optional, any, None)
      L4 HW Entry match drop


    l3_entry_added (optional, any, None)
      L3 Entry Added


    l3_entry_add_to_bgp_failure (optional, any, None)
      L3 Entry BGP add failures


    l4_entry_removed_from_hw (optional, any, None)
      L4 Entry removed from HW


    l3_entry_added_to_bgp (optional, any, None)
      L3 Entry added to BGP


    ip_port_block_alloc_failure (optional, any, None)
      Port block alloc failure


    ip_node_alloc_failure (optional, any, None)
      Node alloc failures



  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'l3_entry_added'= L3 Entry Added; 'l3_entry_deleted'= L3 Entry Deleted; 'l3_entry_added_to_bgp'= L3 Entry added to BGP; 'l3_entry_removed_from_bgp'= Entry removed from BGP; 'l3_entry_added_to_hw'= L3 Entry added to HW; 'l3_entry_removed_from_hw'= L3 Entry removed from HW; 'l3_entry_too_many'= L3 Too many entries; 'l3_entry_match_drop'= L3 Entry match drop; 'l3_entry_match_drop_hw'= L3 HW entry match drop; 'l3_entry_drop_max_hw_exceeded'= L3 Entry Drop due to HW Limit Exceeded; 'l4_entry_added'= L4 Entry added; 'l4_entry_deleted'= L4 Entry deleted; 'l4_entry_added_to_hw'= L4 Entry added to HW; 'l4_entry_removed_from_hw'= L4 Entry removed from HW; 'l4_hw_out_of_entries'= HW out of L4 entries; 'l4_entry_match_drop'= L4 Entry match drop; 'l4_entry_match_drop_hw'= L4 HW Entry match drop; 'l4_entry_drop_max_hw_exceeded'= L4 Entry Drop due to HW Limit Exceeded; 'l4_entry_list_alloc'= L4 Entry list alloc; 'l4_entry_list_free'= L4 Entry list free; 'l4_entry_list_alloc_failure'= L4 Entry list alloc failures; 'ip_node_alloc'= Node alloc; 'ip_node_free'= Node free; 'ip_node_alloc_failure'= Node alloc failures; 'ip_port_block_alloc'= Port block alloc; 'ip_port_block_free'= Port block free; 'ip_port_block_alloc_failure'= Port block alloc failure; 'ip_other_block_alloc'= Other block alloc; 'ip_other_block_free'= Other block free; 'ip_other_block_alloc_failure'= Other block alloc failure; 'entry_added_shadow'= Entry added shadow; 'entry_invalidated'= Entry invalidated; 'l3_entry_add_to_bgp_failure'= L3 Entry BGP add failures; 'l3_entry_remove_from_bgp_failure'= L3 entry BGP remove failures; 'l3_entry_add_to_hw_failure'= L3 entry HW add failure;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  disable_nat_ip_by_bgp (False, any, None)
    Field disable_nat_ip_by_bgp


    uuid (optional, any, None)
      uuid of the object



  logging (False, any, None)
    Field logging


    logging_toggle (optional, any, None)
      'enable'= Enable CGNV6 NAT pool DDoS protection logging (default); 'disable'= Disable CGNV6 NAT pool DDoS protection logging;



  uuid (False, any, None)
    uuid of the object


  zone (False, any, None)
    Disable NAT IP based on DDoS zone name set in BGP


  packets_per_second (False, any, None)
    Field packets_per_second


    udp (optional, any, None)
      Configure packets-per-second threshold per UDP port (default= 3000)


    other (optional, any, None)
      Configure packets-per-second threshold for other L4 protocols(default 10000)


    include_existing_session (optional, any, None)
      Count traffic associated with existing session into the packets-per-second (Default= Disabled)


    action (optional, any, None)
      Field action


    ip (optional, any, None)
      Configure packets-per-second threshold per IP(default 3000000)


    tcp (optional, any, None)
      Configure packets-per-second threshold per TCP port (default= 3000)



  ip_entries (False, any, None)
    Field ip_entries


    uuid (optional, any, None)
      uuid of the object



  state (True, any, None)
    State of the object to be created.


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

