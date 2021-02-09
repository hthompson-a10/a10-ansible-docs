.. _a10_partition_module:


a10_partition -- Configures A10 partition
=========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create/unload a Network partition






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    partition_name (optional, any, None)
      Object partition name



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  ansible_password (True, any, None)
    Password for AXAPI authentication


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  template (False, any, None)
    Field template


    resource_accounting (optional, any, None)
      Attach a resource accounting template (Name of the template)


    uuid (optional, any, None)
      uuid of the object



  application_type (False, any, None)
    'adc'= Application type ADC; 'cgnv6'= Application type CGNv6;


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  shared_vlan (False, any, None)
    Field shared_vlan


    allowable_ip_range (optional, any, None)
      Field allowable_ip_range


    vlan (optional, any, None)
      Field vlan


    mgmt_floating_ip_address (optional, any, None)
      IPv4 Address for Shared VLAN Mgmt IP Address


    uuid (optional, any, None)
      uuid of the object


    vrid (optional, any, None)
      Specify VRRP-A vrid


    allowable_ipv6_range (optional, any, None)
      Field allowable_ipv6_range



  a10_partition (False, any, None)
    Destination/target partition for object/command


  id (False, any, None)
    Specify unique Partition id


  partition_name (True, any, None)
    Object partition name









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

