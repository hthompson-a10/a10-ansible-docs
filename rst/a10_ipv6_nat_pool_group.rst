.. _a10_ipv6_nat_pool_group_module:


a10_ipv6_nat_pool_group -- Configures A10 ipv6.nat.pool-group
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

IPv6 pool group name






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  pool_group_name (True, any, None)
    Specify pool group name


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  vrid (False, any, None)
    Specify VRRP-A vrid (Specify ha VRRP-A vrid)


  ansible_password (True, any, None)
    Password for AXAPI authentication


  member_list (False, any, None)
    Field member_list


    pool_name (optional, any, None)
      Specify NAT pool name


    uuid (optional, any, None)
      uuid of the object



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

