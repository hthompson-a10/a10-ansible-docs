.. _a10_scm_license_src_info_module:


a10_scm_license_src_info -- Configures A10 scm.license-src-info
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

license source opers






Parameters
----------

  oper (False, any, None)
    Field oper


    product (optional, any, None)
      Field product


    uuid (optional, any, None)
      Field uuid


    billing_serial (optional, any, None)
      Field billing_serial


    platform (optional, any, None)
      Field platform


    usb_uuid (optional, any, None)
      Field usb_uuid


    glm_ping_interval (optional, any, None)
      Field glm_ping_interval


    source2 (optional, any, None)
      Field source2


    source1_module_list (optional, any, None)
      Field source1_module_list


    token (optional, any, None)
      Field token


    source1 (optional, any, None)
      Field source1


    source3 (optional, any, None)
      Field source3


    source3_module_list (optional, any, None)
      Field source3_module_list


    source2_module_list (optional, any, None)
      Field source2_module_list



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

