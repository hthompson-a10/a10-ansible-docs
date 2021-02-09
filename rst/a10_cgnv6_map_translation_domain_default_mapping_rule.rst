.. _a10_cgnv6_map_translation_domain_default_mapping_rule_module:


a10_cgnv6_map_translation_domain_default_mapping_rule -- Configures A10 cgnv6.map.translation.domain.default-mapping-rule
=========================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Default mapping rule (DMR)






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  rule_ipv6_prefix (False, any, None)
    Rule IPv6 prefix


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  domain_name (optional, any, None)
    Key to identify parent object


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

