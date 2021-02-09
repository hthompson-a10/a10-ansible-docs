.. _a10_cgnv6_map_translation_domain_basic_mapping_rule_prefix_rule_module:


a10_cgnv6_map_translation_domain_basic_mapping_rule_prefix_rule -- Configures A10 cgnv6.map.translation.domain.basic.mapping.rule.prefix-rule
=============================================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

IPv6 and IPv4 prefix rules






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    MAP BMR prefix rule name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  domain_name (optional, any, None)
    Key to identify parent object


  rule_ipv6_prefix (False, any, None)
    IPv6 prefix of BMR


  state (True, any, None)
    State of the object to be created.


  ipv4_netmask (False, any, None)
    Subnet mask (subnet bigger than /8 is not allowed)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  rule_ipv4_prefix (False, any, None)
    IPv4 prefix of BMR


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


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

