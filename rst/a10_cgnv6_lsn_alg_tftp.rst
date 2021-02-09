.. _a10_cgnv6_lsn_alg_tftp_module:


a10_cgnv6_lsn_alg_tftp -- Configures A10 cgnv6.lsn.alg.tftp
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Change LSN TFTP ALG Settings






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'session-created'= TFTP Client Sessions Created; 'helper-created'= TFTP Helper Sessions created; 'helper-freed'= TFTP Helper Sessions freed; 'helper-freed-used'= TFTP Helper Sessions freed used; 'helper-freed-unused'= TFTP Helper Sessions freed unused; 'helper-already-used'= TFTP Helper Session already used; 'helper-in-rml'= TFTP Helper Session in Remove List;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    session_created (optional, any, None)
      TFTP Client Sessions Created



  uuid (False, any, None)
    uuid of the object


  tftp_value (False, any, None)
    'enable'= Enable TFTP ALG for LSN;


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

