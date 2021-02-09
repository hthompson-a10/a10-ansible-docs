.. _a10_vrrp_a_interface_ethernet_module:


a10_vrrp_a_interface_ethernet -- Configures A10 vrrp-a.interface.ethernet
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

VRRP-A interface ethernet






Parameters
----------

  both (False, any, None)
    both a router and server interface


  ansible_port (True, any, None)
    Port for AXAPI authentication


  ethernet_val (True, any, None)
    Ethernet Interface


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  vlan (False, any, None)
    VLAN ID


  no_heartbeat (False, any, None)
    do not send out heartbeat packet from this interface


  user_tag (False, any, None)
    Customized tag


  router_interface (False, any, None)
    interface to upstream router


  state (True, any, None)
    State of the object to be created.


  server_interface (False, any, None)
    interface to real server


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


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

