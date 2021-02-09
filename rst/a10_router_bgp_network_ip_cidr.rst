.. _a10_router_bgp_network_ip_cidr_module:


a10_router_bgp_network_ip_cidr -- Configures A10 router.bgp.network.ip-cidr
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Specify a ip network to announce via BGP






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  description (False, any, None)
    Network specific description (Up to 80 characters describing this network)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  route_map (False, any, None)
    Route-map to modify the attributes (Name of the route map)


  bgp_as_number (optional, any, None)
    Key to identify parent object


  network_ipv4_cidr (True, any, None)
    Specify network mask


  ansible_password (True, any, None)
    Password for AXAPI authentication


  backdoor (False, any, None)
    Specify a BGP backdoor route


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  comm_value (False, any, None)
    community value in the format 1-4294967295|AA=NN|internet|local-AS|no- advertise|no-export


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

