.. _a10_cgnv6_lsn_user_quota_session_module:


a10_cgnv6_lsn_user_quota_session -- Configures A10 cgnv6.lsn.user-quota-session
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

LSN Per User Statistics






Parameters
----------

  oper (False, any, None)
    Field oper


    session_list (optional, any, None)
      Field session_list


    shared_partition (optional, any, None)
      Field shared_partition


    nat_pool_name (optional, any, None)
      Field nat_pool_name


    top_by_icmp_usage (optional, any, None)
      Field top_by_icmp_usage


    nat_addr (optional, any, None)
      Field nat_addr


    session_count (optional, any, None)
      Field session_count


    top_by_all_usage (optional, any, None)
      Field top_by_all_usage


    pool_shared (optional, any, None)
      Field pool_shared


    inside_addr (optional, any, None)
      Field inside_addr


    top_count (optional, any, None)
      Field top_count


    top_by_tcp_usage (optional, any, None)
      Field top_by_tcp_usage


    all_partitions (optional, any, None)
      Field all_partitions


    partition_name (optional, any, None)
      Field partition_name


    top_by_udp_usage (optional, any, None)
      Field top_by_udp_usage



  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


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

