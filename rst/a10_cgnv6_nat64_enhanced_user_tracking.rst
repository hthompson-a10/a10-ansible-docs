.. _a10_cgnv6_nat64_enhanced_user_tracking_module:


a10_cgnv6_nat64_enhanced_user_tracking -- Configures A10 cgnv6.nat64.enhanced-user-tracking
===========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

NAT64 Enhanced User Data






Parameters
----------

  oper (False, any, None)
    Field oper


    user_count (optional, any, None)
      Field user_count


    shared_partition (optional, any, None)
      Field shared_partition


    nat_pool_name (optional, any, None)
      Field nat_pool_name


    prefix_filter (optional, any, None)
      Field prefix_filter


    inside_addr_v6 (optional, any, None)
      Field inside_addr_v6


    all_partitions (optional, any, None)
      Field all_partitions


    user_list (optional, any, None)
      Field user_list


    partition_name (optional, any, None)
      Field partition_name


    pool_shared (optional, any, None)
      Field pool_shared



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

