.. _a10_cgnv6_fixed_nat_global_module:


a10_cgnv6_fixed_nat_global -- Configures A10 cgnv6.fixed.nat.global
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Fixed NAT Global configuration and Stats






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters4 (optional, any, None)
      'fnatdslite_fwd_ingress_pkt_size_range2'= Fixed DS-Lite Forward Ingress Packet size between 201 and 800; 'fnatdslite_fwd_ingress_pkt_size_range3'= Fixed DS- Lite Forward Ingress Packet size between 801 and 1550; 'fnatdslite_fwd_ingress_pkt_size_range4'= Fixed DS-Lite Forward Ingress Packet size between 1551 and 9000; 'fnatdslite_fwd_egress_pkt_size_range1'= Fixed DS- Lite Forward Egress Packet size between 0 and 200; 'fnatdslite_fwd_egress_pkt_size_range2'= Fixed DS-Lite Forward Egress Packet size between 201 and 800; 'fnatdslite_fwd_egress_pkt_size_range3'= Fixed DS- Lite Forward Egress Packet size between 801 and 1550; 'fnatdslite_fwd_egress_pkt_size_range4'= Fixed DS-Lite Forward Egress Packet size between 1551 and 9000; 'fnatdslite_rev_ingress_pkt_size_range1'= Fixed DS- Lite Reverse Ingress Packet size between 0 and 200; 'fnatdslite_rev_ingress_pkt_size_range2'= Fixed DS-Lite Reverse Ingress Packet size between 201 and 800; 'fnatdslite_rev_ingress_pkt_size_range3'= Fixed DS- Lite Reverse Ingress Packet size between 801 and 1550; 'fnatdslite_rev_ingress_pkt_size_range4'= Fixed DS-Lite Reverse Ingress Packet size between 1551 and 9000; 'fnatdslite_rev_egress_pkt_size_range1'= Fixed DS- Lite Reverse Egress Packet size between 0 and 200; 'fnatdslite_rev_egress_pkt_size_range2'= Fixed DS-Lite Reverse Egress Packet size between 201 and 800; 'fnatdslite_rev_egress_pkt_size_range3'= Fixed DS- Lite Reverse Egress Packet size between 801 and 1550; 'fnatdslite_rev_egress_pkt_size_range4'= Fixed DS-Lite Reverse Egress Packet size between 1551 and 9000;


    counters1 (optional, any, None)
      'all'= all; 'total-nat-in-use'= Total NAT Addresses in-use; 'total-tcp- allocated'= Total TCP Ports Allocated; 'total-tcp-freed'= Total TCP Ports Freed; 'total-udp-allocated'= Total UDP Ports Allocated; 'total-udp-freed'= Total UDP Ports Freed; 'total-icmp-allocated'= Total ICMP Ports Allocated; 'total-icmp-freed'= Total ICMP Ports Freed; 'nat44-data-session-created'= NAT44 Data Sessions Created; 'nat44-data-session-freed'= NAT44 Data Sessions Freed; 'nat64-data-session-created'= NAT64 Data Sessions Created; 'nat64-data-session- freed'= NAT64 Data Sessions Freed; 'dslite-data-session-created'= DS-Lite Data Sessions Created; 'dslite-data-session-freed'= DS-Lite Data Sessions Freed; 'nat-port-unavailable-tcp'= TCP NAT Port Unavailable; 'nat-port-unavailable- udp'= UDP NAT Port Unavailable; 'nat-port-unavailable-icmp'= ICMP NAT Port Unavailable; 'session-user-quota-exceeded'= Sessions User Quota Exceeded; 'nat44-tcp-fullcone-created'= NAT44 TCP Full-Cone Created; 'nat44-tcp-fullcone- freed'= NAT44 TCP Full-Cone Freed; 'nat44-udp-fullcone-created'= NAT44 UDP Full-Cone Created; 'nat44-udp-fullcone-freed'= NAT44 UDP Full-Cone Freed; 'nat44-udp-alg-fullcone-created'= NAT44 UDP ALG Full-Cone Created; 'nat44-udp- alg-fullcone-freed'= NAT44 UDP ALG Full-Cone Freed; 'nat64-tcp-fullcone- created'= NAT64 TCP Full-Cone Created; 'nat64-tcp-fullcone-freed'= NAT64 TCP Full-Cone Freed; 'nat64-udp-fullcone-created'= NAT64 UDP Full-Cone Created; 'nat64-udp-fullcone-freed'= NAT64 UDP Full-Cone Freed; 'nat64-udp-alg-fullcone- created'= NAT64 UDP ALG Full-Cone Created; 'nat64-udp-alg-fullcone-freed'= NAT64 UDP ALG Full-Cone Freed; 'dslite-tcp-fullcone-created'= DS-Lite TCP Full- Cone Created; 'dslite-tcp-fullcone-freed'= DS-Lite TCP Full-Cone Freed; 'dslite-udp-fullcone-created'= DS-Lite UDP Full-Cone Created; 'dslite-udp- fullcone-freed'= DS-Lite UDP Full-Cone Freed; 'dslite-udp-alg-fullcone- created'= DS-Lite UDP ALG Full-Cone Created; 'dslite-udp-alg-fullcone-freed'= DS-Lite UDP ALG Full-Cone Freed; 'fullcone-failure'= Full-Cone Session Creation Failed; 'nat44-eim-match'= NAT44 Endpoint-Independent-Mapping Matched; 'nat64-eim-match'= NAT64 Endpoint-Independent-Mapping Matched; 'dslite-eim- match'= DS-Lite Endpoint-Independent-Mapping Matched; 'nat44-eif-match'= NAT44 Endpoint-Independent-Filtering Matched; 'nat64-eif-match'= NAT64 Endpoint- Independent-Filtering Matched; 'dslite-eif-match'= DS-Lite Endpoint- Independent-Filtering Matched; 'nat44-inbound-filtered'= NAT44 Endpoint- Dependent Filtering Drop; 'nat64-inbound-filtered'= NAT64 Endpoint-Dependent Filtering Drop; 'dslite-inbound-filtered'= DS-Lite Endpoint-Dependent Filtering Drop; 'nat44-eif-limit-exceeded'= NAT44 Endpoint-Independent-Filtering Limit Exceeded; 'nat64-eif-limit-exceeded'= NAT64 Endpoint-Independent-Filtering Limit Exceeded; 'dslite-eif-limit-exceeded'= DS-Lite Endpoint-Independent- Filtering Limit Exceeded; 'nat44-hairpin'= NAT44 Hairpin Session Created; 'nat64-hairpin'= NAT64 Hairpin Session Created; 'dslite-hairpin'= DS-Lite Hairpin Session Created; 'standby-drop'= Fixed NAT LID Standby Drop; 'fixed- nat-fullcone-self-hairpinning-drop'= Self-Hairpinning Drop; 'sixrd-drop'= Fixed NAT IPv6 in IPv4 Packet Drop; 'dest-rlist-drop'= Fixed NAT Dest Rule List Drop; 'dest-rlist-pass-through'= Fixed NAT Dest Rule List Pass-Through; 'dest-rlist- snat-drop'= Fixed NAT Dest Rules List Source NAT Drop; 'cross-cpu-helper- created'= Cross CPU Helper Session Created; 'cross-cpu-helper-free-retry- lookup'= Cross CPU Helper Session Free Retry Lookup; 'cross-cpu-helper-free- not-found'= Cross CPU Helper Session Free not Found; 'cross-cpu-helper-free'= Cross CPU Helper Session Freed; 'cross-cpu-rcv'= Cross CPU Helper Packets Received; 'cross-cpu-bad-l3'= Cross CPU Unsupported L3; 'cross-cpu-bad-l4'= Cross CPU Unsupported L4; 'cross-cpu-no-session'= Cross CPU no Session Found; 'cross-cpu-helper-deleted'= Cross CPU Helper Session Deleted; 'cross-cpu- helper-fixed-nat-lid-standby'= Cross CPU Helper Fixed NAT LID Standby; 'cross- cpu-helper-cpu-mismatch'= Cross CPU Helper CPU Mismatch; 'cross-cpu-sent'= Cross CPU Helper Packets Sent; 'config-not-found'= Fixed NAT Config not Found; 'fullcone-in-del-q'= Full-Cone Session in Delete Queue; 'fullcone-overflow'= Full-Cone Session Conn-Count Overflow; 'fullcone-inbound-idx-mismatch'= Full- Cone Session Fixed NAT LID mismatch; 'fullcone-retry-lookup'= Full-cone session retry look-up; 'fullcone-not-found'= Full-cone session not found; 'fullcone- overflow-eim'= Full-cone EIM Overflow; 'fullcone-overflow-eif'= Full-cone EIF Overflow; 'ha-config-mismatch'= HA Fixed NAT Config Mismatch; 'ha-user-quota- exceeded'= HA User Quota Exceeded; 'ha-fullcone-mismatch'= HA Full-Cone Mismatch; 'ha-dnat-mismatch'= HA Destination NAT Config Mismatch; 'ha-nat-port- unavailable'= HA NAT Port Unavailable; 'ha-fullcone-failure'= HA Full-Cone Failure; 'ha-endpoint-indep-map-match'= HA Endpoint-Independent-Mapping Match; 'udp-alg-eim-mismatch'= UDP ALG Endpoint-Independent Mapping Mismatch; 'udp- alg-no-nat-ip'= UDP ALG User-Quota Unknown NAT IP; 'udp-alg-alloc-failure'= UDP ALG Port Allocation Failure; 'mtu-exceeded'= Packet Exceeded MTU; 'frag'= Fragmented Packets; 'frag-icmp'= ICMP Packet Too Big Sent; 'periodic-log-msg- alloc'= Fixed NAT Periodic Log Msg Allocated; 'periodic-log-msg-free'= Fixed NAT Periodic Log Msg Freed; 'disable-log-msg-alloc'= Fixed NAT Disable Log Msg Allocated; 'disable-log-msg-free'= Fixed NAT Disable Log Msg Freed; 'sip-alg- reuse-contact-fullcone'= SIP ALG Reuse Contact Full-cone Session; 'sip-alg- contact-fullcone-mismatch'= SIP ALG Contact Full-cone Session Mismatch; 'sip- alg-create-contact-fullcone-failure'= SIP ALG Create Contact Full-cone Session Failure; 'sip-alg-single-rtp-fullcone'= SIP ALG Single RTP Full-cone Found; 'sip-alg-rtcp-fullcone-mismatch'= SIP ALG RTCP Full-cone NAT Port Mismatch; 'sip-alg-reuse-rtp-rtcp-fullcone'= SIP ALG Reuse RTP/RTCP Full-cone Session; 'sip-alg-single-rtcp-fullcone'= SIP ALG Single RTCP Full-cone Found; 'sip-alg- create-rtp-fullcone-failure'= SIP ALG Create RTP Full-cone Session Failure; 'sip-alg-create-rtcp-fullcone-failure'= SIP ALG Create RTCP Full-cone Session Failure; 'icmp-out-of-state-uqe-admin-filtered-sent'= Total User Quota Exceeded ICMP admin filtered sent; 'icmp-out-of-state-uqe-host-unreachable-sent'= Total User Quota Exceeded ICMP host unreachable sent; 'icmp-out-of-state-uqe- dropped'= Total User Queue Exceeded ICMP notification dropped; 'nat-esp-ip- conflicts'= Fixed NAT ESP IP Conflicts; 'total-tcp-allocated-shadow'= Total TCP Ports Allocated; 'total-tcp-freed-shadow'= Total TCP Ports Freed; 'total-udp- allocated-shadow'= Total UDP Ports Allocated; 'total-udp-freed-shadow'= Total UDP Ports Freed; 'total-icmp-allocated-shadow'= Total ICMP Ports Allocated; 'total-icmp-freed-shadow'= Total ICMP Ports Freed; 'nat44-data-session-created- shadow'= NAT44 Data Sessions Created; 'nat44-data-session-freed-shadow'= NAT44 Data Sessions Freed; 'nat64-data-session-created-shadow'= NAT64 Data Sessions Created; 'nat64-data-session-freed-shadow'= NAT64 Data Sessions Freed; 'dslite- data-session-created-shadow'= DS-Lite Data Sessions Created; 'dslite-data- session-freed-shadow'= DS-Lite Data Sessions Freed; 'nat44-tcp-fullcone- created-shadow'= NAT44 TCP Full-Cone Created; 'nat44-tcp-fullcone-freed- shadow'= NAT44 TCP Full-Cone Freed; 'nat44-udp-fullcone-created-shadow'= NAT44 UDP Full-Cone Created; 'nat44-udp-fullcone-freed-shadow'= NAT44 UDP Full-Cone Freed; 'nat44-udp-alg-fullcone-created-shadow'= NAT44 UDP ALG Full-Cone Created;


    counters2 (optional, any, None)
      'nat44-udp-alg-fullcone-freed-shadow'= NAT44 UDP ALG Full-Cone Freed; 'nat64-tcp-fullcone-created-shadow'= NAT64 TCP Full-Cone Created; 'nat64-tcp- fullcone-freed-shadow'= NAT64 TCP Full-Cone Freed; 'nat64-udp-fullcone-created- shadow'= NAT64 UDP Full-Cone Created; 'nat64-udp-fullcone-freed-shadow'= NAT64 UDP Full-Cone Freed; 'nat64-udp-alg-fullcone-created-shadow'= NAT64 UDP ALG Full-Cone Created; 'nat64-udp-alg-fullcone-freed-shadow'= NAT64 UDP ALG Full- Cone Freed; 'dslite-tcp-fullcone-created-shadow'= DS-Lite TCP Full-Cone Created; 'dslite-tcp-fullcone-freed-shadow'= DS-Lite TCP Full-Cone Freed; 'dslite-udp-fullcone-created-shadow'= DS-Lite UDP Full-Cone Created; 'dslite- udp-fullcone-freed-shadow'= DS-Lite UDP Full-Cone Freed; 'dslite-udp-alg- fullcone-created-shadow'= DS-Lite UDP ALG Full-Cone Created; 'dslite-udp-alg- fullcone-freed-shadow'= DS-Lite UDP ALG Full-Cone Freed; 'h323-alg-reuse- fullcone'= H323 ALG Reuse Full-cone Session; 'h323-alg-fullcone-mismatch'= H323 ALG Full-cone Session Mismatch; 'h323-alg-create-fullcone-failure'= H323 ALG Create Full-cone Session Failure; 'h323-alg-single-rtp-fullcone'= H323 ALG Single RTP Full-cone Found; 'h323-alg-rtcp-fullcone-mismatch'= H323 ALG RTCP Full-cone NAT Port Mismatch; 'h323-alg-reuse-rtp-rtcp-fullcone'= H323 ALG Reuse RTP/RTCP Full-cone Session; 'h323-alg-single-rtcp-fullcone'= H323 ALG Single RTCP Full-cone Found; 'h323-alg-create-rtp-fullcone-failure'= H323 ALG Create RTP Full-cone Session Failure; 'h323-alg-create-rtcp-fullcone-failure'= H323 ALG Create RTCP Full-cone Session Failure; 'mgcp-alg-reuse-fullcone'= MGCP ALG Reuse Full-cone Session; 'mgcp-alg-fullcone-mismatch'= MGCP ALG Full-cone Session Mismatch; 'mgcp-alg-create-fullcone-failure'= MGCP ALG Create Full-cone Session Failure; 'mgcp-alg-single-rtp-fullcone'= MGCP ALG Single RTP Full-cone Found; 'mgcp-alg-rtcp-fullcone-mismatch'= MGCP ALG RTCP Full-cone NAT Port Mismatch; 'mgcp-alg-reuse-rtp-rtcp-fullcone'= MGCP ALG Reuse RTP/RTCP Full-cone Session; 'mgcp-alg-single-rtcp-fullcone'= MGCP ALG Single RTCP Full-cone Found; 'mgcp-alg-create-rtp-fullcone-failure'= MGCP ALG Create RTP Full-cone Session Failure; 'mgcp-alg-create-rtcp-fullcone-failure'= MGCP ALG Create RTCP Full- cone Session Failure; 'user-unusable-drop'= Fixed NAT User Unusable Drop; 'ipv4-user-unusable'= Fixed NAT IPv4 User Marked Unusable; 'ipv6-user- unusable'= Fixed NAT IPv6 User Marked Unusable; 'ipd-disabled'= Fixed NAT IPD disabled; 'dslite_tunnel_frag'= IPv4 Fragment DS-Lite Packet; 'total-tcp- overload-acquired'= Total TCP ports acquired for port overloading; 'total-udp- overload-acquired'= Total UDP ports acquired for port overloading; 'total-tcp- overload-released'= Total TCP ports released from port overloading; 'total-udp- overload-released'= Total UDP ports released from port overloading; 'total-tcp- alloc-overload'= Total TCP ports allocated via overload; 'total-udp-alloc- overload'= Total UDP ports allocated via overload; 'total-tcp-free-overload'= Total TCP ports freed via overload; 'total-udp-free-overload'= Total UDP ports freed via overload; 'port-overload-smp-delete-scheduled'= Port overload SMP conn delete scheduled; 'port-overload-smp-mem-allocated'= Port overload SMP mem allocated; 'port-overload-out-of-memory'= Port overload out of memory; 'port- overload-smp-free'= Port overload SMP conn free; 'port-overload-smp-free-no- lid'= Port overload SMP conn free no lid; 'port-overload-free-smp-not-found'= Port overload free SMP conn not found; 'port-overload-failed'= Port overload failed; 'total-tcp-overload-acquired-shadow'= Total TCP ports acquired for port overloading shadow; 'total-udp-overload-acquired-shadow'= Total UDP ports acquired for port overloading shadow; 'total-tcp-overload-released-shadow'= Total TCP ports released from port overloading shadow; 'total-udp-overload- released-shadow'= Total UDP ports released from port overloading shadow; 'total-tcp-alloc-overload-shadow'= Total TCP allocated via overload shadow; 'total-udp-alloc-overload-shadow'= Total UDP allocated via overload shadow; 'total-tcp-free-overload-shadow'= Total TCP freed via overload shadow; 'total- udp-free-overload-shadow'= Total UDP freed via overload shadow; 'ha-session- user-quota-exceeded'= HA Sessions User Quota Exceeded; 'tcp-user-quota- exceeded'= TCP User Quota Exceeded; 'udp-user-quota-exceeded'= UDP User Quota Exceeded; 'icmp-user-quota-exceeded'= ICMP User Quota Exceeded; 'ha-tcp-user- quota-exceeded'= HA TCP User Quota Exceeded; 'ha-udp-user-quota-exceeded'= HA UDP User Quota Exceeded; 'ha-icmp-user-quota-exceeded'= HA ICMP User Quota Exceeded; 'ha-nat-port-unavailable-tcp'= HA TCP NAT Port Unavailable; 'ha-nat- port-unavailable-udp'= HA UDP NAT Port Unavailable; 'ha-nat-port-unavailable- icmp'= HA ICMP NAT Port Unavailable; 'fnat44_fwd_ingress_packets_tcp'= Fixed NAT44 Forward Ingress Packets TCP; 'fnat44_fwd_egress_packets_tcp'= Fixed NAT44 Forward Egress Packets TCP; 'fnat44_rev_ingress_packets_tcp'= Fixed NAT44 Reverse Ingress Packets TCP; 'fnat44_rev_egress_packets_tcp'= Fixed NAT44 Reverse Egress Packets TCP; 'fnat44_fwd_ingress_bytes_tcp'= Fixed NAT44 Forward Ingress Bytes TCP; 'fnat44_fwd_egress_bytes_tcp'= Fixed NAT44 Forward Egress Bytes TCP; 'fnat44_rev_ingress_bytes_tcp'= Fixed NAT44 Reverse Ingress Bytes TCP; 'fnat44_rev_egress_bytes_tcp'= Fixed NAT44 Reverse Egress Bytes TCP; 'fnat44_fwd_ingress_packets_udp'= Fixed NAT44 Forward Ingress Packets UDP; 'fnat44_fwd_egress_packets_udp'= Fixed NAT44 Forward Egress Packets UDP; 'fnat44_rev_ingress_packets_udp'= Fixed NAT44 Reverse Ingress Packets UDP; 'fnat44_rev_egress_packets_udp'= Fixed NAT44 Reverse Egress Packets UDP; 'fnat44_fwd_ingress_bytes_udp'= Fixed NAT44 Forward Ingress Bytes UDP; 'fnat44_fwd_egress_bytes_udp'= Fixed NAT44 Forward Egress Bytes UDP; 'fnat44_rev_ingress_bytes_udp'= Fixed NAT44 Reverse Ingress Bytes UDP; 'fnat44_rev_egress_bytes_udp'= Fixed NAT44 Reverse Egress Bytes UDP; 'fnat44_fwd_ingress_packets_icmp'= Fixed NAT44 Forward Ingress Packets ICMP; 'fnat44_fwd_egress_packets_icmp'= Fixed NAT44 Forward Egress Packets ICMP; 'fnat44_rev_ingress_packets_icmp'= Fixed NAT44 Reverse Ingress Packets ICMP; 'fnat44_rev_egress_packets_icmp'= Fixed NAT44 Reverse Egress Packets ICMP; 'fnat44_fwd_ingress_bytes_icmp'= Fixed NAT44 Forward Ingress Bytes ICMP; 'fnat44_fwd_egress_bytes_icmp'= Fixed NAT44 Forward Egress Bytes ICMP; 'fnat44_rev_ingress_bytes_icmp'= Fixed NAT44 Reverse Ingress Bytes ICMP; 'fnat44_rev_egress_bytes_icmp'= Fixed NAT44 Reverse Egress Bytes ICMP; 'fnat44_fwd_ingress_packets_others'= Fixed NAT44 Forward Ingress Packets OTHERS; 'fnat44_fwd_egress_packets_others'= Fixed NAT44 Forward Egress Packets OTHERS; 'fnat44_rev_ingress_packets_others'= Fixed NAT44 Reverse Ingress Packets OTHERS; 'fnat44_rev_egress_packets_others'= Fixed NAT44 Reverse Egress Packets OTHERS; 'fnat44_fwd_ingress_bytes_others'= Fixed NAT44 Forward Ingress Bytes OTHERS; 'fnat44_fwd_egress_bytes_others'= Fixed NAT44 Forward Egress Bytes OTHERS; 'fnat44_rev_ingress_bytes_others'= Fixed NAT44 Reverse Ingress Bytes OTHERS; 'fnat44_rev_egress_bytes_others'= Fixed NAT44 Reverse Egress Bytes OTHERS; 'fnat44_fwd_ingress_pkt_size_range1'= Fixed NAT44 Forward Ingress Packet size between 0 and 200; 'fnat44_fwd_ingress_pkt_size_range2'= Fixed NAT44 Forward Ingress Packet size between 201 and 800; 'fnat44_fwd_ingress_pkt_size_range3'= Fixed NAT44 Forward Ingress Packet size between 801 and 1550; 'fnat44_fwd_ingress_pkt_size_range4'= Fixed NAT44 Forward Ingress Packet size between 1551 and 9000; 'fnat44_fwd_egress_pkt_size_range1'= Fixed NAT44 Forward Egress Packet size between 0 and 200;


    counters3 (optional, any, None)
      'fnat44_fwd_egress_pkt_size_range2'= Fixed NAT44 Forward Egress Packet size between 201 and 800; 'fnat44_fwd_egress_pkt_size_range3'= Fixed NAT44 Forward Egress Packet size between 801 and 1550; 'fnat44_fwd_egress_pkt_size_range4'= Fixed NAT44 Forward Egress Packet size between 1551 and 9000; 'fnat44_rev_ingress_pkt_size_range1'= Fixed NAT44 Reverse Ingress Packet size between 0 and 200; 'fnat44_rev_ingress_pkt_size_range2'= Fixed NAT44 Reverse Ingress Packet size between 201 and 800; 'fnat44_rev_ingress_pkt_size_range3'= Fixed NAT44 Reverse Ingress Packet size between 801 and 1550; 'fnat44_rev_ingress_pkt_size_range4'= Fixed NAT44 Reverse Ingress Packet size between 1551 and 9000; 'fnat44_rev_egress_pkt_size_range1'= Fixed NAT44 Reverse Egress Packet size between 0 and 200; 'fnat44_rev_egress_pkt_size_range2'= Fixed NAT44 Reverse Egress Packet size between 201 and 800; 'fnat44_rev_egress_pkt_size_range3'= Fixed NAT44 Reverse Egress Packet size between 801 and 1550; 'fnat44_rev_egress_pkt_size_range4'= Fixed NAT44 Reverse Egress Packet size between 1551 and 9000; 'fnat64_fwd_ingress_packets_tcp'= Fixed NAT64 Forward Ingress Packets TCP; 'fnat64_fwd_egress_packets_tcp'= Fixed NAT64 Forward Egress Packets TCP; 'fnat64_rev_ingress_packets_tcp'= Fixed NAT64 Reverse Ingress Packets TCP; 'fnat64_rev_egress_packets_tcp'= Fixed NAT64 Reverse Egress Packets TCP; 'fnat64_fwd_ingress_bytes_tcp'= Fixed NAT64 Forward Ingress Bytes TCP; 'fnat64_fwd_egress_bytes_tcp'= Fixed NAT64 Forward Egress Bytes TCP; 'fnat64_rev_ingress_bytes_tcp'= Fixed NAT64 Reverse Ingress Bytes TCP; 'fnat64_rev_egress_bytes_tcp'= Fixed NAT64 Reverse Egress Bytes TCP; 'fnat64_fwd_ingress_packets_udp'= Fixed NAT64 Forward Ingress Packets UDP; 'fnat64_fwd_egress_packets_udp'= Fixed NAT64 Forward Egress Packets UDP; 'fnat64_rev_ingress_packets_udp'= Fixed NAT64 Reverse Ingress Packets UDP; 'fnat64_rev_egress_packets_udp'= Fixed NAT64 Reverse Egress Packets UDP; 'fnat64_fwd_ingress_bytes_udp'= Fixed NAT64 Forward Ingress Bytes UDP; 'fnat64_fwd_egress_bytes_udp'= Fixed NAT64 Forward Egress Bytes UDP; 'fnat64_rev_ingress_bytes_udp'= Fixed NAT64 Reverse Ingress Bytes UDP; 'fnat64_rev_egress_bytes_udp'= Fixed NAT64 Reverse Egress Bytes UDP; 'fnat64_fwd_ingress_packets_icmp'= Fixed NAT64 Forward Ingress Packets ICMP; 'fnat64_fwd_egress_packets_icmp'= Fixed NAT64 Forward Egress Packets ICMP; 'fnat64_rev_ingress_packets_icmp'= Fixed NAT64 Reverse Ingress Packets ICMP; 'fnat64_rev_egress_packets_icmp'= Fixed NAT64 Reverse Egress Packets ICMP; 'fnat64_fwd_ingress_bytes_icmp'= Fixed NAT64 Forward Ingress Bytes ICMP; 'fnat64_fwd_egress_bytes_icmp'= Fixed NAT64 Forward Egress Bytes ICMP; 'fnat64_rev_ingress_bytes_icmp'= Fixed NAT64 Reverse Ingress Bytes ICMP; 'fnat64_rev_egress_bytes_icmp'= Fixed NAT64 Reverse Egress Bytes ICMP; 'fnat64_fwd_ingress_packets_others'= Fixed NAT64 Forward Ingress Packets OTHERS; 'fnat64_fwd_egress_packets_others'= Fixed NAT64 Forward Egress Packets OTHERS; 'fnat64_rev_ingress_packets_others'= Fixed NAT64 Reverse Ingress Packets OTHERS; 'fnat64_rev_egress_packets_others'= Fixed NAT64 Reverse Egress Packets OTHERS; 'fnat64_fwd_ingress_bytes_others'= Fixed NAT64 Forward Ingress Bytes OTHERS; 'fnat64_fwd_egress_bytes_others'= Fixed NAT64 Forward Egress Bytes OTHERS; 'fnat64_rev_ingress_bytes_others'= Fixed NAT64 Reverse Ingress Bytes OTHERS; 'fnat64_rev_egress_bytes_others'= Fixed NAT64 Reverse Egress Bytes OTHERS; 'fnat64_fwd_ingress_pkt_size_range1'= Fixed NAT64 Forward Ingress Packet size between 0 and 200; 'fnat64_fwd_ingress_pkt_size_range2'= Fixed NAT64 Forward Ingress Packet size between 201 and 800; 'fnat64_fwd_ingress_pkt_size_range3'= Fixed NAT64 Forward Ingress Packet size between 801 and 1550; 'fnat64_fwd_ingress_pkt_size_range4'= Fixed NAT64 Forward Ingress Packet size between 1551 and 9000; 'fnat64_fwd_egress_pkt_size_range1'= Fixed NAT64 Forward Egress Packet size between 0 and 200; 'fnat64_fwd_egress_pkt_size_range2'= Fixed NAT64 Forward Egress Packet size between 201 and 800; 'fnat64_fwd_egress_pkt_size_range3'= Fixed NAT64 Forward Egress Packet size between 801 and 1550; 'fnat64_fwd_egress_pkt_size_range4'= Fixed NAT64 Forward Egress Packet size between 1551 and 9000; 'fnat64_rev_ingress_pkt_size_range1'= Fixed NAT64 Reverse Ingress Packet size between 0 and 200; 'fnat64_rev_ingress_pkt_size_range2'= Fixed NAT64 Reverse Ingress Packet size between 201 and 800; 'fnat64_rev_ingress_pkt_size_range3'= Fixed NAT64 Reverse Ingress Packet size between 801 and 1550; 'fnat64_rev_ingress_pkt_size_range4'= Fixed NAT64 Reverse Ingress Packet size between 1551 and 9000; 'fnat64_rev_egress_pkt_size_range1'= Fixed NAT64 Reverse Egress Packet size between 0 and 200; 'fnat64_rev_egress_pkt_size_range2'= Fixed NAT64 Reverse Egress Packet size between 201 and 800; 'fnat64_rev_egress_pkt_size_range3'= Fixed NAT64 Reverse Egress Packet size between 801 and 1550; 'fnat64_rev_egress_pkt_size_range4'= Fixed NAT64 Reverse Egress Packet size between 1551 and 9000; 'fnatdslite_fwd_ingress_packets_tcp'= Fixed DS-Lite Forward Ingress Packets TCP; 'fnatdslite_fwd_egress_packets_tcp'= Fixed DS-Lite Forward Egress Packets TCP; 'fnatdslite_rev_ingress_packets_tcp'= Fixed DS-Lite Reverse Ingress Packets TCP; 'fnatdslite_rev_egress_packets_tcp'= Fixed DS-Lite Reverse Egress Packets TCP; 'fnatdslite_fwd_ingress_bytes_tcp'= Fixed DS-Lite Forward Ingress Bytes TCP; 'fnatdslite_fwd_egress_bytes_tcp'= Fixed DS-Lite Forward Egress Bytes TCP; 'fnatdslite_rev_ingress_bytes_tcp'= Fixed DS-Lite Reverse Ingress Bytes TCP; 'fnatdslite_rev_egress_bytes_tcp'= Fixed DS-Lite Reverse Egress Bytes TCP; 'fnatdslite_fwd_ingress_packets_udp'= Fixed DS-Lite Forward Ingress Packets UDP; 'fnatdslite_fwd_egress_packets_udp'= Fixed DS-Lite Forward Egress Packets UDP; 'fnatdslite_rev_ingress_packets_udp'= Fixed DS-Lite Reverse Ingress Packets UDP; 'fnatdslite_rev_egress_packets_udp'= Fixed DS-Lite Reverse Egress Packets UDP; 'fnatdslite_fwd_ingress_bytes_udp'= Fixed DS-Lite Forward Ingress Bytes UDP; 'fnatdslite_fwd_egress_bytes_udp'= Fixed DS-Lite Forward Egress Bytes UDP; 'fnatdslite_rev_ingress_bytes_udp'= Fixed DS-Lite Reverse Ingress Bytes UDP; 'fnatdslite_rev_egress_bytes_udp'= Fixed DS-Lite Reverse Egress Bytes UDP; 'fnatdslite_fwd_ingress_packets_icmp'= Fixed DS-Lite Forward Ingress Packets ICMP; 'fnatdslite_fwd_egress_packets_icmp'= Fixed DS-Lite Forward Egress Packets ICMP; 'fnatdslite_rev_ingress_packets_icmp'= Fixed DS-Lite Reverse Ingress Packets ICMP; 'fnatdslite_rev_egress_packets_icmp'= Fixed DS-Lite Reverse Egress Packets ICMP; 'fnatdslite_fwd_ingress_bytes_icmp'= Fixed DS-Lite Forward Ingress Bytes ICMP; 'fnatdslite_fwd_egress_bytes_icmp'= Fixed DS-Lite Forward Egress Bytes ICMP; 'fnatdslite_rev_ingress_bytes_icmp'= Fixed DS-Lite Reverse Ingress Bytes ICMP; 'fnatdslite_rev_egress_bytes_icmp'= Fixed DS-Lite Reverse Egress Bytes ICMP; 'fnatdslite_fwd_ingress_packets_others'= Fixed DS-Lite Forward Ingress Packets OTHERS; 'fnatdslite_fwd_egress_packets_others'= Fixed DS-Lite Forward Egress Packets OTHERS; 'fnatdslite_rev_ingress_packets_others'= Fixed DS-Lite Reverse Ingress Packets OTHERS; 'fnatdslite_rev_egress_packets_others'= Fixed DS-Lite Reverse Egress Packets OTHERS; 'fnatdslite_fwd_ingress_bytes_others'= Fixed DS-Lite Forward Ingress Bytes OTHERS; 'fnatdslite_fwd_egress_bytes_others'= Fixed DS-Lite Forward Egress Bytes OTHERS; 'fnatdslite_rev_ingress_bytes_others'= Fixed DS-Lite Reverse Ingress Bytes OTHERS; 'fnatdslite_rev_egress_bytes_others'= Fixed DS- Lite Reverse Egress Bytes OTHERS; 'fnatdslite_fwd_ingress_pkt_size_range1'= Fixed DS-Lite Forward Ingress Packet size between 0 and 200;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    nat44_tcp_fullcone_created (optional, any, None)
      NAT44 TCP Full-Cone Created


    fnat44_fwd_ingress_pkt_size_range4 (optional, any, None)
      Fixed NAT44 Forward Ingress Packet size between 1551 and 9000


    fnat44_fwd_ingress_pkt_size_range1 (optional, any, None)
      Fixed NAT44 Forward Ingress Packet size between 0 and 200


    fnat44_fwd_ingress_packets_icmp (optional, any, None)
      Fixed NAT44 Forward Ingress Packets ICMP


    fnat44_fwd_ingress_pkt_size_range2 (optional, any, None)
      Fixed NAT44 Forward Ingress Packet size between 201 and 800


    total_tcp_alloc_overload (optional, any, None)
      Total TCP ports allocated via overload


    fnatdslite_fwd_ingress_bytes_others (optional, any, None)
      Fixed DS-Lite Forward Ingress Bytes OTHERS


    fnatdslite_rev_ingress_pkt_size_range4 (optional, any, None)
      Fixed DS-Lite Reverse Ingress Packet size between 1551 and 9000


    fnatdslite_rev_egress_packets_udp (optional, any, None)
      Fixed DS-Lite Reverse Egress Packets UDP


    fnatdslite_rev_ingress_pkt_size_range2 (optional, any, None)
      Fixed DS-Lite Reverse Ingress Packet size between 201 and 800


    fnatdslite_rev_ingress_pkt_size_range3 (optional, any, None)
      Fixed DS-Lite Reverse Ingress Packet size between 801 and 1550


    fnatdslite_rev_ingress_pkt_size_range1 (optional, any, None)
      Fixed DS-Lite Reverse Ingress Packet size between 0 and 200


    fnat64_fwd_ingress_bytes_others (optional, any, None)
      Fixed NAT64 Forward Ingress Bytes OTHERS


    fnat64_rev_ingress_packets_udp (optional, any, None)
      Fixed NAT64 Reverse Ingress Packets UDP


    nat44_eif_limit_exceeded (optional, any, None)
      NAT44 Endpoint-Independent-Filtering Limit Exceeded


    nat64_eif_limit_exceeded (optional, any, None)
      NAT64 Endpoint-Independent-Filtering Limit Exceeded


    tcp_user_quota_exceeded (optional, any, None)
      TCP User Quota Exceeded


    fnat64_rev_egress_bytes_tcp (optional, any, None)
      Fixed NAT64 Reverse Egress Bytes TCP


    dslite_data_session_created (optional, any, None)
      DS-Lite Data Sessions Created


    fnatdslite_fwd_egress_bytes_udp (optional, any, None)
      Fixed DS-Lite Forward Egress Bytes UDP


    nat64_data_session_created (optional, any, None)
      NAT64 Data Sessions Created


    total_udp_free_overload (optional, any, None)
      Total UDP ports freed via overload


    fnat44_rev_ingress_pkt_size_range4 (optional, any, None)
      Fixed NAT44 Reverse Ingress Packet size between 1551 and 9000


    fnatdslite_rev_ingress_packets_icmp (optional, any, None)
      Fixed DS-Lite Reverse Ingress Packets ICMP


    fnat44_rev_egress_bytes_udp (optional, any, None)
      Fixed NAT44 Reverse Egress Bytes UDP


    fnat64_fwd_ingress_bytes_icmp (optional, any, None)
      Fixed NAT64 Forward Ingress Bytes ICMP


    nat64_tcp_fullcone_created (optional, any, None)
      NAT64 TCP Full-Cone Created


    dslite_udp_alg_fullcone_freed (optional, any, None)
      DS-Lite UDP ALG Full-Cone Freed


    fnatdslite_rev_ingress_bytes_icmp (optional, any, None)
      Fixed DS-Lite Reverse Ingress Bytes ICMP


    fullcone_failure (optional, any, None)
      Full-Cone Session Creation Failed


    fnat64_fwd_egress_packets_icmp (optional, any, None)
      Fixed NAT64 Forward Egress Packets ICMP


    fnat44_fwd_ingress_pkt_size_range3 (optional, any, None)
      Fixed NAT44 Forward Ingress Packet size between 801 and 1550


    nat64_tcp_fullcone_freed (optional, any, None)
      NAT64 TCP Full-Cone Freed


    nat64_udp_fullcone_created (optional, any, None)
      NAT64 UDP Full-Cone Created


    dest_rlist_drop (optional, any, None)
      Fixed NAT Dest Rule List Drop


    fnat64_fwd_ingress_packets_udp (optional, any, None)
      Fixed NAT64 Forward Ingress Packets UDP


    fnat64_fwd_egress_pkt_size_range4 (optional, any, None)
      Fixed NAT64 Forward Egress Packet size between 1551 and 9000


    nat44_data_session_created (optional, any, None)
      NAT44 Data Sessions Created


    fnatdslite_rev_egress_bytes_icmp (optional, any, None)
      Fixed DS-Lite Reverse Egress Bytes ICMP


    fnat64_fwd_egress_pkt_size_range1 (optional, any, None)
      Fixed NAT64 Forward Egress Packet size between 0 and 200


    fnat64_fwd_egress_pkt_size_range2 (optional, any, None)
      Fixed NAT64 Forward Egress Packet size between 201 and 800


    fnat64_fwd_egress_pkt_size_range3 (optional, any, None)
      Fixed NAT64 Forward Egress Packet size between 801 and 1550


    fnat64_rev_egress_packets_udp (optional, any, None)
      Fixed NAT64 Reverse Egress Packets UDP


    fnat44_fwd_egress_pkt_size_range4 (optional, any, None)
      Fixed NAT44 Forward Egress Packet size between 1551 and 9000


    fnat44_fwd_egress_pkt_size_range2 (optional, any, None)
      Fixed NAT44 Forward Egress Packet size between 201 and 800


    fnat44_fwd_ingress_packets_tcp (optional, any, None)
      Fixed NAT44 Forward Ingress Packets TCP


    nat64_udp_fullcone_freed (optional, any, None)
      NAT64 UDP Full-Cone Freed


    dslite_udp_fullcone_freed (optional, any, None)
      DS-Lite UDP Full-Cone Freed


    udp_user_quota_exceeded (optional, any, None)
      UDP User Quota Exceeded


    fnat44_fwd_ingress_bytes_udp (optional, any, None)
      Fixed NAT44 Forward Ingress Bytes UDP


    fnatdslite_fwd_ingress_packets_others (optional, any, None)
      Fixed DS-Lite Forward Ingress Packets OTHERS


    fnat44_fwd_ingress_bytes_others (optional, any, None)
      Fixed NAT44 Forward Ingress Bytes OTHERS


    dslite_tcp_fullcone_created (optional, any, None)
      DS-Lite TCP Full-Cone Created


    fnat44_fwd_egress_bytes_tcp (optional, any, None)
      Fixed NAT44 Forward Egress Bytes TCP


    nat44_hairpin (optional, any, None)
      NAT44 Hairpin Session Created


    fnatdslite_fwd_egress_packets_icmp (optional, any, None)
      Fixed DS-Lite Forward Egress Packets ICMP


    dest_rlist_snat_drop (optional, any, None)
      Fixed NAT Dest Rules List Source NAT Drop


    total_icmp_freed (optional, any, None)
      Total ICMP Ports Freed


    fnatdslite_fwd_ingress_bytes_tcp (optional, any, None)
      Fixed DS-Lite Forward Ingress Bytes TCP


    fnat44_fwd_egress_pkt_size_range3 (optional, any, None)
      Fixed NAT44 Forward Egress Packet size between 801 and 1550


    fnat64_fwd_ingress_packets_tcp (optional, any, None)
      Fixed NAT64 Forward Ingress Packets TCP


    total_tcp_overload_released (optional, any, None)
      Total TCP ports released from port overloading


    fnatdslite_fwd_egress_packets_others (optional, any, None)
      Fixed DS-Lite Forward Egress Packets OTHERS


    sixrd_drop (optional, any, None)
      Fixed NAT IPv6 in IPv4 Packet Drop


    fnat44_rev_egress_packets_tcp (optional, any, None)
      Fixed NAT44 Reverse Egress Packets TCP


    fnat44_fwd_egress_packets_icmp (optional, any, None)
      Fixed NAT44 Forward Egress Packets ICMP


    nat64_udp_alg_fullcone_created (optional, any, None)
      NAT64 UDP ALG Full-Cone Created


    icmp_user_quota_exceeded (optional, any, None)
      ICMP User Quota Exceeded


    fnat64_fwd_egress_packets_others (optional, any, None)
      Fixed NAT64 Forward Egress Packets OTHERS


    fnat44_fwd_ingress_packets_others (optional, any, None)
      Fixed NAT44 Forward Ingress Packets OTHERS


    total_tcp_allocated (optional, any, None)
      Total TCP Ports Allocated


    dest_rlist_pass_through (optional, any, None)
      Fixed NAT Dest Rule List Pass-Through


    fnat44_fwd_ingress_bytes_tcp (optional, any, None)
      Fixed NAT44 Forward Ingress Bytes TCP


    fnat64_rev_ingress_bytes_udp (optional, any, None)
      Fixed NAT64 Reverse Ingress Bytes UDP


    nat44_eif_match (optional, any, None)
      NAT44 Endpoint-Independent-Filtering Matched


    fnatdslite_rev_egress_bytes_others (optional, any, None)
      Fixed DS-Lite Reverse Egress Bytes OTHERS


    fnatdslite_fwd_egress_packets_tcp (optional, any, None)
      Fixed DS-Lite Forward Egress Packets TCP


    dslite_udp_alg_fullcone_created (optional, any, None)
      DS-Lite UDP ALG Full-Cone Created


    fnat44_rev_ingress_bytes_icmp (optional, any, None)
      Fixed NAT44 Reverse Ingress Bytes ICMP


    fnatdslite_rev_egress_pkt_size_range3 (optional, any, None)
      Fixed DS-Lite Reverse Egress Packet size between 801 and 1550


    fnatdslite_rev_egress_pkt_size_range2 (optional, any, None)
      Fixed DS-Lite Reverse Egress Packet size between 201 and 800


    fnatdslite_rev_egress_pkt_size_range1 (optional, any, None)
      Fixed DS-Lite Reverse Egress Packet size between 0 and 200


    fnat64_fwd_egress_bytes_udp (optional, any, None)
      Fixed NAT64 Forward Egress Bytes UDP


    fnatdslite_rev_egress_pkt_size_range4 (optional, any, None)
      Fixed DS-Lite Reverse Egress Packet size between 1551 and 9000


    fnat44_fwd_egress_bytes_others (optional, any, None)
      Fixed NAT44 Forward Egress Bytes OTHERS


    total_icmp_allocated (optional, any, None)
      Total ICMP Ports Allocated


    fnatdslite_fwd_ingress_bytes_icmp (optional, any, None)
      Fixed DS-Lite Forward Ingress Bytes ICMP


    fnatdslite_fwd_ingress_bytes_udp (optional, any, None)
      Fixed DS-Lite Forward Ingress Bytes UDP


    total_udp_alloc_overload (optional, any, None)
      Total UDP ports allocated via overload


    fnat64_rev_egress_pkt_size_range1 (optional, any, None)
      Fixed NAT64 Reverse Egress Packet size between 0 and 200


    fnat64_rev_egress_pkt_size_range2 (optional, any, None)
      Fixed NAT64 Reverse Egress Packet size between 201 and 800


    fnat64_rev_egress_pkt_size_range3 (optional, any, None)
      Fixed NAT64 Reverse Egress Packet size between 801 and 1550


    nat64_eim_match (optional, any, None)
      NAT64 Endpoint-Independent-Mapping Matched


    fnat64_fwd_egress_packets_udp (optional, any, None)
      Fixed NAT64 Forward Egress Packets UDP


    fnat44_rev_egress_packets_udp (optional, any, None)
      Fixed NAT44 Reverse Egress Packets UDP


    fnatdslite_fwd_egress_bytes_tcp (optional, any, None)
      Fixed DS-Lite Forward Egress Bytes TCP


    fnat64_rev_ingress_bytes_tcp (optional, any, None)
      Fixed NAT64 Reverse Ingress Bytes TCP


    fnat64_rev_egress_bytes_udp (optional, any, None)
      Fixed NAT64 Reverse Egress Bytes UDP


    dslite_eif_match (optional, any, None)
      DS-Lite Endpoint-Independent-Filtering Matched


    total_udp_allocated (optional, any, None)
      Total UDP Ports Allocated


    nat44_udp_alg_fullcone_created (optional, any, None)
      NAT44 UDP ALG Full-Cone Created


    nat44_inbound_filtered (optional, any, None)
      NAT44 Endpoint-Dependent Filtering Drop


    fnat64_fwd_ingress_packets_others (optional, any, None)
      Fixed NAT64 Forward Ingress Packets OTHERS


    fnat44_rev_ingress_packets_tcp (optional, any, None)
      Fixed NAT44 Reverse Ingress Packets TCP


    fnat64_fwd_ingress_pkt_size_range4 (optional, any, None)
      Fixed NAT64 Forward Ingress Packet size between 1551 and 9000


    fnat64_rev_ingress_bytes_icmp (optional, any, None)
      Fixed NAT64 Reverse Ingress Bytes ICMP


    total_tcp_freed (optional, any, None)
      Total TCP Ports Freed


    fnat64_fwd_ingress_pkt_size_range1 (optional, any, None)
      Fixed NAT64 Forward Ingress Packet size between 0 and 200


    fnat64_rev_egress_packets_tcp (optional, any, None)
      Fixed NAT64 Reverse Egress Packets TCP


    standby_drop (optional, any, None)
      Fixed NAT LID Standby Drop


    fnatdslite_fwd_ingress_pkt_size_range4 (optional, any, None)
      Fixed DS-Lite Forward Ingress Packet size between 1551 and 9000


    fnatdslite_rev_ingress_packets_others (optional, any, None)
      Fixed DS-Lite Reverse Ingress Packets OTHERS


    fnatdslite_fwd_ingress_pkt_size_range2 (optional, any, None)
      Fixed DS-Lite Forward Ingress Packet size between 201 and 800


    fnatdslite_fwd_ingress_pkt_size_range3 (optional, any, None)
      Fixed DS-Lite Forward Ingress Packet size between 801 and 1550


    fnatdslite_fwd_ingress_pkt_size_range1 (optional, any, None)
      Fixed DS-Lite Forward Ingress Packet size between 0 and 200


    nat44_data_session_freed (optional, any, None)
      NAT44 Data Sessions Freed


    fnat64_rev_egress_packets_icmp (optional, any, None)
      Fixed NAT64 Reverse Egress Packets ICMP


    fnat44_fwd_egress_packets_udp (optional, any, None)
      Fixed NAT44 Forward Egress Packets UDP


    fnat44_rev_egress_bytes_others (optional, any, None)
      Fixed NAT44 Reverse Egress Bytes OTHERS


    fnat44_rev_egress_bytes_icmp (optional, any, None)
      Fixed NAT44 Reverse Egress Bytes ICMP


    fnat44_rev_ingress_bytes_others (optional, any, None)
      Fixed NAT44 Reverse Ingress Bytes OTHERS


    nat_port_unavailable_icmp (optional, any, None)
      ICMP NAT Port Unavailable


    fnatdslite_fwd_egress_pkt_size_range3 (optional, any, None)
      Fixed DS-Lite Forward Egress Packet size between 801 and 1550


    fnatdslite_fwd_egress_pkt_size_range2 (optional, any, None)
      Fixed DS-Lite Forward Egress Packet size between 201 and 800


    fnatdslite_fwd_egress_pkt_size_range1 (optional, any, None)
      Fixed DS-Lite Forward Egress Packet size between 0 and 200


    port_overload_failed (optional, any, None)
      Port overload failed


    fnatdslite_fwd_egress_pkt_size_range4 (optional, any, None)
      Fixed DS-Lite Forward Egress Packet size between 1551 and 9000


    fnatdslite_rev_ingress_bytes_tcp (optional, any, None)
      Fixed DS-Lite Reverse Ingress Bytes TCP


    fnat64_rev_egress_pkt_size_range4 (optional, any, None)
      Fixed NAT64 Reverse Egress Packet size between 1551 and 9000


    fnat64_fwd_ingress_bytes_tcp (optional, any, None)
      Fixed NAT64 Forward Ingress Bytes TCP


    fnat44_fwd_ingress_packets_udp (optional, any, None)
      Fixed NAT44 Forward Ingress Packets UDP


    fnatdslite_rev_ingress_packets_udp (optional, any, None)
      Fixed DS-Lite Reverse Ingress Packets UDP


    fnatdslite_rev_egress_packets_others (optional, any, None)
      Fixed DS-Lite Reverse Egress Packets OTHERS


    dslite_data_session_freed (optional, any, None)
      DS-Lite Data Sessions Freed


    fnat44_rev_ingress_packets_others (optional, any, None)
      Fixed NAT44 Reverse Ingress Packets OTHERS


    total_nat_in_use (optional, any, None)
      Total NAT Addresses in-use


    dslite_udp_fullcone_created (optional, any, None)
      DS-Lite UDP Full-Cone Created


    fnat44_fwd_egress_bytes_icmp (optional, any, None)
      Fixed NAT44 Forward Egress Bytes ICMP


    fnat44_fwd_egress_pkt_size_range1 (optional, any, None)
      Fixed NAT44 Forward Egress Packet size between 0 and 200


    fnatdslite_fwd_ingress_packets_udp (optional, any, None)
      Fixed DS-Lite Forward Ingress Packets UDP


    total_udp_freed (optional, any, None)
      Total UDP Ports Freed


    nat_port_unavailable_tcp (optional, any, None)
      TCP NAT Port Unavailable


    nat64_udp_alg_fullcone_freed (optional, any, None)
      NAT64 UDP ALG Full-Cone Freed


    fnatdslite_rev_ingress_bytes_udp (optional, any, None)
      Fixed DS-Lite Reverse Ingress Bytes UDP


    nat44_udp_fullcone_freed (optional, any, None)
      NAT44 UDP Full-Cone Freed


    nat44_eim_match (optional, any, None)
      NAT44 Endpoint-Independent-Mapping Matched


    fnat64_rev_egress_bytes_others (optional, any, None)
      Fixed NAT64 Reverse Egress Bytes OTHERS


    fnat44_fwd_egress_bytes_udp (optional, any, None)
      Fixed NAT44 Forward Egress Bytes UDP


    fnat44_rev_egress_packets_others (optional, any, None)
      Fixed NAT44 Reverse Egress Packets OTHERS


    fnat64_rev_ingress_pkt_size_range3 (optional, any, None)
      Fixed NAT64 Reverse Ingress Packet size between 801 and 1550


    fnat64_rev_ingress_pkt_size_range2 (optional, any, None)
      Fixed NAT64 Reverse Ingress Packet size between 201 and 800


    fnat64_rev_ingress_pkt_size_range1 (optional, any, None)
      Fixed NAT64 Reverse Ingress Packet size between 0 and 200


    fnatdslite_rev_ingress_bytes_others (optional, any, None)
      Fixed DS-Lite Reverse Ingress Bytes OTHERS


    fnat64_rev_ingress_pkt_size_range4 (optional, any, None)
      Fixed NAT64 Reverse Ingress Packet size between 1551 and 9000


    total_tcp_free_overload (optional, any, None)
      Total TCP ports freed via overload


    fnat44_rev_egress_packets_icmp (optional, any, None)
      Fixed NAT44 Reverse Egress Packets ICMP


    total_tcp_overload_acquired (optional, any, None)
      Total TCP ports acquired for port overloading


    fnat44_rev_egress_pkt_size_range2 (optional, any, None)
      Fixed NAT44 Reverse Egress Packet size between 201 and 800


    fnat44_rev_egress_pkt_size_range3 (optional, any, None)
      Fixed NAT44 Reverse Egress Packet size between 801 and 1550


    fnat44_rev_egress_pkt_size_range1 (optional, any, None)
      Fixed NAT44 Reverse Egress Packet size between 0 and 200


    fnat64_fwd_egress_bytes_tcp (optional, any, None)
      Fixed NAT64 Forward Egress Bytes TCP


    fnat44_rev_egress_pkt_size_range4 (optional, any, None)
      Fixed NAT44 Reverse Egress Packet size between 1551 and 9000


    fnat64_rev_ingress_bytes_others (optional, any, None)
      Fixed NAT64 Reverse Ingress Bytes OTHERS


    fnat44_rev_ingress_pkt_size_range1 (optional, any, None)
      Fixed NAT44 Reverse Ingress Packet size between 0 and 200


    nat64_data_session_freed (optional, any, None)
      NAT64 Data Sessions Freed


    fnat44_rev_ingress_pkt_size_range3 (optional, any, None)
      Fixed NAT44 Reverse Ingress Packet size between 801 and 1550


    fnat44_rev_ingress_pkt_size_range2 (optional, any, None)
      Fixed NAT44 Reverse Ingress Packet size between 201 and 800


    fnatdslite_rev_egress_packets_icmp (optional, any, None)
      Fixed DS-Lite Reverse Egress Packets ICMP


    nat_port_unavailable_udp (optional, any, None)
      UDP NAT Port Unavailable


    dslite_inbound_filtered (optional, any, None)
      DS-Lite Endpoint-Dependent Filtering Drop


    nat44_udp_fullcone_created (optional, any, None)
      NAT44 UDP Full-Cone Created


    fnatdslite_fwd_egress_bytes_others (optional, any, None)
      Fixed DS-Lite Forward Egress Bytes OTHERS


    fnat44_rev_ingress_packets_udp (optional, any, None)
      Fixed NAT44 Reverse Ingress Packets UDP


    fnat44_rev_ingress_packets_icmp (optional, any, None)
      Fixed NAT44 Reverse Ingress Packets ICMP


    nat64_hairpin (optional, any, None)
      NAT64 Hairpin Session Created


    fixed_nat_fullcone_self_hairpinning_drop (optional, any, None)
      Self-Hairpinning Drop


    nat64_inbound_filtered (optional, any, None)
      NAT64 Endpoint-Dependent Filtering Drop


    fnatdslite_rev_egress_bytes_tcp (optional, any, None)
      Fixed DS-Lite Reverse Egress Bytes TCP


    fnat64_rev_egress_packets_others (optional, any, None)
      Fixed NAT64 Reverse Egress Packets OTHERS


    config_not_found (optional, any, None)
      Fixed NAT Config not Found


    fnatdslite_fwd_egress_bytes_icmp (optional, any, None)
      Fixed DS-Lite Forward Egress Bytes ICMP


    dslite_hairpin (optional, any, None)
      DS-Lite Hairpin Session Created


    total_udp_overload_acquired (optional, any, None)
      Total UDP ports acquired for port overloading


    dslite_tcp_fullcone_freed (optional, any, None)
      DS-Lite TCP Full-Cone Freed


    fnatdslite_fwd_egress_packets_udp (optional, any, None)
      Fixed DS-Lite Forward Egress Packets UDP


    fnat44_rev_ingress_bytes_udp (optional, any, None)
      Fixed NAT44 Reverse Ingress Bytes UDP


    fnat64_fwd_ingress_pkt_size_range3 (optional, any, None)
      Fixed NAT64 Forward Ingress Packet size between 801 and 1550


    fnat64_rev_ingress_packets_tcp (optional, any, None)
      Fixed NAT64 Reverse Ingress Packets TCP


    session_user_quota_exceeded (optional, any, None)
      Sessions User Quota Exceeded


    fnat64_fwd_ingress_pkt_size_range2 (optional, any, None)
      Fixed NAT64 Forward Ingress Packet size between 201 and 800


    fnat64_fwd_egress_bytes_others (optional, any, None)
      Fixed NAT64 Forward Egress Bytes OTHERS


    fnat44_fwd_egress_packets_others (optional, any, None)
      Fixed NAT44 Forward Egress Packets OTHERS


    fnatdslite_rev_egress_bytes_udp (optional, any, None)
      Fixed DS-Lite Reverse Egress Bytes UDP


    fnat44_rev_ingress_bytes_tcp (optional, any, None)
      Fixed NAT44 Reverse Ingress Bytes TCP


    fnatdslite_fwd_ingress_packets_tcp (optional, any, None)
      Fixed DS-Lite Forward Ingress Packets TCP


    total_udp_overload_released (optional, any, None)
      Total UDP ports released from port overloading


    fnat64_rev_egress_bytes_icmp (optional, any, None)
      Fixed NAT64 Reverse Egress Bytes ICMP


    fnat64_fwd_egress_bytes_icmp (optional, any, None)
      Fixed NAT64 Forward Egress Bytes ICMP


    fnatdslite_fwd_ingress_packets_icmp (optional, any, None)
      Fixed DS-Lite Forward Ingress Packets ICMP


    fnat64_rev_ingress_packets_icmp (optional, any, None)
      Fixed NAT64 Reverse Ingress Packets ICMP


    fnat44_fwd_egress_packets_tcp (optional, any, None)
      Fixed NAT44 Forward Egress Packets TCP


    fnat44_rev_egress_bytes_tcp (optional, any, None)
      Fixed NAT44 Reverse Egress Bytes TCP


    fnat64_fwd_ingress_packets_icmp (optional, any, None)
      Fixed NAT64 Forward Ingress Packets ICMP


    fnatdslite_rev_egress_packets_tcp (optional, any, None)
      Fixed DS-Lite Reverse Egress Packets TCP


    fnat64_rev_ingress_packets_others (optional, any, None)
      Fixed NAT64 Reverse Ingress Packets OTHERS


    fnat44_fwd_ingress_bytes_icmp (optional, any, None)
      Fixed NAT44 Forward Ingress Bytes ICMP


    dslite_eim_match (optional, any, None)
      DS-Lite Endpoint-Independent-Mapping Matched


    fnat64_fwd_egress_packets_tcp (optional, any, None)
      Fixed NAT64 Forward Egress Packets TCP


    fnatdslite_rev_ingress_packets_tcp (optional, any, None)
      Fixed DS-Lite Reverse Ingress Packets TCP


    ha_session_user_quota_exceeded (optional, any, None)
      HA Sessions User Quota Exceeded


    nat44_udp_alg_fullcone_freed (optional, any, None)
      NAT44 UDP ALG Full-Cone Freed


    fnat64_fwd_ingress_bytes_udp (optional, any, None)
      Fixed NAT64 Forward Ingress Bytes UDP


    nat44_tcp_fullcone_freed (optional, any, None)
      NAT44 TCP Full-Cone Freed


    dslite_eif_limit_exceeded (optional, any, None)
      DS-Lite Endpoint-Independent-Filtering Limit Exceeded


    nat64_eif_match (optional, any, None)
      NAT64 Endpoint-Independent-Filtering Matched



  uuid (False, any, None)
    uuid of the object


  create_port_mapping_file (False, any, None)
    Create Port Mapping File


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  port_mapping_files_count (False, any, None)
    Number of old fixed_nat files to store


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

