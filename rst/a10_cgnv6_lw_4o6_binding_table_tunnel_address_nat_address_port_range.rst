.. _a10_cgnv6_lw_4o6_binding_table_tunnel_address_nat_address_port_range_module:


a10_cgnv6_lw_4o6_binding_table_tunnel_address_nat_address_port_range -- Configures A10 cgnv6.lw.4o6.binding.table.tunnel.address.nat.address.port-range
=======================================================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Single Port or Port Range Start






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  port_end (True, any, None)
    Port Range End


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  binding_table_name (optional, any, None)
    Key to identify parent object


  tunnel_endpoint_address (True, any, None)
    Configure LW-4over6 IPIP Tunnel Endpoint Address (LW-4over6 Tunnel Endpoint Address)


  nat_address_ipv4_nat_addr (optional, any, None)
    Key to identify parent object


  state (True, any, None)
    State of the object to be created.


  tunnel_address_ipv6_tunnel_addr (optional, any, None)
    Key to identify parent object


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  port_start (True, any, None)
    Single Port or Port Range Start


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

