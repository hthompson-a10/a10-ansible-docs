.. _a10_ipv6_nat_pool_module:


a10_ipv6_nat_pool -- Configures A10 ipv6.nat.pool
=================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

IPv6 pool name






Parameters
----------

  oper (False, any, None)
    Field oper


    pool_name (optional, any, None)
      Specify pool name


    nat_pool_addr_list (optional, any, None)
      Field nat_pool_addr_list



  pool_name (True, any, None)
    Specify pool name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  scaleout_device_id (False, any, None)
    Configure Scaleout device id to which this NAT pool is to be bound (Specify Scaleout device id)


  start_address (False, any, None)
    Configure start IP address of NAT pool


  netmask (False, any, None)
    Configure mask for pool


  port_overload (False, any, None)
    Nat Pool Port overload


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  gateway (False, any, None)
    Configure gateway IP


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'Port-Usage'= Port-Usage; 'Total-Used'= Total-Used; 'Total-Freed'= Total-Freed; 'Failed'= Failed;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    Total_Used (optional, any, None)
      Field Total_Used


    Failed (optional, any, None)
      Field Failed


    Total_Freed (optional, any, None)
      Field Total_Freed


    Port_Usage (optional, any, None)
      Field Port_Usage


    pool_name (optional, any, None)
      Specify pool name



  uuid (False, any, None)
    uuid of the object


  end_address (False, any, None)
    Configure end IP address of NAT pool


  vrid (False, any, None)
    Specify VRRP-A vrid (Specify ha VRRP-A vrid)


  ip_rr (False, any, None)
    Use IP address round-robin behavior


  state (True, any, None)
    State of the object to be created.


  ansible_host (True, any, None)
    Host for AXAPI authentication


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

