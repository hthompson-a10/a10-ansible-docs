.. _a10_overlay_tunnel_vtep_destination_ip_address_vni_module:


a10_overlay_tunnel_vtep_destination_ip_address_vni -- Configures A10 overlay-tunnel.vtep.destination.ip.address.vni
===================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Virtual Segment Id configured on the remote VTEP






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  vtep_id (optional, any, None)
    Key to identify parent object


  segment (True, any, None)
    VNI configured for the remote VTEP


  destination_ip_address_ip_address (optional, any, None)
    Key to identify parent object


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

