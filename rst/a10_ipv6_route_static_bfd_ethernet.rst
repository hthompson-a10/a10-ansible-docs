.. _a10_ipv6_route_static_bfd_ethernet_module:


a10_ipv6_route_static_bfd_ethernet -- Configures A10 ipv6.route.static.bfd.ethernet
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Ethernet interface






Parameters
----------

  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  ansible_port (True, any, None)
    Port for AXAPI authentication


  eth_num (True, any, None)
    Ethernet (not a member of vlan or trunk)


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  threshold (False, any, None)
    action triggering threshold


  state (True, any, None)
    State of the object to be created.


  nexthop_ipv6_ll (True, any, None)
    Nexthop IPv6 address (Link-local)


  template (False, any, None)
    Configure tracking template (bind tracking template name)


  action (False, any, None)
    'down'= BFD down;  (BFD state)


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

