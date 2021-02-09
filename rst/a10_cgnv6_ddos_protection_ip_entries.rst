.. _a10_cgnv6_ddos_protection_ip_entries_module:


a10_cgnv6_ddos_protection_ip_entries -- Configures A10 cgnv6.ddos.protection.ip-entries
=======================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Field ip_entries






Parameters
----------

  oper (False, any, None)
    Field oper


    nat_pool (optional, any, None)
      Field nat_pool


    v4_netmask (optional, any, None)
      Field v4_netmask


    total_entries (optional, any, None)
      Field total_entries


    ddos_ip_entries_list (optional, any, None)
      Field ddos_ip_entries_list


    all (optional, any, None)
      Field all



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

