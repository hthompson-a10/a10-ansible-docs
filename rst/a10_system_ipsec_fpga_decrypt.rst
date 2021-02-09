.. _a10_system_ipsec_fpga_decrypt_module:


a10_system_ipsec_fpga_decrypt -- Configures A10 system.ipsec.fpga-decrypt
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Enable or disable FPGA decryption offload






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  action (False, any, None)
    'enable'= Enable FPGA decryption offload; 'disable'= Disable FPGA decryption offload;


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

