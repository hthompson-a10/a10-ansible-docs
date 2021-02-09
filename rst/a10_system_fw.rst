.. _a10_system_fw_module:


a10_system_fw -- Configures A10 system.fw
=========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure system parameters for firewall






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  application_flow (False, any, None)
    Number of flows


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  basic_dpi_enable (False, any, None)
    Enable basic dpi


  application_mempool (False, any, None)
    Enable application memory pool


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uuid (False, any, None)
    uuid of the object









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

