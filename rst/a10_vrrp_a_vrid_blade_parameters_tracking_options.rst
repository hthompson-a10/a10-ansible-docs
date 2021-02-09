.. _a10_vrrp_a_vrid_blade_parameters_tracking_options_module:


a10_vrrp_a_vrid_blade_parameters_tracking_options -- Configures A10 vrrp.a.vrid.blade.parameters.tracking-options
=================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

VRRP-A tracking






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  trunk_cfg (False, any, None)
    Field trunk_cfg


    trunk (optional, any, None)
      trunk tracking (Trunk Number)


    priority_cost (optional, any, None)
      The amount the priority will decrease


    per_port_pri (optional, any, None)
      per port priority



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  route (False, any, None)
    Field route


    ipv6_destination_cfg (optional, any, None)
      Field ipv6_destination_cfg


    ip_destination_cfg (optional, any, None)
      Field ip_destination_cfg



  vrid_val (optional, any, None)
    Key to identify parent object


  ansible_host (True, any, None)
    Host for AXAPI authentication


  bgp (False, any, None)
    Field bgp


    bgp_ipv6_address_cfg (optional, any, None)
      Field bgp_ipv6_address_cfg


    bgp_ipv4_address_cfg (optional, any, None)
      Field bgp_ipv4_address_cfg



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  interface (False, any, None)
    Field interface


    ethernet (optional, any, None)
      Ethernet Interface (Ethernet interface number)


    priority_cost (optional, any, None)
      The amount the priority will decrease



  vlan_cfg (False, any, None)
    Field vlan_cfg


    vlan (optional, any, None)
      VLAN tracking (VLAN id)


    priority_cost (optional, any, None)
      The amount the priority will decrease


    timeout (optional, any, None)
      Field timeout



  a10_partition (False, any, None)
    Destination/target partition for object/command


  gateway (False, any, None)
    Field gateway


    ipv4_gateway_list (optional, any, None)
      Field ipv4_gateway_list


    ipv6_gateway_list (optional, any, None)
      Field ipv6_gateway_list










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

