.. _a10_object_group_network_module:


a10_object_group_network -- Configures A10 object-group.network
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure Network Object Group






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


    fw_ipv4_address (optional, any, None)
      IPv4 Network Address


    slb_vserver (optional, any, None)
      Virtual Server


    host_v4 (optional, any, None)
      IPv4 Host Address


    ipv6_subnet (optional, any, None)
      IPv6 Network Address


    rev_subnet_mask (optional, any, None)
      Network Mask. 0=apply, 255=ignore


    ipv6_range_end (optional, any, None)
      IPV6 Host address end


    any (optional, any, None)
      Any host


    subnet (optional, any, None)
      IPv4 Network Address


    ip_range_start (optional, any, None)
      IPv4 Host Address start


    ip_range_end (optional, any, None)
      IPV4 Host address end


    seq_num (optional, any, None)
      Sequence number


    fw_ipv6_subnet (optional, any, None)
      IPv6 Network Address


    host_v6 (optional, any, None)
      IPv6 Host Address


    ipv6_range_start (optional, any, None)
      IPv6 Host Address start


    slb_server (optional, any, None)
      Server


    obj_network (optional, any, None)
      Network Object



  user_tag (False, any, None)
    Customized tag


  ansible_password (True, any, None)
    Password for AXAPI authentication


  ansible_host (True, any, None)
    Host for AXAPI authentication


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  net_name (True, any, None)
    Network Object Group Name


  usage (False, any, None)
    'acl'= Use for access-lists (default).; 'fw'= Use for Firewall rule-set;


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ip_version (False, any, None)
    'v4'= IPv4 rule; 'v6'= IPv6 rule;


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

