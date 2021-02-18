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

+-----------------------------------+-------------------------------+-------------------------------------------------+
| Parameters                        | Choices/Defaults              | Comment                                         |
|                                   |                               |                                                 |
|                                   |                               |                                                 |
+===================================+===============================+=================================================+
| state                             | ['noop', 'present', 'absent'] | State of the object to be created.              |
|                                   |                               |                                                 |
| /required                         |                               |                                                 |
+-----------------------------------+-------------------------------+-------------------------------------------------+
| ansible_host                      |                               | Host for AXAPI authentication                   |
|                                   |                               |                                                 |
| /required                         |                               |                                                 |
+-----------------------------------+-------------------------------+-------------------------------------------------+
| ansible_username                  |                               | Username for AXAPI authentication               |
|                                   |                               |                                                 |
| /required                         |                               |                                                 |
+-----------------------------------+-------------------------------+-------------------------------------------------+
| ansible_password                  |                               | Password for AXAPI authentication               |
|                                   |                               |                                                 |
| /required                         |                               |                                                 |
+-----------------------------------+-------------------------------+-------------------------------------------------+
| ansible_port                      |                               | Port for AXAPI authentication                   |
|                                   |                               |                                                 |
| /required                         |                               |                                                 |
+-----------------------------------+-------------------------------+-------------------------------------------------+
| a10_device_context_id             | ['1-8']                       | Device ID for aVCS configuration                |
|                                   |                               |                                                 |
|                                   |                               |                                                 |
+-----------------------------------+-------------------------------+-------------------------------------------------+
| a10_partition                     |                               | Destination/target partition for object/command |
|                                   |                               |                                                 |
|                                   |                               |                                                 |
+-----------------------------------+-------------------------------+-------------------------------------------------+
| destination_ip_address_ip_address |                               | Key to identify parent object                   |
|                                   |                               |                                                 |
|                                   |                               |                                                 |
+-----------------------------------+-------------------------------+-------------------------------------------------+
| vtep_id                           |                               | Key to identify parent object                   |
|                                   |                               |                                                 |
|                                   |                               |                                                 |
+-----------------------------------+-------------------------------+-------------------------------------------------+
| segment                           |                               | VNI configured for the remote VTEP              |
|                                   |                               |                                                 |
| /required                         |                               |                                                 |
+-----------------------------------+-------------------------------+-------------------------------------------------+
| uuid                              |                               | uuid of the object                              |
|                                   |                               |                                                 |
|                                   |                               |                                                 |
+-----------------------------------+-------------------------------+-------------------------------------------------+







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

