.. _a10_cgnv6_map_encapsulation_domain_basic_mapping_rule_prefix_rule_module:


a10_cgnv6_map_encapsulation_domain_basic_mapping_rule_prefix_rule -- Configures A10 cgnv6.map.encapsulation.domain.basic.mapping.rule.prefix-rule
=================================================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

IPv6 and IPv4 prefix rules






Parameters
----------

  ipv4_address_port_settings (False, any, None)
    'prefix-addr'= Each CE is assigned an IPv4 prefix; 'single-addr'= Each CE is assigned an IPv4 address; 'shared-addr'= Each CE is assigned a shared IPv4 address;


  rule_ipv6_prefix (False, any, None)
    IPv6 prefix of BMR


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ea_length (False, any, None)
    Length of Embedded Address (EA) bits


  ipv4_netmask (False, any, None)
    Subnet mask (subnet bigger than /8 is not allowed)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  port_start (False, any, None)
    Starting Port, Must be Power of 2 value


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    MAP BMR prefix rule name


  user_tag (False, any, None)
    Customized tag


  domain_name (optional, any, None)
    Key to identify parent object


  state (True, any, None)
    State of the object to be created.


  share_ratio (False, any, None)
    Port sharing ratio for each NAT IP. Must be Power of 2 value


  rule_ipv4_prefix (False, any, None)
    IPv4 prefix of BMR


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

