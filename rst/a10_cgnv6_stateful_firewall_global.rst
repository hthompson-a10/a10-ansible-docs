.. _a10_cgnv6_stateful_firewall_global_module:


a10_cgnv6_stateful_firewall_global -- Configures A10 cgnv6.stateful.firewall.global
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Stateful Firewall Configuration (default=disabled)






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'tcp_packet_process'= TCP Packet Process; 'udp_packet_process'= UDP Packet Process; 'other_packet_process'= Other Packet Process; 'packet_inbound_deny'= Inbound Packet Denied; 'packet_process_failure'= Packet Error Drop; 'outbound_session_created'= Outbound Session Created; 'outbound_session_freed'= Outbound Session Freed; 'inbound_session_created'= Inbound Session Created; 'inbound_session_freed'= Inbound Session Freed; 'tcp_session_created'= TCP Session Created; 'tcp_session_freed'= TCP Session Freed; 'udp_session_created'= UDP Session Created; 'udp_session_freed'= UDP Session Freed; 'other_session_created'= Other Session Created; 'other_session_freed'= Other Session Freed; 'session_creation_failure'= Session Creation Failure; 'no_fwd_route'= No Forward Route; 'no_rev_route'= No Reverse Route; 'packet_standby_drop'= Standby Drop; 'tcp_fullcone_created'= TCP Full- cone Created; 'tcp_fullcone_freed'= TCP Full-cone Freed; 'udp_fullcone_created'= UDP Full-cone Created; 'udp_fullcone_freed'= UDP Full- cone Freed; 'fullcone_creation_failure'= Full-Cone Creation Failure; 'eif_process'= Endpnt-Independent Filter Matched; 'one_arm_drop'= One-Arm Drop; 'no_class_list_match'= No Class-List Match Drop; 'outbound_session_created_shadow'= Outbound Session Created Shadow; 'outbound_session_freed_shadow'= Outbound Session Freed Shadow; 'inbound_session_created_shadow'= Inbound Session Created Shadow; 'inbound_session_freed_shadow'= Inbound Session Freed Shadow; 'tcp_session_created_shadow'= TCP Session Created Shadow; 'tcp_session_freed_shadow'= TCP Session Freed Shadow; 'udp_session_created_shadow'= UDP Session Created Shadow; 'udp_session_freed_shadow'= UDP Session Freed Shadow; 'other_session_created_shadow'= Other Session Created Shadow; 'other_session_freed_shadow'= Other Session Freed Shadow; 'session_creation_failure_shadow'= Session Creation Failure Shadow; 'bad_session_freed'= Bad Session Proto on Free; 'ctl_mem_alloc'= Memory Alloc; 'ctl_mem_free'= Memory Free; 'tcp_fullcone_created_shadow'= TCP Full-cone Created Shadow; 'tcp_fullcone_freed_shadow'= TCP Full-cone Freed Shadow; 'udp_fullcone_created_shadow'= UDP Full-cone Created Shadow; 'udp_fullcone_freed_shadow'= UDP Full-cone Freed Shadow; 'fullcone_in_del_q'= Full-cone Found in Delete Queue; 'fullcone_overflow_eim'= EIM Overflow; 'fullcone_overflow_eif'= EIF Overflow; 'fullcone_free_found'= Full-cone Free Found From Conn; 'fullcone_free_retry_lookup'= Full-cone Retry Look-up; 'fullcone_free_not_found'= Full-cone Free Not Found; 'eif_limit_exceeded'= EIF Limit Exceeded; 'eif_disable_drop'= EIF Disable Drop; 'eif_process_failure'= EIF Process Failure; 'eif_filtered'= EIF Filtered; 'ha_standby_session_created'= HA Standby Session Created; 'ha_standby_session_eim'= HA Standby Session EIM; 'ha_standby_session_eif'= HA Standby Session EIF;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    session_creation_failure (optional, any, None)
      Session Creation Failure


    tcp_packet_process (optional, any, None)
      TCP Packet Process


    udp_session_freed (optional, any, None)
      UDP Session Freed


    udp_fullcone_freed (optional, any, None)
      UDP Full-cone Freed


    inbound_session_freed (optional, any, None)
      Inbound Session Freed


    outbound_session_created (optional, any, None)
      Outbound Session Created


    tcp_fullcone_created (optional, any, None)
      TCP Full-cone Created


    packet_inbound_deny (optional, any, None)
      Inbound Packet Denied


    inbound_session_created (optional, any, None)
      Inbound Session Created


    no_rev_route (optional, any, None)
      No Reverse Route


    fullcone_creation_failure (optional, any, None)
      Full-Cone Creation Failure


    one_arm_drop (optional, any, None)
      One-Arm Drop


    udp_fullcone_created (optional, any, None)
      UDP Full-cone Created


    tcp_session_freed (optional, any, None)
      TCP Session Freed


    other_session_created (optional, any, None)
      Other Session Created


    udp_session_created (optional, any, None)
      UDP Session Created


    packet_process_failure (optional, any, None)
      Packet Error Drop


    other_packet_process (optional, any, None)
      Other Packet Process


    udp_packet_process (optional, any, None)
      UDP Packet Process


    tcp_fullcone_freed (optional, any, None)
      TCP Full-cone Freed


    no_fwd_route (optional, any, None)
      No Forward Route


    tcp_session_created (optional, any, None)
      TCP Session Created


    other_session_freed (optional, any, None)
      Other Session Freed


    outbound_session_freed (optional, any, None)
      Outbound Session Freed


    eif_process (optional, any, None)
      Endpnt-Independent Filter Matched


    no_class_list_match (optional, any, None)
      No Class-List Match Drop


    packet_standby_drop (optional, any, None)
      Standby Drop



  uuid (False, any, None)
    uuid of the object


  stateful_firewall_value (False, any, None)
    'enable'= Enable stateful firewall;


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  respond_to_user_mac (False, any, None)
    Use the user's source MAC for the next hop rather than the routing table (default= off)


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

