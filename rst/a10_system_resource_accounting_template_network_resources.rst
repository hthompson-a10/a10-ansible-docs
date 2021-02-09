.. _a10_system_resource_accounting_template_network_resources_module:


a10_system_resource_accounting_template_network_resources -- Configures A10 system.resource.accounting.template.network-resources
=================================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Enter the network resource limits






Parameters
----------

  object_group_cfg (False, any, None)
    Field object_group_cfg


    object_group_min_guarantee (optional, any, None)
      Minimum guaranteed value ( Minimum guaranteed value)


    object_group_max (optional, any, None)
      Enter the number of object groups allowed (Object group (default is max-value))



  ansible_username (True, any, None)
    Username for AXAPI authentication


  template_name (optional, any, None)
    Key to identify parent object


  static_ipv4_route_cfg (False, any, None)
    Field static_ipv4_route_cfg


    static_ipv4_route_max (optional, any, None)
      Enter the number of static ipv4 routes allowed (Static ipv4 routes (default is max-value))


    static_ipv4_route_min_guarantee (optional, any, None)
      Minimum guaranteed value ( Minimum guaranteed value)



  static_arp_cfg (False, any, None)
    Field static_arp_cfg


    static_arp_max (optional, any, None)
      Enter the number of static arp entries allowed (Static arp (default is max- value))


    static_arp_min_guarantee (optional, any, None)
      Minimum guaranteed value ( Minimum guaranteed value)



  ipv4_acl_line_cfg (False, any, None)
    Field ipv4_acl_line_cfg


    ipv4_acl_line_max (optional, any, None)
      Enter the number of ACL lines allowed (IPV4 ACL lines (default is max-value))


    ipv4_acl_line_min_guarantee (optional, any, None)
      Minimum guaranteed value ( Minimum guaranteed value)



  object_group_clause_cfg (False, any, None)
    Field object_group_clause_cfg


    object_group_clause_max (optional, any, None)
      Enter the number of object group clauses allowed (Object group clauses (default is max-value))


    object_group_clause_min_guarantee (optional, any, None)
      Minimum guaranteed value ( Minimum guaranteed value)



  threshold (False, any, None)
    Enter the threshold as a percentage (Threshold in percentage(default is 100%))


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  static_neighbor_cfg (False, any, None)
    Field static_neighbor_cfg


    static_neighbor_max (optional, any, None)
      Enter the number of static neighbor entries allowed (Static neighbors (default is max-value))


    static_neighbor_min_guarantee (optional, any, None)
      Minimum guaranteed value ( Minimum guaranteed value)



  ipv6_acl_line_cfg (False, any, None)
    Field ipv6_acl_line_cfg


    ipv6_acl_line_max (optional, any, None)
      Enter the number of ACL lines allowed (IPV6 ACL lines (default is max-value))


    ipv6_acl_line_min_guarantee (optional, any, None)
      Minimum guaranteed value ( Minimum guaranteed value)



  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  static_ipv6_route_cfg (False, any, None)
    Field static_ipv6_route_cfg


    static_ipv6_route_min_guarantee (optional, any, None)
      Minimum guaranteed value ( Minimum guaranteed value)


    static_ipv6_route_max (optional, any, None)
      Enter the number of static ipv6 routes allowed (Static ipv6 routes (default is max-value))



  static_mac_cfg (False, any, None)
    Field static_mac_cfg


    static_mac_min_guarantee (optional, any, None)
      Minimum guaranteed value ( Minimum guaranteed value)


    static_mac_max (optional, any, None)
      Enter the number of static MAC entries allowed (Static MACs (default is max- value))



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

