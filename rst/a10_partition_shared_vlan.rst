.. _a10_partition_shared_vlan_module:


a10_partition_shared_vlan -- Configures A10 partition.shared-vlan
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Enable shared-vlan feature in Network partition






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  vlan (False, any, None)
    Field vlan


  mgmt_floating_ip_address (False, any, None)
    IPv4 Address for Shared VLAN Mgmt IP Address


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  vrid (False, any, None)
    Specify VRRP-A vrid


  allowable_ip_range (False, any, None)
    Field allowable_ip_range


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  allowable_ipv6_range (False, any, None)
    Field allowable_ipv6_range


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  partition_name (optional, any, None)
    Key to identify parent object


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

