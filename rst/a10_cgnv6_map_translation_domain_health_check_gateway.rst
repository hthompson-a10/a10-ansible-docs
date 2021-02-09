.. _a10_cgnv6_map_translation_domain_health_check_gateway_module:


a10_cgnv6_map_translation_domain_health_check_gateway -- Configures A10 cgnv6.map.translation.domain.health-check-gateway
=========================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Health-check gateway for route withdrawn






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


  ipv6_address_list (False, any, None)
    Field ipv6_address_list


    ipv6_gateway (optional, any, None)
      IPv6 Gateway



  withdraw_route (False, any, None)
    'all-link-failure'= Withdraw routes on health-check failure of all IPv4 gateways or all IPv6 gateways; 'any-link-failure'= Withdraw routes on health- check failure of any gateway (default);


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


  address_list (False, any, None)
    Field address_list


    ipv4_gateway (optional, any, None)
      IPv4 Gateway










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

