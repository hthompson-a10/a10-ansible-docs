.. _a10_vrrp_a_force_self_standby_persistent_module:


a10_vrrp_a_force_self_standby_persistent -- Configures A10 vrrp-a.force-self-standby-persistent
===============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

HA VRRP-A Configured  Command to force the unit or a group to HA standby state






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


  vrid (True, any, None)
    Specify one VRRP-A vrid to force into standby state


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

