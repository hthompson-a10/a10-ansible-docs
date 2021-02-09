.. _a10_overlay_tunnel_vtep_source_ip_address_vni_module:


a10_overlay_tunnel_vtep_source_ip_address_vni -- Configures A10 overlay-tunnel.vtep.source.ip.address.vni
=========================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

IP Address of the local tunnel end point






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


  vtep_id (optional, any, None)
    Key to identify parent object


  segment (True, any, None)
    Id of the segment that is being extended


  partition (False, any, None)
    Name of the Partition with the L2 segment being extended (Name of the User Partition with the L2 segment being extended)


  lif (False, any, None)
    Logical interface binding the Provider Partition to the User Partition (logical interface number)


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  gateway (False, any, None)
    This is a Gateway segment id









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

