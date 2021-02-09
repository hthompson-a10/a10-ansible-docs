.. _a10_snmp_server_enable_traps_gslb_module:


a10_snmp_server_enable_traps_gslb -- Configures A10 snmp.server.enable.traps.gslb
=================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Enable GSLB group traps






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  group (False, any, None)
    Enable GSLB group related traps


  uuid (False, any, None)
    uuid of the object


  zone (False, any, None)
    Enable GSLB zone related traps


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  all (False, any, None)
    Enable all GSLB traps


  site (False, any, None)
    Enable GSLB site related traps


  state (True, any, None)
    State of the object to be created.


  service_ip (False, any, None)
    Enable GSLB service-ip related traps


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

