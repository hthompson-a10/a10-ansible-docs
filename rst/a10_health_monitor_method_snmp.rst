.. _a10_health_monitor_method_snmp_module:


a10_health_monitor_method_snmp -- Configures A10 health.monitor.method.snmp
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

SNMP type






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  snmp_port (False, any, None)
    Specify SNMP port, default is 161 (Port Number)


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  monitor_name (optional, any, None)
    Key to identify parent object


  oid (False, any, None)
    Field oid


    mib (optional, any, None)
      'sysDescr'= The MIB-2 OID of system description, 1.1.0; 'sysUpTime'= The MIB-2 OID of system up time, 1.3.0; 'sysName'= The MIB-2 OID of system nume, 1.5.0;


    asn (optional, any, None)
      Specify the format in ASN.1 style



  snmp (False, any, None)
    SNMP type


  ansible_password (True, any, None)
    Password for AXAPI authentication


  community (False, any, None)
    Specify SNMP community, default is 'public' (Community String)


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  operation (False, any, None)
    Field operation


    oper_type (optional, any, None)
      'getnext'= Get-Next-Request command; 'get'= Get-Request command;



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

