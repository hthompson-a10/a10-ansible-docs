.. _a10_cgnv6_map_encapsulation_domain_basic_mapping_rule_module:


a10_cgnv6_map_encapsulation_domain_basic_mapping_rule -- Configures A10 cgnv6.map.encapsulation.domain.basic-mapping-rule
=========================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Basic mapping rule (BMR)






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  rule_ipv4_address_port_settings (False, any, None)
    'prefix-addr'= Each CE is assigned an IPv4 prefix; 'single-addr'= Each CE is assigned an IPv4 address; 'shared-addr'= Each CE is assigned a shared IPv4 address;


  ansible_password (True, any, None)
    Password for AXAPI authentication


  ea_length (False, any, None)
    Length of Embedded Address (EA) bits


  domain_name (optional, any, None)
    Key to identify parent object


  prefix_rule_list (False, any, None)
    Field prefix_rule_list


    ipv4_address_port_settings (optional, any, None)
      'prefix-addr'= Each CE is assigned an IPv4 prefix; 'single-addr'= Each CE is assigned an IPv4 address; 'shared-addr'= Each CE is assigned a shared IPv4 address;


    name (optional, any, None)
      MAP BMR prefix rule name


    ea_length (optional, any, None)
      Length of Embedded Address (EA) bits


    rule_ipv6_prefix (optional, any, None)
      IPv6 prefix of BMR


    ipv4_netmask (optional, any, None)
      Subnet mask (subnet bigger than /8 is not allowed)


    share_ratio (optional, any, None)
      Port sharing ratio for each NAT IP. Must be Power of 2 value


    port_start (optional, any, None)
      Starting Port, Must be Power of 2 value


    rule_ipv4_prefix (optional, any, None)
      IPv4 prefix of BMR


    user_tag (optional, any, None)
      Customized tag


    uuid (optional, any, None)
      uuid of the object



  state (True, any, None)
    State of the object to be created.


  share_ratio (False, any, None)
    Port sharing ratio for each NAT IP. Must be Power of 2 value


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  port_start (False, any, None)
    Starting Port, Must be Power of 2 value


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

