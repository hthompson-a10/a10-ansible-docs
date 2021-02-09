.. _a10_snmp_server_enable_traps_system_module:


a10_snmp_server_enable_traps_system -- Configures A10 snmp.server.enable.traps.system
=====================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Enable system group traps






Parameters
----------

  smp_resource_event (False, any, None)
    Enable system smp resource event trap


  sec_disk (False, any, None)
    Enable system secondary hard disk trap


  all (False, any, None)
    Enable all system group traps


  low_temp (False, any, None)
    Enable system low temperature trap


  high_memory_use (False, any, None)
    Enable system high memory usage trap


  power (False, any, None)
    Enable system power supply trap


  ansible_username (True, any, None)
    Username for AXAPI authentication


  high_temp (False, any, None)
    Enable system high temperature trap


  tacacs_server_up_down (False, any, None)
    Enable system TACACS monitor server up/down trap


  file_sys_read_only (False, any, None)
    Enable file system read-only trap


  fan (False, any, None)
    Enable system fan trap


  shutdown (False, any, None)
    Enable system shutdown trap


  control_cpu_high (False, any, None)
    Enable control CPU usage high trap


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  syslog_severity_one (False, any, None)
    Enable system syslog severity one messages trap


  restart (False, any, None)
    Enable system restart trap


  packet_drop (False, any, None)
    Enable system packet dropped trap


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  license_management (False, any, None)
    Enable system license management traps


  high_disk_use (False, any, None)
    Enable system high disk usage trap


  ansible_host (True, any, None)
    Host for AXAPI authentication


  start (False, any, None)
    Enable system start trap


  state (True, any, None)
    State of the object to be created.


  data_cpu_high (False, any, None)
    Enable data CPU usage high trap


  pri_disk (False, any, None)
    Enable system primary hard disk trap


  ansible_password (True, any, None)
    Password for AXAPI authentication









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

