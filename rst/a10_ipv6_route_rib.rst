.. _a10_ipv6_route_rib_module:


a10_ipv6_route_rib -- Configures A10 ipv6.route.rib
===================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Establish static routes






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


  ipv6_nexthop_ipv6 (False, any, None)
    Field ipv6_nexthop_ipv6


    distance (optional, any, None)
      Distance value for this route


    ipv6_nexthop (optional, any, None)
      Forwarding router's address


    description (optional, any, None)
      Description for static route


    trunk (optional, any, None)
      Trunk interface (Trunk interface number)


    ethernet (optional, any, None)
      Ethernet interface (Ethernet interface number)


    ve (optional, any, None)
      Virtual Ethernet interface (Virtual Ethernet interface number)



  ipv6_address (True, any, None)
    IPV6 address


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  ipv6_nexthop_tunnel (False, any, None)
    Field ipv6_nexthop_tunnel


    tunnel (optional, any, None)
      Tunnel interface (Tunnel interface number)


    distance_nexthop_tunnel (optional, any, None)
      Distance value for this route


    ipv6_nexthop_tunnel_addr (optional, any, None)
      Forwarding router's address


    description (optional, any, None)
      Description for static route



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

