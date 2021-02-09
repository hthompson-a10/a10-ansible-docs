.. _a10_access_list_extended_module:


a10_access_list_extended -- Configures A10 access-list.extended
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure Extended Access List






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  rules (False, any, None)
    Field rules


    any_code (optional, any, None)
      Any ICMP code


    dst_port_end (optional, any, None)
      Edning Destination Port Number


    service_obj_group (optional, any, None)
      Service object group (Source object group name)


    extd_action (optional, any, None)
      'deny'= Deny; 'permit'= Permit; 'l3-vlan-fwd-disable'= Disable L3 forwarding between VLANs;


    ip (optional, any, None)
      Any Internet Protocol


    udp (optional, any, None)
      protocol UDP


    tcp (optional, any, None)
      protocol TCP


    special_type (optional, any, None)
      'echo-reply'= Type 0, echo reply; 'echo-request'= Type 8, echo request; 'info- reply'= Type 16, information reply; 'info-request'= Type 15, information request; 'mask-reply'= Type 18, address mask reply; 'mask-request'= Type 17, address mask request; 'parameter-problem'= Type 12, parameter problem; 'redirect'= Type 5, redirect message; 'source-quench'= Type 4, source quench; 'time-exceeded'= Type 11, time exceeded; 'timestamp'= Type 13, timestamp; 'timestamp-reply'= Type 14, timestamp reply; 'dest-unreachable'= Type 3, destination unreachable;


    src_gt (optional, any, None)
      Match only packets with a greater port number


    icmp_type (optional, any, None)
      ICMP type number


    src_mask (optional, any, None)
      Source Mask 0=apply 255=ignore


    established (optional, any, None)
      TCP established


    src_range (optional, any, None)
      match only packets in the range of port numbers (Starting Port Number)


    extd_seq_num (optional, any, None)
      Sequence number


    src_eq (optional, any, None)
      Match only packets on a given source port (port number)


    dst_subnet (optional, any, None)
      Destination Address


    dst_lt (optional, any, None)
      Match only packets with a lesser port number


    fragments (optional, any, None)
      IP fragments


    src_object_group (optional, any, None)
      Network object group (Source network object group name)


    src_port_end (optional, any, None)
      Ending Port Number


    icmp_code (optional, any, None)
      ICMP code number


    dst_range (optional, any, None)
      Match only packets in the range of port numbers (Starting Destination Port Number)


    src_host (optional, any, None)
      A single source host (Host address)


    extd_remark (optional, any, None)
      Access list entry comment (Notes for this ACL)


    vlan (optional, any, None)
      VLAN ID


    dscp (optional, any, None)
      DSCP


    dst_gt (optional, any, None)
      Match only packets with a greater port number


    dst_object_group (optional, any, None)
      Destination network object group name


    trunk (optional, any, None)
      Ethernet trunk (trunk number)


    icmp (optional, any, None)
      Internet Control Message Protocol


    dst_mask (optional, any, None)
      Destination Mask 0=apply 255=ignore


    dst_any (optional, any, None)
      Any destination host


    src_lt (optional, any, None)
      Match only packets with a lower port number


    acl_log (optional, any, None)
      Log matches against this entry


    src_subnet (optional, any, None)
      Source Address


    dst_eq (optional, any, None)
      Match only packets on a given destination port (port number)


    src_any (optional, any, None)
      Any source host


    dst_host (optional, any, None)
      A single destination host (Host address)


    ethernet (optional, any, None)
      Ethernet interface (Port number)


    special_code (optional, any, None)
      'frag-required'= Code 4, fragmentation required; 'host-unreachable'= Code 1, destination host unreachable; 'network-unreachable'= Code 0, destination network unreachable; 'port-unreachable'= Code 3, destination port unreachable; 'proto-unreachable'= Code 2, destination protocol unreachable; 'route-failed'= Code 5, source route failed;


    transparent_session_only (optional, any, None)
      Only log transparent sessions


    any_type (optional, any, None)
      Any ICMP type



  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  extd (True, any, None)
    IP extended access list


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

