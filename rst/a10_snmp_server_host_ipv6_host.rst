.. _a10_snmp_server_host_ipv6_host_module:


a10_snmp_server_host_ipv6_host -- Configures A10 snmp-server.host.ipv6-host
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Specify IPV6 hosts to receive SNMP traps






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


  ipv6_addr (True, any, None)
    IPV6 address of SNMP trap host


  udp_port (False, any, None)
    The trap host's UDP port number(default= 162)


  state (True, any, None)
    State of the object to be created.


  version (True, any, None)
    'v1'= Use SNMPv1; 'v2c'= Use SNMPv2c; 'v3'= User SNMPv3;


  user (False, any, None)
    SNMPv3 user to send traps (User Name)


  v1_v2c_comm (False, any, None)
    SNMPv1/v2c community string


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

