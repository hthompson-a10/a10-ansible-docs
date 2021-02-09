.. _a10_snmp_server_disable_traps_module:


a10_snmp_server_disable_traps -- Configures A10 snmp.server.disable.traps
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Disable l3v partition SNMP traps






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  gslb (False, any, None)
    Disable all gslb traps on this partition


  slb_change (False, any, None)
    Disable all slb-change traps on this partition


  snmp (False, any, None)
    Disable all snmp traps on this partition


  all (False, any, None)
    Disable all traps on this partition


  vrrp_a (False, any, None)
    Disable all vrrp-a on this partition


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  slb (False, any, None)
    Disable all slb traps on this partition









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

