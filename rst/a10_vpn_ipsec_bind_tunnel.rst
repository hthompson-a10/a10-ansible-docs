.. _a10_vpn_ipsec_bind_tunnel_module:


a10_vpn_ipsec_bind_tunnel -- Configures A10 vpn.ipsec.bind-tunnel
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Binds tunnel interface to the IPsec connection






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  tunnel (False, any, None)
    Tunnel interface index


  next_hop_v6 (False, any, None)
    IPsec Next Hop IPv6 Address


  ipsec_name (optional, any, None)
    Key to identify parent object


  state (True, any, None)
    State of the object to be created.


  next_hop (False, any, None)
    IPsec Next Hop IP Address


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


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

