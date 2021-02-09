.. _a10_cgnv6_fixed_nat_inside_ipv6address_module:


a10_cgnv6_fixed_nat_inside_ipv6address -- Configures A10 cgnv6.fixed.nat.inside.ipv6address
===========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure Fixed NAT






Parameters
----------

  inside_end_address (True, any, None)
    IPv6 Inside User End Address


  inside_netmask (True, any, None)
    Inside User IPv6 Netmask


  partition (True, any, None)
    Inside User Partition (Partition Name)


  ports_per_user (False, any, None)
    Configure Ports per Inside User (ports-per-user)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  nat_start_address (False, any, None)
    Start NAT Address


  dest_rule_list (False, any, None)
    Bind destination based Rule-List (Fixed NAT Rule-List Name)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  usable_nat_ports (False, any, None)
    Field usable_nat_ports


    usable_end_port (optional, any, None)
      End Port of Usable NAT Ports


    usable_start_port (optional, any, None)
      Start Port of Usable NAT Ports



  offset (False, any, None)
    Field offset


    random (optional, any, None)
      Randomly choose the first NAT IP address


    numeric_offset (optional, any, None)
      Configure a numeric offset to the first NAT IP address



  session_quota (False, any, None)
    Configure per user quota on sessions


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  nat_netmask (False, any, None)
    NAT Addresses IP Netmask


  uuid (False, any, None)
    uuid of the object


  ansible_port (True, any, None)
    Port for AXAPI authentication


  dynamic_pool_size (False, any, None)
    Configure size of Dynamic pool (Default= 0)


  inside_start_address (True, any, None)
    IPv6 Inside User Start Address


  nat_ip_list (False, any, None)
    Name of IP List used to specify NAT addresses


  respond_to_user_mac (False, any, None)
    Use the user's source MAC for the next hop rather than the routing table (Default= off)


  vrid (False, any, None)
    VRRP-A vrid (Specify ha VRRP-A vrid)


  nat_end_address (False, any, None)
    IPv4 End NAT Address


  state (True, any, None)
    State of the object to be created.


  ansible_password (True, any, None)
    Password for AXAPI authentication


  method (False, any, None)
    'use-all-nat-ips'= Use all the NAT IP addresses configured; 'use-least-nat- ips'= Use the least number of NAT IP addresses required (default);









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

