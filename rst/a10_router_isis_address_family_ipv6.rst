.. _a10_router_isis_address_family_ipv6_module:


a10_router_isis_address_family_ipv6 -- Configures A10 router.isis.address.family.ipv6
=====================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Address family






Parameters
----------

  isis_tag (optional, any, None)
    Key to identify parent object


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  default_information (False, any, None)
    'originate'= Distribute a default route;


  multi_topology_cfg (False, any, None)
    Field multi_topology_cfg


    transition (optional, any, None)
      Accept and generate both IS-IS IPv6 and Multi-topology IPV6 TLVs


    level_transition (optional, any, None)
      Accept and generate both IS-IS IPv6 and Multi-topology IPV6 TLVs


    multi_topology (optional, any, None)
      Enable multi-topology mode


    level (optional, any, None)
      'level-1'= Level-1 only; 'level-1-2'= Level-1-2; 'level-2'= Level-2 only;



  redistribute (False, any, None)
    Field redistribute


    vip_list (optional, any, None)
      Field vip_list


    isis (optional, any, None)
      Field isis


    redist_list (optional, any, None)
      Field redist_list


    uuid (optional, any, None)
      uuid of the object



  adjacency_check (False, any, None)
    Check ISIS neighbor protocol support


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  summary_prefix_list (False, any, None)
    Field summary_prefix_list


    prefix (optional, any, None)
      IPv6 prefix


    level (optional, any, None)
      'level-1'= Summarize into level-1 area; 'level-1-2'= Summarize into both area and sub-domain; 'level-2'= Summarize into level-2 sub-domain;



  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  distance (False, any, None)
    ISIS Administrative Distance (Distance value)









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

