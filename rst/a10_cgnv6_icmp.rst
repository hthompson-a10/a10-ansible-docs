.. _a10_cgnv6_icmp_module:


a10_cgnv6_icmp -- Configures A10 cgnv6.icmp
===========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

CGNV6 ICMP Statistics






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'icmp-unknown-type'= ICMP Unknown Type; 'icmp-no-port-info'= ICMP Port Info Not Included; 'icmp-no-session-drop'= ICMP No Matching Session Drop; 'icmpv6-unknown-type'= ICMPv6 Unknown Type; 'icmpv6-no-port-info'= ICMPv6 Port Info Not Included; 'icmpv6-no-session-drop'= ICMPv6 No Matching Session Drop; 'icmp-to-icmp'= ICMP to ICMP Conversion; 'icmp-to-icmpv6'= ICMP to ICMPv6 Conversion; 'icmpv6-to-icmp'= ICMPv6 to ICMP Conversion; 'icmpv6-to-icmpv6'= ICMPv6 to ICMPv6 Conversion; 'icmp-bad-type'= Bad Embedded ICMP Type; 'icmpv6-bad-type'= Bad Embedded ICMPv6 Type; '64-known-drop'= NAT64 Forward Known ICMPv6 Drop; '64-unknown-drop'= NAT64 Forward Unknown ICMPv6 Drop; '64-midpoint-hop'= NAT64 Forward Unknown Source Drop; '46-known-drop'= NAT64 Reverse Known ICMP Drop; '46-unknown-drop'= NAT64 Reverse Known ICMPv6 Drop; '46-no-prefix-for-ipv4'= NAT64 Reverse No Prefix Match for IPv4; '46-bad-encap- ip-header-len'= 4to6 Bad Encapsulated IP Header Length; 'icmp-to-icmp-err'= ICMP to ICMP Conversion Error; 'icmp-to-icmpv6-err'= ICMP to ICMPv6 Conversion Error; 'icmpv6-to-icmp-err'= ICMPv6 to ICMP Conversion Error; 'icmpv6-to- icmpv6-err'= ICMPv6 to ICMPv6 Conversion Error; 'encap-cross-cpu-no-match'= ICMP Embedded Cross CPU No Matching Session; 'encap-cross-cpu-preprocess-err'= ICMP Embedded Cross CPU Preprocess Error; 'icmp-to-icmp-unknown-l4'= ICMP Embedded Unknown L4 Protocol; 'icmp-to-icmpv6-unknown-l4'= ICMP to ICMPv6 Embedded Unknown L4 Protocol; 'icmpv6-to-icmp-unknown-l4'= ICMPv6 to ICMP Embedded Unknown L4 Protocol; 'icmpv6-to-icmpv6-unknown-l4'= ICMPv6 to ICMPv6 Embedded Unknown L4 Protocol; 'static-nat'= ICMP Static NAT; 'echo-to-pool- reply'= Ping to Pool Reply; 'echo-to-pool-drop'= Ping to Pool Drop; 'error-to- pool-drop'= Error to Pool Drop; 'echo-to-pool-reply-v6'= Ping6 to Pool Reply; 'echo-to-pool-drop-v6'= Ping6 to Pool Drop; 'error-to-pool-drop-v6'= Error to IPv6 Pool Drop; 'error-ip-mismatch'= ICMP IP address mismatch;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    icmpv6_unknown_type (optional, any, None)
      ICMPv6 Unknown Type


    64_unknown_drop (optional, any, None)
      NAT64 Forward Unknown ICMPv6 Drop


    icmpv6_no_session_drop (optional, any, None)
      ICMPv6 No Matching Session Drop


    icmp_bad_type (optional, any, None)
      Bad Embedded ICMP Type


    icmpv6_to_icmp (optional, any, None)
      ICMPv6 to ICMP Conversion


    icmpv6_bad_type (optional, any, None)
      Bad Embedded ICMPv6 Type


    64_midpoint_hop (optional, any, None)
      NAT64 Forward Unknown Source Drop


    64_known_drop (optional, any, None)
      NAT64 Forward Known ICMPv6 Drop


    46_known_drop (optional, any, None)
      NAT64 Reverse Known ICMP Drop


    46_unknown_drop (optional, any, None)
      NAT64 Reverse Known ICMPv6 Drop


    icmpv6_no_port_info (optional, any, None)
      ICMPv6 Port Info Not Included


    46_no_prefix_for_ipv4 (optional, any, None)
      NAT64 Reverse No Prefix Match for IPv4


    icmp_to_icmpv6 (optional, any, None)
      ICMP to ICMPv6 Conversion


    icmp_no_port_info (optional, any, None)
      ICMP Port Info Not Included


    icmp_to_icmp (optional, any, None)
      ICMP to ICMP Conversion


    icmp_unknown_type (optional, any, None)
      ICMP Unknown Type


    icmpv6_to_icmpv6 (optional, any, None)
      ICMPv6 to ICMPv6 Conversion


    icmp_no_session_drop (optional, any, None)
      ICMP No Matching Session Drop



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

