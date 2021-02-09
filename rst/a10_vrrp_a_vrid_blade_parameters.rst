.. _a10_vrrp_a_vrid_blade_parameters_module:


a10_vrrp_a_vrid_blade_parameters -- Configures A10 vrrp.a.vrid.blade-parameters
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

blade parameters of VRRP-A vrid






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  tracking_options (False, any, None)
    Field tracking_options


    bgp (optional, any, None)
      Field bgp


    trunk_cfg (optional, any, None)
      Field trunk_cfg


    uuid (optional, any, None)
      uuid of the object


    interface (optional, any, None)
      Field interface


    vlan_cfg (optional, any, None)
      Field vlan_cfg


    route (optional, any, None)
      Field route


    gateway (optional, any, None)
      Field gateway



  vrid_val (optional, any, None)
    Key to identify parent object


  state (True, any, None)
    State of the object to be created.


  priority (False, any, None)
    VRRP-A priorty (Priority, default is 150)


  fail_over_policy_template (False, any, None)
    Apply a fail over policy template (VRRP-A fail over policy template name)


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

