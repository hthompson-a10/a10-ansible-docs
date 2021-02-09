.. _a10_ipv6_nat_inside_source_list_module:


a10_ipv6_nat_inside_source_list -- Configures A10 ipv6.nat.inside.source.list
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

IPv6 Access-List






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  list_name (True, any, None)
    IPv6 access-list name


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  pool (False, any, None)
    IPv6 NAT Pool (Pool Name)









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

