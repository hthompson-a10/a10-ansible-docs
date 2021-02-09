.. _a10_system_spe_status_module:


a10_system_spe_status -- Configures A10 system.spe-status
=========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Field spe_status






Parameters
----------

  oper (False, any, None)
    Field oper


    ipv4_allowed (optional, any, None)
      Field ipv4_allowed


    enable (optional, any, None)
      Field enable


    spe_profile (optional, any, None)
      Field spe_profile


    spe_setup_status (optional, any, None)
      Field spe_setup_status


    ipv6_allowed (optional, any, None)
      Field ipv6_allowed



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

