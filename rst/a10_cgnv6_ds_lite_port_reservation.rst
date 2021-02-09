.. _a10_cgnv6_ds_lite_port_reservation_module:


a10_cgnv6_ds_lite_port_reservation -- Configures A10 cgnv6.ds.lite.port-reservation
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

DS-Lite Static Port Reservation






Parameters
----------

  nat_start_port (True, any, None)
    NAT Start Port


  ansible_username (True, any, None)
    Username for AXAPI authentication


  nat_end_port (True, any, None)
    NAT End Port


  inside_addr (True, any, None)
    Inside User IP address


  inside_end_port (True, any, None)
    Inside End Port


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ansible_port (True, any, None)
    Port for AXAPI authentication


  inside_start_port (True, any, None)
    Inside Start Port


  uuid (False, any, None)
    uuid of the object


  tunnel_dest_address (True, any, None)
    DS-Lite Inside User's Tunnel Destination IPv6 Address


  inside (True, any, None)
    Inside User Address and Port Range (DS-Lite Inside User's Tunnel Source IPv6 Address)


  state (True, any, None)
    State of the object to be created.


  nat (True, any, None)
    NAT Port Range (NAT IP address)


  ansible_password (True, any, None)
    Password for AXAPI authentication









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

