.. _a10_object_group_service_module:


a10_object_group_service -- Configures A10 object-group.service
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure Service Object Group






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  description (False, any, None)
    Description of the object-group instance


  ansible_username (True, any, None)
    Username for AXAPI authentication


  rules (False, any, None)
    Field rules


    icmp_code (optional, any, None)
      ICMP code number


    any_code (optional, any, None)
      Any ICMP code


    special_v6_code (optional, any, None)
      'addr-unreachable'= Code 3, address unreachable; 'admin-prohibited'= Code 1, admin prohibited; 'no-route'= Code 0, no route to destination; 'not-neighbour'= Code 2, not neighbor; 'port-unreachable'= Code 4, destination port unreachable;


    range_src (optional, any, None)
      match only packets in the range of source port numbers (Starting Port Number)


    v6_any_code (optional, any, None)
      Any ICMPv6 code


    alg (optional, any, None)
      'FTP'= Specify FTP ALG port range; 'TFTP'= Specify TFTP ALG port range; 'SIP'= Specify SIP ALG port range; 'DNS'= Specify DNS ALG port range; 'PPTP'= Specify PPTP ALG port range; 'RTSP'= Specify RTSP ALG port range;


    lt_dst (optional, any, None)
      Match only packets with a lesser destination port number


    special_type (optional, any, None)
      'echo-reply'= Type 0, echo reply; 'echo-request'= Type 8, echo request; 'info- reply'= Type 16, information reply; 'info-request'= Type 15, information request; 'mask-reply'= Type 18, address mask reply; 'mask-request'= Type 17, address mask request; 'parameter-problem'= Type 12, parameter problem; 'redirect'= Type 5, redirect message; 'source-quench'= Type 4, source quench; 'time-exceeded'= Type 11, time exceeded; 'timestamp'= Type 13, timestamp; 'timestamp-reply'= Type 14, timestamp reply; 'dest-unreachable'= Type 3, destination unreachable;


    icmpv6_type (optional, any, None)
      ICMPv6 type number


    any_type (optional, any, None)
      Any ICMP type


    port_num_end_dst (optional, any, None)
      Ending Destination Port Number


    icmpv6_code (optional, any, None)
      ICMPv6 code number


    icmp_type (optional, any, None)
      ICMP type number


    lt_src (optional, any, None)
      Match only packets with a lower source port number


    gt_src (optional, any, None)
      Match only packets with a greater source port number


    gt_dst (optional, any, None)
      Match only packets with a greater destination port number


    eq_dst (optional, any, None)
      Match only packets on a given destination port (port number)


    v6_any_type (optional, any, None)
      Any ICMP type


    protocol_id (optional, any, None)
      Protocol ID


    icmp (optional, any, None)
      Internet Control Message Protocol


    seq_num (optional, any, None)
      Sequence number


    tcp_udp (optional, any, None)
      'tcp'= Protocol TCP; 'udp'= Protocol UDP;


    special_v6_type (optional, any, None)
      'dest-unreachable'= Type 1, destination unreachable; 'echo-reply'= Type 129, echo reply; 'echo-request'= Type 128, echo request; 'packet-too-big'= Type 2, packet too big; 'param-prob'= Type 4, parameter problem; 'time-exceeded'= Type 3, time exceeded;


    source (optional, any, None)
      Source Port Information


    port_num_end_src (optional, any, None)
      Ending Source Port Number


    eq_src (optional, any, None)
      Match only packets on a given source port (port number)


    icmpv6 (optional, any, None)
      Internet Control Message Protocol version 6


    range_dst (optional, any, None)
      Match only packets in the range of destination port numbers (Starting Destination Port Number)


    special_code (optional, any, None)
      'frag-required'= Code 4, fragmentation required; 'host-unreachable'= Code 1, destination host unreachable; 'network-unreachable'= Code 0, destination network unreachable; 'port-unreachable'= Code 3, destination port unreachable; 'proto-unreachable'= Code 2, destination protocol unreachable; 'route-failed'= Code 5, source route failed;



  user_tag (False, any, None)
    Customized tag


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  svc_name (True, any, None)
    Service Object Group Name


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uuid (False, any, None)
    uuid of the object









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

