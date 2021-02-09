.. _a10_cgnv6_resource_usage_module:


a10_cgnv6_resource_usage -- Configures A10 cgnv6.resource-usage
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure CGNV6 Resource Usage






Parameters
----------

  oper (False, any, None)
    Field oper


    lsn_nat_addr_count_max (optional, any, None)
      Field lsn_nat_addr_count_max


    fixed_nat_inside_user_count_min (optional, any, None)
      Field fixed_nat_inside_user_count_min


    fixed_nat_inside_user_count_default (optional, any, None)
      Field fixed_nat_inside_user_count_default


    lsn_nat_addr_count_default (optional, any, None)
      Field lsn_nat_addr_count_default


    radius_table_size_min (optional, any, None)
      Field radius_table_size_min


    fixed_nat_ip_addr_count_min (optional, any, None)
      Field fixed_nat_ip_addr_count_min


    radius_table_size_max (optional, any, None)
      Field radius_table_size_max


    fixed_nat_inside_user_count_max (optional, any, None)
      Field fixed_nat_inside_user_count_max


    fixed_nat_ip_addr_count_default (optional, any, None)
      Field fixed_nat_ip_addr_count_default


    fixed_nat_ip_addr_count_max (optional, any, None)
      Field fixed_nat_ip_addr_count_max


    lsn_nat_addr_count_min (optional, any, None)
      Field lsn_nat_addr_count_min


    radius_table_size_default (optional, any, None)
      Field radius_table_size_default



  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  radius_table_size (False, any, None)
    Total configurable CGNV6 RADIUS Table entries


  ansible_password (True, any, None)
    Password for AXAPI authentication


  stateless_entries (False, any, None)
    Field stateless_entries


    l4_session_count (optional, any, None)
      Helper size for CGN Stateless Technologies


    uuid (optional, any, None)
      uuid of the object



  state (True, any, None)
    State of the object to be created.


  fixed_nat_ip_addr_count (False, any, None)
    Total configurable CGNV6 Fixed NAT addresses


  fixed_nat_inside_user_count (False, any, None)
    Total configurable CGNV6 Fixed NAT inside users


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  lsn_nat_addr_count (False, any, None)
    Total configurable CGNV6 NAT Pool addresses


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

