.. _a10_ip_route_rib_module:


a10_ip_route_rib -- Configures A10 ip.route.rib
===============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Establish static routes






Parameters
----------

  ip_nexthop_lif (False, any, None)
    Field ip_nexthop_lif


    lif (optional, any, None)
      LIF Interface (Logical tunnel interface number)


    description_nexthop_lif (optional, any, None)
      Description for static route



  ansible_port (True, any, None)
    Port for AXAPI authentication


  ip_nexthop_ipv4 (False, any, None)
    Field ip_nexthop_ipv4


    description_nexthop_ip (optional, any, None)
      Description for static route


    ip_next_hop (optional, any, None)
      Forwarding router's address


    distance_nexthop_ip (optional, any, None)
      Distance value for this route



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  ip_mask (True, any, None)
    Destination prefix mask


  ip_nexthop_tunnel (False, any, None)
    Field ip_nexthop_tunnel


    tunnel (optional, any, None)
      Tunnel interface (Tunnel interface number)


    distance_nexthop_tunnel (optional, any, None)
      Distance value for this route


    ip_next_hop_tunnel (optional, any, None)
      Forwarding router's address


    description_nexthop_tunnel (optional, any, None)
      Description for static route



  ip_dest_addr (True, any, None)
    Destination prefix


  ip_nexthop_partition (False, any, None)
    Field ip_nexthop_partition


    description_nexthop_partition (optional, any, None)
      Description for static route


    partition_name (optional, any, None)
      Name of network partition


    vrid_num_in_partition (optional, any, None)
      Specify ha VRRP-A vrid


    description_partition_vrid (optional, any, None)
      Description for static route



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

