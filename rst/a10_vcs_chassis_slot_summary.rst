.. _a10_vcs_chassis_slot_summary_module:


a10_vcs_chassis_slot_summary -- Configures A10 vcs.chassis.slot-summary
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Chassis Summary Information






Parameters
----------

  oper (False, any, None)
    Field oper


    vmaster_maintenance_interval (optional, any, None)
      Field vmaster_maintenance_interval


    vcs_enabled (optional, any, None)
      Field vcs_enabled


    multicast_addr (optional, any, None)
      Field multicast_addr


    floating_ipv6_list (optional, any, None)
      Field floating_ipv6_list


    chassis_id (optional, any, None)
      Field chassis_id


    version (optional, any, None)
      Field version


    member_list (optional, any, None)
      Field member_list


    floating_ipv4_list (optional, any, None)
      Field floating_ipv4_list


    vmaster_maintenance_left (optional, any, None)
      Field vmaster_maintenance_left


    multicast_port (optional, any, None)
      Field multicast_port



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

