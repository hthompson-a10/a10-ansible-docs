.. _a10_cgnv6_one_to_one_pool_module:


a10_cgnv6_one_to_one_pool -- Configures A10 cgnv6.one.to.one.pool
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure CGNv6 one-to-one pool






Parameters
----------

  pool_name (True, any, None)
    Specify pool name or pool group


  vrid (False, any, None)
    Configure VRRP-A vrid (Specify ha VRRP-A vrid)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  start_address (False, any, None)
    Configure start IP address of NAT pool


  netmask (False, any, None)
    Configure mask for pool


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  stats (False, any, None)
    Field stats


    pool_name (optional, any, None)
      Specify pool name or pool group


    total_address (optional, any, None)
      Total Address


    used_address (optional, any, None)
      Used Address


    free_address (optional, any, None)
      Free Address



  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ansible_port (True, any, None)
    Port for AXAPI authentication


  group (False, any, None)
    Share with a partition group (Partition Group Name)


  uuid (False, any, None)
    uuid of the object


  end_address (False, any, None)
    Configure end IP address of NAT pool


  partition (False, any, None)
    Share with a single partition (Partition Name)


  state (True, any, None)
    State of the object to be created.


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

