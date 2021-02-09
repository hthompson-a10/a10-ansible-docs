.. _a10_cgnv6_one_to_one_pool_group_member_module:


a10_cgnv6_one_to_one_pool_group_member -- Configures A10 cgnv6.one.to.one.pool.group.member
===========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Add a CGNv6 one-to-one pool to this pool-group






Parameters
----------

  pool_group_pool_group_name (optional, any, None)
    Key to identify parent object


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  pool_name (True, any, None)
    Specify CGNv6 one-to-one pool name


  ansible_password (True, any, None)
    Password for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


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

