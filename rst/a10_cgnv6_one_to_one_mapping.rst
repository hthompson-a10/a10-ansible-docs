.. _a10_cgnv6_one_to_one_mapping_module:


a10_cgnv6_one_to_one_mapping -- Configures A10 cgnv6.one.to.one.mapping
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

One to One Mapping






Parameters
----------

  oper (False, any, None)
    Field oper


    pool_name (optional, any, None)
      Field pool_name


    shared_partition (optional, any, None)
      Field shared_partition


    nat_addr_start (optional, any, None)
      Field nat_addr_start


    shared_pool_name (optional, any, None)
      Field shared_pool_name


    inside_addr_start (optional, any, None)
      Field inside_addr_start


    session_mapping_list (optional, any, None)
      Field session_mapping_list


    inside_addr_end (optional, any, None)
      Field inside_addr_end


    inside_address_ipv6 (optional, any, None)
      Field inside_address_ipv6


    inside_address_ipv4 (optional, any, None)
      Field inside_address_ipv4


    nat_addr_val (optional, any, None)
      Field nat_addr_val


    total (optional, any, None)
      Field total


    all_partitions (optional, any, None)
      Field all_partitions


    partition_name (optional, any, None)
      Field partition_name


    nat_addr_end (optional, any, None)
      Field nat_addr_end



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

