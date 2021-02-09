.. _a10_cgnv6_ds_lite_alg_pptp_module:


a10_cgnv6_ds_lite_alg_pptp -- Configures A10 cgnv6.ds.lite.alg.pptp
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

DS-Lite PPTP ALG (default= disabled)






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  pptp_enable (False, any, None)
    'enable'= Enable ALG;


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

