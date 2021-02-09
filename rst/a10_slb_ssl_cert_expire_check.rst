.. _a10_slb_ssl_cert_expire_check_module:


a10_slb_ssl_cert_expire_check -- Configures A10 slb.ssl-cert-expire-check
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Field ssl_cert_expire_check






Parameters
----------

  oper (False, any, None)
    Field oper


    ssl_exception (optional, any, None)
      Field ssl_exception


    expire_check_status (optional, any, None)
      Field expire_check_status


    before (optional, any, None)
      Field before


    interval (optional, any, None)
      Field interval


    email_address (optional, any, None)
      Field email_address


    email_address2 (optional, any, None)
      Field email_address2



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

