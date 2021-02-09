.. _a10_system_platformtype_module:


a10_system_platformtype -- Configures A10 system.platformtype
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Field platformtype






Parameters
----------

  oper (False, any, None)
    Field oper


    platform_id (optional, any, None)
      Field platform_id


    platform_type (optional, any, None)
      Field platform_type


    platform_dpdk (optional, any, None)
      Field platform_dpdk


    platform_axv (optional, any, None)
      Field platform_axv


    platform_lxc (optional, any, None)
      Field platform_lxc


    platform_info (optional, any, None)
      Field platform_info



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

