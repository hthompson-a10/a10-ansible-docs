.. _a10_overlay_tunnel_vtep_destination_ip_address_module:


a10_overlay_tunnel_vtep_destination_ip_address -- Configures A10 overlay-tunnel.vtep.destination-ip-address
===========================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure remote tunnel end point parameters






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


  user_tag (False, any, None)
    Customized tag


  ansible_password (True, any, None)
    Password for AXAPI authentication


  ip_address (True, any, None)
    IP Address of the remote VTEP


  vni_list (False, any, None)
    Field vni_list


    segment (optional, any, None)
      VNI configured for the remote VTEP


    uuid (optional, any, None)
      uuid of the object



  state (True, any, None)
    State of the object to be created.


  encap (False, any, None)
    'nvgre'= Tunnel Encapsulation Type is NVGRE; 'vxlan'= Tunnel Encapsulation Type is VXLAN;


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

