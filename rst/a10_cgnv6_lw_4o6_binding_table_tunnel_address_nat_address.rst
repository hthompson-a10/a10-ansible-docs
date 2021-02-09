.. _a10_cgnv6_lw_4o6_binding_table_tunnel_address_nat_address_module:


a10_cgnv6_lw_4o6_binding_table_tunnel_address_nat_address -- Configures A10 cgnv6.lw.4o6.binding.table.tunnel.address.nat-address
=================================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

NAT IPv4 address






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  binding_table_name (optional, any, None)
    Key to identify parent object


  ansible_password (True, any, None)
    Password for AXAPI authentication


  ansible_host (True, any, None)
    Host for AXAPI authentication


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  tunnel_address_ipv6_tunnel_addr (optional, any, None)
    Key to identify parent object


  ipv4_nat_addr (True, any, None)
    NAT IPv4 Address


  a10_partition (False, any, None)
    Destination/target partition for object/command


  port_range_list (False, any, None)
    Field port_range_list


    tunnel_endpoint_address (optional, any, None)
      Configure LW-4over6 IPIP Tunnel Endpoint Address (LW-4over6 Tunnel Endpoint Address)


    port_start (optional, any, None)
      Single Port or Port Range Start


    port_end (optional, any, None)
      Port Range End










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

