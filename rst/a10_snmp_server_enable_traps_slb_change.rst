.. _a10_snmp_server_enable_traps_slb_change_module:


a10_snmp_server_enable_traps_slb_change -- Configures A10 snmp.server.enable.traps.slb-change
=============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Enable SLB change traps






Parameters
----------

  ssl_cert_expire (False, any, None)
    Enable SSL certificate expiring trap


  all (False, any, None)
    Enable all system group traps


  ssl_cert_change (False, any, None)
    Enable SSL certificate change trap


  ansible_username (True, any, None)
    Username for AXAPI authentication


  vip (False, any, None)
    Enable slb vip create/delete trap


  system_threshold (False, any, None)
    Enable slb system threshold trap


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  connection_resource_event (False, any, None)
    Enable system connection resource event trap


  resource_usage_warning (False, any, None)
    Enable partition resource usage warning trap


  server (False, any, None)
    Enable slb server create/delete trap


  state (True, any, None)
    State of the object to be created.


  server_port (False, any, None)
    Enable slb server port create/delete trap


  ansible_password (True, any, None)
    Password for AXAPI authentication


  vip_port (False, any, None)
    Enable slb vip-port create/delete trap









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

