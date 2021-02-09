.. _a10_interface_trunk_ipv6_router_ospf_module:


a10_interface_trunk_ipv6_router_ospf -- Configures A10 interface.trunk.ipv6.router.ospf
=======================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Open Shortest Path First for IPv6 (OSPFv3)






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


  trunk_ifnum (optional, any, None)
    Key to identify parent object


  state (True, any, None)
    State of the object to be created.


  area_list (False, any, None)
    Field area_list


    instance_id (optional, any, None)
      Set the interface instance ID


    area_id_num (optional, any, None)
      OSPF area ID as a decimal value


    tag (optional, any, None)
      Set the OSPFv3 process tag


    area_id_addr (optional, any, None)
      OSPF area ID in IP address format



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

