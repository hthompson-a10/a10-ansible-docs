.. _a10_system_ipsec_module:


a10_system_ipsec -- Configures A10 system.ipsec
===============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure Crypto Cores for IPsec processing






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


  crypto_mem (False, any, None)
    Crypto memory percentage assigned for IPsec processing (rounded to increments of 10)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  crypto_core (False, any, None)
    Crypto cores assigned for IPsec processing


  packet_round_robin (False, any, None)
    Enable packet round robin for IPsec packets


  fpga_decrypt (False, any, None)
    Field fpga_decrypt


    action (optional, any, None)
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

