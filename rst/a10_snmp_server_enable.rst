.. _a10_snmp_server_enable_module:


a10_snmp_server_enable -- Configures A10 snmp.server.enable
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Enable SNMP service






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  service (False, any, None)
    Enable SNMP service


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


  traps (False, any, None)
    Field traps


    lldp (optional, any, None)
      Enable lldp traps


    all (optional, any, None)
      Enable all SNMP traps


    uuid (optional, any, None)
      uuid of the object


    lsn (optional, any, None)
      Field lsn


    slb_change (optional, any, None)
      Field slb_change


    snmp (optional, any, None)
      Field snmp


    system (optional, any, None)
      Field system


    vrrp_a (optional, any, None)
      Field vrrp_a


    ssl (optional, any, None)
      Field ssl


    vcs (optional, any, None)
      Field vcs


    routing (optional, any, None)
      Field routing


    gslb (optional, any, None)
      Field gslb


    slb (optional, any, None)
      Field slb


    network (optional, any, None)
      Field network










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

