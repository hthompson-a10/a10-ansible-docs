.. _a10_vrrp_a_force_self_standby_module:


a10_vrrp_a_force_self_standby -- Configures A10 vrrp.a.force-self-standby
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

HA VRRP-A Operational Command to force the unit or a group to HA standby state






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  vrid (False, any, None)
    Specify one VRRP-A vrid to force into standby state


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  action (False, any, None)
    'enable'= enable vrrp-a force-self-standby; 'disable'= disable vrrp-a force- self-standby;


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  all_partitions (False, any, None)
    force all partitions in standby state









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

