.. _a10_cgnv6_lw_4o6_binding_table_tunnel_address_module:


a10_cgnv6_lw_4o6_binding_table_tunnel_address -- Configures A10 cgnv6.lw.4o6.binding.table.tunnel-address
=========================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Tunnel IPv6 Endpoint Address






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  nat_address_list (False, any, None)
    Field nat_address_list


    ipv4_nat_addr (optional, any, None)
      NAT IPv4 Address


    user_tag (optional, any, None)
      Customized tag


    port_range_list (optional, any, None)
      Field port_range_list



  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  binding_table_name (optional, any, None)
    Key to identify parent object


  ipv6_tunnel_addr (True, any, None)
    Tunnel IPv6 Endpoint Address


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


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

