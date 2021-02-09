.. _a10_ip_frag_module:


a10_ip_frag -- Configures A10 ip.frag
=====================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

IP fragmentation parameters






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'session-inserted'= Session Inserted; 'session-expired'= Session Expired; 'icmp-rcv'= ICMP Received; 'icmpv6-rcv'= ICMPv6 Received; 'udp-rcv'= UDP Received; 'tcp-rcv'= TCP Received; 'ipip-rcv'= IP-in-IP Received; 'ipv6ip- rcv'= IPv6-in-IP Received; 'other-rcv'= Other Received; 'icmp-dropped'= ICMP Dropped; 'icmpv6-dropped'= ICMPv6 Dropped; 'udp-dropped'= UDP Dropped; 'tcp- dropped'= TCP Dropped; 'ipip-dropped'= IP-in-IP Dropped; 'ipv6ip-dropped'= IPv6-in-IP Dropped; 'other-dropped'= Other Dropped; 'overlap-error'= Overlapping Fragment Dropped; 'bad-ip-len'= Bad IP Length; 'too-small'= Fragment Too Small Drop; 'first-tcp-too-small'= First TCP Fragment Too Small Drop; 'first-l4-too-small'= First L4 Fragment Too Small Drop; 'total-sessions- exceeded'= Total Sessions Exceeded Drop; 'no-session-memory'= Out of Session Memory; 'fast-aging-set'= Fragmentation Fast Aging Set; 'fast-aging-unset'= Fragmentation Fast Aging Unset; 'fragment-queue-success'= Fragment Queue Success; 'unaligned-len'= Payload Length Unaligned; 'exceeded-len'= Payload Length Out of Bounds; 'duplicate-first-frag'= Duplicate First Fragment; 'duplicate-last-frag'= Duplicate Last Fragment; 'total-fragments-exceeded'= Total Queued Fragments Exceeded; 'fragment-queue-failure'= Fragment Queue Failure; 'reassembly-success'= Fragment Reassembly Success; 'max-len-exceeded'= Fragment Max Data Length Exceeded; 'reassembly-failure'= Fragment Reassembly Failure; 'policy-drop'= MTU Exceeded Policy Drop; 'error-drop'= Fragment Processing Drop; 'high-cpu-threshold'= High CPU Threshold Reached; 'low-cpu- threshold'= Low CPU Threshold Reached; 'cpu-threshold-drop'= High CPU Drop; 'ipd-entry-drop'= DDoS Protection Drop; 'max-packets-exceeded'= Too Many Packets Per Reassembly Drop; 'session-packets-exceeded'= Session Max Packets Exceeded; 'frag-session-count'= Fragmentation Session Count; 'sctp-rcv'= SCTP Received; 'sctp-dropped'= SCTP Dropped;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    icmp_rcv (optional, any, None)
      ICMP Received


    icmp_dropped (optional, any, None)
      ICMP Dropped


    session_inserted (optional, any, None)
      Session Inserted


    fast_aging_unset (optional, any, None)
      Fragmentation Fast Aging Unset


    ipip_dropped (optional, any, None)
      IP-in-IP Dropped


    low_cpu_threshold (optional, any, None)
      Low CPU Threshold Reached


    icmpv6_dropped (optional, any, None)
      ICMPv6 Dropped


    ipv6ip_dropped (optional, any, None)
      IPv6-in-IP Dropped


    ipv6ip_rcv (optional, any, None)
      IPv6-in-IP Received


    icmpv6_rcv (optional, any, None)
      ICMPv6 Received


    reassembly_failure (optional, any, None)
      Fragment Reassembly Failure


    too_small (optional, any, None)
      Fragment Too Small Drop


    session_expired (optional, any, None)
      Session Expired


    cpu_threshold_drop (optional, any, None)
      High CPU Drop


    tcp_dropped (optional, any, None)
      TCP Dropped


    sctp_rcv (optional, any, None)
      SCTP Received


    total_sessions_exceeded (optional, any, None)
      Total Sessions Exceeded Drop


    ipd_entry_drop (optional, any, None)
      DDoS Protection Drop


    no_session_memory (optional, any, None)
      Out of Session Memory


    fast_aging_set (optional, any, None)
      Fragmentation Fast Aging Set


    sctp_dropped (optional, any, None)
      SCTP Dropped


    unaligned_len (optional, any, None)
      Payload Length Unaligned


    reassembly_success (optional, any, None)
      Fragment Reassembly Success


    other_dropped (optional, any, None)
      Other Dropped


    total_fragments_exceeded (optional, any, None)
      Total Queued Fragments Exceeded


    policy_drop (optional, any, None)
      MTU Exceeded Policy Drop


    other_rcv (optional, any, None)
      Other Received


    first_l4_too_small (optional, any, None)
      First L4 Fragment Too Small Drop


    udp_rcv (optional, any, None)
      UDP Received


    fragment_queue_failure (optional, any, None)
      Fragment Queue Failure


    session_packets_exceeded (optional, any, None)
      Session Max Packets Exceeded


    tcp_rcv (optional, any, None)
      TCP Received


    udp_dropped (optional, any, None)
      UDP Dropped


    fragment_queue_success (optional, any, None)
      Fragment Queue Success


    overlap_error (optional, any, None)
      Overlapping Fragment Dropped


    high_cpu_threshold (optional, any, None)
      High CPU Threshold Reached


    ipip_rcv (optional, any, None)
      IP-in-IP Received


    first_tcp_too_small (optional, any, None)
      First TCP Fragment Too Small Drop


    duplicate_first_frag (optional, any, None)
      Duplicate First Fragment


    bad_ip_len (optional, any, None)
      Bad IP Length


    exceeded_len (optional, any, None)
      Payload Length Out of Bounds


    max_packets_exceeded (optional, any, None)
      Too Many Packets Per Reassembly Drop


    max_len_exceeded (optional, any, None)
      Fragment Max Data Length Exceeded


    duplicate_last_frag (optional, any, None)
      Duplicate Last Fragment


    error_drop (optional, any, None)
      Fragment Processing Drop



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  max_packets_per_reassembly (False, any, None)
    Max number of fragmented packets allowed per reassembly(0 is unlimited) (default 0)


  state (True, any, None)
    State of the object to be created.


  cpu_threshold (False, any, None)
    Field cpu_threshold


    high (optional, any, None)
      When CPU usage reaches this value, it will stop processing fragments (default= 75%)


    low (optional, any, None)
      When CPU usage remains under this value, it will resume processing fragments (default= 60%)



  max_reassembly_sessions (False, any, None)
    Max number of pending reassembly sessions allowed (default 100000)


  timeout (False, any, None)
    Fragmentation timeout (in milliseconds 4 - 65535 (default is 60000))


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  buff (False, any, None)
    Max buff used for fragmentation (Buffer Value(10000-3000000))









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

