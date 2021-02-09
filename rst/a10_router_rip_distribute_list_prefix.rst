.. _a10_router_rip_distribute_list_prefix_module:


a10_router_rip_distribute_list_prefix -- Configures A10 router.rip.distribute.list.prefix
=========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Filter prefixes in routing updates






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  prefix_cfg (False, any, None)
    Field prefix_cfg


    prefix_list_direction (optional, any, None)
      'in'= Filter incoming routing updates; 'out'= Filter outgoing routing updates;


    ve (optional, any, None)
      Virtual ethernet interface (Virtual ethernet interface number)


    loopback (optional, any, None)
      Loopback interface (Port number)


    tunnel (optional, any, None)
      Tunnel interface (Tunnel interface number)


    ethernet (optional, any, None)
      Ethernet interface (Port number)


    trunk (optional, any, None)
      Trunk interface (Trunk interface number)


    prefix_list (optional, any, None)
      Filter prefixes in routing updates (Name of a prefix list)



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


  uuid (False, any, None)
    uuid of the object









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

