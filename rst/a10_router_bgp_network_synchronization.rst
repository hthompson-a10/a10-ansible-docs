.. _a10_router_bgp_network_synchronization_module:


a10_router_bgp_network_synchronization -- Configures A10 router.bgp.network.synchronization
===========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

help Perform IGP synchronization






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  network_synchronization (False, any, None)
    Perform IGP synchronization


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  bgp_as_number (optional, any, None)
    Key to identify parent object


  state (True, any, None)
    State of the object to be created.


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

