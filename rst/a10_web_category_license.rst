.. _a10_web_category_license_module:


a10_web_category_license -- Configures A10 web.category.license
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

License information






Parameters
----------

  oper (False, any, None)
    Field oper


    grace_period (optional, any, None)
      Field grace_period


    is_grace (optional, any, None)
      Field is_grace


    license_expiry (optional, any, None)
      Field license_expiry


    module_status (optional, any, None)
      Field module_status


    remaining_period (optional, any, None)
      Field remaining_period


    license_status (optional, any, None)
      Field license_status


    license_type (optional, any, None)
      Field license_type


    serial_number (optional, any, None)
      Field serial_number



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

