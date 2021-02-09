.. _a10_ip_nat_range_list_module:


a10_ip_nat_range_list -- Configures A10 ip.nat.range-list
=========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

IP Source NAT Static range list






Parameters
----------

  v4_count (False, any, None)
    Number of addresses to be translated in this range


  local_netmaskv4 (False, any, None)
    Mask for this Address range


  ansible_username (True, any, None)
    Username for AXAPI authentication


  local_start_ipv4_addr (False, any, None)
    Local Start IPv4 Address of this list


  local_start_ipv6_addr (False, any, None)
    Local Start IPv6 Address of this list


  v6_acl_name (False, any, None)
    Access list name


  global_start_ipv4_addr (False, any, None)
    Global Start IPv4 Address of this list


  v6_vrid (False, any, None)
    VRRP-A vrid (Specify ha VRRP-A vrid)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  global_start_ipv6_addr (False, any, None)
    Global Start IPv6 Address of this list


  ansible_host (True, any, None)
    Host for AXAPI authentication


  name (True, any, None)
    Name for this Static List


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  v6_count (False, any, None)
    Number of addresses to be translated in this range


  a10_partition (False, any, None)
    Destination/target partition for object/command


  v4_acl_name (False, any, None)
    Access list name


  v4_vrid (False, any, None)
    VRRP-A vrid (Specify ha VRRP-A vrid)


  v4_acl_id (False, any, None)
    Access list ID


  state (True, any, None)
    State of the object to be created.


  global_netmaskv4 (False, any, None)
    Mask for this Address range


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

