.. _a10_cgnv6_lw_4o6_binding_table_module:


a10_cgnv6_lw_4o6_binding_table -- Configures A10 cgnv6.lw.4o6.binding-table
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure LW-4over6 Binding Table






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    LW-4over6 Binding Table Name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  tunnel_address_list (False, any, None)
    Field tunnel_address_list


    ipv6_tunnel_addr (optional, any, None)
      Tunnel IPv6 Endpoint Address


    nat_address_list (optional, any, None)
      Field nat_address_list


    user_tag (optional, any, None)
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

