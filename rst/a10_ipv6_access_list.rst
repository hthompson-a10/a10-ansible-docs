.. _a10_ipv6_access_list_module:


a10_ipv6_access_list -- Configures A10 ipv6.access-list
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure a IPv6 Access List






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    Named Access List


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


    udp (optional, any, None)
      protocol UDP


    tcp (optional, any, None)
      protocol TCP


    special_type (optional, any, None)
      'echo-reply'= Type 129, echo reply; 'echo-request'= help Type 128, echo request; 'packet-too-big'= Type 2, packet too big; 'param-prob'= Type 4, parameter problem; 'time-exceeded'= Type 3, time exceeded; 'dest-unreachable'= Type 1, destination unreachable;


    src_gt (optional, any, None)
      Match only packets with a greater port number


    icmp_type (optional, any, None)
      ICMP type number


    src_eq (optional, any, None)
      Match only packets on a given source port (port number)


    established (optional, any, None)
      TCP established


    src_range (optional, any, None)
      match only packets in the range of port numbers (Starting Port Number)


    dst_subnet (optional, any, None)
      Destination Address


    dst_lt (optional, any, None)
      Match only packets with a lesser port number


    geo_location (optional, any, None)
      Specify geo-location name


    ipv6 (optional, any, None)
      Any Internet Protocol


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


    remark (optional, any, None)
      Access list entry comment (Notes for this ACL)


    dst_any (optional, any, None)
      Any destination host


    seq_num (optional, any, None)
      Sequence Number


    acl_log (optional, any, None)
      Log matches against this entry


    src_lt (optional, any, None)
      Match only packets with a lower port number


    dst_eq (optional, any, None)
      Match only packets on a given destination port (port number)


    src_any (optional, any, None)
      Any source host


    dst_host (optional, any, None)
      A single destination host (Host address)


    action (optional, any, None)
      'deny'= Deny; 'permit'= Permit; 'l3-vlan-fwd-disable'= Disable L3 forwarding between VLANs;


    ethernet (optional, any, None)
      Ethernet interface (Port number)


    special_code (optional, any, None)
      'addr-unreachable'= Code 3, address unreachable; 'admin-prohibited'= Code 1, admin prohibited; 'no-route'= Code 0, no route to destination; 'not-neighbour'= Code 2, not neighbor; 'port-unreachable'= Code 4, destination port unreachable;


    src_subnet (optional, any, None)
      Source Address


    any_type (optional, any, None)
      Any ICMP type



  user_tag (False, any, None)
    Customized tag


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

