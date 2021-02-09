.. _a10_vrrp_a_fail_over_policy_template_module:


a10_vrrp_a_fail_over_policy_template -- Configures A10 vrrp-a.fail-over-policy-template
=======================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Define a VRRP-A failover policy template






Parameters
----------

  vlan_cfg (False, any, None)
    Field vlan_cfg


    vlan (optional, any, None)
      VLAN tracking (VLAN id)


    timeout (optional, any, None)
      Field timeout


    weight (optional, any, None)
      The failover event weight



  ansible_username (True, any, None)
    Username for AXAPI authentication


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  interface (False, any, None)
    Field interface


    ethernet (optional, any, None)
      Ethernet Interface (Ethernet interface number)


    weight (optional, any, None)
      The failover event weight



  a10_partition (False, any, None)
    Destination/target partition for object/command


  gateway (False, any, None)
    Field gateway


    gw_ipv6_address_cfg (optional, any, None)
      Field gw_ipv6_address_cfg


    gw_ipv4_address_cfg (optional, any, None)
      Field gw_ipv4_address_cfg



  uuid (False, any, None)
    uuid of the object


  ansible_port (True, any, None)
    Port for AXAPI authentication


  trunk_cfg (False, any, None)
    Field trunk_cfg


    per_port_weight (optional, any, None)
      Per port failover weight


    weight (optional, any, None)
      failover event weight


    trunk (optional, any, None)
      trunk tracking (trunk id)



  name (True, any, None)
    VRRP-A fail over policy template name


  ansible_password (True, any, None)
    Password for AXAPI authentication


  route (False, any, None)
    Field route


    ipv6_destination_cfg (optional, any, None)
      Field ipv6_destination_cfg


    ip_destination_cfg (optional, any, None)
      Field ip_destination_cfg



  ansible_host (True, any, None)
    Host for AXAPI authentication


  bgp (False, any, None)
    Field bgp


    bgp_ipv6_address_cfg (optional, any, None)
      Field bgp_ipv6_address_cfg


    bgp_ipv4_address_cfg (optional, any, None)
      Field bgp_ipv4_address_cfg



  state (True, any, None)
    State of the object to be created.


  user_tag (False, any, None)
    Customized tag









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

