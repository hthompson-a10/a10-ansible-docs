.. _a10_cgnv6_fixed_nat_full_cone_session_module:


a10_cgnv6_fixed_nat_full_cone_session -- Configures A10 cgnv6.fixed.nat.full-cone-session
=========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Full Cone Sessions for Fixed NAT






Parameters
----------

  oper (False, any, None)
    Field oper


    shared_partition (optional, any, None)
      Field shared_partition


    session_type (optional, any, None)
      Field session_type


    debug_session (optional, any, None)
      Field debug_session


    graceful (optional, any, None)
      Field graceful


    all_partitions (optional, any, None)
      Field all_partitions


    partition_name (optional, any, None)
      Field partition_name


    inside_port (optional, any, None)
      Field inside_port


    inside_addr_v6_start (optional, any, None)
      Field inside_addr_v6_start


    nat_addr_start (optional, any, None)
      Field nat_addr_start


    inside_addr (optional, any, None)
      Field inside_addr


    nat_addr (optional, any, None)
      Field nat_addr


    pcp (optional, any, None)
      Field pcp


    session_count (optional, any, None)
      Field session_count


    inside_addr_end (optional, any, None)
      Field inside_addr_end


    inside_addr_v6 (optional, any, None)
      Field inside_addr_v6


    nat_port (optional, any, None)
      Field nat_port


    inside_addr_v6_end (optional, any, None)
      Field inside_addr_v6_end


    session_list (optional, any, None)
      Field session_list


    inside_addr_start (optional, any, None)
      Field inside_addr_start


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

