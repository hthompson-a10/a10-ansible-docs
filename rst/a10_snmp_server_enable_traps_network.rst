.. _a10_snmp_server_enable_traps_network_module:


a10_snmp_server_enable_traps_network -- Configures A10 snmp.server.enable.traps.network
=======================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Enable network group traps






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


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  trunk_port_threshold (False, any, None)
    Enable network trunk-port-threshold trap


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

