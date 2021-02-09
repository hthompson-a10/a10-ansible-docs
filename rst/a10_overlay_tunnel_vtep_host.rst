.. _a10_overlay_tunnel_vtep_host_module:


a10_overlay_tunnel_vtep_host -- Configures A10 overlay-tunnel.vtep.host
=======================================================================

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


  ip_addr (True, any, None)
    IPv4 address of the overlay host


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  vtep_id (optional, any, None)
    Key to identify parent object


  ansible_password (True, any, None)
    Password for AXAPI authentication


  overlay_mac_addr (True, any, None)
    MAC Address of the overlay host


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  destination_vtep (True, any, None)
    Configure the VTEP IP address (IPv4 address of the VTEP for the remote host)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  vni (True, any, None)
     Configure the segment id ( VNI of the remote host)









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

