.. _a10_cgnv6_nat64_alg_ftp_module:


a10_cgnv6_nat64_alg_ftp -- Configures A10 cgnv6.nat64.alg.ftp
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

NAT64 FTP ALG (default= enabled)






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ftp_enable (False, any, None)
    'disable'= Disable NAT64 FTP ALG;


  ansible_username (True, any, None)
    Username for AXAPI authentication


  trans_eprt_to_port (False, any, None)
    'disable'= disable;


  ansible_password (True, any, None)
    Password for AXAPI authentication


  xlat_no_trans_pasv (False, any, None)
    'enable'= enable;


  trans_epsv_to_pasv (False, any, None)
    'disable'= disable;


  trans_lpsv_to_pasv (False, any, None)
    'disable'= disable;


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  trans_lprt_to_port (False, any, None)
    'disable'= disable;









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

