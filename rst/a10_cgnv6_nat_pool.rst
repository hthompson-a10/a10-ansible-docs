.. _a10_cgnv6_nat_pool_module:


a10_cgnv6_nat_pool -- Configures A10 cgnv6.nat.pool
===================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure CGNv6 NAT pool






Parameters
----------

  oper (False, any, None)
    Field oper


    nat_ip_list (optional, any, None)
      Field nat_ip_list


    pool_name (optional, any, None)
      Specify pool name or pool group



  pool_name (True, any, None)
    Specify pool name or pool group


  all (False, any, None)
    Share with all partitions


  usable_nat_ports_end (False, any, None)
    End Port of Usable NAT Ports


  ansible_username (True, any, None)
    Username for AXAPI authentication


  exclude_ip (False, any, None)
    Field exclude_ip


    exclude_ip_start (optional, any, None)
      Single IP address or IP address range start


    exclude_ip_end (optional, any, None)
      Address range end



  start_address (False, any, None)
    Configure start IP address of NAT pool


  netmask (False, any, None)
    Configure mask for pool


  usable_nat_ports (False, any, None)
    Configure usable NAT ports


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  max_users_per_ip (False, any, None)
    Number of users that can be assigned to a NAT IP


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    pool_name (optional, any, None)
      Specify pool name or pool group


    udp (optional, any, None)
      UDP


    users (optional, any, None)
      Users


    tcp_freed (optional, any, None)
      TCP Freed


    udp_peak (optional, any, None)
      UDP Peak


    tcp (optional, any, None)
      TCP


    tcp_rsvd (optional, any, None)
      TCP Reserved


    tcp_peak (optional, any, None)
      TCP Peak


    icmp_total (optional, any, None)
      ICMP Total


    ip_total (optional, any, None)
      IP Total


    udp_freed (optional, any, None)
      UDP Freed


    udp_total (optional, any, None)
      UDP Total


    icmp_rsvd (optional, any, None)
      ICMP Reserved


    ip_used (optional, any, None)
      IP Used


    icmp_hit_full (optional, any, None)
      ICMP Hit Full


    icmp (optional, any, None)
      ICMP


    ip_free (optional, any, None)
      IP Free


    tcp_hit_full (optional, any, None)
      TCP Hit Full


    tcp_total (optional, any, None)
      TCP total


    udp_rsvd (optional, any, None)
      UDP Reserved


    udp_hit_full (optional, any, None)
      UDP Hit Full


    icmp_freed (optional, any, None)
      ICMP Freed


    icmp_peak (optional, any, None)
      ICMP Peak



  group (False, any, None)
    Share with a partition group (Partition Group Name)


  tcp_time_wait_interval (False, any, None)
    Minutes before TCP NAT ports can be reused


  port_batch_v2_size (False, any, None)
    '64'= Allocate 64 ports at a time; '128'= Allocate 128 ports at a time; '256'= Allocate 256 ports at a time; '512'= Allocate 512 ports at a time; '1024'= Allocate 1024 ports at a time; '2048'= Allocate 2048 ports at a time; '4096'= Allocate 4096 ports at a time;


  end_address (False, any, None)
    Configure end IP address of NAT pool


  vrid (False, any, None)
    Configure VRRP-A vrid (Specify ha VRRP-A vrid)


  state (True, any, None)
    State of the object to be created.


  simultaneous_batch_allocation (False, any, None)
    Allocate same TCP and UDP batches at once


  partition (False, any, None)
    Share with a single partition (Partition Name)


  per_batch_port_usage_warning_threshold (False, any, None)
    Configure warning log threshold for per batch port usage (default= disabled) (Number of ports)


  usable_nat_ports_start (False, any, None)
    Start Port of Usable NAT Ports (needs to be even)


  shared (False, any, None)
    Share this pool with other partitions (default= not shared)


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

