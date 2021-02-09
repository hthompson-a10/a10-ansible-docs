.. _a10_cgnv6_nat_inside_source_static_module:


a10_cgnv6_nat_inside_source_static -- Configures A10 cgnv6.nat.inside.source.static
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Static Address Translations






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  partition (True, any, None)
    Inside User Partition (Partition Name)


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  src_address (True, any, None)
    Original Source Address


  ansible_password (True, any, None)
    Password for AXAPI authentication


  vrid (False, any, None)
    VRRP-A vrid (Specify ha VRRP-A vrid)


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  nat_address (False, any, None)
    NAT Address


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

