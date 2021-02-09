.. _a10_cgnv6_lsn_system_status_module:


a10_cgnv6_lsn_system_status -- Configures A10 cgnv6.lsn.system-status
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Field system_status






Parameters
----------

  oper (False, any, None)
    Field oper


    tcp_nat_ports_free (optional, any, None)
      Field tcp_nat_ports_free


    lsn_cps (optional, any, None)
      Field lsn_cps


    udp_nat_ports_used (optional, any, None)
      Field udp_nat_ports_used


    tcp_nat_ports_used (optional, any, None)
      Field tcp_nat_ports_used


    data_sessions_free (optional, any, None)
      Field data_sessions_free


    smp_sessions_free (optional, any, None)
      Field smp_sessions_free


    radius_entries_used (optional, any, None)
      Field radius_entries_used


    data_sessions_used (optional, any, None)
      Field data_sessions_used


    smp_sessions_used (optional, any, None)
      Field smp_sessions_used


    radius_entries_free (optional, any, None)
      Field radius_entries_free


    udp_nat_ports_free (optional, any, None)
      Field udp_nat_ports_free



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

