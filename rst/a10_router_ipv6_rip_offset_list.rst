.. _a10_router_ipv6_rip_offset_list_module:


a10_router_ipv6_rip_offset_list -- Configures A10 router.ipv6.rip.offset-list
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Modify RIP metric






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  acl_cfg (False, any, None)
    Field acl_cfg


    ve (optional, any, None)
      Virtual ethernet interface (Virtual ethernet interface number)


    loopback (optional, any, None)
      Loopback interface (Port number)


    tunnel (optional, any, None)
      Tunnel interface (Tunnel interface number)


    metric (optional, any, None)
      Metric value


    acl (optional, any, None)
      Access-list name


    trunk (optional, any, None)
      Trunk interface (Trunk interface number)


    ethernet (optional, any, None)
      Ethernet interface (Port number)


    offset_list_direction (optional, any, None)
      'in'= Filter incoming updates; 'out'= Filter outgoing updates;



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

