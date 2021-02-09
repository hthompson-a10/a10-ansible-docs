.. _a10_bootimage_module:


a10_bootimage -- Configures A10 bootimage
=========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Set next Boot Image






Parameters
----------

  oper (False, any, None)
    Field oper


    cf_default (optional, any, None)
      Field cf_default


    hd_pri (optional, any, None)
      Field hd_pri


    cf_sec (optional, any, None)
      Field cf_sec


    hd_default (optional, any, None)
      Field hd_default


    hd_sec (optional, any, None)
      Field hd_sec


    cf_pri (optional, any, None)
      Field cf_pri



  hd_cfg (False, any, None)
    Field hd_cfg


    pri (optional, any, None)
      Primary image


    sec (optional, any, None)
      Secondary image


    hd (optional, any, None)
      Hard disk



  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  cf_cfg (False, any, None)
    Field cf_cfg


    cf (optional, any, None)
      Compact flash


    cf_pri (optional, any, None)
      Primary image



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

