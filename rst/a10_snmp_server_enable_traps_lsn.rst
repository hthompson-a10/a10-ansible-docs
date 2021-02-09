.. _a10_snmp_server_enable_traps_lsn_module:


a10_snmp_server_enable_traps_lsn -- Configures A10 snmp.server.enable.traps.lsn
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Enable LSN group traps






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  max_port_threshold (False, any, None)
    Maximum threshold


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  per_ip_port_usage_threshold (False, any, None)
    Enable LSN trap when IP total port usage reaches the threshold (default 64512)


  total_port_usage_threshold (False, any, None)
    Enable LSN trap when NAT total port usage reaches the threshold (default 655350000)


  fixed_nat_port_mapping_file_change (False, any, None)
    Enable LSN trap when fixed nat port mapping file change


  state (True, any, None)
    State of the object to be created.


  all (False, any, None)
    Enable all LSN group traps


  max_ipport_threshold (False, any, None)
    Maximum threshold


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  traffic_exceeded (False, any, None)
    Enable LSN trap when NAT pool reaches the threshold


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

