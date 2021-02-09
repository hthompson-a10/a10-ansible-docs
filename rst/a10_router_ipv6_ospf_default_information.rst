.. _a10_router_ipv6_ospf_default_information_module:


a10_router_ipv6_ospf_default_information -- Configures A10 router.ipv6.ospf.default-information
===============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Control distribution of default information






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  route_map (False, any, None)
    Route map reference (Pointer to route-map entries)


  metric (False, any, None)
    OSPF default metric (OSPF metric)


  originate (False, any, None)
    Distribute a default route


  ansible_password (True, any, None)
    Password for AXAPI authentication


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  always (False, any, None)
    Always advertise default route


  metric_type (False, any, None)
    OSPF metric type for default routes


  ospf_process_id (optional, any, None)
    Key to identify parent object


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

