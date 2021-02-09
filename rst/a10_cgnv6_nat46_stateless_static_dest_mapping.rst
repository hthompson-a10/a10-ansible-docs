.. _a10_cgnv6_nat46_stateless_static_dest_mapping_module:


a10_cgnv6_nat46_stateless_static_dest_mapping -- Configures A10 cgnv6.nat46.stateless.static-dest-mapping
=========================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Stateless NAT46 mapping (IPv4 <-> IPv6)






Parameters
----------

  count (False, any, None)
    Set number of consecutive mappings (Number of mappings)


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  vrid (False, any, None)
    VRRP-A vrid (Specify ha VRRP-A vrid)


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  to_shared (False, any, None)
    Send NATed traffic through shared partition


  v6_address (True, any, None)
    IPv6 address


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  shared (False, any, None)
    Share/Expose this mapping with other partitions


  a10_partition (False, any, None)
    Destination/target partition for object/command


  v4_address (True, any, None)
    IPv4 address









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

