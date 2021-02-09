.. _a10_cgnv6_lsn_port_reservation_module:


a10_cgnv6_lsn_port_reservation -- Configures A10 cgnv6.lsn.port-reservation
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Set Port Reservations






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  inside_port_end (True, any, None)
    Inside End Port


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  inside (True, any, None)
    Inside User Address and Port Range (Inside User IP address)


  nat_port_end (True, any, None)
    NAT End Port


  state (True, any, None)
    State of the object to be created.


  inside_port_start (True, any, None)
    Inside Start Port


  nat (True, any, None)
    NAT IP address


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  nat_port_start (True, any, None)
    NAT Start Port









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

